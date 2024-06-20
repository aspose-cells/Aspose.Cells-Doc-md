---
title: Отключить экспорт блоков сценариев и свойств документа
type: docs
weight: 410
url: /ru/java/disable-exporting-frame-scripts-and-document-properties/
---

{{% alert color="primary" %}} 

Aspose.Cells экспортирует сценарии рамки и свойства документа при преобразовании книги в HTML. В версии 8.6.0 Aspose.Cells for Java появляется опция, которая позволяет отключить экспорт сценариев рамки и свойств документа по желанию. Пожалуйста, используйте свойство [HtmlSaveOptions.setExportFrameScriptsAndProperties()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportFrameScriptsAndProperties) для отключения экспорта.

{{% /alert %}} 
## **Отключение экспорта сценариев рамки и свойств документа**
Следующий образец кода позволяет отключить экспорт сценариев рамки и свойств документа. После преобразования книги в HTML выходной файл не будет содержать никаких сценариев рамки и свойств документа.

Вот пример кода.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableExporting-DisableExporting.java" >}}
