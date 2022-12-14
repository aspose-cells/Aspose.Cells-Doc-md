---
title: Автоподбор строк и столбцов
type: docs
weight: 20
url: /ru/net/autofit-rows-and-columns/
---
{{% alert color="primary" %}}

Microsoft Excel позволяет пользователям автоматически изменять ширину и высоту ячеек в соответствии с их содержимым. Эта функция также доступна по номеру Aspose.Cells, поэтому разработчики могут автоматически изменять размер ячейки во время выполнения.

{{% /alert %}}

## **Автоматическая установка**

Aspose.Cells предоставляет[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook)класс, представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook)класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)коллекция, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Класс предоставляет широкий спектр свойств и методов для управления рабочим листом. В этой статье рассматривается использование[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)класс для автоподбора строк или столбцов.

### **Автоподбор строки — простой**

 Самый простой подход к автоматическому изменению ширины и высоты строки — вызвать метод[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) метод.[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index)метод принимает индекс строки (строки, размер которой нужно изменить) в качестве параметра.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsandColumns-1.cs" >}}

### **Автоподбор строки в диапазоне Cells**

 Строка состоит из множества столбцов. Aspose.Cells позволяет разработчикам автоматически подбирать строку на основе содержимого диапазона ячеек в строке, вызывая перегруженную версию[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)метод. Он принимает следующие параметры:

- **Индекс строки**, индекс строки, которая будет автоматически подобрана.
- **Индекс первого столбца**, индекс первого столбца строки.
- **Индекс последнего столбца**, индекс последнего столбца строки.

[**AutoFitRow**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)метод проверяет содержимое всех столбцов в строке, а затем автоматически подбирает строку.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowinSpecificRange-1.cs" >}}

### **Автоподбор столбца в диапазоне Cells**

 Столбец состоит из множества строк. Можно автоматически подогнать столбец на основе содержимого диапазона ячеек в столбце, вызвав перегруженную версию[**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)метод, который принимает следующие параметры:

- **Индекс столбца**индекс столбца, который будет автоматически подобран.
- **Индекс первой строки**, индекс первой строки столбца.
- **Индекс последней строки**, индекс последней строки столбца.

[**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)метод проверяет содержимое всех строк в столбце, а затем автоматически подбирает столбец.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitColumninSpecificRange-1.cs" >}}

### **Автоподбор строк для объединенных Cells**

 С помощью Aspose.Cells можно автоматически подбирать строки даже для ячеек, которые были объединены с помощью[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) API. [**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)класс предоставляет[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) свойство, которое можно использовать для автоподбора строк для объединенных ячеек.[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype)принимает[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype) перечислимое, которое имеет следующие члены.

- Нет: игнорировать объединенные ячейки.
- FirstLine: увеличивает высоту только первой строки.
- LastLine: увеличивает высоту только последней строки.
- EachLine: увеличивает только высоту каждой строки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsforMergedCells-1.cs" >}}

{{% alert color="primary" %}}

 Вы также можете попробовать использовать перегруженные версии[**AutoFitRows**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrows) & [**AutoFitColumns**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitcolumns) методы, принимающие диапазон строк/столбцов и экземпляр[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) для автоматической подгонки выбранных строк/столбцов к желаемому[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)соответственно.

Сигнатуры вышеупомянутых методов следующие:

1.  AutoFitRows(int startRow, int endRow,[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)опции)
1. AutoFitColumns(int firstColumn, int lastColumn,[**AutoFitterOptions**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)опции)

{{% /alert %}}

## **Важно знать**

{{% alert color="primary" %}}

 Если ячейка объединена, методы автоподбора не будут применяться, что аналогично поведению в Microsoft Excel. Обойти это можно с помощью автофильтра API. Более того, если текст в ячейке переносится,[**AutoFitColumn**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) метод также не будет применяться. Еще одна вещь, которую вам нужно знать, это то, что*Автоподбор*методы отнимают много времени. Таким образом, вы должны вызывать эти методы как можно реже, чтобы обеспечить эффективность вашего приложения.

{{% /alert %}}

## **Предварительные темы**
- [Автоподбор строк для объединенных Cells](/cells/ru/net/autofit-rows-for-merged-cells/)
