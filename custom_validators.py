from wtforms import validators

def height_validator(form,field):
    if float(field.data) < 120 or float(field.data) > 220:
            raise validators.ValidationError('Participant is too short or too high for our \
                 research!')

def weight_validator(form,field):
    if float(field.data) < 20 or float(field.data) > 200:
            raise validators.ValidationError('Participant is too light or too heavy for our \
                 research!')