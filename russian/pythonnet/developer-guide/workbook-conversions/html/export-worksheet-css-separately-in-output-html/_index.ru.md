---
title: Экспорт CSS таблицы рабочего листа отдельно в выходном HTML
type: docs
weight: 80
url: /ru/python-net/export-worksheet-css-separately-in-output/
---

## **Возможные сценарии использования**

Aspose.Cells для Python via .NET обеспечивает возможность отдельного экспорта CSS листа для листа при преобразовании файла Excel в HTML. Используйте для этого свойство [**HtmlSaveOptions.export_worksheet_css_separately**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_worksheet_css_separately) и установите его в **true** при сохранении файла Excel в формат HTML.

## **Экспорт CSS таблицы рабочего листа отдельно в выходном HTML**

Следующий образец кода создает Excel файл, добавляет некоторый текст в ячейку **B5** красного цвета, а затем сохраняет его в формате HTML, используя свойство [**HtmlSaveOptions.export_worksheet_css_separately**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_worksheet_css_separately). Пожалуйста, ознакомьтесь с [выходным HTML](60489766.zip), сгенерированным кодом для справки. Вы найдете **stylesheet.css** как результат работы образца кода.

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.py" >}}

## **Экспорт книги с одним листом в HTML**

При преобразовании тетради с несколькими листами в HTML с помощью Aspose.Cells для Python via .NET создается HTML-файл вместе с папкой, содержащей CSS и несколько HTML-файлов. При открытии этого HTML-файла в браузере видны вкладки. То же поведение требуется и для тетради с одним листом при преобразовании в HTML. Ранее не создавалась отдельная папка для книг с одним листом, создавался только HTML-файл. Такой HTML-файл не показывает вкладки при открытии в браузере. MS Excel создает для одного листа правильную папку и HTML-файл, поэтому такое же поведение реализовано с помощью API Aspose.Cells для Python via .NET. Можно загрузить пример файла для использования в приведённом ниже коде:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SetSingleSheetTabNameInHtml-1.py" >}}
