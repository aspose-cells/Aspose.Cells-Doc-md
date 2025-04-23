---
title: 自定义数据透视表的全球化设置
type: docs
weight: 20
url: /zh/java/customize-globalization-settings-for-pivot-table/
---

## **可能的使用场景**

有时您希望根据自己的需求自定义*数据透视表总计、子总计、总计、所有项、多个项、列标签、行标签、空值*文本。Aspose.Cells允许您自定义数据透视表的全球化设置，以处理此类情况。您还可以使用此功能将标签更改为其他语言，如阿拉伯语、印度语、波兰语等。

## **自定义数据透视表的全球化设置**

以下示例代码解释了如何为数据透视表自定义全球化设置。它创建了一个名为*CustomPivotTableGlobalizationSettings*的类，从基类[**GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings)派生，并重写所有必要方法。这些方法返回*数据透视总计、小计、总计、所有项、多项、列标签、行标签、空值*的自定义文本。然后将此类的对象分配给[**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings)属性。代码加载包含数据透视表的[源Excel文件](40468491.xlsx)，刷新和计算数据，然后将其保存为[输出PDF文件](40468490.pdf)。以下截图显示了样例代码对输出PDF的影响。如截图所示，数据透视表的不同部分现在具有由[**GlobalizationSettings**](https://reference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings)类的重写方法返回的自定义文本。

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-CustomizeGlobalizationSettingsforPivotTable-1.java" >}}
{{< app/cells/assistant language="java" >}}
