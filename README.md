# Library

Library prosty system do zarządzania książkami w bibliotece.
Składa się on z trzech serwisów:

- `books-api` - serwis do zarządzania książkami
- `image-api` - serwis do zarządzania obrazami książek
- `image-uploader` - serwis do przesyłania obrazów książek

Nie będziemy zagłębiać się w szczegóły implementacji, ponieważ naszym celem jest wdrożenie aplikacji na AWS.

## Books api

Aplikacja pozwala na dodawanie oraz przeglądanie książek.
Napisany w Flasku, ale przygotowany do wdrożenia w Lambdę.
Jako bazę danych używa DynamoDB.
Po zapisaniu ksiażki do bazy danych, wysyła wiadomość do kolejki SQS, która jest przetwarzana przez `image-uploader`.

## Image api

Ten serwis wystawia jeden endpoint, który zwraca obrazek książki.
Należy wdrożyć do w Lambdę.
Triggerem dla tej Lambdy jest zapytanie http.
Nie ma bazy danych, ponieważ obrazki są przechowywane w S3.
Jeśli obrazek nie istnieje w S3, to jest to traktowane jako błąd 404.

## Image uploader

Serwis do przesyłania obrazów książek.
Triggerem dla tej Lambdy jest wiadomość z kolejki SQS.
Wiadomość taka zawiera informacje o książce, której obrazek ma zostać przesłany.
Te informacje to:

- `id` - identyfikator książki
- `url` - adres, z którego obrazek ma zostać pobrany.

Obrazki są zapisywane w S3.
Następnie będą dostępne w `image-api`.


