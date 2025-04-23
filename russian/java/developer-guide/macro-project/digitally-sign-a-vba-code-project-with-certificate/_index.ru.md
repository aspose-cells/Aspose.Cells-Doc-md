---
title: Цифровая подпись проекта VBA с помощью сертификата
type: docs
weight: 110
url: /ru/java/digitally-sign-a-vba-code-project-with-certificate/
---

{{% alert color="primary" %}}

Вы можете цифрово подписать свой проект кода VBA, используя Aspose.Cells с его методом [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#sign-com.aspose.cells.DigitalSignature-). Пожалуйста, следуйте этим шагам, чтобы проверить, подписан ли ваш файл Excel цифровой сертификат.

- Нажмите **Visual Basic** на вкладке **Разработчиков**, чтобы открыть **Интегрированную среду разработки Visual Basic for Applications**
- Нажмите **Сервис** > **Цифровые подписи...** в **Среде VBA**

и отобразится **Форма цифровой подписи**, показывающая, подписан ли документ цифровым сертификатом или нет.

{{% /alert %}} 

## **Цифровая подпись проекта VBA с сертификатом на C#**

Приведенный ниже образец кода иллюстрирует, как использовать метод [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#sign-com.aspose.cells.DigitalSignature-). Вот входные и выходные файлы образца кода. Вы можете использовать любой файл Excel и любой сертификат, чтобы протестировать этот код.

- [Исходный файл Excel](5115028.xlsm), используемый в образцовом коде.
- [Образец файла pfx](5115039.pfx) для создания цифровой подписи. Пожалуйста, установите его на ваш компьютер, чтобы запустить этот код. Пароль - 1234.
- [Файл Excel вывода](5115029.xlsm), сгенерированный образцовым кодом.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ManagingVBAModules-DigitallySignVbaProjectWithCertificate.java" >}}
{{< app/cells/assistant language="java" >}}
