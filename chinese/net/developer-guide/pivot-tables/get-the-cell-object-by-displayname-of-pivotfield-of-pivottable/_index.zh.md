---
title: 根据数据透视表的PivotField显示名称获取单元格对象
type: docs
weight: 70
url: /zh/net/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
---

{{% alert color="primary" %}}

Aspose.Cells提供了[**PivotTable.GetCellByDisplayName()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/getcellbydisplayname)方法，您可以使用它根据数据透视表字段的显示名称访问单元格对象。当您想要突出显示或格式化数据透视表字段标题时，此方法很有用。本文解释了如何通过数据字段的显示名称检索单元格对象，然后对其应用格式。

{{% /alert %}}

## **通过透视表的透视字段的DisplayName获取单元格对象**

以下代码访问工作表的第一个透视表，然后通过透视表的第二个数据字段的显示名称获取单元格。然后将单元格的填充颜色和字体颜色分别更改为浅蓝色和黑色。下面的屏幕截图显示了代码执行之前和之后透视表的外观。

|**透视表 - 在之前**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PivotTablesAndPivotCharts-GetCellByDisplayName-GetCellObjectByDisplayName.cs" >}}

|**透视表 - 在之后**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
{{< app/cells/assistant language="csharp" >}}
