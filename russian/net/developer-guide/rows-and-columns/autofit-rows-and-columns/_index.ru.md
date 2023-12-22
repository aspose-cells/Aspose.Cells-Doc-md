---
title: Автоподбор строк и столбцов
type: docs
weight: 20
url: /ru/net/autofit-rows-and-columns/
description: В этой статье показано, как автоматически подогнать строки, столбцы, строки объединенных ячеек и строку в диапазоне ячеек по номеру Aspose.Cells for .NET API.
keywords: Autofit rows, autofit columns, autofit row in a range of cells, autofit rows of merged cells
---
{{% alert color="primary" %}}

Microsoft Excel позволяет пользователям автоматически изменять ширину и высоту ячеек в соответствии с их содержимым. Эта функция также доступна по номеру Aspose.Cells, поэтому разработчики могут автоматически изменять размеры ячейки во время выполнения.

{{% /alert %}}

##  **Авто Установка**

Aspose.Cells предоставляет[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook)класс, представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook)класс содержит[**Рабочие листы**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)коллекция, которая обеспечивает доступ к каждому листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) сорт.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Класс предоставляет широкий спектр свойств и методов для управления листом. В этой статье рассматривается использование[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)class для автоподбора строк или столбцов.

###  **Автоподбор строк – простой**

 Самый простой подход к автоматическому изменению ширины и высоты строки — вызвать метод[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) сорт[**Автоподбор строки**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index) метод.[**Автоподбор строки**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrow/index)Метод принимает индекс строки (строки, размер которой нужно изменить) в качестве параметра.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsandColumns-1.cs" >}}

###  **Как автоподбор строки в диапазоне Cells**

 Строка состоит из множества столбцов. Aspose.Cells позволяет разработчикам автоматически подгонять строку на основе содержимого диапазона ячеек внутри строки, вызывая перегруженную версию метода[**Автоподбор строки**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)метод. Он принимает следующие параметры:

- *Индекс строки**: индекс строки, которая будет автоматически подогнана.
- *Индекс первого столбца** — индекс первого столбца строки.
- *Индекс последнего столбца** – индекс последнего столбца строки.

[**Автоподбор строки**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitrow/methods/1)Метод проверяет содержимое всех столбцов в строке, а затем автоматически подгоняет строку.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowinSpecificRange-1.cs" >}}

###  **Как автоматически подогнать столбец в диапазоне Cells**

 Столбец состоит из множества строк. Можно автоматически подогнать столбец на основе содержимого диапазона ячеек столбца, вызвав перегруженную версию[**Автоподбор столбца**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)метод, который принимает следующие параметры:

- *Индекс столбца**: индекс столбца, который будет автоматически подставлен.
- *Индекс первой строки** — индекс первой строки столбца.
- *Индекс последней строки** — индекс последней строки столбца.

[**Автоподбор столбца**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1)Метод проверяет содержимое всех строк в столбце, а затем автоматически подгоняет столбец.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitColumninSpecificRange-1.cs" >}}

###  **Как автоматически подогнать строки для объединенных Cells**

 С помощью Aspose.Cells можно автоматически подогнать строки даже для ячеек, которые были объединены с помощью[**Параметры автоподборщика**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) API. [**Параметры автоподборщика**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)класс обеспечивает[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype) свойство, которое можно использовать для автоматического подбора строк для объединенных ячеек.[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/properties/autofitmergedcellstype)принимает[**AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype) перечисляемый, который имеет следующие члены.

- Нет: игнорировать объединенные ячейки.
- FirstLine: увеличивает только высоту первой строки.
- LastLine: увеличивает высоту только последней строки.
- EachLine: увеличивает только высоту каждой строки.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-AutofitRowsforMergedCells-1.cs" >}}

{{% alert color="primary" %}}

 Вы также можете попробовать использовать перегруженные версии[**Автоподбор строк**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitrows) & [**Автоподбор столбцов**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/autofitcolumns) методы, принимающие диапазон строк/столбцов и экземпляр[**Параметры автоподборщика**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions) чтобы автоматически подогнать выбранные строки/столбцы по вашему желанию[**Параметры автоподборщика**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)соответственно.

Сигнатуры вышеупомянутых методов следующие:

1.  AutoFitRows(int startRow, int endRow,[**Параметры автоподборщика**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)параметры)
1.  AutoFitColumns(int firstColumn, int LastColumn,[**Параметры автоподборщика**](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions)параметры)

{{% /alert %}}

##  **Важно знать**

{{% alert color="primary" %}}

Если ячейка объединена, методы автоподбора не будут применены, что аналогично Microsoft Excel. Эту проблему можно обойти, используя автофильтр API. Более того, если текст в ячейке переносится,[**Автоподбор столбца**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/autofitcolumn/methods/1) метод также не будет применяться. Еще одна вещь, которую вам нужно знать, это то, что*Автоподбор*методы требуют много времени. Поэтому вам следует вызывать эти методы как можно реже, чтобы обеспечить эффективность вашего приложения.

{{% /alert %}}

##  **Предварительные темы**
- [Автоподбор строк для объединенных Cells](/cells/ru/net/autofit-rows-for-merged-cells/)
