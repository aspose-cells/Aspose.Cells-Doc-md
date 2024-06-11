---
title: 在ODS文件中使用背景
type: docs
weight: 150
url: /zh/net/working-with-background-in-ods-files/
---

## **ODS文件中的背景**

可以将背景添加到ODS文件中的工作表。背景可以是彩色背景或图形背景。在打开文件时背景不可见，但如果文件作为PDF打印，则在生成的PDF中可以看到背景。在打印预览对话框中也可以看到背景。

Aspose.Cells提供了读取后台信息并在ODS文件中添加背景的能力。

## **从ODS文件读取背景信息**

Aspose.Cells提供了[**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground)类来管理ODS文件中的背景。以下代码示例演示了使用[**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground)类加载[源ODS](90112030.ods)文件并读取背景信息。请参阅代码生成的控制台输出以供参考。

### **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadODSBackground-1.cs" >}}

### **控制台输出**

背景类型：图形

背景位置：中心

## **向ODS文件添加彩色背景**

Aspose.Cells提供了[**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground)类来管理ODS文件中的背景。以下代码示例演示了使用[**OdsPageBackground.Color**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground/properties/color)属性向ODS文件添加颜色背景。请参阅代码生成的[输出ODS](90112031.ods)文件以供参考。

### **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-SetODSColoredBackground-1.cs" >}}

## **向ODS文件添加图形背景**

Aspose.Cells提供了[**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground)类来管理ODS文件中的背景。以下代码示例演示了使用[**OdsPageBackground.GraphicData**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground/properties/graphicdata)属性向ODS文件添加图形背景。请参阅代码生成的[输出ODS](90112030.ods)文件以供参考。

### **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-SetODSGraphicBackground-1.cs" >}}
