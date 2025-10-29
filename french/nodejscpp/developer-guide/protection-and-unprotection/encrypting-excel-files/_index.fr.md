---
title: Crypter des fichiers Excel avec Node.js via C++
linktitle: Chiffrement des fichiers Excel
type: docs
weight: 90
url: /fr/nodejs-cpp/encrypting-excel-files/
description: Apprenez comment chiffrer et protéger par mot de passe des fichiers Excel avec Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) vous permet de chiffrer et de protéger par mot de passe vos feuilles de calcul. Il utilise des algorithmes fournis par un fournisseur de services cryptographiques (CSP), un ensemble d'algorithmes cryptographiques avec différentes propriétés. Le CSP par défaut est 'Compatible avec Office 97/2000' ou 'Chiffrement faible (XOR)'. Il est important de choisir la bonne longueur de clé de chiffrement. Certains CSP ne prennent pas en charge plus de 40 ou 56 bits. Cela est considéré comme un chiffrement faible. Pour un chiffrement fort, une longueur de clé minimale de 128 bits est requise. Microsoft Windows contient également des CSP qui offrent des types de chiffrement forts, par exemple le 'Fournisseur cryptographique fort Microsoft'. Pour vous donner une idée, un chiffrement de 128 bits est ce que les banques utilisent pour chiffrer la connexion avec leurs systèmes de banque en ligne.

Aspose.Cells vous permet de chiffrer et de protéger par mot de passe des fichiers Microsoft Excel avec le type de chiffrement de votre choix.

{{% /alert %}}

## **Utilisation de Microsoft Excel**

Pour définir les paramètres de chiffrement de fichier dans Microsoft Excel (ici Microsoft Excel 2003) :

1. Dans le menu **Outils**, sélectionnez **Options**. Une boîte de dialogue apparaîtra.
1. Sélectionnez l'onglet **Sécurité**.
1. Saisissez un mot de passe et cliquez sur **Avancé**
1. Choisissez le type de chiffrement et confirmez le mot de passe.

## ** Chiffrement avec Aspose.Cells for Node.js via C++**

L'exemple suivant montre comment chiffrer et protéger par mot de passe un fichier Excel à l'aide de l'API Aspose.Cells.

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

### **Option de spécification du mot de passe pour modifier**

L'exemple suivant montre comment définir l'option **Mot de passe pour modifier** de Microsoft Excel pour un fichier existant à l'aide de l'API Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Set the password for modification.
workbook.getSettings().getWriteProtection().setPassword("1234");

// Save the excel file.
workbook.save(path.join(dataDir, "SpecifyPasswordToModifyOption.out.xls"));
```

## **Vérifiez le mot de passe du fichier chiffré**

 Pour vérifier le mot de passe du fichier crypté, Aspose.Cells for Node.js via C++ fournit la méthode [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-). Ces méthodes acceptent deux paramètres, le flux de fichier et le mot de passe à vérifier.
Le code d'exemple suivant démontre l'utilisation de la méthode [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-) pour vérifier si le mot de passe fourni est valide ou non.

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

## **Chiffrement/Déchiffrement du fichier ODS avec Aspose.Cells**

 Aspose.Cells vous permet de chiffrer et de déchiffrer les fichiers ODS. Le fichier ODS décrypté peut être ouvert dans Excel et OpenOffice, cependant le fichier ODS crypté ne peut être ouvert que par OpenOffice après avoir fourni le mot de passe. Excel ne peut pas ouvrir le fichier ODS crypté et peut afficher un message d'avertissement. Les options de chiffrement ne sont pas applicables pour les fichiers ODS contrairement à d'autres types de fichiers. Pour chiffrer un fichier ODS, chargez-le et définissez la valeur [**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--) avec le mot de passe réel avant de l'enregistrer. Le fichier ODS crypté de sortie peut uniquement être ouvert dans OpenOffice.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = RunExamples.Get_SourceDirectory();
// Output directory
const outputDir = RunExamples.Get_OutputDirectory();

// Open an ODS file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleODSFile.ods"));

// Password protect the file
workbook.getSettings().setPassword("1234");

// Save the ODS file
workbook.save(path.join(outputDir, "outputEncryptedODSFile.ods"));
```

Pour déchiffrer un fichier ODS, chargez le fichier en fournissant un mot de passe dans le [**LoadOptions.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getPassword--). Une fois le fichier chargé, définissez la chaîne [**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--) comme nulle.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

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
{{< app/cells/assistant language="nodejs-cpp" >}}
