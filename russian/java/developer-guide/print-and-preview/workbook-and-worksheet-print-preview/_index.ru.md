---
title: Предварительный просмотр печати рабочей книги и листа
type: docs
weight: 130
url: /ru/java/workbook-and-worksheet-print-preview/
---

## **Сценарий использования**

Могут возникнуть случаи, когда файлы Excel с миллионами страниц требуется преобразовать в PDF или изображения. Обработка таких файлов потребует много времени и ресурсов. В таких случаях функция Предварительного просмотра печати рабочей книги и листа может оказаться полезной. Перед преобразованием таких файлов пользователь может проверить общее количество страниц и затем решить, требуется ли преобразование файла. В данной статье рассматривается использование классов [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) и [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) для определения общего количества страниц.

## **Предварительный просмотр печати рабочей книги и листа**

Aspose.Cells предоставляет функцию предварительного просмотра печати. Для этого API предоставляет классы [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) и [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview). Для создания предварительного просмотра всей рабочей книги создайте экземпляр класса [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview), передав объекты [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) и [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) в конструктор. Класс [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) содержит метод [**EvaluatedPageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookprintingpreview#EvaluatedPageCount), который возвращает количество страниц в созданном предварительном просмотре. Аналогично классу [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview), класс [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) используется для создания предварительного просмотра для конкретного листа. Для создания предварительного просмотра листа создайте экземпляр класса [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview), передав объекты [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) и [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) в конструктор. Класс [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) также предоставляет метод [**EvaluatedPageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetprintingpreview#EvaluatedPageCount), который возвращает количество страниц в созданном предварительном просмотре.

Следующий фрагмент кода демонстрирует использование как класса [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview), так и класса [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview), используя [образец excel-файла](Book1.xlsx).

### **Образец кода**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-PrintPreview-1.java" >}}

Следующим выводом является результат выполнения вышеприведенного кода.

### **Вывод в консоль**

{{< highlight java >}}

Workbook page count: 1</br>
Worksheet page count: 1

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
