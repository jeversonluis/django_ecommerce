from django import forms


class ContactForm(forms.Form):
    nome_completo = forms.CharField(
        error_messages={"required": "Obrigatório o preenchimento do nome!"},
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Seu nome completo"
            }
        )
    )

    email = forms.EmailField(
        error_messages={"invalid": "Digite um e-mail válido!"},
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite seu email"
            }
        )
    )

    mensagem = forms.CharField(
        error_messages={"required": "É obrigatório o preenchimento da mensagem!"},
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua mensagem"
            }
        )
    )

    # Função para caso haja alguma obrigatoriedade do email ser do "gmail" por exemplo
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("O email deve ser do 'gmail.com'")
        return email
