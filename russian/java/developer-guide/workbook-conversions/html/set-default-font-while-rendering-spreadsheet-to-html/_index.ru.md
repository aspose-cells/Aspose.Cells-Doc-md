---
title: Установить шрифт по умолчанию при рендеринге электронной таблицы в HTML
type: docs
weight: 830
url: /ru/java/set-default-font-while-rendering-spreadsheet-to/
---
{{% alert color="primary" %}} 

 Aspose.Cells позволяет вам установить шрифт по умолчанию при рендеринге электронной таблицы в HTML. Пожалуйста, используйте[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName)для этой цели. Это свойство полезно, когда в электронной таблице есть ячейки с недопустимыми или несуществующими шрифтами. Затем эти ячейки будут отображаться шрифтом, указанным с помощью[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName) имущество.

{{% /alert %}} 
## **Установить шрифт по умолчанию при рендеринге электронной таблицы в HTML**
Следующий пример кода создает книгу и добавляет некоторый текст в ячейку B4 первого рабочего листа и задает для нее какой-то неизвестный/несуществующий шрифт. Затем он сохраняет книгу в HTML, устанавливая разные имена шрифтов по умолчанию, такие как Courier New, Arial, Times New Roman и т. д.

 На снимке экрана показан эффект от установки разных имен шрифтов по умолчанию через[HtmlSaveOptions.DefaultFontName](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#DefaultFontName)имущество.

![дело:изображение_альтернативный_текст](set-default-font-while-rendering-spreadsheet-to-html_1.png)

 Код генерирует[выходной HTML-файл с Courier New](5472568) ,[вывод HTML с помощью Arial](5472567) и[выходной HTML-файл с Times New Roman](5472565).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToHTML-.java" >}}
