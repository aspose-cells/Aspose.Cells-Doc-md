---
title: Uppdatera ActiveX ComboBox kontroll med Node.js via C++
linktitle: Uppdatera ActiveX ComboBox kontroll
type: docs
weight: 170
url: /sv/nodejs-cpp/update-activex-combobox-control/
description: Lär dig hur du läser och skriver värden för ActiveX ComboBox kontrollen med Aspose.Cells for Node.js via C++. 
---

## **Möjliga användningsscenario**
Du kan läsa eller skriva värdena för ActiveX ComboBox-kontrollen med Aspose.Cells for Node.js via C++. Vänligen få åtkomst till kontrollen via [Shape.getActiveXControl()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getActiveXControl--) egenskapen och kontrollera dess typ via [ActiveXControlBase.getType()](https://reference.aspose.com/cells/nodejs-cpp/activexcontrolbase/#getType--) egenskapen, den bör returnera värdet [ControlType.ComboBox](https://reference.aspose.com/cells/nodejs-cpp/controltype/) och sedan kasta om det till [ComboBoxActiveXControl](https://reference.aspose.com/cells/nodejs-cpp/comboboxactivexcontrol/) objekt för att läsa eller ändra dess olika egenskaper.

Vänligen ladda ner den [provexemplet Excel-fil](5115124.xlsx) som används i följande provkod.
## **Uppdatera ActiveX ComboBox Control**
Följande skärmbild visar effekten av provkoden på den [provexemplet Excel-filen](5115124.xlsx). Som du kan se har ActiveX ComboBox-värdet uppdaterats till "Detta är kombinationsruta-kontroll".

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **Exempelkod**
Följande provkod uppdaterar värdet för ActiveX ComboBox Control som finns i [provexemplet Excel-filen](5115124.xlsx).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SourceFile_activex.xlsx");
// Create a workbook
const wb = new AsposeCells.Workbook(filePath);

// Access first shape from first worksheet
const shape = wb.getWorksheets().get(0).getShapes().get(0);

// Access ActiveX ComboBox Control and update its value
if (shape.getActiveXControl() != null)
{
// Access Shape ActiveX Control
const c = shape.getActiveXControl();

if (c instanceof AsposeCells.ComboBoxActiveXControl)
{
// Type cast ActiveXControl into ComboBoxActiveXControl and change its value
const comboBoxActiveX = new AsposeCells.ComboBoxActiveXControl(c);
comboBoxActiveX.setValue("This is combo box control with updated value.");

}

}

// Save the workbook
const outputFilePath = path.join(dataDir, "OutputFile_out.xlsx");
wb.save(outputFilePath);
```
