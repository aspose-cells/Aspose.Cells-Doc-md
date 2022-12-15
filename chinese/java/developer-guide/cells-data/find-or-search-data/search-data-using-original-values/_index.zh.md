---
title: 使用原始值搜索数据
type: docs
weight: 540
url: /zh/java/search-data-using-original-values/
---
{{% alert color="primary" %}} 

有时数据的价值是隐藏的，因为它是以某种方式格式化的。例如，假设单元格 D4 具有公式 =Sum(A1:A2) 并且其值为 20 但其格式为 ---，则值 20 被隐藏并且无法使用 Microsoft Excel 查找选项找到。但是，您可以使用 Aspose.Cells 找到它[LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES)

{{% /alert %}} 
## **使用原始值搜索数据**
以下示例代码说明了上述观点。它找到使用 Microsoft Excel 查找选项无法找到的单元格 D4，但 Aspose.Cells 可以使用[LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#ORIGINAL_VALUES).请阅读代码中的注释以获取更多信息。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.java" >}}
## **控制台输出**
这是上述示例代码的控制台输出。

{{< highlight "java" >}}

 Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]{{< /highlight >}}
