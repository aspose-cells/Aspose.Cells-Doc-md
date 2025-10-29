---
title: Печать и предварительный просмотр книги
linktitle: Печать и предварительный просмотр
type: docs
weight: 70
url: /ru/python-net/workbook-and-worksheet-print-preview/
description: Aspose.Cells для Python via .NET поддерживает печать и предварительный просмотр файлов Excel без установки Microsoft Excel.
---

{{% alert color="primary" %}}

После создания листа часто хочется напечатать его копию на бумаге. В этой статье объясняется, как печатать таблицы с помощью Aspose.Cells для Python via .NET.

{{% /alert %}}

## **Введение в печать**

Microsoft Excel предполагает, что вы хотите распечатать всю область листа, если не указана выделенная область. Чтобы печатать с помощью Aspose.Cells для Python via .NET, сначала импортируйте пространство имен aspose.cells.rendering в программу. В нем есть несколько полезных классов, например, [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) и [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender).

### **Печать с использованием SheetRender**

Класс [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/) представляет собой рабочий лист и имеет метод [**to_printer**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_printer/), который может напечатать рабочий лист. В следующем примере кода показано, как напечатать рабочий лист.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintingExcelWorkbookUsingSheetRender.py" >}}

### **Печать с использованием WorkbookRender**

Для печати всего рабочего книги переберите листы и напечатайте их или используйте класс [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintingUsingWorkbookRender-1.py" >}}

{{% alert color="primary" %}}

Aspose.Cells для Python via .NET также предоставляет перегрузки для методов [**WorkbookRender.to_printer()**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_printer/#str-str) и [**SheetRender.to_printer()**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_printer/#aspose.pydrawing.printing.PrinterSettings), поэтому можно установить имя печатной задачи при печати таблиц Excel. По умолчанию все задания печати создаются с именем "Document".

{{% /alert %}}

## **Предварительный просмотр печати**

Могут возникнуть случаи, когда файлы Excel с миллионами страниц нужно преобразовать в PDF или изображения. Обработка таких файлов потребует много времени и ресурсов. В таких случаях функция предварительного просмотра печати рабочей книги и рабочего листа может оказаться полезной. Перед преобразованием таких файлов пользователь может проверить общее количество страниц и затем решить, нужно ли преобразовать файл или нет. Эта статья фокусируется на использовании классов [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) и [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) для определения общего числа страниц.

Aspose.Cells для Python via .NET предоставляет функцию предварительного просмотра печати. Для этого API предоставляет классы [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) и [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview). Для создания предварительного просмотра всего файла создайте экземпляр класса [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview), передав в конструктор объекты [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) и [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions). Класс [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) предоставляет метод [**evaluated_page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview/evaluated_page_count/), возвращающий количество страниц в созданном предварительном просмотре. Аналогично классу [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview), класс [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) используется для генерации предварительного просмотра для конкретного листа. Для создания предварительного просмотра листа создайте экземпляр класса [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview), передав в конструктор объекты [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) и [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions). Класс [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) также предоставляет метод [**SheetPrintingPreview.evaluated_page_count**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview/evaluated_page_count/), возвращающий количество страниц в созданном предварительном просмотре.

Следующий фрагмент кода демонстрирует использование обоих классов [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookprintingpreview) и [**SheetPrintingPreview**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetprintingpreview) с использованием [образцового файла Excel](94896177.xlsx).

### **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-PrintPreview-1.py" >}}

Следующим выводом является результат выполнения вышеприведенного кода.

### **Вывод в консоль**

{{< highlight java >}}

Workbook page count: 1
Worksheet page count: 1

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
