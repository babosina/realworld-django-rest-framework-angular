from django.core.management.base import BaseCommand

from articles.models import Article, Comment, Tag
from users.models import User


class Command(BaseCommand):
    help = "Seed database with dummy data"

    def handle(self, *args, **options):
        self.stdout.write("Seeding database...")

        # Clear existing data
        User.objects.all().delete()
        Article.objects.all().delete()
        Tag.objects.all().delete()
        Comment.objects.all().delete()

        # Create users
        user1 = User.objects.create_user(
            username="john",
            email="john@example.com",
            password="password123",
            bio="Backend developer passionate about Django",
        )
        user2 = User.objects.create_user(
            username="jane",
            email="jane@example.com",
            password="password123",
            bio="Frontend developer specializing in Angular",
        )
        user3 = User.objects.create_user(
            username="bob",
            email="bob@example.com",
            password="password123",
            bio="Full-stack developer",
        )

        # Users follow each other
        user1.following.add(user2)
        user2.following.add(user1, user3)
        user3.following.add(user2)

        self.stdout.write(self.style.SUCCESS(f"✓ Created {User.objects.count()} users"))

        # Create tags
        django_tag = Tag.objects.create(name="django")
        python_tag = Tag.objects.create(name="python")
        angular_tag = Tag.objects.create(name="angular")
        web_tag = Tag.objects.create(name="webdev")
        api_tag = Tag.objects.create(name="api")

        self.stdout.write(self.style.SUCCESS(f"✓ Created {Tag.objects.count()} tags"))

        # Create articles
        article1 = Article.objects.create(
            title="Getting Started with Django REST Framework",
            description="Learn how to build RESTful APIs with Django",
            body="Django REST Framework is a powerful toolkit for building Web APIs. "
            "It provides features like serialization, authentication, and viewsets...",
            author=user1,
        )
        article1.tag_list.add(django_tag, python_tag, api_tag)

        article2 = Article.objects.create(
            title="Angular Best Practices 2024",
            description="Modern Angular development tips and tricks",
            body="Angular has evolved significantly. Here are the best practices "
            "for building scalable applications in 2024...",
            author=user2,
        )
        article2.tag_list.add(angular_tag, web_tag)

        article3 = Article.objects.create(
            title="Building a Full-Stack App with Django and Angular",
            description="Complete guide to integrating Django backend with Angular frontend",
            body="This tutorial covers everything you need to know about building "
            "a modern full-stack application...",
            author=user3,
        )
        article3.tag_list.add(django_tag, angular_tag, web_tag)

        article4 = Article.objects.create(
            title="Python Tips for Django Developers",
            description="Advanced Python techniques for better Django code",
            body="Learn advanced Python concepts that will make your Django code "
            "more efficient and maintainable...",
            author=user1,
        )
        article4.tag_list.add(python_tag, django_tag)

        article5 = Article.objects.create(
            title="Understanding Django ORM",
            description="Deep dive into Django's database abstraction layer",
            body="The Django ORM provides a powerful way to interact with databases. "
            "Let's explore its features in detail...",
            author=user3,
        )
        article5.tag_list.add(django_tag, python_tag)

        self.stdout.write(
            self.style.SUCCESS(f"✓ Created {Article.objects.count()} articles")
        )

        # Add favorites
        user2.favorite_articles.add(article1, article3)
        user1.favorite_articles.add(article2, article3)
        user3.favorite_articles.add(article1, article2)

        # Create comments
        Comment.objects.create(
            article=article1, author=user2, body="Great article! Very helpful."
        )
        Comment.objects.create(
            article=article1,
            author=user3,
            body="Thanks for sharing. Looking forward to more!",
        )
        Comment.objects.create(
            article=article2, author=user1, body="Excellent tips, will try these out."
        )
        Comment.objects.create(
            article=article2, author=user3, body="Very comprehensive guide!"
        )
        Comment.objects.create(
            article=article3, author=user1, body="This is exactly what I needed."
        )
        Comment.objects.create(
            article=article3, author=user2, body="Well explained!"
        )
        Comment.objects.create(
            article=article4, author=user2, body="Mind = blown. Thanks!"
        )

        self.stdout.write(
            self.style.SUCCESS(f"✓ Created {Comment.objects.count()} comments")
        )

        self.stdout.write(
            self.style.SUCCESS("\n✓ Database seeded successfully!\n")
        )
        self.stdout.write(f"  Users: {User.objects.count()}")
        self.stdout.write(f"  Articles: {Article.objects.count()}")
        self.stdout.write(f"  Tags: {Tag.objects.count()}")
        self.stdout.write(f"  Comments: {Comment.objects.count()}")
        self.stdout.write("\nTest credentials:")
        self.stdout.write("  john@example.com / password123")
        self.stdout.write("  jane@example.com / password123")
        self.stdout.write("  bob@example.com / password123")
