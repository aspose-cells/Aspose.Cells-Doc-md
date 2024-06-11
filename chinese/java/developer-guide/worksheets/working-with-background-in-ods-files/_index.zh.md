---
title: 在ODS文件中使用背景
type: docs
weight: 170
url: /zh/java/working-with-background-in-ods-files/
---

## **ODS文件中的背景**

ODS 文件的工作表可以添加背景。背景可以是颜色背景或图形背景。在打开文件时，背景是看不见的，但如果将文件打印为 PDF，则在生成的 PDF 中背景是可见的。在打印预览对话框中，背景同样是可见的。

Aspose.Cells提供了读取ODS文件中背景信息和添加背景的功能。

## **从OSD文件中读取背景信息**

Aspose.Cells提供了[**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)类来管理ODS文件中的背景。以下代码示例演示了通过加载源ODS文件读取背景信息，使用[**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)类的用法。请参考由代码生成的控制台输出。

### **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-ReadODSBackground-1.java" >}}

### **控制台输出**

背景类型：图形

背景位置：中心位置

## **向ODS文件添加彩色背景**

Aspose.Cells提供了[**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)类来管理ODS文件中的背景。以下代码示例演示了使用[**ODSPageBackground.Color**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#Color)属性向ODS文件添加彩色背景。请参考由代码生成的输出ODS文件。

### **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSColoredBackground-1.java" >}}

## **向ODS文件添加图形背景**

Aspose.Cells提供了[**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground)类来管理ODS文件中的背景。以下代码示例演示了使用[**ODSPageBackground.GraphicData**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#GraphicData)属性向ODS文件添加图形背景。请参考由代码生成的输出ODS文件。

### **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSGraphicBackground-1.java" >}}
