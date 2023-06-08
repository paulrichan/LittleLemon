APIs to test.

Be sure to create your own superuser and provide the correct Token when using Insomnia to get data. All routes are protected with IsAuthenticated.

/restaurant/
/restaurant/booking/tables
/menu/
/menu/<int:pk>
/auth/users/
/auth/token/login
/auth/token/logout
/api-auth-token/

To run test - IMPORTANT - use this script below:
python manage.py test tests