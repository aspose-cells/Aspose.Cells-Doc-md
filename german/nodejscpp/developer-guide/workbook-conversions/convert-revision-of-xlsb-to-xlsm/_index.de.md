---  
title: Revision einer XLSB in XLSM mit Node.js über C++ konvertieren  
linktitle: Revision von XLSB zu XLSM konvertieren  
type: docs  
weight: 290  
url: /de/nodejs-cpp/convert-revision-of-xlsb-to-xlsm/  
description: Lernen Sie, wie Sie Revisionen von XLSB Dateien vollständig in das XLSM Format mit Aspose.Cells for Node.js via C++ konvertieren.  
---  

{{% alert color="primary" %}}  

Aspose.Cells unterstützt jetzt die vollständige Konvertierung von Revisionen von XLSB-Dateien in XLSM-Dateien. Revisionen befinden sich im Pfad \xl\revisions. Sie können sie anzeigen, indem Sie die Erweiterung Ihrer XLSB-Datei in ZIP ändern. Der Pfad \xl\revisions enthält Dateien, die mit .bin enden.  

Wenn Sie Ihre XLSB-Datei mit Aspose.Cells in eine XLSM-Datei umwandeln, werden diese .bin-Dateien erfolgreich in .xml-Dateien umgewandelt, wie in diesen beiden Screenshots gezeigt.  

{{% /alert %}}  

Der folgende Code zeigt, wie Sie die XLSB-Datei mithilfe von Aspose.Cells for Node.js via C++ in das XLSM-Format konvertieren.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsb");

// Open workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save Workbook to XLSM format
workbook.save(path.join(dataDir, "output_out.xlsm"), AsposeCells.SaveFormat.Xlsm);
```  

