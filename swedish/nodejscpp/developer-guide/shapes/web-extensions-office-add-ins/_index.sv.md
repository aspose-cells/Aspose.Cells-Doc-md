---  
title: Web tillägg  Office tillägg med Node.js via C++  
linktitle: Webbutökningar  Office tillägg  
type: docs  
weight: 130  
url: /sv/nodejs-cpp/web-extensions-office-add-ins/  
---  

Webbutökningar utökar Office-applikationer och interagerar med innehållet i Office-dokument. Webbutökningar lägger till ytterligare funktionalitet till Office-klienten för att förbättra användarupplevelsen och produktiviteten.

Aspose.Cells ger också möjligheten att arbeta med webbutökningar.

## **Lägg till webbförlängning**

Du kan lägga till Webutvidgningar (Office-tillägg) i Excel genom att klicka på fliken **Insätt** och sedan klicka på länken **Butik**/**Hämta tillägg**. I Tilläggsboxen bläddrar du efter det tillägg du vill ha och lägger till det.

Aspose.Cells erbjuder också möjligheten att lägga till Webutvidgningar med hjälp av [**WebExtension**](https://reference.aspose.com/cells/nodejs-cpp/webextension)- och [**WebExtensionTaskPane**](https://reference.aspose.com/cells/nodejs-cpp/webextensiontaskpane)-klasserna. Följande kodexempel visar hur man använder [**WebExtension**](https://reference.aspose.com/cells/nodejs-cpp/webextension)- och [**WebExtensionTaskPane**](https://reference.aspose.com/cells/nodejs-cpp/webextensiontaskpane)-klasser för att lägga till ett webbutvidgning till en Excel-fil. Se [utdata-Excelfilen](89849869.xlsx) genererad av koden för referens.

### **Exempelkod**

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

## **Få tillgång till information om webbförlängning**

Aspose.Cells ger möjligheten att komma åt information om Webutvidgningar i en Excel-fil. Följande kodexempel visar hur man får åtkomst till webbutvidgningsinformation genom att ladda [exempel-Excelfilen](89849870.xlsx). Se den genererade konsolutmatningen för referens.

### **Exempelkod**

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

### **Konsoloutput**

{{< highlight javascript >}}

Width: 350

IsVisible: True

IsLocked: False

DockState: right

StoreName: en-US

StoreType: OMEX

WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF

{{< /highlight >}}  

