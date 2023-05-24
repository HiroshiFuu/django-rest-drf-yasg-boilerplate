# django-rest-drf-yasg-boilerplate

A Django RESTfull Framework Boilerplate

## Structure

* settings, urls and wsgi in configuration
* core app for main functions and backend app for rest API
* each API version has its serializer, url and view in its own folder

## Features

* User has a Profile model with a Role model
* User's profile has a timezone field of choices from timezones.py
* Password is validated against upper, lower and numeric
* Both Token and Bearer are accepted
* Serializer with example is enabled
* check_allowed_versions decorator checks for API version
* check_token_auth decorator checks for token authentication
* restrict_admin decorator restricts endpoint for admin only
* conditional_decorator decorator allows to set a decorator based on conditions

## Additional Packages

* added files for django-json-widget
* fix some CSS for djangocms-admin-style
* include an one-time link module that able to generate one-time only links

## Extra Scripts

* Dockerfile and compose yaml
* Linux service
* uwsgi files
* Cython scripts
