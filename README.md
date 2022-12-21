# django-graphql
Demo for graphql based on Django

## How to run the project

1. Install Python 3.11 and Poetry (skip)
1. Git clone this repository
1. Enter project folder and run command:
    ```
    $ cd django-graphql
    $ poetry install
    ```
1. Execute database migration
    ```
    $ cd mysite
    $ python manage.py migrate
    ```
1. Start the project (**make sure you are in the `mysite` directory**)
    ```
    # make sure you are in the 'mysite' directory
    $ python manage.py runserver
    ```

## How to send queries

1. Open [here(http://127.0.0.1:8000/polls/init)](http://127.0.0.1:8000/polls/init) to initialize data
1. Open http://127.0.0.1:8000/graphql/ to make graphql queries
    ```
    query {
      studyPlans(userId: 1) {
          id
          name
          participants{
            id
            name
          }
      }
      # Here is the debug field that will output the SQL queries
      _debug {
          sql {
            rawSql
          }
      }
    }
    ```
    Or
    ```
    query {
      studyPlan(id: 1) {
        id
        name
        participants {
          id
          name
        }
      }
      # Here is the debug field that will output the SQL queries
      _debug {
          sql {
            rawSql
          }
      }
    }
    ```

## How to run the tests

1. Enter project **ROOT** folder and run command:
    ```
    $ pytest mysite
    ```
    You'll see the output:
    ```
    ================================ test session starts =================================
    platform darwin -- Python 3.11.0, pytest-7.2.0, pluggy-1.0.0
    django: settings: mysite.settings (from ini)
    rootdir: /Users/zhujian/projects/local-demo/django-graphql, configfile: pytest.ini
    plugins: django-4.5.2
    collected 3 items

    mysite/polls/tests.py ...                                                      [100%]

    ================================= 3 passed in 0.09s ==================================
    ```