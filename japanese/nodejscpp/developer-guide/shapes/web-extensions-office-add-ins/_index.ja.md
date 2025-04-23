---  
title: Web拡張機能  Office アドインをNode.jsをC++経由で  
linktitle: Web拡張機能  Officeアドイン  
type: docs  
weight: 130  
url: /ja/nodejs-cpp/web-extensions-office-add-ins/  
---  

Web拡張機能は、Officeアプリケーションを拡張し、Office文書のコンテンツとやり取りします。Web拡張機能は、ユーザーエクスペリエンスと生産性を向上させるためにOfficeクライアントに追加機能を提供します。

Aspose.CellsもWeb拡張機能と連携する機能を提供しています。

## **Web拡張機能の追加**

ExcelにWeb拡張機能（Officeアドイン）を追加できます。**挿入**タブをクリックし、その後**ストア**/**アドインを取得**リンクをクリックしてください。アドインボックスで目的のアドインを参照して追加します。

Aspose.Cellsは、[**WebExtension**](https://reference.aspose.com/cells/nodejs-cpp/webextension)と[**WebExtensionTaskPane**](https://reference.aspose.com/cells/nodejs-cpp/webextensiontaskpane)クラスを使用してWeb拡張を追加する機能も提供します。次のコード例は、[**WebExtension**](https://reference.aspose.com/cells/nodejs-cpp/webextension)と[**WebExtensionTaskPane**](https://reference.aspose.com/cells/nodejs-cpp/webextensiontaskpane)クラスを使用してExcelファイルにWeb拡張を追加する方法を示しています。詳細は[出力Excelファイル](89849869.xlsx)を参照してください。

### **サンプルコード**

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

## **Web拡張機能情報へのアクセス**

Aspose.Cellsは、Excelファイル内のWeb拡張情報にアクセスする機能を提供します。次のコード例は、[サンプルExcelファイル](89849870.xlsx)をロードし、Web拡張情報にアクセスする方法を示しています。結果はコンソール出力から確認できます。

### **サンプルコード**

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

### **コンソール出力**

{{< highlight javascript >}}

Width: 350

IsVisible: True

IsLocked: False

DockState: right

StoreName: en-US

StoreType: OMEX

WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF

{{< /highlight >}}  

