---
title: 在ODS文件中使用背景
type: docs
weight: 170
url: /zh/java/working-with-background-in-ods-files/
---

## **ODS文件中的背景**

在 ODS 文件中可以添加背景。背景可以是颜色背景或图形背景。文件打开时背景不可见，但如果该文件被打印为 PDF，则背景在生成的 PDF 中可见。打印预览对话框中也会显示背景。

Aspose.Cells 提供了读取背景信息并在 ODS 文件中添加背景的功能。

## **从 OSD 文件中读取背景信息**

Aspose.Cells 提供了管理 ODS 文件中背景的[**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)类。以下代码示例演示了通过加载[source ODS文件](GraphicBackground.ods)并读取背景信息来使用[**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)类。请参考代码生成的控制台输出。

### **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-ReadODSBackground-1.java" >}}

### **控制台输出**

背景类型：图形

背景位置：水平居中垂直居中

## **为ODS文件添加彩色背景**

Aspose.Cells 提供了管理 ODS 文件中背景的[**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)类。以下代码示例演示了使用[**ODSPageBackground.Color**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#Color)属性向 ODS 文件添加颜色背景。请参考代码生成的[output ODS文件](ColoredBackground.ods)。

### **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSColoredBackground-1.java" >}}

## **为ODS文件添加图形背景**

Aspose.Cells 提供了管理 ODS 文件中背景的[**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)类。以下代码示例演示了使用[**ODSPageBackground.GraphicData**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#GraphicData)属性向 ODS 文件添加图形背景。请参考代码生成的[output ODS文件](GraphicBackground.ods)。

### **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSGraphicBackground-1.java" >}}
