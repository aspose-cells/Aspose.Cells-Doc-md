---
title: Экспорт Excel в HTML с сеткой
type: docs
weight: 760
url: /ru/java/export-excel-to-html-with-gridlines/
---

{{% alert color="primary" %}} 

Если вы хотите экспортировать свой файл Excel в HTML с сеткой, то используйте свойство [HtmlSaveOptions.ExportGridLines](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportGridLines) и установите его в **true**.

{{% /alert %}} 
## **Экспорт Excel в HTML с сеткой**
Следующий образец кода создает книгу и заполняет ее лист некоторыми значениями, а затем сохраняет его в формате HTML после установки значения [HtmlSaveOptions.ExportGridLines](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportGridLines) в **true**.

На следующем снимке экрана показано сгенерированное этим образцом кода выходное HTML. Как видно, он также отображает сетку в выходном HTML.

![todo:image_alt_text](export-excel-to-html-with-gridlines_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExportExceltoHTML-ExportExceltoHTML.java" >}}
{{< app/cells/assistant language="java" >}}
