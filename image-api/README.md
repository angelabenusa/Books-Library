# Image-API

To aplikacje, która pobiera obrazki z S3, a następnie zwraca je w odpowiedzi na zapytanie HTTP.

## Lambda

Do wdrożenia aplikacji na AWS wykorzystano funkcję lambda.
Jest to funkcja triggerowana zapytaniem HTTP

## Zmienne środowiskowe

Aplikacja wykorzystuje zmienne środowiskowe, które należy ustawić w AWS.

- `BOOKS_AWS_ACCESS_KEY_ID`
- `BOOKS_AWS_SECRET_ACCESS_KEY`
- `BOOKS_AWS_REGION`
- `BUCKET_NAME`

Uwaga: Aby uniknąć przekazywania access key, secret acccess key oraz regionu, można użyć odpowiedniego Service Account.

## Pipeline

```bash
make lint
```

Aby utworzyć plik `app.zip` należy wykonać polecenie:

```bash
make build
```

Powyższy plik, należy wgrać na AWS jako funkcję lambda.


