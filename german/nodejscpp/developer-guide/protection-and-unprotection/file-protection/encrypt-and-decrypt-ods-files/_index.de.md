---
title: ODS Dateien mit Node.js über C++ verschlüsseln und entschlüsseln
linktitle: ODS Dateien verschlüsseln und entschlüsseln
type: docs
weight: 10
url: /de/nodejs-cpp/encrypt-and-decrypt-ods-files/
description: ODS Dateien mit Aspose.Cells for Node.js via C++ passwortgeschützt und verschlüsselt. 
---

{{% alert color="primary" %}}
OpenOffice.org ist eine voll ausgestattete Office-Suite, die das Passwortschutz und die Verschlüsselung von Dateien unterstützt. Eine verschlüsselte ODS-Datei kann jedoch nur geöffnet werden, nachdem das Passwort eingegeben wurde. Excel kann die verschlüsselte ODS-Datei nicht öffnen und warnt möglicherweise. Die Verschlüsselungsoptionen sind für ODS-Dateien im Gegensatz zu anderen Dateitypen nicht anwendbar. 
Aspose.Cells ermöglicht die Verschlüsselung und Entschlüsselung von ODS-Dateien. Entschlüsselte ODS-Dateien können sowohl in Excel als auch in OpenOffice geöffnet werden.
{{% /alert %}}

## **Mit OpenOffice Calc verschlüsseln**
1. Wählen Sie **Speichern unter** und aktivieren Sie das Kästchen **Mit Passwort speichern**.
1. Klicken Sie auf die **Speichern**-Schaltfläche.
1. Geben Sie Ihr gewünschtes Passwort in die Felder **Kennwort eingeben zum Öffnen** und **Kennwort bestätigen** im Fenster **Passwort festlegen** ein, das geöffnet wird. 
1. Klicken Sie auf die Schaltfläche **OK**, um die Datei zu speichern.

## **ODS-Datei mit Aspose.Cells for Node.js via C++ verschlüsseln**
Um eine ODS-Datei zu verschlüsseln, laden Sie die Datei und setzen Sie den [**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--) Wert vor dem Speichern auf das tatsächliche Passwort. Die verschlüsselte ODS-Ausgabedatei kann nur in OpenOffice geöffnet werden.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "source");
const outputDir = path.join(__dirname, "output");

// Open an ODS file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleODSFile.ods"));

// Password protect the file
workbook.getSettings().setPassword("1234");

// Save the ODS file
workbook.save(path.join(outputDir, "outputEncryptedODSFile.ods"));
```

## **Entschlüsseln Sie die ODS-Datei mit Aspose.Cells for Node.js via C++**
Um eine ODS-Datei zu entschlüsseln, laden Sie die Datei, indem Sie ein Passwort in [**LoadOptions.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getPassword--) angeben. Sobald die Datei geladen ist, setzen Sie den [**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--) String auf null.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open an encrypted ODS file
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Ods);

// Set original password
loadOptions.setPassword("1234");

// Load the encrypted ODS file with the appropriate load options
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleEncryptedODSFile.ods"), loadOptions);

// Set the password to null
workbook.getSettings().setPassword(null);

// Save the decrypted ODS file
workbook.save(outputDir + "outputDecryptedODSFile.ods");
```
