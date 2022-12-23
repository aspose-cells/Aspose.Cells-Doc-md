---
title: Печать и предварительный просмотр книги
linktitle: Печать и предварительный просмотр
type: docs
weight: 70
url: /ru/net/workbook-and-worksheet-print-preview/
description: Aspose.Cells поддерживает печать и предварительный просмотр файлов Excel без установки Excel Microsoft.
---
{{% alert color="primary" %}}

После создания рабочего листа часто требуется распечатать его твердую копию. В этой статье объясняется, как печатать электронные таблицы с помощью Aspose.Cells.

{{% /alert %}}

## **Введение в печать**

Microsoft Excel предполагает, что вы хотите напечатать всю область рабочего листа, если вы не укажете выделение. Для печати с использованием Aspose.Cells сначала импортируйте в программу пространство имен Aspose.Cells.Rendering. Он имеет несколько полезных классов, например,[**Листрендеринг**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) и[**Рабочая книгаВизуализация**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender).

### **Печать с помощью SheetRender**

[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) класс представляет рабочий лист и имеет[**Принтер**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toprinter/index)метод, который может распечатать рабочий лист. В следующем примере кода показано, как распечатать лист.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingSheetRender-PrintingExcelWorkbookUsingSheetRender.cs" >}}

### **Печать с помощью WorkbookRender**

 Чтобы распечатать всю книгу, выполните итерацию по листам и распечатайте их или используйте[**Рабочая книгаВизуализация**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)учебный класс.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingUsingWorkbookRender-1.cs" >}}

{{% alert color="primary" %}}

 Aspose.Cells также обеспечивает перегрузки для[**WorkbookRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.workbookrender/toprinter/methods/3) и[**SheetRender.ToPrinter()**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toprinter/methods/2) методы, поэтому можно установить имя задания на печать при печати электронных таблиц Excel. По умолчанию все задания на печать создаются с именем «Документ».

{{% /alert %}}

## **Предварительный просмотр печати**

Могут быть случаи, когда файлы Excel с миллионами страниц необходимо преобразовать в PDF или изображения. Обработка таких файлов потребует много времени и ресурсов. В таких случаях функция предварительного просмотра рабочей книги и рабочего листа может оказаться полезной. Перед преобразованием таких файлов пользователь может проверить общее количество страниц, а затем решить, следует ли преобразовать файл или нет. В этой статье основное внимание уделяется использованию[**Рабочая книгаПечатьПредварительный просмотр**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)и[**ЛистПечатьПредварительный просмотр**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)классы, чтобы узнать общее количество страниц.

 Aspose.Cells предоставляет функцию предварительного просмотра перед печатью. Для этого API предоставляет[**Рабочая книгаПечатьПредварительный просмотр**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) и[**ЛистПечатьПредварительный просмотр**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) классы. Чтобы создать предварительный просмотр всей книги, создайте экземпляр[**Рабочая книгаПечатьПредварительный просмотр**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) класс, пройдя[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) и[**Имажеорпринтоптионс**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions) объекты конструктору.[**Рабочая книгаПечатьПредварительный просмотр**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview) класс предоставляет[**Эвалуатедпажекаунт**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview/properties/evaluatedpagecount) метод, который возвращает количество страниц в сгенерированном предварительном просмотре. Похожий на[**Рабочая книгаПечатьПредварительный просмотр**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)класс,[**ЛистПечатьПредварительный просмотр**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)Класс используется для создания предварительного просмотра печати для определенного рабочего листа. Чтобы создать предварительный просмотр рабочего листа, создайте экземпляр[**ЛистПечатьПредварительный просмотр**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)класс, пройдя[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)и[**Имажеорпринтоптионс**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)объекты конструктору.[**ЛистПечатьПредварительный просмотр**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview)класс также предоставляет[**Эвалуатедпажекаунт**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview/properties/evaluatedpagecount)метод, который возвращает количество страниц в сгенерированном предварительном просмотре.

Следующий фрагмент кода демонстрирует использование обоих[**Рабочая книгаПечатьПредварительный просмотр**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookprintingpreview)и[**ЛистПечатьПредварительный просмотр**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetprintingpreview) занятия с помощью[образец эксель файла](94896177.xlsx).

### **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-PrintPreview-1.cs" >}}

Ниже приведен вывод, полученный при выполнении вышеуказанного кода.

### **Консольный вывод**

Количество страниц рабочей книги: 1
Количество страниц рабочего листа: 1


## **Предварительные темы**
- [Настройка шрифтов для визуализации электронных таблиц](/cells/ru/net/configuring-fonts-for-rendering-spreadsheets/)
- [Преобразование рабочего листа в изображение — удаление пробелов вокруг данных](/cells/ru/net/convert-worksheet-to-image-remove-whitespace-around-data/)
- [Преобразование рабочего листа в изображение и рабочего листа в изображение на странице](/cells/ru/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [Преобразование рабочего листа в изображение с использованием параметров ImageOrPrint](/cells/ru/net/converting-worksheet-to-image-using-imageorprint-options/)
- [Экспорт диапазона Cells на листе в изображение](/cells/ru/net/export-range-of-cells-in-a-worksheet-to-image/)
- [Экспорт рабочего листа или диаграммы в изображение с желаемой шириной и высотой](/cells/ru/net/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Извлечение изображений из рабочих листов с помощью ImageOrPrintOptions](/cells/ru/net/extract-images-from-worksheets-using-imageorprintoptions/)
- [Создать миниатюру рабочего листа](/cells/ru/net/generate-thumbnail-of-the-worksheet/)
- [Вывод пустой страницы, когда нечего печатать](/cells/ru/net/output-blank-page-when-there-is-nothing-to-print/)
- [Параметры страницы и параметры печати](/cells/ru/net/page-setup-and-printing-options/)
- [Печать диапазона страниц с использованием SheetRender и WorkbookRender](/cells/ru/net/printing-range-of-pages-using-sheetrender-and-workbookrender/)
- [Визуализация последовательности страниц с использованием свойств PageIndex и PageCount в ImageOrPrintOptions](/cells/ru/net/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [Рендеринг рабочего листа в графическом контексте](/cells/ru/net/render-worksheet-to-graphic-context/)
- [Укажите индивидуальный или частный набор шрифтов для визуализации рабочей книги](/cells/ru/net/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
- [Укажите имя задания или документа при печати с помощью Aspose.Cells.](/cells/ru/net/specify-job-or-document-name-while-printing-with-aspose-cells/)
