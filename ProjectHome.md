Social Network Authentication with Gigya



> "As the social web grows in size and influence, you need to ensure that your website is  optimized to take advantage of this new phenomenon" -- http://www.gigya.com



**Easily integrate your django project with all major social networks**

this django app currently only supports authentication.


Installation


  1. pip install http://django-gigyauth.googlecode.com/svn/trunk

> 2. add 'gigyauth' to your INSTALLED\_APPS

> 3. obtain the default templates: http://django-gigyauth.googlecode.com/svn/trunk/

> 4. make sure you have the templates checked out somewhere django can get to them - i.e:
> > cd (your templates directory)
> > svn co http://django-gigyauth.googlecode.com/svn/trunk/gigyauth/templates/gigyauth/
> > you may also want to check out the example base file which define the blocks
> > that the above command depends on:
> > svn co http://django-gigyauth.googlecode.com/svn/trunk/gigyauth/templates/example_base.html


> 5. update settings.py to include your correct gigya api key:

```
         GIGYAUTH_API_KEYS='<your api key>' in settings.py
```
> Also be sure to enable the authentication backend
```
     AUTHENTICATION_BACKENDS = (
        'gigyauth.backends.gigyaoauth.GigyaBackend',
     )
```

> Add the following to your urls.py file
```
      (r'^auth/', include('gigyauth.urls')),
```

Also note, that this code currently assumes you've constructed a custom user profile AUTH\_PROFILE\_MODULE
with a model that has the field 'uid' in it.  Make sure to add this field to store the gigyauth token.