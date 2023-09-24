from django.contrib.auth.base_user import BaseUserManager

class CustomManager(BaseUserManager):
    def create_user(self, first_name, last_name, phone, role, password, **extra_fields):
        if not first_name:
            raise ValueError("Not first_name")
        if not last_name:
            raise ValueError("Not last_name")
        if not phone:
            raise ValueError("Not phone")
        if not role:
            raise ValueError("Not role")
        if not password:
            raise ValueError("Not password")
        
        user = self.model(
            first_name = first_name,
            last_name = last_name,
            phone = phone,
            role = role,
            **extra_fields
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, first_name, last_name, phone, role, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            role=role,
            password=password,
            **extra_fields
        )