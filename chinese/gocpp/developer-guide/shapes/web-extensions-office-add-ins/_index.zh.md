---
title: Web扩展  Office插件用Golang通过C++实现
linktitle: Web扩展  Office插件
type: docs
weight: 130
url: /zh/go-cpp/web-extensions-office-add-ins/
description: 学习如何使用Aspose.Cells通过Golang与C++在Excel文件中添加和访问Web扩展（Office插件）。
---

Web扩展扩展Office应用程序并与Office文档中的内容交互。Web扩展为Office客户端添加额外功能，以改善用户体验和生产力。

Aspose.Cells还提供了与Web扩展配合使用的功能。

## **添加Web扩展**

可以通过点击 **插入** 标签，然后点击 **商店**/**获取加载项** 链接，在Excel中添加Web扩展（Office加载项）。在加载项框中浏览你想要的加载项并添加它。

Aspose.Cells 还提供了使用 [**WebExtension**](https://reference.aspose.com/cells/go-cpp/webextension/) 和 [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/) 类添加Web扩展的功能。以下代码演示了如何用 [**WebExtension**](https://reference.aspose.com/cells/go-cpp/webextension/) 和 [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/) 类为Excel文件添加Web扩展。请参阅由代码生成的 [输出Excel文件](89849869.xlsx)。

### **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WebExtensionsOfficeAddIns.go" >}}
## **访问Web扩展信息**

Aspose.Cells 提供了访问Excel文件中Web扩展信息的能力。以下示例展示了如何加载 [示例Excel文件](89849870.xlsx) 来访问Web扩展信息。请查看代码生成的控制台输出。

### **示例代码**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WebExtensionsOfficeAddIns-1.go" >}}
### **控制台输出**

{{< highlight java >}}
Width: 350
IsVisible: True
IsLocked: False
DockState: right
StoreName: en-US
StoreType: OMEX
WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF
{{< /highlight >}}
