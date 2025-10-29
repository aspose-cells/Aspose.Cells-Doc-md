---
title: 使用 Golang 通过 C++ 操作 ODS 文件中的背景
linktitle: 在ODS文件中使用背景
type: docs
weight: 150
url: /zh/go-cpp/working-with-background-in-ods-files/
description: 了解如何使用 Golang 通过 C++ 和 Aspose.Cells 管理 ODS 文件中的彩色和图形背景。
---

## **ODS文件中的背景**

可以将背景添加到ODS文件中的工作表。背景可以是彩色背景或图形背景。在打开文件时背景不可见，但如果文件作为PDF打印，则在生成的PDF中可以看到背景。在打印预览对话框中也可以看到背景。

Aspose.Cells提供了读取后台信息并在ODS文件中添加背景的能力。

## **从ODS文件读取背景信息**

 Aspose.Cells 提供 [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) 类来管理 ODS 文件中的背景。以下示例演示了通过加载 [源 ODS](90112030.ods) 文件并读取背景信息来使用 [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) 类。请参阅代码生成的控制台输出作为参考。

### **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithBackgroundInOdsFiles.go" >}}
### **控制台输出**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **向ODS文件添加彩色背景**

 Aspose.Cells 提供 [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) 类来管理 ODS 文件中的背景。以下示例演示了如何使用 [**OdsPageBackground.Color**](https://reference.aspose.com/cells/cpp/aspose.cells/color/) 属性向 ODS 文件添加彩色背景。请参阅代码生成的 [输出 ODS](90112031.ods) 文件作为参考。

### **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithBackgroundInOdsFiles-1.go" >}}
## **向ODS文件添加图形背景**

 Aspose.Cells 提供 [**OdsPageBackground**](https://reference.aspose.com/cells/go-cpp/odspagebackground/) 类来管理 ODS 文件中的背景。以下示例演示了如何使用 [**OdsPageBackground.GetGraphicData()**](https://reference.aspose.com/cells/go-cpp/odspagebackground/getgraphicdata/) 属性向 ODS 文件添加图形背景。请参阅代码生成的 [输出 ODS](90112030.ods) 文件作为参考。

### **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithBackgroundInOdsFiles-2.go" >}}
