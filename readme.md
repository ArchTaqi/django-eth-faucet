# Django Eth Faucet

## Dockerize Quick Start

```bash
$ export ETH_COLD_WALLET_ADDRESS=""
$ export ETH_COLD_WALLET_PRIVATE_KEY=""
$ docker-compose build
$ docker-compose up -d
$ docker-compose down -v
$ docker exec -it faucet_backend bash
```

> Got to http://127.0.0.1:8000/admin/ use "admin@faucet.xyz" as username and "rvh-ycq4ZWQ4bzp.jdw" as password to login to admin dashbaord.
> To run apis use the file `api.http` or Below snippets via `curl`.

#### Request Facuets
```bash
curl --location 'http://127.0.0.1:8000/faucet/fund/' \
--header 'Content-Type: application/json' \
--data '{
    "wallet_address": "0x2B4E3Df272E05b5318C69C95274055973C36fE1D"
}'
```

#### Read Facuet Stats
```bash
curl --location 'http://127.0.0.1:8000/faucet/stats/'
```