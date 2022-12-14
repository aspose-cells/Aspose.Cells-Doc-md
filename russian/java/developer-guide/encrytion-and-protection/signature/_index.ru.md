---
title: Назначение и проверка цифровых подписей
linktitle: Подпись
type: docs
weight: 100
url: /ru/java/assign-and-validate-digital-signatures/
description: Цифровая подпись файла Excel, проверка. Чтобы защитить подлинность содержимого рабочей книги файла Excel, вы можете добавить цифровую подпись, используя коды C# с Aspose.Cells для .Net.
---
{{% alert color="primary" %}}

 Цифровая подпись гарантирует, что файл рабочей книги действителен и никто не изменил его. Вы можете создать личную цифровую подпись с помощью**САМОСЕРТ** инструмент, поставляемый с пакетом Office Microsoft или любым другим инструментом. Вы даже можете купить цифровую подпись. После того как вы создадите или получите цифровую подпись, вы должны прикрепить ее к своей книге. Добавление цифровой подписи аналогично запечатыванию конверта. Если конверт приходит запечатанный, у вас есть определенная уверенность в том, что никто не подделывал его содержимое.

 Aspose.Cells for Java API предоставить[**com.aspose.cells.DigitalSignatureCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignatureCollection) & [**com.aspose.cells.DigitalSignature**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignature) классы для подписи электронных таблиц, а также их проверки.

{{% /alert %}}

## **Подписание электронных таблиц**

Для процесса подписи требуется сертификат, как обсуждалось выше. Наряду с сертификатом необходимо также иметь его пароль для успешной подписи электронных таблиц с использованием Aspose.Cells API.

Следующий фрагмент кода демонстрирует использование Aspose.Cells for Java API для подписи электронной таблицы.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SigningSpreadsheets-SigningSpreadsheets.java" >}}

{{% alert color="primary" %}}

 В случае, если указанный пароль не совпадает с паролем сертификата, возникает исключение типа*javax.crypto.BadPaddingException* будет брошен.

{{% /alert %}}

## **Проверка электронных таблиц**

Следующий фрагмент кода демонстрирует использование Aspose.Cells for Java API для проверки электронной таблицы.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ValidatingSpreadsheets-ValidatingSpreadsheets.java" >}}
