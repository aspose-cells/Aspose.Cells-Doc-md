---
title: Экспортируйте CSS листов в отдельный HTML вывод с помощью Golang через C++
linktitle: Экспорт CSS таблицы рабочего листа отдельно в выходном HTML
type: docs
weight: 80
url: /ru/go-cpp/export-worksheet-css-separately-in-output/
description: Узнайте, как экспортировать CSS листа отдельно при преобразовании Excel в HTML с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Aspose.Cells позволяет экспортировать CSS листа отдельно при преобразовании файла Excel в HTML. Используйте свойство [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportworksheetcssseparately/) для этой цели и установите его в **true** при сохранении файла в формат HTML.

## **Экспорт CSS таблицы рабочего листа отдельно в выходном HTML**

Следующий образец кода создает Excel файл, добавляет некоторый текст в ячейку **B5** красного цвета, а затем сохраняет его в формате HTML, используя свойство [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportworksheetcssseparately/). Пожалуйста, ознакомьтесь с [выходным HTML](60489766.zip), сгенерированным кодом для справки. Вы найдете **stylesheet.css** как результат работы образца кода.

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportWorksheetCssSeparatelyInOutputHtml.go" >}}
## **Экспортировать книгу с одним листом в HTML**

Когда книга с несколькими листами конвертируется в HTML с помощью Aspose.Cells, создается HTML-файл вместе с папкой, содержащей CSS и несколько HTML-файлов. При открытии этого HTML-файла в браузере отображаются вкладки. Тоже поведение требуется для книги с одним листом при конвертации в HTML. Ранее не создавалась отдельная папка для книг с одним листом, создавался только HTML-файл, который не показывал вкладки. Microsoft Excel создает соответствующую папку и HTML-файл для одного листа, поэтому это поведение реализовано с помощью API Aspose.Cells. Скачать пример файла для использования в приведенном ниже коде можно по следующей ссылке:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Образец кода**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportWorksheetCssSeparatelyInOutputHtml-1.go" >}}
