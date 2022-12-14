---
title: Отключить экспорт сценариев фреймов и свойств документа
type: docs
weight: 410
url: /ru/java/disable-exporting-frame-scripts-and-document-properties/
---
{{% alert color="primary" %}} 

 Aspose.Cells экспортирует сценарии фреймов и свойства документа при преобразовании книги в HTML. В версии 8.6.0 Aspose.Cells for Java появилась опция, позволяющая отключить экспорт сценариев фреймов и свойств документа. Пожалуйста, используйте[HtmlSaveOptions.setExportFrameScriptsAndProperties()](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportFrameScriptsAndProperties) свойство, чтобы отключить экспорт.

{{% /alert %}} 
## **Отключить экспорт скриптов фреймов и свойств документа**
Следующий пример кода позволяет отключить экспорт сценариев фреймов и свойств документа. После преобразования рабочей книги в формат HTML выходной файл не будет содержать никаких сценариев фреймов и свойств документа.

Вот пример кода.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableExporting-DisableExporting.java" >}}
