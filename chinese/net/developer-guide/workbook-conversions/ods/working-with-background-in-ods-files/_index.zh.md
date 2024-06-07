---
title: 在ODS文件中使用背景
type: docs
weight: 150
url: /zh/net/working-with-background-in-ods-files/
---

## **ODS文件中的背景**

可以向ODS文件的工作表添加背景。背景可以是彩色背景或图形背景。当文件打开时，背景是不可见的，但如果文件打印为PDF，则生成的PDF中会显示背景。打印预览对话框中也会显示背景。

Aspose.Cells提供读取背景信息并在ODS文件中添加背景的功能。

## **从ODS文件中读取背景信息**

Aspose.Cells提供[**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground)类来管理ODS文件中的背景。以下代码示例演示了通过加载源ODS文件[**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground)类的使用以读取背景信息。请查看代码输出中生成的控制台输出以供参考。

### **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadODSBackground-1.cs" >}}

### **控制台输出**

背景类型：图形

背景位置：CenterCenter

## **为ODS文件添加彩色背景**

Aspose.Cells提供[**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground)类来管理ODS文件中的背景。以下代码示例演示了使用[**OdsPageBackground.Color**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground/properties/color)属性将颜色背景添加到ODS文件中。请查看代码输出中生成的[output ODS](90112031.ods)文件以供参考。

### **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-SetODSColoredBackground-1.cs" >}}

## **为ODS文件添加图形背景**

Aspose.Cells提供[**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground)类来管理ODS文件中的背景。以下代码示例演示了使用[**OdsPageBackground.GraphicData**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground/properties/graphicdata)属性向ODS文件添加图形背景。请查看代码输出中生成的[output ODS](90112030.ods)文件以供参考。

### **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-SetODSGraphicBackground-1.cs" >}}
