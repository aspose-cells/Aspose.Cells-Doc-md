---
title: 指定要存储在 Excel 文件中的有效数字
type: docs
weight: 30
url: /zh/net/specifying-significant-digits-to-be-stored-in-excel-file/
---
## **可能的使用场景**

默认情况下，Aspose.Cells 在 excel 文件中存储双精度值的 17 位有效数字，这与 MS-Excel 仅存储 15 位有效数字不同。您可以使用以下方法将 Aspose.Cells 的默认行为从 17 位有效数字更改为 15 位有效数字[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits)财产。

## **指定要存储在 Excel 文件中的有效数字**

以下示例代码强制 Aspose.Cells 在 excel 文件中存储双精度值时使用 15 位有效数字。请检查[输出excel文件](22774105.xlsx).将其扩展名更改为 .zip 并解压缩，您将看到，excel 文件中仅存储了 15 位有效数字。下面截图说明效果[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits)输出 excel 文件的属性。

![待办事项：图片_替代_文本](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-SignificantDigits.cs" >}}
