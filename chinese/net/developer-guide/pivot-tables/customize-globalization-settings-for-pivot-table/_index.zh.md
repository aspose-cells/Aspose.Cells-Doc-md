---
title: 自定义数据透视表的全球化设置
type: docs
weight: 50
url: /zh/net/customize-globalization-settings-for-pivot-table/
---
## **可能的使用场景**

有时您想自定义*数据透视总计、小计、总计、所有项目、多项、列标签、行标签、空白值*文本根据您的要求。 Aspose.Cells 允许您自定义数据透视表的全球化设置以应对此类场景。您还可以使用此功能将标签更改为其他语言，如阿拉伯语、印地语、波兰语等。

## **自定义数据透视表的全球化设置**

以下示例代码说明了如何自定义数据透视表的全球化设置。它创建了一个类*自定义数据透视表全球化设置*从基类派生[**全球化设置**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)并覆盖所有必要的方法。这些方法返回自定义的文本*数据透视总计、小计、总计、所有项目、多项、列标签、行标签、空白值*.然后将这个类的对象赋值给[**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings)财产。代码加载[源文件](40468488.xlsx)包含数据透视表，刷新并计算其数据并将其另存为[输出 PDF](40468487.pdf)文件。以下屏幕截图显示了示例代码对输出 PDF 的影响。正如您在屏幕截图中看到的那样，数据透视表的不同部分现在具有由重写方法返回的自定义文本[**全球化设置**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)班级。

![待办事项：图片_替代_文本](customize-globalization-settings-for-pivot-table_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CustomizePivotTableGlobalSettings-CustomizePivotTableGlobalSettings.cs" >}}
