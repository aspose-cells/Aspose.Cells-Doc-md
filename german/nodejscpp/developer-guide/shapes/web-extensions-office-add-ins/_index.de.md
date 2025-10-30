---  
title: Web Erweiterungen  Office Add ins mit Node.js via C++  
linktitle: Web Erweiterungen  Office Add ins  
type: docs  
weight: 130  
url: /de/nodejs-cpp/web-extensions-office-add-ins/  
---  

Web-Erweiterungen erweitern Office-Anwendungen und interagieren mit dem Inhalt in Office-Dokumenten. Web-Erweiterungen fügen Office-Clients zusätzliche Funktionen hinzu, um die Benutzererfahrung und Produktivität zu verbessern.

Aspose.Cells bietet auch die Möglichkeit, mit Web-Erweiterungen zu arbeiten.

## **Web-Erweiterung hinzufügen**

Sie können Web-Erweiterungen (Office-Add-Ins) in Excel hinzufügen, indem Sie auf die Registerkarte **Einfügen** klicken und dann auf den Link **Store**/**Add-Ins holen**. Im Add-In-Fenster durchsuchen Sie nach dem gewünschten Add-In und fügen es hinzu.

Aspose.Cells bietet auch die Funktion, Web-Erweiterungen mit den Klassen [**WebExtension**](https://reference.aspose.com/cells/nodejs-cpp/webextension) und [**WebExtensionTaskPane**](https://reference.aspose.com/cells/nodejs-cpp/webextensiontaskpane) hinzuzufügen. Das folgende Codebeispiel zeigt die Verwendung der Klassen [**WebExtension**](https://reference.aspose.com/cells/nodejs-cpp/webextension) und [**WebExtensionTaskPane**](https://reference.aspose.com/cells/nodejs-cpp/webextensiontaskpane), um eine Web-Erweiterung zu einer Excel-Datei hinzuzufügen. Bitte sehen Sie sich die [Ausgabedatei](89849869.xlsx) an, die durch den Code erstellt wurde.

### **Beispielcode**

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

## **Zugriff auf Web-Erweiterungsinformationen**

Aspose.Cells ermöglicht den Zugriff auf Informationen von Web-Erweiterungen in einer Excel-Datei. Das folgende Codebeispiel zeigt, wie man Web-Erweiterungsinformationen durch Laden der [Beispiel-Excel-Datei](89849870.xlsx) abruft. Bitte sehen Sie sich die Konsolenausgabe an, die vom Code erzeugt wird.

### **Beispielcode**

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

### **Konsolenausgabe**

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
