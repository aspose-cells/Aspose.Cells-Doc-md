---
title: Цифровая подпись проекта VBA с сертификатом в C++
linktitle: Цифровая подпись проекта VBA с помощью сертификата
type: docs
weight: 110
url: /ru/go-cpp/digitally-sign-a-vba-code-project-with-certificate/
description: Узнайте, как цифрово подписать ваш проект VBA, используя Aspose.Cells for C++ с сертификатом.
---

{{% alert color="primary" %}} 

Вы можете цифрово подписать ваш проект VBA с помощью Aspose.Cells и его метода [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/go-cpp/vbaproject/sign/). Пожалуйста, следуйте этим шагам, чтобы проверить, подписан ли ваш файл Excel с помощью сертификата.

- Нажмите **Visual Basic** на вкладке **Developer**, чтобы открыть **Visual Basic for Applications IDE**.
- Нажмите **Tools** > **Digital Signatures...** в **Visual Basic for Applications IDE**.

Это покажет **Digital Signature Form**, указывающую, подписан ли документ с помощью сертификата или нет.

{{% /alert %}} 

## **Цифровая подпись проекта VBA с сертификатом в C++**

Следующий пример кода иллюстрирует, как использовать метод [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/go-cpp/vbaproject/sign/). Вот входные и выходные файлы примера кода. Вы можете использовать любой файл Excel и любой сертификат для тестирования этого кода.

- [Исходный файл Excel](5115028.xlsm), используемый в образцовом коде.
- [Образец файла pfx](5115039.pfx) для создания цифровой подписи. Пожалуйста, установите его на ваш компьютер, чтобы запустить этот код. Пароль - 1234.
- [Файл Excel вывода](5115029.xlsm), сгенерированный образцовым кодом.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DigitallySignAVbaCodeProjectWithCertificate.go" >}}
