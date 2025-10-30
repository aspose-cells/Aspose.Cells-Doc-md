---
title: Aggiorna il controllo ActiveX ComboBox con Node.js tramite C++
linktitle: Aggiorna il controllo ComboBox ActiveX
type: docs
weight: 170
url: /it/nodejs-cpp/update-activex-combobox-control/
description: Impara come leggere e scrivere i valori del controllo ActiveX ComboBox usando Aspose.Cells for Node.js via C++. 
---

## **Possibili Scenari di Utilizzo**
Puoi leggere o scrivere i valori del controllo ActiveX ComboBox usando Aspose.Cells for Node.js via C++. Accedi al controllo ActiveX tramite la proprietà [Shape.getActiveXControl()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getActiveXControl--) e controlla il suo tipo tramite la proprietà [ActiveXControlBase.getType()](https://reference.aspose.com/cells/nodejs-cpp/activexcontrolbase/#getType--), dovrebbe restituire il valore [ControlType.ComboBox](https://reference.aspose.com/cells/nodejs-cpp/controltype/) e poi castarlo in un oggetto [ComboBoxActiveXControl](https://reference.aspose.com/cells/nodejs-cpp/comboboxactivexcontrol/) per leggere o modificare le sue varie proprietà.

Si prega di scaricare il [file Excel di esempio](5115124.xlsx) utilizzato nel seguente codice di esempio.
## **Aggiorna il controllo ComboBox ActiveX**
Lo screenshot seguente mostra l'effetto del codice di esempio sul [file Excel di esempio](5115124.xlsx). Come si può vedere, il valore del ComboBox ActiveX è stato aggiornato a "Questo è un controllo combobox".

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **Codice di Esempio**
Il seguente codice di esempio aggiorna il valore del controllo ActiveX ComboBox presente all'interno del [file Excel di esempio](5115124.xlsx).

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
{{< app/cells/assistant language="nodejs-cpp" >}}
