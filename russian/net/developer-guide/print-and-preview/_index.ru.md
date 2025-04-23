---
title: Печать и предварительный просмотр книги
linktitle: Печать и предварительный просмотр
type: docs
weight: 70
url: /ru/net/workbook-and-worksheet-print-preview/
description: Aspose.Cells поддерживает печать и предварительный просмотр файлов Excel без установки Microsoft Excel.
---

{{% alert color="primary" %}}

После создания рабочего листа вы часто хотите напечатать его на бумаге. В этой статье объясняется, как распечатать электронные таблицы с помощью Aspose.Cells.

{{% /alert %}}

## **Введение в печать**

Microsoft Excel предполагает, что вы хотите напечатать всю область рабочего листа, если не указано иное. Для печати с помощью Aspose.Cells сначала импортируйте пространство имен Aspose.Cells.Rendering в программу. В нем есть несколько полезных классов, например, [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) и [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender).

### **Печать с использованием SheetRender**

Класс [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) представляет собой рабочий лист и имеет метод [**ToPrinter**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toprinter/index), который может напечатать рабочий лист. В следующем примере кода показано, как напечатать рабочий лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingSheetRender-PrintingExcelWorkbookUsingSheetRender.cs" >}}

### **Печать с использованием WorkbookRender**

Для печати всего рабочего книги переберите листы и напечатайте их или используйте класс [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingWorkbookRender-1.cs" >}}

{{% alert color="primary" %}}

Aspose.Cells также предоставляет перегрузки для методов [**WorkbookRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.workbookrender/toprinter/methods/3) и [**SheetRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toprinter/methods/2), поэтому можно установить имя печатного задания при печати электронных таблиц Excel. По умолчанию все печатные задания создаются с именем "Документ".

{{% /alert %}}

## **Предварительный просмотр печати**

Могут возникнуть случаи, когда файлы Excel с миллионами страниц нужно преобразовать в PDF или изображения. Обработка таких файлов потребует много времени и ресурсов. В таких случаях функция предварительного просмотра печати рабочей книги и рабочего листа может оказаться полезной. Перед преобразованием таких файлов пользователь может проверить общее количество страниц и затем решить, нужно ли преобразовать файл или нет. Эта статья фокусируется на использовании классов [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) и [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) для определения общего числа страниц.

Aspose.Cells предоставляет функцию предварительного просмотра печати. Для этого API предоставляет классы [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) и [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview). Чтобы создать предварительный просмотр печати всей рабочей книги, создайте экземпляр класса [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview), передавая объекты [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) и [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) конструктору. Класс [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) предоставляет метод [**EvaluatedPageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview/properties/evaluatedpagecount), который возвращает количество страниц в сгенерированном предварительном просмотре. Аналогично классу [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview), класс [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) используется для создания предварительного просмотра печати для конкретного рабочего листа. Чтобы создать предварительный просмотр печати рабочего листа, создайте экземпляр класса [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview), передавая объекты [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) и [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) конструктору. Класс [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) также предоставляет метод [**EvaluatedPageCount**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview/properties/evaluatedpagecount), возвращающий количество страниц в сгенерированном предварительном просмотре.

Следующий фрагмент кода демонстрирует использование обоих классов [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) и [**SheetPrintingPreview**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) с использованием [образцового файла Excel](94896177.xlsx).

### **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-PrintPreview-1.cs" >}}

Следующим выводом является результат выполнения вышеприведенного кода.

### **Вывод в консоль**

{{< highlight java >}}

Workbook page count: 1
Worksheet page count: 1

{{< /highlight >}}

## **Продвинутые темы**
- [Настройка шрифтов для отображения электронных таблиц](/cells/ru/net/configuring-fonts-for-rendering-spreadsheets/)
- [Преобразование рабочего листа в изображение - Удаление пустого места вокруг данных](/cells/ru/net/convert-worksheet-to-image-remove-whitespace-around-data/)
- [Преобразование Рабочего листа в изображение и Рабочего листа в изображение по странице](/cells/ru/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [Преобразование рабочего листа в изображение с использованием параметров ImageOrPrint](/cells/ru/net/converting-worksheet-to-image-using-imageorprint-options/)
- [Экспорт диапазона ячеек листа в изображение](/cells/ru/net/export-range-of-cells-in-a-worksheet-to-image/)
- [Экспорт листа или диаграммы в изображение с заданными шириной и высотой](/cells/ru/net/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Извлечение изображений из листов с использованием параметров ImageOrPrintOptions](/cells/ru/net/extract-images-from-worksheets-using-imageorprintoptions/)
- [Генерация миниатюры листа](/cells/ru/net/generate-thumbnail-of-the-worksheet/)
- [Вывод пустой страницы, когда нечего печатать](/cells/ru/net/output-blank-page-when-there-is-nothing-to-print/)
- [Настройки страницы и опции печати](/cells/ru/net/page-setup-and-printing-options/)
- [Печать диапазона страниц с использованием SheetRender и WorkbookRender](/cells/ru/net/printing-range-of-pages-using-sheetrender-and-workbookrender/)
- [Отобразить последовательность страниц с использованием свойств PageIndex и PageCount класса ImageOrPrintOptions](/cells/ru/net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [Отобразить Рабочий лист на графический контекст](/cells/ru/net/render-worksheet-to-graphic-context/)
- [Указание индивидуального или частного набора шрифтов для рендеринга книги](/cells/ru/net/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
- [Укажите название задания или документа при печати с помощью Aspose.Cells](/cells/ru/net/specify-job-or-document-name-while-printing-with-aspose-cells/)
{{< app/cells/assistant language="csharp" >}}
