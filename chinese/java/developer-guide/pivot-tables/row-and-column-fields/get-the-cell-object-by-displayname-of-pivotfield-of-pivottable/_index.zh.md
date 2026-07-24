---
title: 根据数据透视表的PivotField显示名称获取单元格对象
type: docs
weight: 310
url: /zh/java/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
---

{{% alert color="primary" %}} 

Aspose.Cells 提供 [PivotTable.getCellByDisplayName()](https://reference.aspose.com/cells/zh/java/com.aspose.cells/pivottable#getCellByDisplayName-java.lang.String-) 方法，您可以用它通过枢轴字段的显示名称访问单元格对象。当你想突出显示或格式化枢轴字段标题时，这个方法非常有用。本文解释了如何通过显示名称获取数据字段的单元格对象并对其应用格式。

{{% /alert %}} 
## **通过透视表的透视字段的DisplayName获取单元格对象**
以下代码访问工作表的第一个数据透视表，然后通过数据透视表的第二个数据字段的显示名称获取单元格。然后，将单元格的填充颜色和字体颜色分别更改为浅蓝色和黑色。以下屏幕截图显示了执行代码前后的数据透视表外观。
### **数据透视表 - 在执行前**
![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)
### **数据透视表 - 在执行后**
![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellObject-GetCellObject.java" >}}






{{< app/cells/assistant language="java" >}}
