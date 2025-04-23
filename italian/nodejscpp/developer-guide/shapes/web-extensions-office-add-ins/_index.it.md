---  
title: Componenti Web  Componenti aggiuntivi Office con Node.js tramite C++  
linktitle: Estensioni Web  Componenti aggiuntivi di Office  
type: docs  
weight: 130  
url: /it/nodejs-cpp/web-extensions-office-add-ins/  
---  

Le estensioni Web estendono le applicazioni di Office e interagiscono con i contenuti nei documenti di Office. Le estensioni Web aggiungono funzionalità aggiuntive al client di Office per migliorare l'esperienza dell'utente e la produttività.

Aspose.Cells fornisce anche la capacità di lavorare con le estensioni Web.

## **Aggiungi estensione Web**

Puoi aggiungere Web Extensions (Office Add-in) in Excel cliccando sulla scheda **Inserisci** e poi cliccando sul collegamento **Store**/**Ottieni componenti aggiuntivi**. Nella casella dei componenti aggiuntivi, cerca l’addin desiderato e aggiungilo.

Aspose.Cells offre anche la funzione di aggiungere Web Extensions utilizzando le classi [**WebExtension**](https://reference.aspose.com/cells/nodejs-cpp/webextension) e [**WebExtensionTaskPane**](https://reference.aspose.com/cells/nodejs-cpp/webextensiontaskpane). Il seguente esempio di codice dimostra l’uso delle classi [**WebExtension**](https://reference.aspose.com/cells/nodejs-cpp/webextension) e [**WebExtensionTaskPane**](https://reference.aspose.com/cells/nodejs-cpp/webextensiontaskpane) per aggiungere un’estensione web a un file Excel. Si prega di consultare il [file Excel di output](89849869.xlsx) generato dal codice come riferimento.

### **Codice di Esempio**

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

## **Accesso alle informazioni sull'estensione Web**

Aspose.Cells fornisce la possibilità di accedere alle informazioni delle Web Extensions in un file Excel. Il seguente esempio di codice dimostra come accedere alle informazioni delle Web Extensions caricando il [file Excel di esempio](89849870.xlsx). Si prega di consultare l’output della console generato dal codice come riferimento.

### **Codice di Esempio**

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

### **Output della console**

{{< highlight javascript >}}

Width: 350

IsVisible: True

IsLocked: False

DockState: right

StoreName: en-US

StoreType: OMEX

WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF

{{< /highlight >}}  

