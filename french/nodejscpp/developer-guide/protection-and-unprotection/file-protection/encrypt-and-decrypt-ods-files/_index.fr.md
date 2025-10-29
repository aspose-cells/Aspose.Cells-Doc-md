---
title: Chiffrer et déchiffrer des fichiers ODS avec Node.js via C++
linktitle: Crypter et décrypter les fichiers ODS
type: docs
weight: 10
url: /fr/nodejs-cpp/encrypt-and-decrypt-ods-files/
description: Protéger par mot de passe et chiffrer des fichiers ODS en utilisant Aspose.Cells for Node.js via C++. 
---

{{% alert color="primary" %}}
OpenOffice.org est une suite bureautique complète qui supporte la protection par mot de passe et le chiffrement de fichiers. Cependant, un fichier ODS chiffré peut uniquement être ouvert par OpenOffice après avoir fourni le mot de passe. Excel ne peut pas ouvrir le fichier ODS chiffré et pourrait afficher des messages d’avertissement. Les options de chiffrement ne sont pas applicables aux fichiers ODS contrairement à d’autres types de fichiers. 
Aspose.Cells vous permet de chiffrer et déchiffrer des fichiers ODS. Les fichiers ODS déchiffrés peuvent être ouverts dans Excel et OpenOffice.
{{% /alert %}}

## **Chiffrer avec OpenOffice Calc**
1. Sélectionnez **Enregistrer sous** et cliquez sur la case **Enregistrer avec mot de passe**.
1. Cliquez sur le bouton **Enregistrer**.
1. Saisissez votre mot de passe souhaité dans les champs **Entrer le mot de passe pour ouvrir** et **Confirmer le mot de passe** dans la fenêtre Définir le mot de passe qui s'ouvre. 
1. Cliquez sur le bouton **OK** pour enregistrer le fichier.

## **Chiffrer le fichier ODS avec Aspose.Cells for Node.js via C++**
Pour chiffrer un fichier ODS, chargez le fichier et définissez la valeur [**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--) sur le mot de passe réel avant de l'enregistrer. Le fichier ODS chiffré en sortie peut être ouvert dans OpenOffice uniquement.

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

## **Déchiffrer le fichier ODS avec Aspose.Cells for Node.js via C++**
Pour déchiffrer un fichier ODS, chargez le fichier en fournissant un mot de passe dans le [**LoadOptions.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getPassword--). Une fois le fichier chargé, mettez la chaîne [**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--) à null.

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
{{< app/cells/assistant language="nodejs-cpp" >}}
