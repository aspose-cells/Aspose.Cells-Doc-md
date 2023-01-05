---
title: 刷新数据透视表时指定数据透视表是否兼容Excel2003
type: docs
weight: 880
url: /zh/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---
{{% alert color="primary" %}} 

Aspose.Cells 提供了[数据透视表.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible)刷新数据透视表时可用于指定数据透视表是否与 Excel2003 兼容的属性。如果**真的** 字符串必须小于或等于 255 个字符，因此如果字符串大于 255 个字符，它将被截断。如果**错误的**，字符串不会有上述限制。默认值为**真的**.

{{% /alert %}} 
## **刷新数据透视表时指定数据透视表是否兼容Excel2003**
下面的示例代码解释了[数据透视表.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible)财产。原始字符串的长度为 383 个字符。但当[数据透视表.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible)属性设置为**真的**数据透视表刷新后，数据透视表B5单元格的数据被截断，变成255个字符长。然而，当[数据透视表.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible)属性已设置**错误的**再次刷新数据透视表，数据透视表B5单元格的数据没有被截断，仍然是383个字符长。请下载[示例 excel 文件](5472558.xlsx)在此代码中使用，[输出excel文件](5472557.xlsx)由它生成及其控制台输出供您参考。另请阅读代码中的注释，以便更好地理解此属性。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-IsPivotTableCompatibleForExcel2003-.java" >}}
## **控制台输出**
这是使用给定的执行时上述示例代码的控制台输出[示例 excel 文件](5472558.xlsx).



{{< highlight "java" >}}

 Length of original data string: 383

Length of cell B5 after setting IsExcel2003Compatible property to True: 255

Length of cell B5 after setting IsExcel2003Compatible property to False: 383

{{< /highlight >}}
