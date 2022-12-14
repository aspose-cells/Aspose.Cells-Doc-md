---
title: 在 ODS 文件中使用背景
type: docs
weight: 170
url: /zh/java/working-with-background-in-ods-files/
---
## **ODS 文件中的背景**

ODS 文件中的工作表可以添加背景。背景可以是彩色背景或图形背景。文件打开时背景不可见，但如果文件打印为 PDF，则背景在生成的 PDF 中可见。在打印预览对话框中也可以看到背景。

Aspose.Cells 提供读取背景信息和在ODS文件中添加背景的能力。

## **从 OSD 文件中读取背景信息**

Aspose.Cells 提供了[**ODSPage背景**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)类来管理 ODS 文件中的背景。下面的代码示例演示了使用[**ODSPage背景**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)通过加载类[来源消耗臭氧层物质](GraphicBackground.ods)文件并阅读背景信息。请参阅代码生成的控制台输出以供参考。

### **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-ReadODSBackground-1.java" >}}

### **控制台输出**

背景类型：图形

背景位置：CENTER_CENTER

## **为 ODS 文件添加彩色背景**

Aspose.Cells 提供了[**ODSPage背景**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)类来管理 ODS 文件中的背景。下面的代码示例演示了使用[**ODSPageBackground.Color**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#Color)属性向 ODS 文件添加颜色背景。请参阅[输出消耗臭氧层物质](ColoredBackground.ods)代码生成的文件供参考。

### **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSColoredBackground-1.java" >}}

## **向 ODS 文件添加图形背景**

Aspose.Cells 提供了[**ODSPage背景**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)类来管理 ODS 文件中的背景。下面的代码示例演示了使用[**ODSPageBackground.GraphicData**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#GraphicData)属性将图形背景添加到 ODS 文件。请参阅[输出消耗臭氧层物质](GraphicBackground.ods)代码生成的文件供参考。

### **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSGraphicBackground-1.java" >}}
