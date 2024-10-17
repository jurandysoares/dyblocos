# png

Código para recortar os blocos

```sh
for img in *.png; do
    convert ${img} -crop 49x49+5+5 /tmp/${img}
done
```