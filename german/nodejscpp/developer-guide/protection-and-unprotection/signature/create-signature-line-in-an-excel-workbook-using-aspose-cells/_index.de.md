---  
title: Signaturzeile in einer Excel Arbeitsmappe mit Aspose.Cells for Node.js via C++ erstellen  
linktitle: Erstellen Sie eine Signaturlinie in einer Excel Arbeitsmappe mit Aspose.Cells  
type: docs  
weight: 150  
url: /de/nodejs-cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/  
description: Dieser Artikel beschreibt, wie man mit Node.js Code und Aspose.Cells for Node.js via C++ eine Signaturzeile in einer Excel Arbeitsmappe erstellt.  
keywords: Signaturzeile in einer Excel Arbeitsmappe mit Node.js über C++ erstellen, Wie man eine Signaturzeile in einer Excel Arbeitsmappe erstellt, Wie man eine Signaturzeile hinzufügt, Wie man eine Signaturzeile zu Excel Dateien hinzufügt.  
---  

## **Einführung**  

Microsoft Excel bietet die Möglichkeit, **Signaturlinie** in Excel-Arbeitsmappen hinzuzufügen. Sie können eine Signaturlinie hinzufügen, indem Sie auf die Registerkarte **Einfügen** klicken und dann **Signaturlinie** aus der Gruppe **Text** auswählen.  

## **Wie man eine Signaturlinie für Excel erstellt**  

Aspose.Cells for Node.js via C++ bietet diese Funktion ebenfalls und hat die Eigenschaft [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) hierfür freigegeben. Dieser Artikel erklärt, wie man diese Eigenschaft nutzt, um eine Signaturzeile mit Aspose.Cells hinzuzufügen.  

Der folgende Beispielcode fügt eine Signaturzeile mit der Eigenschaft [**Picture.getSignatureLine()**](https://reference.aspose.com/cells/nodejs-cpp/picture/#getSignatureLine--) hinzu und speichert die Arbeitsmappe.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Create signature line object
const signatureLine = new AsposeCells.SignatureLine();
signatureLine.setSigner("John Doe");
signatureLine.setTitle("Development Lead");
signatureLine.setEmail("john.doe@aspose.com");

// Adds a Signature Line to the worksheet.
workbook.getWorksheets().get(0).getShapes().addSignatureLine(1, 1, signatureLine);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
