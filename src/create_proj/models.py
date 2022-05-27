from django.db import models


class BackEndChoices(models.TextChoices):
    """."""

    DJANGO = "django", "Django"
    FLASK  = "flask" , "Flask"
    SPRING = "spring", "Spring"
    ASP_DOT_NET = "asp.net", "Asp.net"
    NODE_JS = "node.js", "Node.js"
    RUBY_ON_RAILS = "ruby on rails", "Ruby on Rails"


class FrontEndChoices(models.TextChoices):
    """."""

    REACT = "react", "React"
    ANGULAR = "angular", "Angular"
    VUE = "vue", "Vue.js"


class DatabaseChoices(models.TextChoices):
    """."""

    MYSQL = "mysql", "MySQL"
    MSSQL = "mssql", "Microsoft SQL Server"
    PGSQL = "postgres", "PostgreSQL"
    ORACLE = "oracle", "Oracle"


class Project(models.Model):
    """."""

    backend = models.CharField(choices=BackEndChoices.choices, max_length=20)
    frontend = models.CharField(choices=FrontEndChoices.choices, max_length=20)
    database = models.CharField(choices=DatabaseChoices.choices, max_length=20)
