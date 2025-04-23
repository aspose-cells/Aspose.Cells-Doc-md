---  
title: Extensions Web  Compléments Office avec Node.js via C++  
linktitle: Extensions Web  Modules complémentaires Office  
type: docs  
weight: 130  
url: /fr/nodejs-cpp/web-extensions-office-add-ins/  
---  

Les extensions Web étendent les applications Office et interagissent avec le contenu des documents Office. Les extensions Web ajoutent des fonctionnalités supplémentaires au client Office pour améliorer l'expérience utilisateur et la productivité.

Aspose.Cells offre également la possibilité de travailler avec des extensions Web.

## **Ajouter une extension Web**

Vous pouvez ajouter des extensions Web (compléments Office) dans Excel en cliquant sur l'onglet **Insertion** puis en cliquant sur le lien **Store**/**Obtenir des compléments**. Dans la boîte de dialogue Add-ins, recherchez le complément souhaité et ajoutez-le.

Aspose.Cells offre également la fonctionnalité d'ajouter des extensions Web en utilisant les classes [**WebExtension**](https://reference.aspose.com/cells/nodejs-cpp/webextension) et [**WebExtensionTaskPane**](https://reference.aspose.com/cells/nodejs-cpp/webextensiontaskpane). L'exemple de code suivant montre comment utiliser les classes [**WebExtension**](https://reference.aspose.com/cells/nodejs-cpp/webextension) et [**WebExtensionTaskPane**](https://reference.aspose.com/cells/nodejs-cpp/webextensiontaskpane) pour ajouter une extension Web à un fichier Excel. Veuillez consulter le [fichier Excel de sortie](89849869.xlsx) généré par le code pour référence.

### **Code d'exemple**

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

## **Accéder aux informations sur l'extension Web**

Aspose.Cells permet d'accéder aux informations des extensions Web dans un fichier Excel. L'exemple de code ci-dessous montre comment accéder aux informations des extensions Web en chargeant le [fichier Excel d'exemple](89849870.xlsx). Veuillez consulter la sortie console générée par le code pour référence.

### **Code d'exemple**

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

### **Sortie console**

{{< highlight javascript >}}

Width: 350

IsVisible: True

IsLocked: False

DockState: right

StoreName: en-US

StoreType: OMEX

WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF

{{< /highlight >}}  

