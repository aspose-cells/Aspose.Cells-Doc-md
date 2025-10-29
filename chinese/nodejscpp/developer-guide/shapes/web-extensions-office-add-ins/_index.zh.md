---  
title: Web扩展  使用Node.js通过C++开发Office加载项  
linktitle: Web扩展  Office插件  
type: docs  
weight: 130  
url: /zh/nodejs-cpp/web-extensions-office-add-ins/  
---  

Web扩展扩展了Office应用程序，并与Office文档中的内容交互。Web扩展为Office客户端添加了额外功能，以提高用户体验和提高工作效率。

Aspose.Cells还提供了与Web扩展配合使用的功能。

## **添加Web扩展**

可以通过点击 **插入** 标签，然后点击 **商店**/**获取加载项** 链接，在Excel中添加Web扩展（Office加载项）。在加载项框中浏览你想要的加载项并添加它。

Aspose.Cells 还提供了使用 [**WebExtension**](https://reference.aspose.com/cells/nodejs-cpp/webextension) 和 [**WebExtensionTaskPane**](https://reference.aspose.com/cells/nodejs-cpp/webextensiontaskpane) 类添加Web扩展的功能。以下代码演示了如何用 [**WebExtension**](https://reference.aspose.com/cells/nodejs-cpp/webextension) 和 [**WebExtensionTaskPane**](https://reference.aspose.com/cells/nodejs-cpp/webextensiontaskpane) 类为Excel文件添加Web扩展。请参阅由代码生成的 [输出Excel文件](89849869.xlsx)。

### **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const outDir = path.join(__dirname, "output");

const workbook = new AsposeCells.Workbook();

const extensions = workbook.getWorksheets().getWebExtensions();
const taskPanes = workbook.getWorksheets().getWebExtensionTaskPanes();

const extensionIndex = extensions.add();
const taskPaneIndex = taskPanes.add();

const extension = extensions.get(extensionIndex);
extension.getReference().setId("wa104379955");
extension.getReference().setStoreName("en-US");
extension.getReference().setStoreType(AsposeCells.WebExtensionStoreType.OMEX);

const taskPane = taskPanes.get(taskPaneIndex);
taskPane.setIsVisible(true);
taskPane.setDockState("right");
taskPane.setWebExtension(extension);

workbook.save(path.join(outDir, "AddWebExtension_Out.xlsx"));
```

## **访问Web扩展信息**

Aspose.Cells 提供了访问Excel文件中Web扩展信息的能力。以下示例展示了如何加载 [示例Excel文件](89849870.xlsx) 来访问Web扩展信息。请查看代码生成的控制台输出。

### **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Load sample Excel file
const filePath = path.join(sourceDir, "WebExtensionsSample.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const taskPanes = workbook.getWorksheets().getWebExtensionTaskPanes();

for (let i = 0; i < taskPanes.getCount(); i++) {
const taskPane = taskPanes.get(i);
console.log("Width: " + taskPane.getWidth());
console.log("IsVisible: " + taskPane.isVisible());
console.log("IsLocked: " + taskPane.isLocked());
console.log("DockState: " + taskPane.getDockState());
console.log("StoreName: " + taskPane.getWebExtension().getReference().getStoreName());
console.log("StoreType: " + taskPane.getWebExtension().getReference().getStoreType());
console.log("WebExtension.Id: " + taskPane.getWebExtension().getId());
}
```

### **控制台输出**

{{< highlight javascript >}}

Width: 350

IsVisible: True

IsLocked: False

DockState: right

StoreName: en-US

StoreType: OMEX

WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
