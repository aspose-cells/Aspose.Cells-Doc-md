---
title: Удалить пустые строки и столбцы на листе
type: docs
weight: 300
url: /ru/net/delete-blank-rows-and-columns-in-a-worksheet/
---
{{% alert color="primary" %}}

Можно удалить все пустые строки и столбцы с рабочего листа. Это полезно, например, когда вы создаете файл PDF из файла Excel Microsoft и хотите преобразовать только строки и столбцы, содержащие данные или связанные объекты.

Используйте следующие методы Aspose.Cells для удаления пустых строк и столбцов:

1.  Чтобы удалить пустые строки, используйте[**Cells.DeleteBlankRows()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankrows) метод. Обратите внимание, для пустых строк, которые будут удалены, требуется не только[**Строка.IsBlank**](https://reference.aspose.com/cells/net/aspose.cells/row/isblank/) должно быть истинным, но также не должно быть видимого комментария, определенного для любой ячейки в этих строках, и сводной таблицы, диапазон которой пересекается с ними.
1.  Чтобы удалить пустые столбцы, используйте[**Cells.УдалитьБланкКолонкс()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleteblankcolumns) метод.

{{% /alert %}}

##  C# код для удаления пустых строк

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankRows-1.cs" >}}

##  Код C# для удаления пустых столбцов

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteBlankRowsColumns-DeletingBlankColumns-1.cs" >}}
