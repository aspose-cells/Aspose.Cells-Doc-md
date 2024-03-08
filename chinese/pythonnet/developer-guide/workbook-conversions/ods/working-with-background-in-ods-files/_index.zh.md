---
title: 使用 ODS 文件中的后台
type: docs
weight: 150
url: /zh/python-net/working-with-background-in-ods-files/
description: 如何使用 ODS 文件中的背景 Aspose.Cells for Python via .NET API。
keywords: Python work with Background in ODS Files, Read Background Information from ODS file Pyton via NET, Add Colored Background to ODS file using Python via NET, Python via NET Add Graphic Background to ODS file.
---
##  **ODS 文件的背景**

背景可以添加到 ODS 文件中的工作表。背景可以是彩色背景或图形背景。文件打开时背景不可见，但如果文件打印为 PDF，则背景在生成的 PDF 中可见。背景在打印预览对话框中也可见。

Aspose.Cells for Python via .NET 提供读取背景信息并在 ODS 文件中添加背景的功能。

##  **从 ODS 文件中读取背景信息**

Aspose.Cells for Python via .NET 提供[**Ods页面背景**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground)类来管理 ODS 文件中的背景。下面的代码示例演示了使用[**Ods页面背景**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground)类通过加载[来源ODS](90112030.ods)文件并阅读背景信息。请参阅代码生成的控制台输出以供参考。

###  **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-ReadODSBackground-1.py" >}}

###  **控制台输出**

背景类型：图形

背景位置：CenterCenter

##  **将彩色背景添加到 ODS 文件**

Aspose.Cells for Python via .NET 提供[**Ods页面背景**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground)类来管理 ODS 文件中的背景。下面的代码示例演示了使用[**OdsPageBackground.color**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground/color/)属性向 ODS 文件添加彩色背景。请参阅[输出ODS](90112031.ods)代码生成的文件供参考。

###  **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-SetODSColoredBackground-1.py" >}}

##  **将图形背景添加到ODS文件**

Aspose.Cells for Python via .NET 提供[**Ods页面背景**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground)类来管理 ODS 文件中的背景。下面的代码示例演示了使用[**OdsPageBackground.graphic_data**](https://reference.aspose.com/cells/python-net/aspose.cells.ods/odspagebackground/graphic_data/)属性将图形背景添加到 ODS 文件。请参阅[输出ODS](90112030.ods)代码生成的文件供参考。

###  **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-SetODSGraphicBackground-1.py" >}}
