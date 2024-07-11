# Image-Uploader

To aplikacja, która pobiera obrazki z kolejki SQS, przetwarza je i zapisuje w S3

## Lambda

Do wdrożenia aplikacji na AWS wykorzystano funkcję lambda.
Jest to funkcja triggerowana pojawieniem się wiadomości w kolejce SQS.

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
