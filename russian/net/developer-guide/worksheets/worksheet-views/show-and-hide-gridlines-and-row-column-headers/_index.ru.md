---
title: Показывать и скрывать сетку и заголовки строк и столбцов
type: docs
weight: 30
url: /ru/net/show-and-hide-gridlines-and-row-column-headers/
description: В этой статье приведен образцовый код для использования API C# или библиотеки .NET для программного скрытия или показа сетки, заголовков строк и столбцов на листе Excel.
---

{{% alert color="primary" %}}

Aspose.Cells поддерживает скрытие и показ сетки листа Excel, которая обычно видна. Он также обеспечивает контроль видимости заголовков строк и столбцов листа.

{{% /alert %}}

## **Отображение и скрытие линий сетки**

Все листы Excel по умолчанию имеют сетку. Они помогают выделять клетки для удобства ввода данных. Сетка позволяет нам просматривать лист как коллекцию клеток, каждая клетка легко идентифицируется.

### **Управление видимостью сетки**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets), позволяющую разработчикам получить доступ к каждому листу Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) предоставляет широкий спектр свойств и методов для управления листом. Чтобы контролировать видимость сетки, используйте свойство [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) класса [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) - это логическое свойство, что означает, что оно может содержать только значение **true** или **false**.

#### **Отображение линий сетки**

Сделать сетку видимой, установив для свойства [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) класса [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) значение **true**.

#### **Скрытие линий сетки**

Скрыть сетку, установив для свойства [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) класса [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) значение **false**.

Приведен полный пример, демонстрирующий использование свойства [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) путем открытия файла Excel (book1.xls), скрытия сетки на первом листе и сохранения измененного файла как output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideGridlines-1.cs" >}}

## **Показывать и скрывать заголовки строк и столбцов**

Все листы Excel состоят из клеток, расположенных в строках и столбцах. Все строки и столбцы имеют уникальные значения, которые используются для их идентификации и для идентификации отдельных клеток. Например, строки нумеруются - 1, 2, 3, 4 и т. д., а столбцы упорядочены по алфавиту - A, B, C, D и т. д. Значения строк и столбцов отображаются в заголовках. С помощью Aspose.Cells разработчики могут управлять видимостью этих заголовков строк и столбцов.

### **Управление видимостью листов**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets), позволяющую разработчикам получить доступ к каждому листу Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) предоставляет широкий спектр свойств и методов для управления листом. Для управления видимости заголовков строк и столбцов используйте свойство [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) класса [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) - это логическое свойство, что означает, что оно может содержать только значение **true** или **false**.

#### **Отображение заголовков строк/столбцов**

Сделать заголовки строк и столбцов видимыми, установив для свойства [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) класса [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) значение **true**.

#### **Скрытие заголовков строк/столбцов**

Скрыть заголовки строк и столбцов, установив для свойства [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) класса [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) значение **false**.

Приведен полный пример, показывающий, как использовать свойство [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) путем открытия файла Excel (book1.xls), скрытия заголовков строк и столбцов на первом листе и сохранения измененного файла как output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideRowColumnHeaders-1.cs" >}}

{{% alert color="primary" %}}

Также возможно использовать методы [**UnhideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderows) и [**UnhideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumns) класса [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), чтобы сделать несколько строк и столбцов видимыми.

{{% /alert %}}
