---
title: Web扩展  Office插件
type: docs
weight: 130
url: /zh/net/web-extensions-office-add-ins/
---

Web扩展扩展了Office应用程序，并与Office文档中的内容交互。Web扩展为Office客户端添加了额外功能，以提高用户体验和提高工作效率。

Aspose.Cells还提供了与Web扩展配合使用的功能。

## **添加Web扩展**

你可以通过点击**插入**选项卡，然后点击**商店**/**获取附加组件**链接来在Excel中添加Web扩展(Office Add-ins)。在附加组件框中，浏览你想要的附加组件并添加它。

Aspose.Cells还提供了通过使用[**WebExtension**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextension)和[**WebExtensionTaskPane**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextensiontaskpane)类添加Web扩展的功能。以下代码示例演示了如何使用[**WebExtension**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextension)和[**WebExtensionTaskPane**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextensiontaskpane)类向Excel文件添加网页扩展。 请参考由代码生成的[输出Excel文件](89849869.xlsx)。

### **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AddWebExtension-1.cs" >}}

## **访问Web扩展信息**

Aspose.Cells提供了访问Excel文件中Web扩展信息的功能。以下代码示例演示了如何通过加载[示例Excel文件](89849870.xlsx)来访问Web扩展信息。 请参考由代码生成的控制台输出。

### **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AccessWebExtensionInformation-1.cs" >}}

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
{{< app/cells/assistant language="csharp" >}}
