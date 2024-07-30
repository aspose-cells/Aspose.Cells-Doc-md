---
title: Показывать и скрывать сетку и заголовки строк и столбцов
type: docs
weight: 30
url: /ru/python-net/show-and-hide-gridlines-and-row-column-headers/
description: В этой статье приведен образец кода для использования API Aspose.Cells для Python via .NET для программного скрытия или показа сетки, заголовков строк и столбцов листа Excel.
keywords: Библиотека Python Excel, Показывает и скрывает сетку Python, Как показать и скрыть заголовки строк и столбцов в Python, Как показать и скрыть сетку и заголовки строк и столбцов в Python.
---

{{% alert color="primary" %}}

Aspose.Cells для Python via .NET поддерживает скрытие и показ сетки листа, которая изначально видима. Он также позволяет управлять видимостью заголовков строк и столбцов листа.

{{% /alert %}}

## **Отображение и скрытие линий сетки**

Все листы Excel по умолчанию имеют сетку. Они помогают выделять клетки для удобства ввода данных. Сетка позволяет нам просматривать лист как коллекцию клеток, каждая клетка легко идентифицируется.

### **Управление видимостью сетки**

Aspose.Cells для Python via .NET предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/), который представляет собой файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/), которая позволяет разработчикам получить доступ к каждому листу Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-et/aspose.cells/worksheet/). Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) предоставляет широкий диапазон свойств и методов для управления листом. Для управления видимостью сетки используйте свойство класса [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/). [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) - это свойство Boolean, что означает, что оно может хранить только значение **true** или **false**.

#### **Отображение линий сетки**

Сделать сетку видимой, установив для свойства [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) класса [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) значение **true**.

#### **Скрытие линий сетки**

Скрыть сетку, установив для свойства [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) класса [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) значение **false**.

Приведен полный пример, демонстрирующий использование свойства [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) путем открытия файла Excel (book1.xls), скрытия сетки на первом листе и сохранения измененного файла как output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideGridlines-1.py" >}}

## **Показывать и скрывать заголовки строк и столбцов**

Все листы в файле Excel состоят из ячеек, которые расположены в строках и столбцах. Все строки и столбцы имеют уникальные значения, которые используются для их идентификации и идентификации отдельных ячеек. Например, строки пронумерованы - 1, 2, 3, 4, и так далее, а столбцы упорядочены по алфавиту - A, B, C, D, и так далее. Значения строк и столбцов отображаются в заголовках. С помощью Aspose.Cells для Python via .NET разработчики могут контролировать видимость этих заголовков строк и столбцов.

### **Управление видимостью листов**

Aspose.Cells для Python via .NET предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/), который представляет собой файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/pytho-net/aspose.cells/workbook/) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/), которая позволяет разработчикам получить доступ к каждому листу Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/). Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) предоставляет широкий диапазон свойств и методов для управления листом. Для контроля видимости заголовков строк и столбцов используйте свойство класса [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/). [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) - это свойство Boolean, что означает, что оно может хранить только значение **true** или **false**.

#### **Отображение заголовков строк/столбцов**

Сделать заголовки строк и столбцов видимыми, установив для свойства [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) класса [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) значение **true**.

#### **Скрытие заголовков строк/столбцов**

Скрыть заголовки строк и столбцов, установив для свойства [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) класса [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) значение **false**.

Приведен полный пример, показывающий, как использовать свойство [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) путем открытия файла Excel (book1.xls), скрытия заголовков строк и столбцов на первом листе и сохранения измененного файла как output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideRowColumnHeaders-1.py" >}}

{{% alert color="primary" %}}

Также возможно использовать методы [**unhide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_rows) и [**unhide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_columns) класса [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells), чтобы сделать несколько строк и столбцов видимыми.

{{% /alert %}}
