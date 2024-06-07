---
title: 指定要存储在Excel文件中的有效数字位数
type: docs
weight: 20
url: /zh/java/specifying-significant-digits-to-be-stored-in-excel-file/
---

## **可能的使用场景**

默认情况下，Aspose.Cells在电子表格中存储17位双精度值的有效数字，而Excel应用程序仅存储15位有效数字。您可以更改Aspose.Cells的默认行为，即在使用属性[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits)时，可以将有效数字位数从17更改为15。

## **指定要存储在Excel文件中的有效数字位数**

以下示例代码强制Aspose.Cells在存储双精度值时使用15位有效数字。请检查[输出Excel文件](23166982.xlsx)。将其扩展名更改为.zip并解压缩，您将看到，只有15位有效数字存储在Excel文件中。以下截图说明了[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits)属性对输出Excel文件的影响。

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-SignificantDigits-SignificantDigits.java" >}}
