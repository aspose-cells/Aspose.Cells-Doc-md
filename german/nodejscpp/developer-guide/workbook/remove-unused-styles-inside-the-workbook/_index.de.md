---  
title: Nicht verwendete Styles innerhalb der Arbeitsmappe mit Node.js über C++ entfernen  
linktitle: Entfernen Sie unbenutzte Stile innerhalb der Arbeitsmappe  
type: docs  
weight: 340  
url: /de/nodejs-cpp/remove-unused-styles-inside-the-workbook/  
description: Lernen Sie, wie Sie nicht verwendete Styles aus einer Arbeitsmappe mit Aspose.Cells for Node.js via C++ entfernen können.  
---  

{{% alert color="primary" %}}  
Unbenutzte Stile in Excel-Dateien beanspruchen nicht nur Speicherplatz, sondern verursachen auch Leistungsprobleme beim Umwandeln in verschiedene Formate wie PDF, HTML usw. Aspose.Cells bietet [**Workbook.removeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#removeUnusedStyles--) zum Entfernen aller unbenutzten Stile innerhalb der Arbeitsmappe.  
{{% /alert %}}  

Der folgende Code erklärt die Verwendung von [**Workbook.removeUnusedStyles()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#removeUnusedStyles--). Der Code lädt die [Vorlagendatei](5115520.xlsx), die Sie über den bereitgestellten Link herunterladen können. Sie enthält einen unbenutzten Stil namens **AsposeStyle**; dieser Stil und alle anderen unbenutzten Stile werden nach der Ausführung des Codes entfernt.  

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Template-With-Unused-Custom-Style.xlsx");

// Load template excel file containing unused styles
const workbook = new AsposeCells.Workbook(filePath);

// Remove all unused styles inside the template this will also remove AsposeStyle which is an unused style inside the template
workbook.removeUnusedStyles();

// Save the file
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
