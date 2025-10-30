---  
title: Wie man die AutoRecover Eigenschaft einer Arbeitsmappe mit Node.js über C++ festlegt  
linktitle: So legen Sie die Eigenschaft AutoRecover einer Arbeitsmappe fest  
type: docs  
weight: 220  
url: /de/nodejs-cpp/how-to-set-autorecover-property-of-workbook/  
description: Erfahren Sie, wie Sie die AutoRecover Eigenschaft einer Arbeitsmappe mit Aspose.Cells for Node.js via C++ festlegen.  
---  

{{% alert color="primary" %}}  
Sie können Aspose.Cells verwenden, um die AutoRecover-Eigenschaft der Arbeitsmappe festzulegen. Der Standardwert dieser Eigenschaft ist **true**. Wenn Sie sie auf **false** setzen, deaktiviert Microsoft Excel AutoRecover (Autospeichern) für diese Excel-Datei.  

Aspose.Cells bietet die [**Workbook.getAutoRecover()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getAutoRecover--)-Eigenschaft, um diese Option zu aktivieren oder zu deaktivieren.  
{{% /alert %}}  

Der folgende Code erklärt, wie die Eigenschaft [**Workbook.getAutoRecover()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getAutoRecover--) der Arbeitsmappe verwendet wird. Der Code liest zunächst den Standardwert dieser Eigenschaft, der **true** ist, setzt sie dann auf **false** und speichert die Arbeitsmappe. Anschließend liest er die Arbeitsmappe erneut und liest den Wert dieser Eigenschaft, der jetzt **false** ist.  

## Node.js-Code zum Festlegen der AutoRecover-Eigenschaft der Arbeitsmappe  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Read AutoRecover property
console.log("AutoRecover: " + workbook.getSettings().getAutoRecover());

// Set AutoRecover property to false
workbook.getSettings().setAutoRecover(false);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));

// Read the saved workbook again
const workbook2 = new AsposeCells.Workbook(path.join(dataDir, "output_out.xlsx"));

// Read AutoRecover property
console.log("AutoRecover: " + workbook2.getSettings().getAutoRecover());
```  

## **Ergebnis**  

Hier ist die Konsolenausgabe des obigen Beispielcodes.  

{{< highlight java >}}  
AutoRecover: True  
AutoRecover: False  
{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
