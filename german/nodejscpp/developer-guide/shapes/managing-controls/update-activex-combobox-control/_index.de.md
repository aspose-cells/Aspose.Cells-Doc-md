---
title: Aktualisieren Sie das ActiveX ComboBox Steuerelement mit Node.js via C++
linktitle: Aktualisieren Sie die ActiveX ComboBox Steuerelemente
type: docs
weight: 170
url: /de/nodejs-cpp/update-activex-combobox-control/
description: Lernen, wie man Werte eines ActiveX ComboBox Steuerelements mit Aspose.Cells for Node.js via C++ liest und schreibt. 
---

## **Mögliche Verwendungsszenarien**
 Sie können die Werte des ActiveX-ComboBox-Steuerelements mit Aspose.Cells for Node.js via C++ lesen oder schreiben. Greifen Sie auf das ActiveX-Steuerelement über [Shape.getActiveXControl()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getActiveXControl--) zu und prüfen Sie seinen Typ über [ActiveXControlBase.getType()](https://reference.aspose.com/cells/nodejs-cpp/activexcontrolbase/#getType--), es sollte den Wert [ControlType.ComboBox](https://reference.aspose.com/cells/nodejs-cpp/controltype/) zurückgeben, und wandeln Sie es dann in ein [ComboBoxActiveXControl](https://reference.aspose.com/cells/nodejs-cpp/comboboxactivexcontrol/) Objekt um, um seine Eigenschaften zu lesen oder zu modifizieren.

Bitte laden Sie die im folgenden Beispielcode verwendete [Beispieldatei](5115124.xlsx) herunter.
## **Aktualisieren Sie das ActiveX-ComboBox-Steuerelement**
Der folgende Screenshot zeigt die Auswirkung des Beispielcodes auf die [Beispieldatei](5115124.xlsx). Wie Sie sehen können, wurde der Wert der ActiveX-ComboBox auf "Dies ist die Kombinationsfeldsteuerung" aktualisiert.

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **Beispielcode**
Der folgende Beispielcode aktualisiert den Wert des ActiveX-ComboBox-Steuerungselements, das sich in der [Beispieldatei Excel](5115124.xlsx) befindet.

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
