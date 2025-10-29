---
title: Web扩展  Office插件
type: docs
weight: 130
url: /zh/python-net/web-extensions-office-add-ins/
---

Web扩展扩展了Office应用程序，并与Office文档中的内容交互。Web扩展为Office客户端添加了额外功能，以提高用户体验和提高工作效率。

Aspose.Cells for Python via .NET还提供了处理Web扩展的功能。

## **添加Web扩展**

你可以通过点击**插入**选项卡，然后点击**商店**/**获取附加组件**链接来在Excel中添加Web扩展(Office Add-ins)。在附加组件框中，浏览你想要的附加组件并添加它。

Aspose.Cells for Python via .NET还提供了通过[**WebExtension**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextension)和[**WebExtensionTaskPane**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextensiontaskpane)类添加Web扩展的功能。以下示例演示了使用[**WebExtension**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextension)和[**WebExtensionTaskPane**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextensiontaskpane)类为Excel文件添加Web扩展。请参阅由代码生成的[输出Excel文件](89849869.xlsx)，作为参考。

### **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-WebExtension-Workbook-AddWebExtension-1.py" >}}

## **访问Web扩展信息**

Aspose.Cells for Python via .NET提供了访问Excel文件中Web扩展信息的能力。以下示例演示了加载[示例Excel文件](89849870.xlsx)以访问Web扩展信息。请查看代码生成的控制台输出作为参考。

### **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-WebExtension-Workbook-AccessWebExtensionInformation-1.py" >}}

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
{{< app/cells/assistant language="python-net" >}}
