---
title: Экспорт диапазона области печати в HTML
type: docs
weight: 60
url: /ru/java/export-print-area-range-to-html/
---

## Возможные сценарии использования

Это очень распространенный сценарий, при котором нам необходимо экспортировать только область печати, т.е. выбранный диапазон ячеек, а не весь лист, в HTML. Эта функция уже доступна для создания PDF-файлов, теперь вы можете выполнять это действие и для HTML. Сначала установите область печати в объекте настройки страницы листа. Затем используйте [**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportPrintAreaOnly) для экспорта только выбранного диапазона.

## Код Java для экспорта диапазона области печати в HTML

Следующий образец кода загружает книгу, а затем экспортирует область печати в HTML. Образец файла для тестирования этой функции можно скачать по следующей ссылке:

[sampleInlineCharts.xlsx](79527960.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

