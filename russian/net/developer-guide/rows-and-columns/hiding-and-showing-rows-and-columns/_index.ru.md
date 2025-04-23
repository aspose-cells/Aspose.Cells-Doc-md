---
title: Скрытие и отображение строк и столбцов
type: docs
weight: 60
url: /ru/net/hiding-and-showing-rows-and-columns/
---

{{% alert color="primary" %}}

Иногда имеет смысл скрывать определенные строки или столбцы на листе и показывать их позже. Эту возможность предоставляет Microsoft Excel, также как и Aspose.Cells.

{{% /alert %}}

## **Управление видимостью строк и столбцов**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection), позволяющий разработчикам обращаться к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), представляющую все ячейки на листе. Коллекция [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) предоставляет несколько методов для управления строками или столбцами на листе. Некоторые из них рассмотрены ниже.

### **Скрытие строк и столбцов**

Разработчики могут скрыть строку или столбец, вызвав методы [**HideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) и [**HideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) соответственно из коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Оба метода принимают индекс строки и столбца в качестве параметра для скрытия конкретной строки или столбца.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Также можно скрыть строку или столбец, установив высоту строки или ширину столбца равным 0 соответственно.

{{% /alert %}}

### **Показ строк и столбцов**

Разработчики могут показать любую скрытую строку или столбец, вызвав методы [**UnhideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) и [**UnhideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) из коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Оба метода принимают два параметра:

- **Индекс строки или столбца** - индекс строки или столбца, который используется для отображения конкретной строки или столбца.
- **Высота строки или ширина столбца** - высота строки или ширина столбца, назначенные строке или столбцу после отображения.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

При восстановлении ширины скрытого столбца до ранее назначенной ширины или до его исходной ширины рекомендуется отобразить столбец с отрицательной шириной. Например: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **Скрытие нескольких строк и столбцов**

Разработчики могут скрыть сразу несколько строк или столбцов, вызвав методы [**HideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) и [**HideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) из коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). Оба метода принимают начальный индекс строки или столбца и количество строк или столбцов, которые должны быть скрыты.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

Также можно использовать методы [**UnhideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) и [**UnhideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns) класса [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), чтобы сделать видимыми несколько строк и столбцов.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
