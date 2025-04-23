---
title: 指定在刷新数据透视表时数据透视表是否兼容Excel2003
type: docs
weight: 880
url: /zh/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}} 

Aspose.Cells提供[PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible)属性，您可以使用该属性来指定在刷新数据透视表时该数据透视表是否与Excel 2003兼容。如果设置为**true**，则字符串长度必须小于或等于255个字符，因此，如果字符串长度大于255个字符，将被截断。如果设置为**false**，字符串将不受上述限制。默认值为**true**。

{{% /alert %}} 
## **指定在刷新数据透视表时数据透视表是否兼容Excel2003**
以下示例代码说明了如何使用[PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible)属性。原始字符串长度为383个字符。但是当将[PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible)属性设置为**true**并刷新数据透视表时，数据透视表的B5单元格的数据被截断为255个字符。然而，当[PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible)属性设置为**false**并再次刷新数据透视表时，数据透视表的B5单元格的数据不会被截断，仍保持383个字符。请下载此代码中使用的[示例Excel文件](5472558.xlsx)、生成的[输出Excel文件](5472557.xlsx)以及控制台输出以供参考。还请阅读代码内的注释以更好地理解此属性。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-IsPivotTableCompatibleForExcel2003-.java" >}}
## **控制台输出**
以下是执行上述示例代码时使用给定的[示例Excel文件](5472558.xlsx)的控制台输出。



{{< highlight java >}}

 Length of original data string: 383

Length of cell B5 after setting IsExcel2003Compatible property to True: 255

Length of cell B5 after setting IsExcel2003Compatible property to False: 383

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
