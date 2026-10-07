import csv
from pathlib import Path

from django.core.management.base import BaseCommand
from employee.models import Employee
from projects.models import Project, Allocation


class Command(BaseCommand):
    help = "Importa funcionários, projetos e alocações dos arquivos CSV"

    def handle(self, *args, **kwargs):

        base_dir = Path("data")

        # ==============================
        # FUNCIONÁRIOS
        # ==============================

        employees_file = base_dir / "employees.csv"

        with open(employees_file, "r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            for row in reader:

                employee, created = Employee.objects.get_or_create(
                    email=row["email"],
                    defaults={
                        "name": row["name"],
                        "hire_date": row["hire_date"],
                        "birthday": row["birthday"],
                        "hourly_rate": row["hourly_rate"],
                        "department": row["department"],
                        "description": row.get("description", ""),
                    }
                )

                if created:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Funcionário criado: {employee.name}"
                        )
                    )
                else:
                    self.stdout.write(
                        f"Funcionário já existe: {employee.name}"
                    )

        # ==============================
        # PROJETOS
        # ==============================

        projects_file = base_dir / "projects.csv"

        with open(projects_file, "r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            for row in reader:

                project, created = Project.objects.get_or_create(
                    project_name=row["name"],
                    defaults={
                        "start_date": row["start_date"],
                        "end_date": row["end_date"],
                        "materials": row["materials"],
                    }
                )

                if created:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Projeto criado: {project.project_name}"
                        )
                    )
                else:
                    self.stdout.write(
                        f"Projeto já existe: {project.project_name}"
                    )

        # ==============================
        # ALOCAÇÕES
        # ==============================

        allocations_file = base_dir / "allocations.csv"

        with open(allocations_file, "r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            for row in reader:

                employee = Employee.objects.get(
                    email=row["employee_email"]
                )

                project = Project.objects.get(
                    project_name=row["project_name"]
                )

                allocation, created = Allocation.objects.get_or_create(
                    employee=employee,
                    project=project,
                    date=row["date"],
                    defaults={
                        "start_time": row["start_time"],
                        "end_time": row["end_time"],
                        "status": row["status"],
                    }
                )

                if created:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Alocação criada: "
                            f"{employee.name} → "
                            f"{project.project_name} "
                            f"({allocation.date})"
                        )
                    )
                else:
                    self.stdout.write(
                        f"Alocação já existe: "
                        f"{employee.name} → "
                        f"{project.project_name} "
                        f"({allocation.date})"
                    )

        self.stdout.write(
            self.style.SUCCESS(
                "\nImportação concluída!"
            )
        )