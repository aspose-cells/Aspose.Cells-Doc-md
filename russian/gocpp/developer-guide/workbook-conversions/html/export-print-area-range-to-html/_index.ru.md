---
title: Экспорт области печати в HTML с помощью Golang через C++
linktitle: Экспорт диапазона области печати в HTML
type: docs
weight: 60
url: /ru/go-cpp/export-print-area-range-to/
description: Узнайте, как экспортировать диапазон области печати в HTML с использованием Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Это распространенный сценарий, когда нужно экспортировать только область печати, то есть выбранный диапазон ячеек, а не весь лист, в HTML. Эта функция уже доступна для рендеринга PDF, однако теперь вы можете выполнять эту задачу и для HTML. Сначала установите область печати в объекте настройки страницы листа. Затем используйте флаг [**HtmlSaveOptions.GetExportPrintAreaOnly()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportprintareaonly/), чтобы экспортировать только выбранный диапазон.

## **Образец кода**

Следующий пример загружает книгу и экспортирует диапазон области печати в HTML. Тестовый файл для этой функции можно скачать по следующей ссылке:

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportPrintAreaRangeToHtml.go" >}}
