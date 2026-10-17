from django import forms


class StudentForm(forms.Form):

    name = forms.CharField(
        label="Full Name",
        max_length=50,
        min_length=3,
        required=True,
        help_text="Enter your full name"
    )

    email = forms.EmailField(
        label="Email Address",
        required=True,
        help_text="Enter a valid email address"
    )

    age = forms.IntegerField(
        label="Age",
        min_value=18,
        max_value=60,
        required=True
    )

    phone = forms.CharField(
        label="Phone Number",
        max_length=10,
        min_length=10,
        required=True
    )

    gender = forms.ChoiceField(
        label="Gender",
        choices=[
            ("Male", "Male"),
            ("Female", "Female"),
            ("Other", "Other")
        ],
        required=True
    )

    department = forms.ChoiceField(
        label="Department",
        choices=[
            ("Computer", "Computer Engineering"),
            ("IT", "Information Technology"),
            ("EXTC", "Electronics and Telecommunication"),
            ("AI", "Artificial Intelligence")
        ],
        required=True
    )

    year = forms.ChoiceField(
        label="Year",
        choices=[
            ("1", "First Year"),
            ("2", "Second Year"),
            ("3", "Third Year"),
            ("4", "Fourth Year")
        ],
        required=True
    )

    cgpa = forms.FloatField(
        label="CGPA",
        min_value=0,
        max_value=10,
        required=True
    )

    website = forms.URLField(
        label="Portfolio Website",
        required=False
    )

    date_of_birth = forms.DateField(
        label="Date of Birth",
        widget=forms.DateInput(attrs={"type": "date"}),
        required=True
    )

    address = forms.CharField(
        label="Address",
        widget=forms.Textarea,
        max_length=200,
        required=True
    )

    password = forms.CharField(
        label="Password",
        min_length=8,
        max_length=20,
        widget=forms.PasswordInput,
        required=True
    )

    newsletter = forms.BooleanField(
        label="Subscribe to Newsletter",
        required=False
    )

    skills = forms.MultipleChoiceField(
        label="Programming Skills",
        choices=[
            ("Python", "Python"),
            ("Java", "Java"),
            ("C", "C"),
            ("JavaScript", "JavaScript"),
            ("SQL", "SQL")
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    comments = forms.CharField(
        label="Additional Comments",
        widget=forms.Textarea,
        max_length=300,
        required=False
    )