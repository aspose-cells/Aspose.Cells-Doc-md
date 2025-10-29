---
title: Вставка, удаление строк и столбцов
type: docs
weight: 40
url: /ru/cpp/inserting-deleting-rows-and-columns/
---

## **Введение**
При создании новой рабочей книги с нуля или работы с существующей рабочей книгой нам может понадобиться добавить дополнительные строки или столбцы для размещения дополнительных данных. Наоборот, нам также может потребоваться удалить строки или столбцы из указанных позиций в рабочем листе. Для выполнения этих требований Aspose.Cells предоставляет очень простой набор классов и методов, описанных ниже.
### **Управление строками и столбцами**
Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), который представляет собой файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит коллекцию [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), которая позволяет получить доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен классом [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Класс [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет коллекцию [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/), представляющую все ячейки на рабочем листе.

Коллекция [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) предоставляет несколько методов для управления строками и столбцами на рабочем листе. Некоторые из них описаны ниже.

{{% alert color="primary" %}} 

При добавлении строк или столбцов содержимое на рабочем листе сдвигается вниз или вправо, а если строки или столбцы удаляются, содержимое сдвигается вверх или влево.

{{% /alert %}} 
#### **Вставить строку**
Вставьте строку в рабочий лист в любом месте, вызвав метод [InsertRow](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) из коллекции [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Метод [InsertRow](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) принимает индекс строки, куда будет вставлена новая строка.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertRow-new.cpp" >}}


#### **Вставка нескольких строк**
Для вставки нескольких строк в рабочий лист вызовите метод [InsertRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) из коллекции [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Метод [InsertRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) принимает два параметра:

- Индекс строки, индекс строки, с которой будут вставлены новые строки.
- Количество строк, общее количество строк, которые необходимо вставить.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertingMultipleRows-new.cpp" >}}


#### **Удаление нескольких строк**
Для удаления нескольких строк из рабочего листа вызовите метод [DeleteRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) из коллекции [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Метод [DeleteRows](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) принимает два параметра:

- Индекс строки, индекс строки, с которой строки будут удалены.
- Количество строк, общее количество строк, которые нужно удалить.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeletingMultipleRows-new.cpp" >}}


#### **Вставить столбец**
Разработчики также могут вставить столбец в рабочий лист в любом месте, вызвав метод [InsertColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) из коллекции [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Метод [InsertColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertcolumn/) принимает индекс столбца, куда будет вставлен новый столбец.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-InsertColumn-new.cpp" >}}


#### **Удалить столбец**
Чтобы удалить столбец из рабочего листа в любом месте, вызовите метод [DeleteColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) из коллекции [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/). Метод [DeleteColumn](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deletecolumn/) принимает индекс столбца для удаления.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-InsertingDeletingRowsAndColumns-DeleteColumn-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
