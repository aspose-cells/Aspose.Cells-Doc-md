---  
title: Excel Dateien mit Node.js via C++ verschlüsseln und entschlüsseln  
linktitle: Excel Dateien verschlüsseln und entschlüsseln  
type: docs  
weight: 10  
url: /de/nodejs-cpp/encrypt-and-decrypt-excel-files/  
description: So verschlüsseln und entschlüsseln Sie Excel Dateien mit Node.js via C++. Sperren und entsperren Sie Excel Dateien.  
---  

{{% alert color="primary" %}}  
Microsoft Excel (97 - 365) ermöglicht es Ihnen, Ihre Tabellenkalkulationen zu verschlüsseln und mit einem Passwort zu schützen. Es verwendet Algorithmen, die von einem kryptografischen Dienstanbieter oder CSP bereitgestellt werden, ein Satz kryptografischer Algorithmen mit unterschiedlichen Eigenschaften. Der Standard-CSP ist 'Office 97/2000 Kompatibel' oder 'Schwache Verschlüsselung (XOR)'. Es ist wichtig, die richtige Schlüssellänge zu wählen. Einige CSPs unterstützen nicht mehr als 40 oder 56 Bits. Das gilt als schwache Verschlüsselung. Für starke Verschlüsselung ist eine Mindestschlüssellänge von 128 Bits erforderlich. Microsoft Windows enthält ebenfalls CSPs, die starke Verschlüsselungstypen anbieten, wie z. B. den 'Microsoft Strong Cryptographic Provider'. Um Ihnen eine Vorstellung zu geben, 128-Bit-Verschlüsselung wird von Banken verwendet, um die Verbindung mit ihren Internetbanking-Systemen zu verschlüsseln.  

Mit Aspose.Cells können Sie Microsoft Excel-Dateien mit dem gewünschten Verschlüsselungstyp verschlüsseln und mit einem Passwort schützen.  
{{% /alert %}}  

## **Verwendung von Microsoft Excel**  

Um die Dateiverschlüsselungseinstellungen in Microsoft Excel festzulegen (hier Microsoft Excel 2003):  

1. Wählen Sie im Menü **Extras** die Option **Optionen** aus. Es wird ein Dialogfeld angezeigt.  
2. Klicken Sie auf die Registerkarte **Sicherheit**.  
3. Geben Sie ein Passwort ein und klicken Sie auf **Erweitert**  
4. Wählen Sie den Verschlüsselungstyp aus und bestätigen Sie das Passwort.  

## **Excel-Datei mit Aspose.Cells for Node.js via C++ verschlüsseln**  

Das folgende Beispiel zeigt, wie man eine Excel-Datei mit Aspose.Cells API verschlüsselt und passwortgeschützt macht.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Specify XOR encryption type.
workbook.setEncryptionOptions(AsposeCells.EncryptionType.XOR, 40);

// Specify Strong Encryption type (RC4, Microsoft Strong Cryptographic Provider).
workbook.setEncryptionOptions(AsposeCells.EncryptionType.StrongCryptographicProvider, 128);

// Password protect the file.
workbook.getSettings().setPassword("1234");

// Save the excel file.
workbook.save(path.join(dataDir, "encryptedBook1.out.xls"));
```  

### **Option zum Passwort zum Ändern angeben**  

Das folgende Beispiel zeigt, wie Sie die **Passwort zum Ändern** Microsoft Excel-Option für eine vorhandene Datei mithilfe der Aspose.Cells-API festlegen.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xls"));

// Set the password for modification.
workbook.getSettings().getWriteProtection().setPassword("1234");

// Save the excel file.
workbook.save(path.join(dataDir, "SpecifyPasswordToModifyOption.out.xls"));
```  


## **Entschlüsseln der Excel-Datei mit Aspose.Cells for Node.js via C++**  
Es ist sehr einfach, eine passwortgeschützte Excel-Datei mit Aspose.Cells API zu öffnen und zu entschlüsseln, wie im folgenden Code gezeigt:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open encrypted file with password.
const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setPassword("password");
const workbook = new AsposeCells.Workbook(filePath, loadOptions);

// Remove password.
workbook.getSettings().setPassword(null);

// Save the file.
workbook.save(filePath);
```  


## **Erweiterte Themen**  
- [ODS-Dateien verschlüsseln und entschlüsseln](/cells/de/nodejs-cpp/encrypt-and-decrypt-ods-files/)  
- [Festlegen des Verschlüsselungstyps](/cells/de/nodejs-cpp/setting-strong-encryption-type/)  
- [Autor beim Schreibschutz des Arbeitsmappenschreibens spezifizieren](/cells/de/nodejs-cpp/specify-author-while-write-protecting-workbook/)  
- [Passwort von verschlüsselten Dateien überprüfen](/cells/de/nodejs-cpp/verify-password-of-encrypted-excel-and-ods-files/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
