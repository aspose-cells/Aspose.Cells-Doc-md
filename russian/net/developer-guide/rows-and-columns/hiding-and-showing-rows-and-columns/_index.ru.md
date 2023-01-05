---
title: Скрытие и отображение строк и столбцов
type: docs
weight: 60
url: /ru/net/hiding-and-showing-rows-and-columns/
---
{{% alert color="primary" %}}

Иногда имеет смысл скрыть определенные строки или столбцы на листе и отобразить их позже. Microsoft Excel предоставляет эту функцию, как и Aspose.Cells.

{{% /alert %}}

## **Управление видимостью строк и столбцов**

 Aspose.Cells предоставляет класс,[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , представляющий файл Excel Microsoft.[**Рабочая тетрадь**](https://reference.aspose.com/cells/net/aspose.cells/workbook) класс содержит[**Рабочий листКоллекция**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) что позволяет разработчикам получать доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) учебный класс.[**Рабочий лист**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) класс предоставляет[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) коллекция, представляющая все ячейки рабочего листа.[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)collection предоставляет несколько методов для управления строками или столбцами на листе. Некоторые из них обсуждаются ниже.

### **Скрытие строк и столбцов**

 Разработчики могут скрыть строку или столбец, вызвав метод[**HideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) и[**СкрытьКолонку**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) методы[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)сборник соответственно. Оба метода принимают индекс строки и столбца в качестве параметра, чтобы скрыть конкретную строку или столбец.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Также можно скрыть строку или столбец, установив для высоты строки или ширины столбца значение 0 соответственно.

{{% /alert %}}

### **Отображение строк и столбцов**

 Разработчики могут показать любую скрытую строку или столбец, вызвав метод[**UnhideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) и[**Показать столбец**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) методы[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)сборник соответственно. Оба метода принимают два параметра:

- **Индекс строки или столбца** - индекс строки или столбца, который используется для отображения конкретной строки или столбца.
- **Высота строки или ширина столбца** - высота строки или ширина столбца, назначенная строке или столбцу после отображения.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

При отображении скрытого столбца, если вам нужно восстановить его ранее заданную ширину или исходную ширину, отобразите столбец с отрицательной шириной. Например: рабочий лист.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Скрытие нескольких строк и столбцов**

 Разработчики могут скрыть сразу несколько строк или столбцов, вызвав метод[**HideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) и[**Скрыть столбцы**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) методы[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)сборник соответственно. Оба метода принимают в качестве параметров начальный индекс строки или столбца и количество строк или столбцов, которые должны быть скрыты.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

 Также можно использовать[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) учебный класс'[**UnhideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) и[**Показать столбцы**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns)методы, чтобы сделать несколько строк и столбцов видимыми.

{{% /alert %}}
