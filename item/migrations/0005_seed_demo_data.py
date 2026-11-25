import os

from django.contrib.auth.hashers import make_password
from django.db import migrations


DEMO_IMAGES = [
    'item_images/OIP_1.webp',
    'item_images/OIP_2.webp',
    'item_images/OPAC.jpeg',
    'item_images/custom-mustang-boss-302-matchbox-moving-parts-v0-qwxwf33r975d1.webp',
    'item_images/qXmGDp3R_6dbb6c2863924338805ecb360048e39f.jpg',
    'item_images/teddy-bear-pictures-8hq6erq5v0e3yfxe.jpg',
]


def seed_demo_data(apps, schema_editor):
    Category = apps.get_model('item', 'Category')
    Item = apps.get_model('item', 'Item')
    User = apps.get_model('auth', 'User')

    # Never touch an existing database with real/demo data already in it.
    if Item.objects.exists():
        return

    User.objects.get_or_create(
        username='admin',
        defaults={
            'email': 'admin@example.com',
            'password': make_password(
                os.environ.get('DEMO_ADMIN_PASSWORD', 'demo1234')
            ),
            'is_staff': True,
            'is_superuser': True,
            'is_active': True,
        },
    )

    demo_user, _ = User.objects.get_or_create(
        username='demo',
        defaults={'email': 'demo@example.com', 'is_active': True},
    )

    categories = {}
    for name in ('Vehicles', 'Home', 'Toys', 'Other'):
        categories[name], _ = Category.objects.get_or_create(name=name)

    demo_items = [
        ('Mustang Model Car', 'A small collectible mustang model.', 25.0, 'Vehicles', DEMO_IMAGES[3]),
        ('Comfy Armchair', 'A gently used armchair in good condition.', 40.0, 'Home', DEMO_IMAGES[0]),
        ('Teddy Bear', 'Soft teddy bear, great for a gift.', 12.0, 'Toys', DEMO_IMAGES[5]),
        ('Classic Poster', 'Vintage-style poster for your room.', 18.0, 'Other', DEMO_IMAGES[2]),
        ('Matchbox Set', 'Matchbox moving parts collection.', 30.0, 'Vehicles', DEMO_IMAGES[4]),
        ('Decorative Piece', 'A nice decorative item for the home.', 15.0, 'Home', DEMO_IMAGES[1]),
    ]

    for name, description, price, category_name, image in demo_items:
        Item.objects.get_or_create(
            name=name,
            defaults={
                'description': description,
                'price': price,
                'is_solid': True,
                'is_sold': False,
                'image': image,
                'category': categories[category_name],
                'created_by': demo_user,
            },
        )


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_rename_discription_item_description'),
    ]

    operations = [
        migrations.RunPython(seed_demo_data, migrations.RunPython.noop),
    ]
