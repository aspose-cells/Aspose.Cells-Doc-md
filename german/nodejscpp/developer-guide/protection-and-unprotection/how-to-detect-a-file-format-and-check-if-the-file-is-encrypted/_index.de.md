---  
title: Wie erkennt man ein Dateiformat und prüft, ob die Datei mit Node.js über C++ verschlüsselt ist  
linktitle: Wie man ein Dateiformat erkennt und überprüft, ob die Datei verschlüsselt ist  
type: docs  
weight: 2700  
url: /de/nodejs-cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/  
description: Lernen, wie man das Dateiformat erkennt und überprüft, ob eine Datei mit Aspose.Cells for Node.js via C++ verschlüsselt ist.  
---  

{{% alert color="primary" %}}  
Manchmal muss man das Format einer Datei erkennen, bevor man sie öffnet, da die Dateierweiterung nicht garantiert, dass der Inhalt geeignet ist. Die Datei könnte verschlüsselt (kennwortgeschützt) sein, sodass sie nicht direkt gelesen werden kann oder wir sollten sie nicht lesen. Aspose.Cells for Node.js via C++ bietet die statische Methode [**FileFormatUtil.detectFileFormat(Uint8Array)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#detectFileFormat-uint8array-) und einige relevante APIs, die Sie zur Verarbeitung von Dokumenten nutzen können.  
{{% /alert %}}  

Der folgende Beispielcode veranschaulicht, wie man ein Dateiformat (unter Verwendung des Dateipfads) erkennt und ihre Erweiterung überprüft. Sie können auch feststellen, ob die Datei verschlüsselt ist.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Detect file format
const info = AsposeCells.FileFormatUtil.detectFileFormat(new Uint8Array(require("fs").readFileSync(filePath)));

// Gets the detected load format
console.log("The spreadsheet format is: " + AsposeCells.FileFormatUtil.loadFormatToExtension(info.getLoadFormat()));

// Check if the file is encrypted.
console.log("The file is encrypted: " + info.isEncrypted());
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
