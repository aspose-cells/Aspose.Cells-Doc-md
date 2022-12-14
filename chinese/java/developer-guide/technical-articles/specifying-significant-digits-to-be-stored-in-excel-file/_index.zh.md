---
title: 指定要存储在 Excel 文件中的有效数字
type: docs
weight: 20
url: /zh/java/specifying-significant-digits-to-be-stored-in-excel-file/
---
## **可能的使用场景**

默认情况下，Aspose.Cells 在电子表格中存储双精度值的 17 位有效数字，这与仅存储 15 位有效数字的 Excel 应用程序不同。对于这种情况，您可以更改 Aspose.Cells 的默认行为，即；您可以在使用时将有效位数从 17 更改为 15[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits)财产。

## **指定要存储在 Excel 文件中的有效数字**

以下示例代码强制 Aspose.Cells 在 excel 文件中存储双精度值时使用 15 位有效数字。请检查[输出excel文件](23166982.xlsx).将其扩展名更改为 .zip 并解压缩，您将看到，excel 文件中仅存储了 15 位有效数字。下面截图说明效果[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits)输出 excel 文件的属性。

![待办事项：图片_替代_文本](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-SignificantDigits-SignificantDigits.java" >}}
