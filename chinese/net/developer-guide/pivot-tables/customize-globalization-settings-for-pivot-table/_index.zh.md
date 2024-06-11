---
title: 自定义数据透视表的全球化设置
type: docs
weight: 50
url: /zh/net/customize-globalization-settings-for-pivot-table/
---

## **可能的使用场景**

有时您希望根据自己的需求自定义*数据透视表总计、子总计、总计、所有项、多个项、列标签、行标签、空值*文本。Aspose.Cells允许您自定义数据透视表的全球化设置，以处理此类情况。您还可以使用此功能将标签更改为其他语言，如阿拉伯语、印度语、波兰语等。

## **自定义数据透视表的全球化设置**

以下示例代码说明了如何自定义数据透视表的全球化设置。它创建了一个从基类[**PivotGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/)派生的类*CustomPivotTableGlobalizationSettings*，并覆盖了其所有必要的方法。这些方法返回*数据透视表总计、子总计、总计、所有项、多个项、列标签、行标签、空值*的自定义文本。然后，将此类的对象分配给[**WorkbookSettings.GlobalizationSettings.PivotSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/pivotsettings/)属性。该代码加载包含数据透视表的[源Excel文件](40468488.xlsx)，刷新并计算其数据，并将其保存为[输出PDF](40468487.pdf)文件。以下屏幕截图显示了示例代码对输出PDF的影响。正如您在屏幕截图中所看到的，数据透视表的不同部分现在具有由[**PivotGlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells.settings/pivotglobalizationsettings/)类的覆盖方法返回的自定义文本。

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CustomizePivotTableGlobalSettings-CustomizePivotTableGlobalSettings.cs" >}}
