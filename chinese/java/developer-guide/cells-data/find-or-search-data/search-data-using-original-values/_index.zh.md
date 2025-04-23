---
title: 使用原始值搜索数据
type: docs
weight: 540
url: /zh/java/search-data-using-original-values/
---

{{% alert color="primary" %}} 

有时，数据的值是隐藏的，因为它以某种方式格式化。例如，假设单元格D4的公式为=Sum(A1:A2)，其值为20，但被格式化为---，那么这个值20就是隐藏的，不能通过Microsoft Excel的查找选项找到。但你可以使用Aspose.Cells，根据[LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/zh-CN/java/com.aspose.cells/lookintype#ORIGINAL-VALUES)找到它。

{{% /alert %}} 
## **使用原始值搜索数据**
以下示例代码说明了上述内容。它查找单元格D4，这个单元格不能通过Microsoft Excel的查找方式找到，但Aspose.Cells可以使用[LookInType.ORIGINAL_VALUES](https://reference.aspose.com/cells/zh-CN/java/com.aspose.cells/lookintype#ORIGINAL-VALUES)找到它。请阅读代码中的注释获取更多信息。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchDataUsingOriginalValues-SearchDataUsingOriginalValues.java" >}}
## **控制台输出**
这是上面示例代码的控制台输出。

{{< highlight java >}}

 Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
