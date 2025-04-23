---
title: Удаление пустых строк и столбцов в листе
type: docs
weight: 300
url: /ru/net/delete-blank-rows-and-columns-in-a-worksheet/
---

{{% alert color="primary" %}}

Можно удалить все пустые строки и столбцы из листа. Это полезно, например, при создании файла PDF из файла Microsoft Excel и требуется конвертировать только строки и столбцы, содержащие данные или связанные объекты.

Используйте следующие методы Aspose.Cells для удаления пустых строк и столбцов:

1. Для удаления пустых строк используйте метод [**Cells.DeleteBlankRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankrows). Обратите внимание, для удаляемых пустых строк требуется, чтобы [**Row.IsBlank**](https://reference.aspose.com/cells/net/aspose.cells/row/isblank/) был равен true, а также не должно быть видимых комментариев для любой ячейки в этих строках, и не должно быть сводной таблицы, диапазон которой пересекается с ними.
1. Чтобы удалить пустые столбцы, используйте метод [**Cells.DeleteBlankColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankcolumns).

{{% /alert %}}

## C# код для удаления пустых строк

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankRows-1.cs" >}}

## C# код для удаления пустых столбцов

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankColumns-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
