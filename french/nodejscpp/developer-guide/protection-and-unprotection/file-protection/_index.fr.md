---  
title: Chiffrer et déchiffrer des fichiers Excel avec Node.js via C++  
linktitle: Chiffrer et déchiffrer les fichiers Excel  
type: docs  
weight: 10  
url: /fr/nodejs-cpp/encrypt-and-decrypt-excel-files/  
description: Comment chiffrer et déchiffrer des fichiers Excel en utilisant Node.js via C++. Verrouiller et déverrouiller des fichiers Excel.  
---  

{{% alert color="primary" %}}  
Microsoft Excel (97 - 365) vous permet de chiffrer et de protéger par mot de passe vos feuilles de calcul. Il utilise des algorithmes fournis par un fournisseur de services cryptographiques (CSP), un ensemble d'algorithmes cryptographiques avec différentes propriétés. Le CSP par défaut est 'Compatible avec Office 97/2000' ou 'Chiffrement faible (XOR)'. Il est important de choisir la bonne longueur de clé de chiffrement. Certains CSP ne prennent pas en charge plus de 40 ou 56 bits. Cela est considéré comme un chiffrement faible. Pour un chiffrement fort, une longueur de clé minimale de 128 bits est requise. Microsoft Windows contient également des CSP qui offrent des types de chiffrement forts, par exemple le 'Fournisseur cryptographique fort Microsoft'. Pour vous donner une idée, un chiffrement de 128 bits est ce que les banques utilisent pour chiffrer la connexion avec leurs systèmes de banque en ligne.  

Aspose.Cells vous permet de chiffrer et de protéger par mot de passe des fichiers Microsoft Excel avec le type de chiffrement de votre choix.  
{{% /alert %}}  

## **Utilisation de Microsoft Excel**  

Pour définir les paramètres de chiffrement de fichier dans Microsoft Excel (ici Microsoft Excel 2003) :  

1. Dans le menu **Outils**, sélectionnez **Options**. Une boîte de dialogue apparaîtra.  
 2. Sélectionnez l'onglet **Sécurité**.  
 3. Entrez un mot de passe et cliquez sur **Avancé**  
 4. Choisissez le type de chiffrement et confirmez le mot de passe.  

## ** Chiffrement du fichier Excel avec Aspose.Cells for Node.js via C++**  

L'exemple suivant montre comment crypter et protéger par mot de passe un fichier Excel à l'aide de l'API Aspose.Cells.  

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

### ** Spécification de l'option Mot de passe pour modification**  

L'exemple suivant montre comment définir l'option **Mot de passe pour modifier** de Microsoft Excel pour un fichier existant à l'aide de l'API Aspose.Cells.  

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


## ** Déchiffrement du fichier Excel avec Aspose.Cells for Node.js via C++**  
Il est très facile d'ouvrir un fichier Excel protégé par mot de passe et de le décrypter en utilisant l'API Aspose.Cells comme indiqué dans le code suivant :  

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


## **Sujets avancés**  
- [Chiffrer et déchiffrer des fichiers ODS](/cells/fr/nodejs-cpp/encrypt-and-decrypt-ods-files/)  
- [Définition du type de chiffrement fort](/cells/fr/nodejs-cpp/setting-strong-encryption-type/)  
- [Spécifier l'auteur lors de la protection en écriture du classeur](/cells/fr/nodejs-cpp/specify-author-while-write-protecting-workbook/)  
- [Vérifier le mot de passe des fichiers chiffrés](/cells/fr/nodejs-cpp/verify-password-of-encrypted-excel-and-ods-files/)  


