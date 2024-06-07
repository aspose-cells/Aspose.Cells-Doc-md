---
title: 使用原始值搜索数据
type: docs
weight: 540
url: /zh/java/search-data-using-original-values/
---

{{% alert color="primary" %}} 

有时，数据的值由于某种原因而被隐藏。 例如，假设单元格D4具有公式=Sum（A1：A2），其值为20，但其格式为---，则值20将被隐藏，并且无法使用Microsoft Excel查找选项找到。 但是，您可以使用Aspose.Cells找到它使用[LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES)

{{% /alert %}} 
## **使用原始值搜索数据**
以下示例代码说明了上述观点。 它找到了不能使用Microsoft Excel查找选项找到的单元格D4，但Aspose.Cells可以使用[LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES)找到它。 请阅读代码内部的注释以获取更多信息。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.java" >}}
## **控制台输出**
这是上述示例代码的控制台输出。

{{< highlight java >}}

 Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
