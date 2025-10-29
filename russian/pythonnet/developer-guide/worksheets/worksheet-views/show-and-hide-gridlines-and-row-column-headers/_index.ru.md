---
title: Показывать и скрывать сетку и заголовки строк и столбцов
type: docs
weight: 30
url: /ru/python-net/show-and-hide-gridlines-and-row-column-headers/
description: Эта статья содержит пример кода для использования API Aspose.Cells для Python via .NET для программного скрытия или отображения линий сетки, заголовков строк и столбцов листа Excel.
keywords: Библиотека Excel для Python, отображение и скрытие линий сетки, как показывать и скрывать заголовки строк и столбцов в Python, как показывать и скрывать линии сетки и заголовки строк и столбцов в Python.
---

{{% alert color="primary" %}}

Aspose.Cells для Python via .NET поддерживает скрытие и отображение линий сетки листа, которые видимы по умолчанию. Также есть возможность управлять видимостью заголовков строк и столбцов листа.

{{% /alert %}}

## **Отображение и скрытие линий сетки**

Все листы Excel по умолчанию имеют сетку. Они помогают выделять клетки для удобства ввода данных. Сетка позволяет нам просматривать лист как коллекцию клеток, каждая клетка легко идентифицируется.

### **Управление видимостью сетки**

Aspose.Cells для Python via .NET предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/), которая позволяет разработчикам получать доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/). Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) включает широкий спектр свойств и методов для управления листом. Для управления видимостью линий сетки используйте свойство [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) класса [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/). [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) — булевое свойство, что означает, что оно может хранить только значение **true** или **false**.

#### **Отображение линий сетки**

Сделать сетку видимой, установив для свойства [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) класса [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) значение **true**.

#### **Скрытие линий сетки**

Скрыть сетку, установив для свойства [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) класса [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) значение **false**.

Приведен полный пример, демонстрирующий использование свойства [**is_gridlines_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_gridlines_visible/) путем открытия файла Excel (book1.xls), скрытия сетки на первом листе и сохранения измененного файла как output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideGridlines-1.py" >}}

## **Показывать и скрывать заголовки строк и столбцов**

Все листы в файле Excel состоят из ячеек, расположенных в ряды и столбцы. Все строки и столбцы имеют уникальные значения, используемые для их идентификации и идентификации отдельных ячеек. Например, строки нумеруются — 1, 2, 3, 4 и так далее — а столбцы идут в алфавитном порядке — A, B, C, D и так далее. Значения строк и столбцов отображаются в заголовках. С помощью Aspose.Cells для Python via .NET разработчики могут управлять видимостью этих заголовков строк и столбцов.

### **Управление видимостью листов**

Aspose.Cells для Python via .NET предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/), которая позволяет разработчикам получать доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/). Класс [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) предоставляет широкие свойства и методы для управления листом. Чтобы управлять видимостью заголовков строк и столбцов, используйте свойство [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) класса [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/). [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) — булевое свойство, что означает, что оно может хранить только значение **true** или **false**.

#### **Отображение заголовков строк/столбцов**

Сделать заголовки строк и столбцов видимыми, установив для свойства [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) класса [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) значение **true**.

#### **Скрытие заголовков строк/столбцов**

Скрыть заголовки строк и столбцов, установив для свойства [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) класса [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) значение **false**.

Приведен полный пример, показывающий, как использовать свойство [**is_row_column_headers_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_row_column_headers_visible/) путем открытия файла Excel (book1.xls), скрытия заголовков строк и столбцов на первом листе и сохранения измененного файла как output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Display-DisplayHideRowColumnHeaders-1.py" >}}

{{% alert color="primary" %}}

Также возможно использовать методы [**unhide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_rows) и [**unhide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_columns) класса [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells), чтобы сделать несколько строк и столбцов видимыми.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
