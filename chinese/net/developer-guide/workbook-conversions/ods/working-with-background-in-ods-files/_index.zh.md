---
title: 使用 ODS 文件中的背景
type: docs
weight: 150
url: /zh/net/working-with-background-in-ods-files/
---
## **ODS 文件中的背景**

背景可以添加到 ODS 文件中的工作表。背景可以是彩色背景或图形背景。文件打开时背景不可见，但如果文件打印为 PDF，则背景在生成的 PDF 中可见。背景在打印预览对话框中也可见。

Aspose.Cells 提供读取背景信息的能力，在ODS文件中添加背景。

## **从 ODS 文件中读取背景信息**

Aspose.Cells 提供了[**Ods页面背景**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground)类来管理 ODS 文件中的背景。下面的代码示例演示了使用[**Ods页面背景**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground)通过加载类[来源 ODS](90112030.ods)文件并阅读背景信息。请参阅代码生成的控制台输出以供参考。

### **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadODSBackground-1.cs" >}}

### **控制台输出**

背景类型：图形

背景位置：CenterCenter

## **将彩色背景添加到 ODS 文件**

Aspose.Cells 提供了[**Ods页面背景**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground)类来管理 ODS 文件中的背景。下面的代码示例演示了使用[**OdsPageBackground.Color**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground/properties/color)属性将颜色背景添加到 ODS 文件。请参阅[输出 ODS](90112031.ods)代码生成的文件供参考。

### **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-SetODSColoredBackground-1.cs" >}}

## **将图形背景添加到 ODS 文件**

Aspose.Cells 提供了[**Ods页面背景**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground)类来管理 ODS 文件中的背景。下面的代码示例演示了使用[**OdsPageBackground.GraphicData**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground/properties/graphicdata)属性将图形背景添加到 ODS 文件。请参阅[输出 ODS](90112030.ods)代码生成的文件供参考。

### **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-SetODSGraphicBackground-1.cs" >}}
