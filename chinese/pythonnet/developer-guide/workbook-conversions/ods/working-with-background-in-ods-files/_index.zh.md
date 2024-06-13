---
title: 在ODS文件中使用背景
type: docs
weight: 150
url: /zh/python-net/working-with-background-in-ods-files/
description: 如何使用Aspose.Cells for Python via .NET API在ODS文件中处理背景。
keywords: Python在ODS文件中处理背景，从ODS文件中读取背景信息Pyton via NET，使用Python via NET为ODS文件添加彩色背景，Python via NET为ODS文件添加图形背景。
---

## **ODS文件中的背景**

可以将背景添加到ODS文件中的工作表。背景可以是彩色背景或图形背景。在打开文件时背景不可见，但如果文件作为PDF打印，则在生成的PDF中可以看到背景。在打印预览对话框中也可以看到背景。

Aspose.Cells for Python via .NET提供读取背景信息并在ODS文件中添加背景的能力。

## **从ODS文件读取背景信息**

Aspose.Cells for Python via .NET 提供 [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) 类来管理ODS文件中的背景。以下示例演示了通过加载 [source ODS](90112030.ods) 文件并读取背景信息来使用 [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) 类的方法。请参考代码生成的控制台输出。

### **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-ReadODSBackground-1.py" >}}

### **控制台输出**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **向ODS文件添加彩色背景**

Aspose.Cells for Python via .NET 提供 [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) 类来管理ODS文件中的背景。以下示例演示了通过使用 [**OdsPageBackground.color**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground/color/) 属性向ODS文件添加彩色背景的方法。请参考代码生成的 [output ODS](90112031.ods) 文件。

### **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-SetODSColoredBackground-1.py" >}}

## **向ODS文件添加图形背景**

Aspose.Cells for Python via .NET 提供 [**OdsPageBackground**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground) 类来管理ODS文件中的背景。以下示例演示了通过使用 [**OdsPageBackground.graphic_data**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground/graphic_data/) 属性向ODS文件添加图形背景的方法。请参考代码生成的 [output ODS](90112030.ods) 文件。

### **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-SetODSGraphicBackground-1.py" >}}
