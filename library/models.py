from django.db import models


class Tecnologia(models.Model):
    """Linguagem ou framework (ex: Python, Django, Docker)."""
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)

    class Meta:
        verbose_name = "Tecnologia"
        verbose_name_plural = "Tecnologias"
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Autor(models.Model):
    """Pessoa que escreveu/criou um recurso."""
    nome = models.CharField(max_length=150)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Recurso(models.Model):
    """Livro, curso ou artigo sobre programacao."""

    TIPO_CHOICES = [
        ('livro', 'Livro'),
        ('curso', 'Curso'),
        ('artigo', 'Artigo'),
        ('video', 'Video'),
    ]

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='artigo')
    url = models.URLField(blank=True)
    data_publicacao = models.DateField(null=True, blank=True)

    tecnologia = models.ForeignKey(
        Tecnologia,
        on_delete=models.CASCADE,
        related_name='recursos'
    )
    autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        related_name='recursos'
    )

    class Meta:
        verbose_name = "Recurso"
        verbose_name_plural = "Recursos"
        ordering = ['-data_publicacao', 'titulo']

    def __str__(self):
        return f"{self.titulo} ({self.get_tipo_display()})"