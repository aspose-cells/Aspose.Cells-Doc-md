---
title: 指定在更新数据透视表时，数据透视表是否兼容Excel2003
type: docs
weight: 880
url: /zh/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}} 

Aspose.Cells提供了[PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible)属性，您可以使用该属性在刷新数据透视表时指定数据透视表是否兼容Excel2003。如果**true**，则字符串的长度必须小于或等于255个字符，因此，如果字符串大于255个字符，它将被截断。如果**false**，则字符串将没有上述限制。默认值为**true**。

{{% /alert %}} 
## **指定在更新数据透视表时，数据透视表是否兼容Excel2003**
以下示例代码解释了[PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible)属性的用法。原始字符串长383个字符。但是当[PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible)属性设置为**true**并刷新数据透视表时，数据透视表的B5单元格数据被截断并变为255个字符长。然而，当[PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible)属性设置为**false**并且再次刷新数据透视表时，数据透视表的B5单元格数据不会被截断，仍保持383个字符长。请下载用于此代码的[示例Excel文件](5472558.xlsx)、生成的[输出Excel文件](5472557.xlsx)及其控制台输出以供参考。此外，请阅读代码内部的注释，以更好地理解此属性。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-IsPivotTableCompatibleForExcel2003-.java" >}}
## **控制台输出**
以下是执行给定[示例Excel文件](5472558.xlsx)时上述示例代码的控制台输出。



{{< highlight java >}}

 Length of original data string: 383

Length of cell B5 after setting IsExcel2003Compatible property to True: 255

Length of cell B5 after setting IsExcel2003Compatible property to False: 383

{{< /highlight >}}
