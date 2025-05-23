---
title: Экспорт CSS таблицы рабочего листа отдельно в выходном HTML
type: docs
weight: 80
url: /ru/java/export-worksheet-css-separately-in-output-html/
---

## **Возможные сценарии использования**

Aspose.Cells предоставляет возможность экспортировать CSS таблицы рабочего листа отдельно при конвертации файла Excel в формат HTML. Пожалуйста, используйте свойство HtmlSaveOptions.ExportWorksheetCSSSeparately для этой цели и установите его значение true при сохранении файла Excel в формат HTML.

## **Экспорт CSS таблицы рабочего листа отдельно в выходном HTML**

Следующий образец кода создает файл Excel, добавляет некоторый текст в ячейку B5 красного цвета, а затем сохраняет его в формате HTML, используя свойство HtmlSaveOptions.ExportWorksheetCSSSeparately. Пожалуйста, ознакомьтесь с [выходным HTML](60489780.zip), сгенерированным кодом для справки. В результате образца кода внутри него будет файл stylesheet.css.

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.java" >}}

## **Экспорт книги с одним листом в HTML**

Когда книга с несколькими листами конвертируется в HTML с помощью Aspose.Cells, создается файл HTML вместе с папкой, содержащей CSS и несколько файлов HTML. Когда этот файл HTML открывается в браузере, вкладки видны. Та же функция требуется для книги с одним листом при конвертации в HTML. Раньше не создавалась отдельная папка для книг с одним листом, и создавался только файл HTML. Такой файл HTML не показывает вкладку при открытии в браузере. Excel создает правильную папку и HTML для одиночных листов, и поэтому та же функция реализуется с помощью Aspose.Cells. Образец файла можно загрузить по следующей ссылке для использования в коде образца:

[sampleSingleSheet.xlsx](79527948.xlsx)

## **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-SetSingleSheetTabNameInHtml-1.java" >}}
{{< app/cells/assistant language="java" >}}
