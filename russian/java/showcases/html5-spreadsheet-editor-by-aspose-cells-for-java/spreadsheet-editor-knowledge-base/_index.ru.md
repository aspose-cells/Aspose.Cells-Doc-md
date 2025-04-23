---
title: База знаний редактора таблиц
type: docs
weight: 30
url: /ru/java/spreadsheet-editor-knowledge-base/
---

## **Встраивайте HTML5 редактор таблиц в любое место**

HTML5 редактор таблиц может быть встроен в любой веб-сайт, блог и форумы для совместного использования таблиц по всему интернету. Его можно встроить как самостоятельный редактор, либо загрузить с файлом таблицы.

**Встраивание как самостоятельного редактора**

Для встраивания как самостоятельного редактора используйте тег HTML IFRAME для добавления на веб-сайт. Например:

{{< highlight html >}}

 <iframe src="http://spreadsheet-editor.aspose.com/" width="800" height="600">

    Your web browser does not support IFRAMEs

</iframe>

{{< /highlight >}}

**Встраивание с таблицей**

Для загрузки таблицы в встроенный редактор используйте параметр **url**. Например:

{{< highlight html >}}

 <iframe src="http://spreadsheet-editor.aspose.com/?url=http://example.com/Sample.xlsx" width="800" height="600">

    Your web browser does not support IFRAMEs

</iframe>

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
