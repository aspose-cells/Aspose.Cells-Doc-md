---
title: Установка сильного типа шифрования
type: docs
weight: 10
url: /ru/java/setting-strong-encryption-type/
---

{{% alert color="primary" %}}

Microsoft Excel (97-2007/2010) позволяет шифровать и защищать паролем таблицы. Он использует алгоритмы, предоставленные поставщиком криптосервисов. Поставщик криптосервисов (или CSP) представляет собой набор криптографических алгоритмов с различными свойствами. По умолчанию используется CSP "Office 97/2000 Compatible". Это CSP с некоторыми известными публичными проблемами безопасности. Таблицы, защищенные "слабым шифрованием (XOR)" или шифрованием типа "Office 97/2000 Compatible", могут быть легко взломаны.

Чтобы преодолеть эту проблему, используйте один из сильных типов шифрования, предоставленных Microsoft Excel. Вы можете изменить тип шифрования на самый сильный из доступных CSP. Для сильного шифрования требуется минимальная длина ключа 128 бит, например, 'Microsoft Strong Cryptographic Provider'.

Вы также можете шифровать и защищать паролем файлы Excel с сильным типом шифрования с использованием API Aspose.Cells.

{{% /alert %}}

## **Применение шифрования с помощью Microsoft Excel**

Для реализации шифрования файлов в Microsoft Excel (например, 2007):

1. В меню **Сервис** выберите **Параметры**.
1. Выберите вкладку **Безопасность**.
1. Введите значение для поля **Пароль для открытия**.
1. Нажмите **Дополнительно**.
1. Выберите тип шифрования и подтвердите пароль.

   **Настройка шифрования в Microsoft Excel**

![todo:image_alt_text](setting-strong-encryption-type_1.png)

## **Применение шифрования с помощью Aspose.Cells**

Приведенный ниже пример кода применяет надежное шифрование к файлу и устанавливает пароль.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ApplyingEncryption-ApplyingEncryption.java" >}}
{{< app/cells/assistant language="java" >}}
