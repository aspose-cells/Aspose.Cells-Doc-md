---
title: 通过数据透视表字段的显示名称获取单元格对象
type: docs
weight: 310
url: /zh/java/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
---

{{% alert color="primary" %}} 

Aspose.Cells提供了[PivotTable.getCellByDisplayName()](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#getCellByDisplayName\(java.lang.String\))方法，您可以使用它通过数据字段的显示名称访问单元格对象。当您想要突出显示或格式化数据透视表字段标题时，此方法非常有用。本文介绍如何通过数据字段的显示名称检索单元格对象，然后对其应用格式。

{{% /alert %}} 
## **通过数据透视表的PivotField的DisplayName获取Cell对象**
以下代码访问工作表的第一个数据透视表，然后获取数据透视表的第二个数据字段的显示名称单元格。然后将单元格的填充颜色和字体颜色分别更改为浅蓝色和黑色。以下屏幕截图显示了执行代码前后数据透视表的外观。
### **数据透视表 - 执行前**
![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)
### **数据透视表 - 执行后**
![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetCellObject-GetCellObject.java" >}}






