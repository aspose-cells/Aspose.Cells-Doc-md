---
title: Назначение и проверка цифровых подписей
linktitle: Подпись
type: docs
weight: 100
url: /ru/java/assign-and-validate-digital-signatures/
description: Цифровая подпись Excel файла, проверка. Для защиты подлинности содержимого рабочей книги Excel файла вы можете добавить цифровую подпись, используя коды C# с помощью Aspose.Cells для .Net.
---

{{% alert color="primary" %}}

Цифровая подпись дает уверенность в том, что файл книги действителен и его никто не изменял. Вы можете создать личную цифровую подпись, используя инструмент **SELFCERT**, поставляемый вместе с пакетом Microsoft Office или другим инструментом. Вы также можете купить цифровую подпись. После создания или приобретения цифровой подписи вы должны прикрепить ее к своей книге. Прикрепление цифровой подписи аналогично запечатыванию конверта. Если пришел запечатанный конверт, у вас есть определенная уверенность в том, что никто не трогал его содержимое.

Aspose.Cells for Java API предоставляет классы [**com.aspose.cells.DigitalSignatureCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignatureCollection) и [**com.aspose.cells.DigitalSignature**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignature) для подписи таблиц и их проверки.

{{% /alert %}}

## **Подписание таблиц**

Для процесса подписи необходим сертификат, как было обсуждено выше. Кроме сертификата, также необходим пароль для успешной подписи таблиц при использовании API Aspose.Cells.

В следующем фрагменте кода показано использование API Aspose.Cells for Java для подписи таблицы.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SigningSpreadsheets-SigningSpreadsheets.java" >}}

{{% alert color="primary" %}}

В случае, если указанный пароль не совпадает с паролем сертификата, будет сгенерировано исключение типа *javax.crypto.BadPaddingException*.

{{% /alert %}}

## **Проверка таблиц**

В следующем фрагменте кода показано использование API Aspose.Cells for Java для проверки таблицы.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ValidatingSpreadsheets-ValidatingSpreadsheets.java" >}}
