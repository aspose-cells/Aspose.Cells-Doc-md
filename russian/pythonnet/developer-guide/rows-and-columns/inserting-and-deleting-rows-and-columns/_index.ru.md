---
title: Вставка и удаление строк и столбцов файлов Excel
linktitle: Вставка и удаление строк и столбцов
type: docs
weight: 70
url: /ru/python-net/inserting-and-deleting-rows-and-columns/
description: В этой статье показано, как вставлять и удалять строки и столбцы с помощью API Aspose.Cells для Python via .NET.
keywords: Библиотека Python Excel, Aspose.Cells Python управляет строками и столбцами, вставка строк и столбцов в Python, удаление строк и столбцов в Python, удаление строк и столбцов.
---

## **Введение**

При создании нового листа Excel с нуля или работе с существующим листом нам может потребоваться добавить дополнительные строки или столбцы для размещения большего объема данных. Напротив, также может потребоваться удалить строки или столбцы из указанных позиций в листе.
Для удовлетворения этих требований Aspose.Cells для Python via .NET предоставляет очень простой набор классов и методов, описанных ниже.

### **Управлять строками и столбцами**

Aspose.Cells для Python via .NET предоставляет класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection), позволяющую получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) предоставляет коллекцию [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells), представляющую все ячейки на листе.

Коллекция [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) предоставляет несколько методов для управления строками и столбцами на листе. Некоторые из них рассматриваются ниже.

{{% alert color="primary" %}}

При добавлении строк или столбцов содержимое на рабочем листе сдвигается вниз или вправо, а если строки или столбцы удаляются, содержимое сдвигается вверх или влево.

{{% /alert %}}


## **Вставить строки и столбцы**

### **Как вставить строку**

Вставьте строку на листе в любом месте, вызвав метод [**insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row/) коллекции [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Метод [**insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row/) принимает индекс строки, куда будет вставлена новая строка.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingARow-1.py" >}}

### **Как вставить несколько строк**

Для вставки нескольких строк на лист, вызовите метод [**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int) коллекции [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Метод [**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int) принимает два параметра:

- Индекс строки, индекс строки, с которой будут вставлены новые строки.
- Количество строк, общее количество строк, которые необходимо вставить.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.py" >}}

### **Как вставить строку с форматированием**

Чтобы вставить строку с параметрами форматирования, используйте перегрузку [**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int-aspose.cells.InsertOptions), которая принимает [**InsertOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions) в качестве параметра. Установите свойство [**copy_format_type**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions/copy_format_type/) класса [**InsertOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions) с перечислением [**CopyFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells/copyformattype/). Перечисление [**CopyFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells/copyformattype/) имеет три элемента, перечисленные ниже.

- SAME_AS_ABOVE: Форматирует строку так же, как и выше.
- SAME_AS_BELOW: Форматирует строку так же, как и ниже.
- CLEAR: Очищает форматирование.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.py" >}}

### **Как вставить столбец**

Разработчики также могут вставлять столбец в лист на любой позиции, вызвав метод [**insert_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_column/#int) коллекции [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Метод [**insert_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_column/#int) принимает индекс столбца, куда будет вставлен новый столбец.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingAColumn-1.py" >}}

## **Удалить строки и столбцы**

### **Как удалить несколько строк**

Чтобы удалить несколько строк из листа, вызовите метод [**delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/#int-int) коллекции [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Метод [**delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/#int-int) принимает два параметра:

- Индекс строки, индекс строки, с которой строки будут удалены.
- Количество строк, общее количество строк, которые нужно удалить.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.py" >}}


### **Как удалить столбец**

Чтобы удалить столбец из листа в любом месте, вызовите метод [**delete_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_column/#int) коллекции [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Метод [**delete_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_column/#int) принимает индекс удаляемого столбца.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-DeletingAColumn-1.py" >}}
