---  
title: Fügen Sie benutzerdefinierte XML Teile hinzu und wählen Sie sie nach ID mit Node.js via C++ aus  
linktitle: Benutzerdefinierte XML Teile hinzufügen und nach ID auswählen  
type: docs  
weight: 70  
url: /de/nodejs-cpp/add-custom-xml-parts-and-select-them-by-id/  
description: Erfahren Sie, wie man benutzerdefinierte XML Teile zu Excel Dokumenten hinzufügt und sie nach ID mit Aspose.Cells for Node.js via C++ auswählt.  
---  

## **Mögliche Verwendungsszenarien**  

Benutzerdefinierte XML-Teile sind die XML-Daten, die in den Microsoft Excel-Dokumenten gespeichert sind und von den Anwendungen genutzt werden, die damit arbeiten. Derzeit gibt es keine direkte Möglichkeit, sie mit der Microsoft Excel-Benutzeroberfläche hinzuzufügen. Sie können sie jedoch programmatisch auf verschiedene Arten hinzufügen, z.B. mit VSTO, mit Aspose.Cells usw. Verwenden Sie [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--), wenn Sie ein benutzerdefiniertes XML-Teil mithilfe der Aspose.Cells-API hinzufügen möchten. Sie können auch seine ID mit der Eigenschaft [**CustomXmlPart.getID()**](https://reference.aspose.com/cells/nodejs-cpp/customxmlpart/#getID--) setzen. Wenn Sie ein benutzerdefiniertes XML-Teil nach ID auswählen möchten, verwenden Sie [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--) Methode.  

## **Benutzerdefinierte XML-Teile hinzufügen und nach ID auswählen**  

Der folgende Beispielcode fügt zuerst vier benutzerdefinierte XML-Teile mit [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--)-Methode hinzu. Dann setzt er ihre IDs mit der [**CustomXmlPart.getID()**](https://reference.aspose.com/cells/nodejs-cpp/customxmlpart/#getID--)-Eigenschaft. Schließlich findet oder wählt er eines der hinzugefügten benutzerdefinierten XML-Teile mit [**Workbook.getCustomXmlParts()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getCustomXmlParts--)-Methode aus. Bitte beachten Sie auch die Konsolenausgabe des unten angegebenen Codes als Referenz.  

## **Beispielcode**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);

// Some data in the form of byte array.
// Please use correct XML and Schema instead.
const btsData = new Uint8Array([1, 2, 3]);
const btsSchema = new Uint8Array([1, 2, 3]);

// Create four custom xml parts.
wb.getCustomXmlParts().add(btsData, btsSchema);
wb.getCustomXmlParts().add(btsData, btsSchema);
wb.getCustomXmlParts().add(btsData, btsSchema);
wb.getCustomXmlParts().add(btsData, btsSchema);

// Assign ids to custom xml parts.
wb.getCustomXmlParts().get(0).setID("Fruit");
wb.getCustomXmlParts().get(1).setID("Color");
wb.getCustomXmlParts().get(2).setID("Sport");
wb.getCustomXmlParts().get(3).setID("Shape");

// Specify search custom xml part id.
let srchID = "Fruit";
srchID = "Color";
srchID = "Sport";

// Search custom xml part by the search id.
const cxp = wb.getCustomXmlParts().selectByID(srchID);

// Print the found or not found message on console.
if (cxp.isNull()) {
console.log(`Not Found: CustomXmlPart ID ${srchID}`);
} else {
console.log(`Found: CustomXmlPart ID ${srchID}`);
}

console.log("AddCustomXMLPartsAndSelectThemByID executed successfully.");
```  

## **Konsolenausgabe**  

{{< highlight java >}}  
 Found: CustomXmlPart ID Sport  
{{< /highlight >}}  

