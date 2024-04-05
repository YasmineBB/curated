from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Testimonial
from .forms import TestimonialForm


def testimonials(request):
    """ A view to display testimonials/features """

    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'testimonials/testimonials.html', context)

@login_required
def add_testimonial(request):
    """ Add a testimonial/feature to the database """
    if not request.user.is_superuser and request.user.is_anonymous:
        messages.error(request, 'Ooops! Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            testimonial = form.save()
            messages.success(request, f'Success! You added a feature by {testimonial.buyer_name} to the database.')
            return redirect(reverse('testimonials'))
        else:
            messages.error(request, 'Failed to add feature. Please ensure the form is valid.')
    else:
        form = TestimonialForm()
        
    template = 'testimonials/add_testimonial.html' 
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_testimonial(request, testimonial_id):
    """ A view to make changes to a feature/testimonial in the database """
    if not request.user.is_superuser:
        messages.error(request, 'Ooops! Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            form.save()
            messages.success(request, f'Success! You have updated the feature of {testimonial.buyer_name}.')
            return redirect(reverse('testimonials'))
        else:
            messages.error(request, 'Failed to update feature. Please ensure the form is valid.')
    else:
        form = TestimonialForm(instance=testimonial)
        messages.info(request, f'You are editing the feature of {testimonial.buyer_name}')

    template = 'testimonials/edit_testimonial.html'
    context = {
        'form': form,
        'testimonial': testimonial,
    }

    return render(request, template, context)


@login_required
def delete_testimonial(request, testimonial_id):
    """ A view to delete feature/testimonial from the database """
    if not request.user.is_superuser:
        messages.error(request, 'Ooops! Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)
    testimonial.delete()
    messages.success(request, f'You deleted the feature for {testimonial.buyer_name} from the database!')
    return redirect(reverse('testimonials'))
