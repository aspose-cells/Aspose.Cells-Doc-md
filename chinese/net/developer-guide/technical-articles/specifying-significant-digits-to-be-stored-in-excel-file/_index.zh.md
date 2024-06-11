---
title: 指定要存储在Excel文件中的有效数字
type: docs
weight: 30
url: /zh/net/specifying-significant-digits-to-be-stored-in-excel-file/
---

## **可能的使用场景**

默认情况下，Aspose.Cells在Excel文件中存储双精度值的17个有效数字，而MS-Excel仅存储15个有效数字。您可以使用[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits)属性将Aspose.Cells的默认行为从17个有效数字更改为15个有效数字。

## **指定要在Excel文件中存储的有效数字**

以下示例代码强制Aspose.Cells在Excel文件中存储双精度值时使用15个有效数字。请检查[输出Excel文件](22774105.xlsx)。将其扩展名更改为.zip并解压缩，您会看到，在Excel文件中只存储了15个有效数字。以下截图解释[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits)属性对输出Excel文件的影响。

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-SignificantDigits.cs" >}}
