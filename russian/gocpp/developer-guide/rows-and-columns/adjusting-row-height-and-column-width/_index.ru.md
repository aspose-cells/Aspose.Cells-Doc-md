---
title: Настройка высоты строки и ширины столбца
type: docs
weight: 10
url: /ru/go-cpp/adjusting-row-height-and-column-width/
---

{{% alert color="primary" %}}

При работе с электронными таблицами и добавлении данных в строки или столбцы может потребоваться изменение высоты строк или ширины столбцов. Иногда применение форматирования к строкам или столбцам означает, что текущая высота или ширина должны измениться для отображения данных. Обычно пользователи изменяют высоту строк и ширины столбцов в среде WYSIWYG с помощью Microsoft Excel. Однако разработчики Aspose.Cells могут выполнять эти операции во время выполнения.

{{% /alert %}}

## **Работа со строками**

### **Изменение высоты строки**

Aspose.Cells предоставляет класс [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/), который представляет файл Microsoft Excel. Класс [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) содержит коллекцию [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/), позволяющую получить доступ к каждому листу в файле Excel. Лист представлен классом [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). Класс [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) включает коллекцию [Cells](https://reference.aspose.com/cells/go-cpp/cells/), которая представляет все ячейки листа. Коллекция [Cells](https://reference.aspose.com/cells/go-cpp/cells/) предоставляет несколько методов для управления строками или столбцами. Некоторые из них рассмотрены ниже.

#### **Установка высоты строки**

Можно задать высоту одной строки, вызвав метод [SetRowHeight](https://reference.aspose.com/cells/go-cpp/cells/setrowheight/) коллекции [Cells](https://reference.aspose.com/cells/go-cpp/cells/). Метод [SetRowHeight](https://reference.aspose.com/cells/go-cpp/cells/setrowheight/) принимает следующие параметры:

- **Индекс строки**, индекс строки, высоту которой вы изменяете.
- **Высота строки**, высота строки, применяемая к строке.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-GPP-SettingHeightOfRow.go" >}}

#### **Установка высоты всех строк на листе**

Если разработчикам нужно установить одинаковую высоту для всех строк листа, они могут сделать это с помощью метода [SetStandardHeight](https://reference.aspose.com/cells/go-cpp/cells/setstandardheight/) коллекции [Cells](https://reference.aspose.com/cells/go-cpp/cells/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingHeightOfAllRowsInWorksheet.go" >}}

## **Работа с колонками**

### **Установка ширины колонки**

Установите ширину столбца, вызвав метод [SetColumnWidth](https://reference.aspose.com/cells/go-cpp/cells/setcolumnwidth/) коллекции [Cells](https://reference.aspose.com/cells/go-cpp/cells/). Метод [SetColumnWidth](https://reference.aspose.com/cells/go-cpp/cells/setcolumnwidth/) принимает следующие параметры:

- **Индекс колонки**, индекс колонки, ширину которой вы изменяете.
- **Ширина колонки**, желаемая ширина колонки.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingWidthOfColumn.go" >}}

### **Установка ширины всех колонок на листе**

Чтобы установить одинаковую ширину столбцов для всех столбцов листа, используйте метод [SetStandardWidth](https://reference.aspose.com/cells/go-cpp/cells/setstandardwidth/) коллекции [Cells](https://reference.aspose.com/cells/go-cpp/cells/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingWidthOfAllColumnsInWorksheet.go" >}}
