from decouple import config

default_directory = config('UPLOAD_ROUTE', 'uploads/')


def directory_items(instance, filename):
    return '%s/medications/%s/%s' % (default_directory, instance.name, filename)



