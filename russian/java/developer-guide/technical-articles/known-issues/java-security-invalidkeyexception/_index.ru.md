---
title: java.security.InvalidKeyException
type: docs
weight: 10
url: /ru/java/java-security-invalidkeyexception/
---

## **Сводка**
По умолчанию AES поддерживает ключ длиной 128 бит, если вы планируете использовать ключ длиной 192 или 256 бит, компилятор java выдаст исключение Illegal key size. Это не из-за какой-либо ошибки Aspose.Cells API, а из-за ограниченной функциональности JDK/JRE. Файлы политики по умолчанию в JDK/JRE ограничены из-за импортных ограничений в некоторых странах. Пользователям необходимо получить файлы политики "Unlimited Strength" и установить их в их JRE для использования расширенной функциональности криптографии для шифрования/дешифрования.
## **Симптомы**
Вы можете получить исключение java.security.InvalidKeyException: Illegal key size или параметры по умолчанию, или java.security.InvalidKeyException: Illegal key size при загрузке защищенной электронной таблицы. 
## **Решение**
Решение очень простое и описано ниже.

1. Скачайте расширение криптографии Java (JCE) Unlimited Strength Jurisdiction Policy Files.
1. Распакуйте JAR файлы из скачанного архива и поместите их в каталог ${java.home}/jre/lib/security/.
1. Перезапустите программу.
## **Ссылки для загрузки**
Пожалуйста, используйте ссылку для загрузки, которая соответствует вашей версии JDK/JRE.

- [Расширение криптографии Java (JCE) Unlimited Strength Jurisdiction Policy Files 6](https://www.oracle.com/java/technologies/jce-6-download.html)
- [Расширение криптографии Java (JCE) Unlimited Strength Jurisdiction Policy Files 7](https://www.oracle.com/java/technologies/jce-7-download.html)
- [Расширение криптографии Java (JCE) Unlimited Strength Jurisdiction Policy Files 8](https://www.oracle.com/java/technologies/javase-jce8-downloads.html)
{{< app/cells/assistant language="java" >}}
