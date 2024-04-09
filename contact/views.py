from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import GetInTouchForm
from .models import ContactForm
from profiles.models import UserProfile

from django.contrib import messages


def contact(request):
    """ A view to submit a contact form """
    if request.method == 'POST':
        get_in_touch_form = GetInTouchForm(request.POST)
        if get_in_touch_form.is_valid():
            get_in_touch_form.save()
            messages.success(request, 'Your enquiry was sent successfully. \
                Please allow up to 48 hours for a response.')
            return render(request, 'contact/contact_success.html')
        else:
            messages.error(request, 'There was an error sending your enquiry. \
            Please ensure all fields are valid and try again.')
            return redirect('contact')

    else:
        if request.user.is_authenticated:
            try:
                user = UserProfile.objects.get(user=request.user)
                get_in_touch_form = GetInTouchForm(initial={
                    'contact_name': user,
                    'contact_email': user.user.email,
                })
            except UserProfile.DoesNotExist:
                get_in_touch_form = GetInTouchForm()
        else:
            get_in_touch_form = GetInTouchForm()

    template = 'contact/contact.html'
    context = {
        'form': get_in_touch_form,
    }

    return render(request, template, context)


@login_required
def enquiries(request):
    """ A view to display contact enquiries """
    if not request.user.is_superuser:
        messages.error(request, 'Ooops! Sorry, only store owners can do that.')
        return redirect(('home'))

    enquiries = ContactForm.objects.all()

    context = {
        'enquiries': enquiries,
    }

    return render(request, 'contact/enquiries.html', context)
