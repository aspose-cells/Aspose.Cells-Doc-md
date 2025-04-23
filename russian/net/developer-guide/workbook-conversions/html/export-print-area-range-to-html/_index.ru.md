---
title: Экспорт диапазона области печати в HTML
type: docs
weight: 60
url: /ru/net/export-print-area-range-to/
---

## **Возможные сценарии использования**

Это обычный сценарий, когда необходимо экспортировать только область печати, т.е. выбранный диапазон ячеек, а не весь лист в HTML. Эта функция уже доступна для отображения PDF, однако теперь вы можете выполнить эту задачу также для HTML. Сначала установите область печати в объекте настройки страницы листа. Затем используйте флаг [**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportprintareaonly) для экспорта только выбранного диапазона.

## Образец кода

Следующий образец кода загружает книгу и затем экспортирует область печати в HTML. Образец файла для тестирования этой функции можно скачать по следующей ссылке:

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportPrintAreaToHtml-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
