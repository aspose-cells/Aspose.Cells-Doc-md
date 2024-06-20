---
title: Экспорт CSS таблицы рабочего листа отдельно в выходном HTML
type: docs
weight: 80
url: /ru/net/export-worksheet-css-separately-in-output/
---

## **Возможные сценарии использования**

Aspose.Cells предоставляет возможность отдельно экспортировать таблицу CSS листа при преобразовании вашего Excel файла в HTML. Пожалуйста, используйте свойство [**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately) для этой цели и установите его в **true** во время сохранения Excel файла в формате HTML.

## **Экспорт CSS таблицы рабочего листа отдельно в выходном HTML**

Следующий образец кода создает Excel файл, добавляет некоторый текст в ячейку **B5** красного цвета, а затем сохраняет его в формате HTML, используя свойство [**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately). Пожалуйста, ознакомьтесь с [выходным HTML](60489766.zip), сгенерированным кодом для справки. Вы найдете **stylesheet.css** как результат работы образца кода.

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportWorksheetCSSSeparatelyInOutputHTML.cs" >}}

## **Экспорт книги с одним листом в HTML**

Когда книга с несколькими листами преобразуется в HTML с помощью Aspose.Cells, создается HTML-файл вместе с папкой, содержащей CSS и несколькими HTML-файлами. Когда этот HTML-файл открывается в браузере, вкладки видны. То же самое поведение необходимо для книги с одним листом при преобразовании в HTML. Ранее для книг с одним листом не создавалась отдельная папка, и был создан только HTML-файл. Такой HTML-файл не показывает вкладки при открытии в браузере. MS Excel создает правильную папку и HTML для одного листа, и, следовательно, те же самые возможности реализуются с помощью API Aspose.Cells. Образец файла можно скачать по следующей ссылке для использования в нижеприведенном образце кода:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetSingleSheetTabNameInHtml-1.cs" >}}
