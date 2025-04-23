---
title: Вставка и удаление строк и столбцов файлов Excel
linktitle: Вставка и удаление строк и столбцов
type: docs
weight: 70
url: /ru/net/inserting-and-deleting-rows-and-columns/
description: В этой статье показано, как вставлять и удалять строки и столбцы с помощью Aspose.Cells for .NET API.
keywords: Aspose.Cells C# управлять строками и столбцами, вставлять строки и столбцы, удалять строки и столбцы
---

## **Введение**

При создании нового листа Excel с нуля или работе с существующим листом нам может потребоваться добавить дополнительные строки или столбцы для размещения большего объема данных. Напротив, также может потребоваться удалить строки или столбцы из указанных позиций в листе.
Для выполнения этих требований Aspose.Cells предоставляет очень простой набор классов и методов, рассматриваемых ниже.

### **Управлять строками и столбцами**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection), позволяющую получить доступ к каждому листу Excel в файле. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) предоставляет коллекцию [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells), представляющую все ячейки на листе.

Коллекция [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) предоставляет несколько методов для управления строками и столбцами на листе. Некоторые из них рассматриваются ниже.

{{% alert color="primary" %}}

При добавлении строк или столбцов содержимое на рабочем листе сдвигается вниз или вправо, а если строки или столбцы удаляются, содержимое сдвигается вверх или влево.

{{% /alert %}}


## **Вставить строки и столбцы**

### **Как вставить строку**

Вставьте строку на листе в любом месте, вызвав метод [**InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Метод [**InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) принимает индекс строки, куда будет вставлена новая строка.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARow-1.cs" >}}

### **Как вставить несколько строк**

Для вставки нескольких строк на лист, вызовите метод [**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Метод [**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) принимает два параметра:

- Индекс строки, индекс строки, с которой будут вставлены новые строки.
- Количество строк, общее количество строк, которые необходимо вставить.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.cs" >}}

### **Как вставить строку с форматированием**

Чтобы вставить строку с параметрами форматирования, используйте перегрузку [**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows), которая принимает [**InsertOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) в качестве параметра. Установите свойство [**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) класса [**InsertOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) с перечислением [**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype). Перечисление [**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) имеет три элемента, перечисленные ниже.

- SameAsAbove: Форматирует строку так же, как и строка выше.
- SameAsBelow: Форматирует строку так же, как и строка ниже.
- Очистить: Очищает форматирование.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.cs" >}}

### **Как вставить столбец**

Разработчики также могут вставлять столбец в лист на любой позиции, вызвав метод [**InsertColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Метод [**InsertColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) принимает индекс столбца, куда будет вставлен новый столбец.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingAColumn-1.cs" >}}

## **Удалить строки и столбцы**

### **Как удалить несколько строк**

Чтобы удалить несколько строк из листа, вызовите метод [**DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Метод [**DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) принимает два параметра:

- Индекс строки, индекс строки, с которой строки будут удалены.
- Количество строк, общее количество строк, которые нужно удалить.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.cs" >}}


### **Как удалить столбец**

Чтобы удалить столбец из листа в любом месте, вызовите метод [**DeleteColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) коллекции [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). Метод [**DeleteColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) принимает индекс удаляемого столбца.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingAColumn-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
