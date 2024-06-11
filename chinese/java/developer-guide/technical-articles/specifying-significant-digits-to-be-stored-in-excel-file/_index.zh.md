---
title: 指定要存储在Excel文件中的有效数字位数
type: docs
weight: 20
url: /zh/java/specifying-significant-digits-to-be-stored-in-excel-file/
---

## **可能的使用场景**

默认情况下，Aspose.Cells在电子表格中存储双精度值的17个有效数字，而Excel应用程序仅存储15个有效数字。您可以更改Aspose.Cells的默认行为，即您可以在使用[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits)属性时将有效数字位数从17更改为15。

## **指定要存储在Excel文件中的有效数字位数**

以下示例代码强制Aspose.Cells在存储Excel文件中的双精度值时使用15个有效数字。请检查[输出Excel文件](23166982.xlsx)。更改其扩展名为.zip并解压缩，您将会看到，该Excel文件中只存储了15个有效数字。以下屏幕截图解释了[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits)属性对输出Excel文件的影响。

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-SignificantDigits-SignificantDigits.java" >}}
