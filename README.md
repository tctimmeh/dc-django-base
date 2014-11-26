# DC Django Base

## Installation

### Settings

    TEMPLATE_CONTEXT_PROCESSORS = (
        "django.contrib.auth.context_processors.auth",
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.core.context_processors.static",
        "django.core.context_processors.tz",
        "django.contrib.messages.context_processors.messages",
        "django.core.context_processors.request",
        "allauth.account.context_processors.account",
        "allauth.socialaccount.context_processors.socialaccount",
    )
     
    AUTHENTICATION_BACKENDS = (
        "django.contrib.auth.backends.ModelBackend",
        "allauth.account.auth_backends.AuthenticationBackend",
    )
    
    INSTALLED_APPS = (
        'YOUR_APP_HERE',
        'dcbase',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'allauth.socialaccount.providers.*', # PUT ALL OAUTH PROVIDERS HERE
        'widget_tweaks',
        'django_gravatar',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.sites',
    )
    
    SITE_ID = 1
    
    ACCOUNT_EMAIL_REQUIRED = True

For e-mail verification on user accounts be sure to enable it in settings:

    ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

For development set a console email backend (unless you have a real SMTP server, then configure that):

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 

### Urls

    url(r'', include('dcbase.urls')),

### Templates

Create a `base.html` in the root of your templates directory. Extend `dcbase/base.html` and override
blocks that are global to your site. For example:

    {% extends "dcbase/base.html" %}
    
    {% block headerBarBrand %}My Site Brand{% endblock %}
    {% block footerBar %}
        Footer content!
    {% endblock %}

## Templates

DC-Base provides templates to override and include.

### Base

The `dcbase/base.html` provides the basic page framework and layout. Provide your site's base template by extending this template
and overriding the following blocks.

- **pageTitle**: title of the page, as it will appear in the browser window's title bar
- **style**: inline CSS to include in the page style tag. you need to include your own enclosing \<style> element.
- **head**: extra content to include in the page head tag. use this to link external css, add meta tags, etc.
- **headerBarBrand**: content for the "brand" link in the upper right, usually the app title or site logo
- **headerBarBrandLink**: target of the "brand" link, usually the app's home page. default is site root.
- **headerBarRight**: extra nav items (\<li>'s) to include on the right side of the header bar
- **content**: the main content of the page. should normally start with a div with class "container" or "container-fluid"
- **footerBar**: content for the footer nav bar. this is a bootstrap navbar so the content here should probably be a \<ul>
- **script**: any additional scripts or script links the page needs. inline scripts must supply their own enclosing \<script> tag

#### Narrow Dialog Base

Extend from `dcbase/base-narrow-dialog.html` for any page that is just a single, vertical form or dialog. Override the following
blocks to provide the dialog content:

- **panelHeading**: title of the dialog panel. include any required \<h*> tags.
- **panelType**: the type of panel (e.g. success, danger, etc.). default is "default"
- **panelBody**: content of the dialog panel

### Forms

Include `dcbase/form.html` or `dcbase/form-horizontal.html` to create consistently styled forms. These templates expect a context
variable called `form`.

Set the `autofocus` context variable to the id of a form field which should be automatically focused when the page loads. For example

    {% include "dcbase/form.html" with autofocus="id_important_field" %}

## User Profiles

Create app-specific user profile data by following these instructions. 

Create a database model to encapsulate the profile data. Give it a `OneToOneField` to the `User` model and call it `user`.

Create a `ModelForm` to update the new profile model.

Create a URL to the view that will edit the new profile model. To be consistent with other profile urls it should be in the form
of `^accounts/profile/edit/CATEGORY/$`, where CATEGORY is unique to your app.  Make sure the url has a name, such as
`account_profile_edit_CATEGORY`.

Create the view for the above URL. The view class should look similar to this:

    @profile_form_view()
    class ProfileEditCATEGORYView(ProfileEditFormView):
        form_class = MyProfileForm
        profile_nav_name = _('Nav Name')
        profile_panel_name = _('Panel Name')
        profile_edit_url = reverse_lazy('account_profile_edit_CATEGORY')
    
    profileEditCATEGORYView = login_required(ProfileEditCATEGORYView.as_view())

The class-level attribute are:

* **profile_nav_name**: the title that will appear on the user profile navigation bar
* **profile_panel_name**: the title that will appear on the panel that holds the form
* **profile_edit_url**: URL to the page that allows editing of this profile model

After these things are done a new pane will appear in the user's profile edit page. This new page will contain the form for the
apps profile model.

New users will automatically get an instance of the new profile model in the database. If this is a new profile model for a site
with existing users then be sure to use a database migration to create an instance for every existing user.

