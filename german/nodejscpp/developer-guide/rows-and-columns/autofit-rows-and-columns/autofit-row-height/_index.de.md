---
title: Automatisches Anpassen der Zeilenhöhe beim Laden einer Datei mit Node.js über C++
linktitle: Automatische Anpassung der Zeilenhöhe beim Laden der Datei
type: docs
weight: 120
url: /de/nodejs-cpp/autofit-row-height/
description: Erfahren Sie, wie Sie Zeilen anpassen können, deren Höhe nicht individuell eingestellt ist, beim Laden einer Datei mit Aspose.Cells for Node.js via C++.
keywords: Automatisches Anpassen der Zeilenhöhe beim Laden einer Datei mit Node.js über C++, automatische Anpassung der Zeilenhöhe beim Öffnen einer Excel Datei mit Node.js über C++ 
---

## **Mögliche Verwendungsszenarien**
Die Höhe der Zeile passt sich automatisch an die Schriftart des Inhalts an, aber wenn die Höhe der zwischengespeicherten Zeile nicht mit der Höhe des Inhalts in der Datei übereinstimmt, wird MS Excel die Zeilenhöhe beim Laden der Datei automatisch anpassen, während Aspose.Cells for Node.js via C++ dies aus Leistungsgründen nicht automatisch macht. Wenn Sie das Aspose.Cells-Programm verwenden möchten, um die Zeilenhöhen beim Laden von Dateien automatisch anzupassen, können Sie dies durch den Parameter [setAutoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setAutoFitterOptions-autofitteroptions-) in Ihrem Code erreichen.

Bitte beachten Sie die folgende Bilddaten. Wir können beobachten, dass die zwischengespeicherte Zeilenhöhe in Zeile 11 15 beträgt, aber Excel hat die Zeilenhöhe beim Laden der Datei automatisch angepasst.
<br>
<img src="1.png" width=70% />

## **Zeilenhöhe mit Aspose.Cells for Node.js via C++ anpassen**
Wenn Sie die Datei direkt laden und im PDF-Format speichern, werden die Daten im PDF nicht vollständig angezeigt, da die zwischengespeicherte Zeilenhöhe nur 15 beträgt.
<br>
<img src="2.png" width=70% />
<br>
Wenn Sie beim Laden der Datei den Parameter [setAutoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setAutoFitterOptions-autofitteroptions-) auf true setzen, passt Aspose.Cells die Zeilenhöhe automatisch an. Die angepasste Zeilenhöhe kann die Textanzeige effektiv gewährleisten.
<br>
<img src="3.png" width=70% />

## **Beispielcode für Node.js**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
workbook.save(path.join(dataDir, "out.pdf"));

const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setAutoFitterOptions(new AsposeCells.AutoFitterOptions());
loadOptions.getAutoFitterOptions().setOnlyAuto(true);
const book = new AsposeCells.Workbook(filePath, loadOptions);
book.save(path.join(dataDir, "out2.pdf"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
