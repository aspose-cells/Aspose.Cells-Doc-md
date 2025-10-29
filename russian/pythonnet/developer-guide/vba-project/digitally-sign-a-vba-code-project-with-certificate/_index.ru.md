---
title: Цифровая подпись проекта VBA с помощью сертификата
type: docs
weight: 110
url: /ru/python-net/digitally-sign-a-vba-code-project-with-certificate/
---

{{% alert color="primary" %}}

Вы можете подписать свой VBA-код проект с помощью Aspose.Cells для Python via .NET и его метода [**Workbook.vba_project.sign()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/sign/#aspose.cells.digitalsignatures.DigitalSignature). Следуйте этим шагам, чтобы проверить, подписан ли ваш Excel-файл цифровой подписью.

- Нажмите **Visual Basic** на вкладке **Разработчиков**, чтобы открыть **Интегрированную среду разработки Visual Basic for Applications**
- Нажмите **Инструменты** > **Цифровые подписи...** в **Интегрированной среде разработки Visual Basic for Applications**

и отобразится **Форма цифровой подписи**, показывающая, подписан ли документ цифровым сертификатом или нет.

{{% /alert %}} 

## **Цифровая подпись VBA-проекта с сертификатом в Python**

Следующий образец кода иллюстрирует, как использовать метод [**Workbook.vba_project.sign()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/sign/#aspose.cells.digitalsignatures.DigitalSignature). Вот входные и выходные файлы образца кода. Вы можете использовать любой файл Excel и любой сертификат, чтобы протестировать этот код.

- [Исходный файл Excel](5115028.xlsm), используемый в образцовом коде.
- [Образец файла pfx](5115039.pfx) для создания цифровой подписи. Пожалуйста, установите его на ваш компьютер, чтобы запустить этот код. Пароль - 1234.
- [Файл Excel вывода](5115029.xlsm), сгенерированный образцовым кодом.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-DigitallySignVbaProjectWithCertificate-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
