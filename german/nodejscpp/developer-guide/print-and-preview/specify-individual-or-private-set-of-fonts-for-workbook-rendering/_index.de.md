---  
title: Individuelle oder private Schriftartensätze für die Arbeitsmappenkonvertierung mit Node.js via C++ angeben  
linktitle: Individuelle oder private Schriftsätze für das Rendern von Arbeitsbüchern angeben  
type: docs  
weight: 40  
url: /de/nodejs-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/  
description: Erfahren Sie, wie Sie individuelle oder private Schriftartensätze für die Arbeitsmappenrendering mithilfe von Aspose.Cells for Node.js via C++ angeben.  
---  

## **Mögliche Verwendungsszenarien**  

Im Allgemeinen geben Sie das Verzeichnis oder die Liste der Schriftarten für alle Arbeitsmappen an, aber manchmal müssen Sie für Ihre Arbeitsmappen individuelle oder private Schriftartensätze angeben. Aspose.Cells for Node.js via C++ bietet die Klasse [**IndividualFontConfigs**](https://reference.aspose.com/cells/nodejs-cpp/individualfontconfigs), die verwendet werden kann, um individuelle oder private Schriftartensätze für Ihre Arbeitsmappe anzugeben.  

## **Individuelle oder private Schriftsätze für das Rendern von Arbeitsbüchern angeben**  

Der folgende Beispielcode lädt die [Beispieldatei Excel](67338268.xlsx) mit ihren individuellen oder privaten Schriftarten, die mit der Klasse [**IndividualFontConfigs**](https://reference.aspose.com/cells/nodejs-cpp/individualfontconfigs) angegeben sind. Bitte sehen Sie sich die [Beispielschriftart](67338271.zip) an, die im Code verwendet wird, sowie das [Ausgabepdf](67338269.pdf), das damit erstellt wurde. Die folgende Bildschirmaufnahme zeigt, wie das Ausgabepdf aussieht, wenn die Schriftart erfolgreich gefunden wird.  

![todo:image_alt_text](specify-individual-or-private-set-of-fonts-for-workbook-rendering_1.png)  

## **Beispielcode**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Path of your custom font directory.
const customFontsDir = "C:\\TempDir\\CustomFonts";

// Specify individual font configs custom font directory.
const fontConfigs = new AsposeCells.IndividualFontConfigs();

// If you comment this line or if custom font directory is wrong or 
// if it does not contain required font then output pdf will not be rendered correctly.
fontConfigs.setFontFolder(customFontsDir, false);

// Specify load options with font configs.
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
opts.setFontConfigs(fontConfigs);

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.xlsx");
// Output directory
const outputDir = path.join(__dirname, "output");
// Load the sample Excel file with individual font configs. 
const wb = new AsposeCells.Workbook(filePath, opts);

// Save to PDF format.
wb.save(outputDir + "outputSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.pdf", AsposeCells.SaveFormat.Pdf);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
