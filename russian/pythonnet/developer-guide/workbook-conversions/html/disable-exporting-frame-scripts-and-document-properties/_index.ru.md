---
title: Отключить экспорт блоков сценариев и свойств документа
type: docs
weight: 310
url: /ru/python-net/disable-exporting-frame-scripts-and-document-properties/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET экспортирует скрипты рамок и свойства документа при конвертации книги в HTML. В версии 8.6.0 API Aspose.Cells for Python via .NET добавлена возможность по желанию отключить экспорт скриптов рамок и свойств документа. Для этого используйте свойство HtmlSaveOptions.ExportFrameScriptsAndProperties.

{{% /alert %}}

## **Отключение экспорта сценариев рамки и свойств документа**

Следующий образец кода позволяет отключить экспорт сценариев рамки и свойств документа. После преобразования книги в HTML выходной файл не будет содержать никаких сценариев рамки и свойств документа.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-HtmlExportFrameScripts-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
