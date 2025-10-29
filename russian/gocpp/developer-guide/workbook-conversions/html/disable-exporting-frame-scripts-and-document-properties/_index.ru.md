---
title: Отключите экспорт скриптов рамки и свойств документа с помощью Golang через C++
type: docs
weight: 310
url: /ru/go-cpp/disable-exporting-frame-scripts-and-document-properties/
description: Отключите экспорт скриптов рамки и свойств документа с помощью Aspose.Cells и Golang через C++.
---

{{% alert color="primary" %}}

Aspose.Cells экспортирует скрипты кадров и свойства документа при преобразовании рабочей книги в HTML. В версии 8.6.0 Aspose.Cells for C++ появилась опция, которая позволяет по желанию отключить экспорт скриптов кадров и свойств документа. Используйте свойство HtmlSaveOptions.ExportFrameScriptsAndProperties для отключения экспорта.

{{% /alert %}}

## **Отключение экспорта сценариев рамки и свойств документа**

Следующий образец кода позволяет отключить экспорт сценариев рамки и свойств документа. После преобразования книги в HTML выходной файл не будет содержать никаких сценариев рамки и свойств документа.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableExportingFrameScriptsAndDocumentProperties.go" >}}
