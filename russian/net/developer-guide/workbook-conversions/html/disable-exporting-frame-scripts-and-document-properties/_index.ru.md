---
title: Отключить экспорт блоков сценариев и свойств документа
type: docs
weight: 310
url: /ru/net/disable-exporting-frame-scripts-and-document-properties/
---

{{% alert color="primary" %}}

Aspose.Cells экспортирует скрипты фреймов и свойства документа при конвертации книги Excel в HTML. Версия Aspose.Cells for .NET 8.6.0 вводит опцию, которая позволяет опционально отключать экспорт скриптов фреймов и свойств документа. Пожалуйста, используйте свойство HtmlSaveOptions.ExportFrameScriptsAndProperties для отключения экспорта.

{{% /alert %}}

## **Отключение экспорта сценариев рамки и свойств документа**

Следующий образец кода позволяет отключить экспорт сценариев рамки и свойств документа. После преобразования книги в HTML выходной файл не будет содержать никаких сценариев рамки и свойств документа.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-HtmlExportFrameScripts-1.cs" >}}
