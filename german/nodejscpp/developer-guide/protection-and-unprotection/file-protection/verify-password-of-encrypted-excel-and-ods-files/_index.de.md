---  
title: Passwort von verschlüsselten Dateien mit Node.js über C++ überprüfen  
linktitle: Passwort von verschlüsselten Dateien verifizieren  
type: docs  
weight: 10  
url: /de/nodejs-cpp/verify-password-of-encrypted-excel-and-ods-files/  
description: Überprüfen Sie das Passwort verschlüsselter Excel (xlsx, xlsb, xls, xlsm) und Open Office (ODS) Dateien mit Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Wenn Excel- (xlsx, xlsb, xls, xlsm) und Open Office- (ODS) Dateien mit einem Passwort gesperrt sind, unterstützt Aspose eine einfache Passwortüberprüfung, ohne spezifische Daten der Dateien zu analysieren.  
{{% /alert %}}  

## **Das Passwort der verschlüsselten Datei verifizieren**  

Um das Passwort der verschlüsselten Datei zu überprüfen, bietet Aspose.Cells for Node.js via C++ die [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-) Methode an. Diese Methode akzeptiert zwei Parameter, den Datenstrom der Datei und das zu überprüfende Passwort.  
Der folgende Code-Schnipsel zeigt die Verwendung der Methode [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-) zur Überprüfung, ob das angegebene Passwort gültig ist oder nicht.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "EncryptedBook1.xlsx");

// Create a Stream object
const fs = require("fs");
const fstream = fs.readFileSync(filePath);

const isPasswordValid = AsposeCells.FileFormatUtil.verifyPassword(fstream, "1234");

console.log("Password is Valid: " + isPasswordValid);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
