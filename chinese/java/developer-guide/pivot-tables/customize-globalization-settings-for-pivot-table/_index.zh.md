---
title: 自定义数据透视表的全球化设置
type: docs
weight: 20
url: /zh/java/customize-globalization-settings-for-pivot-table/
---

## **可能的使用场景**

有时您想根据您的需求自定义数据透视表的*透视总计，小计，总计，所有项目，多个项目，列标签，行标签，空值*文本。Aspose.Cells允许您自定义数据透视表的全球化设置，以处理这种情况。您还可以使用此功能将标签更改为阿拉伯语，印地语，波兰语等其他语言。

## **自定义数据透视表的全球化设置**

以下示例代码说明了如何自定义数据透视表的全球化设置。它创建了一个从基类[**GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings)派生的*CustomPivotTableGlobalizationSettings*类，并覆盖了所有必要的方法。这些方法返回*Pivot Total, Sub Total, Grand Total, All Items, Multiple Items, Column Labels, Row Labels, Blank Values*的定制文本。然后它将这个类的对象分配给[**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings)属性。代码加载了包含数据透视表的[源Excel文件](40468491.xlsx)，并刷新和计算其数据，然后将其保存为[输出PDF文件](40468490.pdf)。以下屏幕截图显示了示例代码对输出PDF的影响。如屏幕截图所示，数据透视表的不同部分现在都有由[**GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings)类的重写方法返回的定制文本。

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-CustomizeGlobalizationSettingsforPivotTable-1.java" >}}
