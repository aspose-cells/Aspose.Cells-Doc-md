---
title: Печать и предварительный просмотр рабочей книги с помощью C++
linktitle: Печать и предварительный просмотр
type: docs
weight: 70
url: /ru/cpp/workbook-and-worksheet-print-preview/
description: Aspose.Cells поддерживает печать и предварительный просмотр Excel файлов без установки Microsoft Excel с использованием C++
---

{{% alert color="primary" %}}

После создания рабочего листа вы часто хотите напечатать его на бумаге. В этой статье объясняется, как распечатать электронные таблицы с помощью Aspose.Cells.

{{% /alert %}}

## **Введение в печать**

Microsoft Excel предполагает, что вы хотите напечатать всю область рабочего листа, если не указано иное. Для печати с помощью Aspose.Cells сначала импортируйте пространство имен Aspose.Cells.Rendering в программу. В нем есть несколько полезных классов, например, [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) и [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/).


## **Предварительный просмотр печати**

Могут возникнуть случаи, когда файлы Excel с миллионами страниц нужно преобразовать в PDF или изображения. Обработка таких файлов потребует много времени и ресурсов. В таких случаях функция предварительного просмотра печати рабочей книги и рабочего листа может оказаться полезной. Перед преобразованием таких файлов пользователь может проверить общее количество страниц и затем решить, нужно ли преобразовать файл или нет. Эта статья фокусируется на использовании классов [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) и [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) для определения общего числа страниц.

Aspose.Cells предоставляет функцию предварительного просмотра печати. Для этого API предоставляет классы [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) и [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/). Чтобы создать предварительный просмотр печати всей рабочей книги, создайте экземпляр класса [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/), передавая объекты [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) и [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) конструктору. Класс [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) предоставляет метод [**GetEvaluatedPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/getevaluatedpagecount/), который возвращает количество страниц в сгенерированном предварительном просмотре. Аналогично классу [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/), класс [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) используется для создания предварительного просмотра печати для конкретного рабочего листа. Чтобы создать предварительный просмотр печати рабочего листа, создайте экземпляр класса [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/), передавая объекты [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) и [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) конструктору. Класс [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) также предоставляет метод [**GetEvaluatedPageCount()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/getevaluatedpagecount/), возвращающий количество страниц в сгенерированном предварительном просмотре.

Следующий фрагмент кода демонстрирует использование обоих классов [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookprintingpreview/) и [**SheetPrintingPreview**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetprintingpreview/) с использованием [образцового файла Excel](94896177.xlsx).

### **Образец кода**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Create image or print options
    ImageOrPrintOptions imgOptions;

    // Create workbook printing preview
    WorkbookPrintingPreview preview(workbook, imgOptions);
    cout << "Workbook page count: " << preview.GetEvaluatedPageCount() << endl;

    // Create sheet printing preview
    SheetPrintingPreview preview2(workbook.GetWorksheets().Get(0), imgOptions);
    cout << "Worksheet page count: " << preview2.GetEvaluatedPageCount() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

Следующим выводом является результат выполнения вышеприведенного кода.

### **Вывод в консоль**

{{< highlight java >}}

Workbook page count: 1
Worksheet page count: 1

{{< /highlight >}}

## **Продвинутые темы**
- [Настройка шрифтов для отображения электронных таблиц](/cells/ru/cpp/configuring-fonts-for-rendering-spreadsheets/)
- [Преобразование рабочего листа в изображение - Удаление пустого места вокруг данных](/cells/ru/cpp/convert-worksheet-to-image-remove-whitespace-around-data/)
- [Преобразование Рабочего листа в изображение и Рабочего листа в изображение по странице](/cells/ru/cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)
- [Преобразование рабочего листа в изображение с использованием параметров ImageOrPrint](/cells/ru/cpp/converting-worksheet-to-image-using-imageorprint-options/)
- [Экспорт диапазона ячеек листа в изображение](/cells/ru/cpp/export-range-of-cells-in-a-worksheet-to-image/)
- [Экспорт листа или диаграммы в изображение с заданными шириной и высотой](/cells/ru/cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
- [Извлечение изображений из листов с использованием параметров ImageOrPrintOptions](/cells/ru/cpp/extract-images-from-worksheets-using-imageorprintoptions/)
- [Генерация миниатюры листа](/cells/ru/cpp/generate-thumbnail-of-the-worksheet/)
- [Вывод пустой страницы, когда нечего печатать](/cells/ru/cpp/output-blank-page-when-there-is-nothing-to-print/)
- [Настройки страницы и опции печати](/cells/ru/cpp/page-setup-and-printing-options/)
- [Отобразить последовательность страниц с использованием свойств PageIndex и PageCount класса ImageOrPrintOptions](/cells/ru/cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
- [Отобразить Рабочий лист на графический контекст](/cells/ru/cpp/render-worksheet-to-graphic-context/)
- [Указание индивидуального или частного набора шрифтов для рендеринга книги](/cells/ru/cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
