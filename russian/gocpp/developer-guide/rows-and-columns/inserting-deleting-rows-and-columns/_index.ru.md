---
title: Вставка, удаление строк и столбцов
type: docs
weight: 40
url: /ru/go-cpp/inserting-deleting-rows-and-columns/
---

## **Введение**

При создании новой рабочей книги с нуля или работы с существующей рабочей книгой нам может понадобиться добавить дополнительные строки или столбцы для размещения дополнительных данных. Наоборот, нам также может потребоваться удалить строки или столбцы из указанных позиций в рабочем листе. Для выполнения этих требований Aspose.Cells предоставляет очень простой набор классов и методов, описанных ниже.

### **Управление строками и столбцами**

Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/), который представляет файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) содержит коллекцию [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). Класс [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) содержит коллекцию [Cells](https://reference.aspose.com/cells/go-cpp/cells/), которая представляет все ячейки листа.

Коллекция [Cells](https://reference.aspose.com/cells/go-cpp/cells/) включает несколько методов для управления строками и столбцами в листе. Некоторые из них рассматриваются ниже.

{{% alert color="primary" %}}

При добавлении строк или столбцов содержимое на рабочем листе сдвигается вниз или вправо, а если строки или столбцы удаляются, содержимое сдвигается вверх или влево.

{{% /alert %}}

Вставьте строку в лист в любую точку, вызвав метод [InsertRow](https://reference.aspose.com/cells/go-cpp/cells/insertrow/) коллекции [Cells](https://reference.aspose.com/cells/go-cpp/cells/). Метод [InsertRow](https://reference.aspose.com/cells/go-cpp/cells/insertrow/) принимает индекс строки, в которую будет вставлена новая строка.
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertRow.go" >}}

#### **Вставка нескольких строк**

Для вставки нескольких строк в лист вызовите метод [InsertRows](https://reference.aspose.com/cells/go-cpp/cells/insertrows_int_int/) коллекции [Cells](https://reference.aspose.com/cells/go-cpp/cells/). Метод [InsertRows](https://reference.aspose.com/cells/go-cpp/cells/insertrowinsertrows_int_ints/) принимает два параметра:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertingMultipleRows.go" >}}

#### **Удаление нескольких строк**

Чтобы удалить несколько строк из листа, вызовите метод [DeleteRows](https://reference.aspose.com/cells/go-cpp/cells/deleterows_int_int_bool/) коллекции [Cells](https://reference.aspose.com/cells/go-cpp/cells/). Метод [DeleteRows](https://reference.aspose.com/cells/go-cpp/cells/deleterows_int_int_bool/) принимает два параметра:

- Индекс строки, индекс строки, с которой строки будут удалены.
- Количество строк, общее количество строк, которые нужно удалить.

#### **Вставить столбец**

Разработчики также могут вставить столбец в лист в любой точке, вызвав метод [InsertColumn](https://reference.aspose.com/cells/go-cpp/cells/insertcolumn_int/) коллекции [Cells](https://reference.aspose.com/cells/go-cpp/cells/). Метод [InsertColumn](https://reference.aspose.com/cells/go-cpp/cells/insertcolumn_int/) принимает индекс столбца, в который будет вставлен новый столбец.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertColumn.go" >}}

Чтобы удалить столбец из листа в любой точке, вызовите метод [DeleteColumn](https://reference.aspose.com/cells/go-cpp/cells/deletecolumn_int/) коллекции [Cells](https://reference.aspose.com/cells/go-cpp/cells/). Метод [DeleteColumn](https://reference.aspose.com/cells/go-cpp/cells/deletecolumn_int/) принимает индекс удаляемого столбца.
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteColumn.go" >}}
