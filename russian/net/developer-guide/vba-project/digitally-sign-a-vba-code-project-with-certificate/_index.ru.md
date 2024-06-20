---
title: Цифровая подпись проекта VBA с помощью сертификата
type: docs
weight: 110
url: /ru/net/digitally-sign-a-vba-code-project-with-certificate/
---

{{% alert color="primary" %}}

Вы можете цифрово подписать свой проект кода VBA, используя Aspose.Cells с его методом [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/methods/sign). Пожалуйста, следуйте этим шагам, чтобы проверить, подписан ли ваш файл Excel цифровой сертификат.

- Нажмите **Visual Basic** на вкладке **Разработчиков**, чтобы открыть **Интегрированную среду разработки Visual Basic for Applications**
- Нажмите **Инструменты** > **Цифровые подписи...** в **Интегрированной среде разработки Visual Basic for Applications**

и отобразится **Форма цифровой подписи**, показывающая, подписан ли документ цифровым сертификатом или нет.

{{% /alert %}} 

## **Цифровая подпись проекта VBA с сертификатом на C#**

Следующий образец кода иллюстрирует, как использовать метод [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/methods/sign). Вот входные и выходные файлы образца кода. Вы можете использовать любой файл Excel и любой сертификат, чтобы протестировать этот код.

- [Исходный файл Excel](5115028.xlsm), используемый в образцовом коде.
- [Образец файла pfx](5115039.pfx) для создания цифровой подписи. Пожалуйста, установите его на ваш компьютер, чтобы запустить этот код. Пароль - 1234.
- [Файл Excel вывода](5115029.xlsm), сгенерированный образцовым кодом.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-DigitallySignVbaProjectWithCertificate-1.cs" >}}
