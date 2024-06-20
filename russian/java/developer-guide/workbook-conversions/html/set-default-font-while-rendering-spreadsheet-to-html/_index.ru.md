---
title: Установить шрифт по умолчанию при рендеринге электронных таблиц в HTML
type: docs
weight: 830
url: /ru/java/set-default-font-while-rendering-spreadsheet-to/
---

{{% alert color="primary" %}} 

Aspose.Cells позволяет установить шрифт по умолчанию при рендеринге электронных таблиц в HTML. Пожалуйста, используйте [HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName) для этой цели. Это свойство полезно, когда некоторые ячейки в электронной таблице имеют недопустимые или несуществующие шрифты. Тогда эти ячейки будут отображаться шрифтом, указанным в свойстве [HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName).

{{% /alert %}} 
## **Установить шрифт по умолчанию при рендеринге электронных таблиц в HTML**
Следующий образец кода создает книгу и добавляет некоторый текст в ячейку B4 первого листа и устанавливает ее шрифт на неизвестный/не существующий шрифт. Затем он сохраняет книгу в HTML, устанавливая разные имена шрифтов по умолчанию, такие как Courier New, Arial, Times New Roman, и т. д.

Снимок экрана показывает эффект установки различных имен шрифтов по умолчанию через свойство [HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName).

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

Код генерирует [выходной HTML файл с Courier New](5472568), [выходной HTML с Arial](5472567) и [выходной HTML файл с Times New Roman](5472565).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToHTML-.java" >}}
