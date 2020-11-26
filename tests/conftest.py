import pytest
from starlette.applications import Starlette
from starlette.testclient import TestClient
from wtforms import FileField, StringField, BooleanField
from wtforms.validators import DataRequired, ValidationError
from wtforms.widgets import CheckboxInput

from starlette_wtf.form import StarletteForm


@pytest.fixture
def app():
    """Create Starlette app instance
    """
    return Starlette()


@pytest.fixture
def client(app):
    """Create Starlette test client
    """
    return TestClient(app)


@pytest.fixture
def BasicForm():
    """Return BasicForm class
    """
    class BasicForm(StarletteForm):
        name = StringField(validators=[DataRequired()])
        avatar = FileField()
        checkbox = BooleanField(widget=CheckboxInput(), default=True)
        
    return BasicForm


@pytest.fixture
def FormWithCustomValidators():
    """Return FormWithCustomValidators class
    """
    class FormWithCustomValidators(StarletteForm):
        field1 = StringField()
        field2 = StringField()

        def validate_field1(self, value):
            if not value == 'value1':
                raise ValidationError('Field value is incorrect.')

        def validate_field2(self, value):
            if not value == 'value2':
                raise ValidationError('Field value is incorrect.')

    return FormWithCustomValidators
    
    
@pytest.fixture
def FormWithCustomAsyncValidators():
    """Return FormWithCustomAsyncValidators class
    """
    class FormWithCustomAsyncValidators(StarletteForm):
        field1 = StringField()
        field2 = StringField()

        async def validate_field1(self, value):
            if not value == 'value1':
                raise ValidationError('Field value is incorrect.')

        async def validate_field2(self, value):
            if not value == 'value2':
                raise ValidationError('Field value is incorrect.')
            
    return FormWithCustomAsyncValidators
