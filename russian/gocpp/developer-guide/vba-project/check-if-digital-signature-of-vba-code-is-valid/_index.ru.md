---
title: Проверка действительности цифровой подписи VBA кода с Golang через C++
linktitle: Проверить, действителен ли цифровой подпись кода VBA
type: docs
weight: 120
url: /ru/go-cpp/check-if-digital-signature-of-vba-code-is-valid/
description: Узнайте, как проверить действительность цифровой подписи в VBA коде с помощью Aspose.Cells и Golang через C++.
---

{{% alert color="primary" %}}

Aspose.Cells позволяет проверить, является ли цифровая подпись VBA-кода действительной, используя свойство [**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/go-cpp/vbaproject/isvalidsigned/). Если подпись действительна, оно вернет **true**, в противном случае — **false**. Цифровая подпись VBA-кода становится недействительной, если вы измените VBA-код.

{{% /alert %}}

## **Проверьте, действительна ли цифровая подпись VBA-кода в C++**

Следующий код демонстрирует использование этого свойства с помощью [пример файла Excel](5115030.xlsm), который можно скачать по предоставленной ссылке. Этот файл Excel имеет действительную подпись, но при изменении его VBA-кода и сохранении рабочей книги подпись становится недействительной.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CheckIfDigitalSignatureOfVbaCodeIsValid.go" >}}
