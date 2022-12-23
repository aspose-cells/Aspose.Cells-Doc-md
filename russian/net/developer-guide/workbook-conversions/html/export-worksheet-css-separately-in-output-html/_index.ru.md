---
title: Экспорт рабочего листа CSS отдельно в выводе HTML
type: docs
weight: 80
url: /ru/net/export-worksheet-css-separately-in-output/
---
## **Возможные сценарии использования**

 Aspose.Cells предоставляет возможность экспорта рабочего листа CSS отдельно при преобразовании файла Excel в HTML. Пожалуйста, используйте[**HtmlSaveOptions.ExportWorksheetCSSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately) свойство для этой цели и установите его в**истинный** при сохранении файла Excel в формате HTML.

## **Экспорт рабочего листа CSS отдельно в выводе HTML**

Следующий пример кода создает файл Excel, добавляет некоторый текст в ячейку**В5** в**Красный**цвет, а затем сохраняет его в формате HTML, используя[**HtmlSaveOptions.ExportWorksheetCSSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately) имущество. Пожалуйста, смотрите[вывод HTML](60489766.zip) сгенерированный кодом для справки. Ты найдешь**таблица стилей.css**внутри него как результат примера кода.

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportWorksheetCSSSeparatelyInOutputHTML.cs" >}}

## **Экспорт книги с одним листом в HTML**

Когда рабочая книга с несколькими листами преобразуется в HTML с помощью Aspose.Cells, создается файл HTML вместе с папкой, содержащей CSS и несколько файлов HTML. Когда этот файл HTML открыт в браузере, вкладки видны. Такое же поведение требуется для книги с одним листом при ее преобразовании в HTML. Раньше для книг с одним листом не создавалась отдельная папка, и создавался только файл HTML. Такой файл HTML не отображает вкладку при открытии в браузере. MS Excel создает правильную папку и HTML для одного листа, и, следовательно, такое же поведение реализуется с использованием API-интерфейсов Aspose.Cells. Образец файла можно загрузить по следующей ссылке для использования в примере кода ниже:

[образецSingleSheet.xlsx](79527937.xlsx)

## **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetSingleSheetTabNameInHtml-1.cs" >}}
