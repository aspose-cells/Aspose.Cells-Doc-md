---
title: Удаление пустых строк и столбцов в листе
type: docs
weight: 300
url: /ru/python-net/delete-blank-rows-and-columns-in-a-worksheet/
description: В данной статье описано, как удалить пустые строки и столбцы в листе с использованием библиотеки Aspose.Cells для Python via .NET.
keywords: Библиотека Python Excel, удаление пустых строк Python, удаление пустых столбцов Python, удаление пустых строк Python, удаление пустых столбцов Python, удаление или удаление пустых строк и столбцов Python.
---

{{% alert color="primary" %}}

Можно удалить все пустые строки и столбцы из листа. Это полезно, например, при создании файла PDF из файла Microsoft Excel и требуется конвертировать только строки и столбцы, содержащие данные или связанные объекты.

Используйте следующие методы Aspose.Cells для удаления пустых строк и столбцов:

1. Для удаления пустых строк используйте метод [**Cells.delete_blank_rows()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_blank_rows). Обратите внимание, для удаляемых пустых строк требуется, чтобы [**Row.is_blank**](https://reference.aspose.com/cells/python-net/aspose.cells/row/is_blank/) был равен true, а также не должно быть видимых комментариев для любой ячейки в этих строках, и не должно быть сводной таблицы, диапазон которой пересекается с ними.
1. Чтобы удалить пустые столбцы, используйте метод [**Cells.delete_blank_columns()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_blank_columns).

{{% /alert %}}

## C# код для удаления пустых строк

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-DeletingBlankRows-1.py" >}}

## C# код для удаления пустых столбцов

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-DeletingBlankColumns-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
