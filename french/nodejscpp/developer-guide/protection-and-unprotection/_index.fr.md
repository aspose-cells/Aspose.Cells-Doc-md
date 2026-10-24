---
title: Protéger et Déprotéger avec Node.js via C++
linktitle: Chiffrement et protection
description: Cette section présente comment chiffrer et déchiffrer des fichiers Excel et protéger les données Excel, couvrant le chiffrement des fichiers, la protection en lecture seule, la protection de la structure du classeur, la protection des feuilles de calcul et les signatures numériques à l'aide de code JavaScript
keywords: Aspose.Cells, Node.js, C++, chiffrer, déchiffrer, mot de passe, protéger, déprotéger, protection du classeur, protection de la feuille de calcul, lecture seule, signature numérique, JavaScript
type: docs
weight: 68
url: /fr/nodejs-cpp/protect-and-unprotect/
alias: [/nodejs-cpp/security-features/]
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Les classeurs Excel stockent souvent des informations sensibles, financières, commerciales ou personnelles qui doivent être préservées de tout accès non autorisé. Aspose.Cells for Node.js via C++ offre un ensemble complet de fonctionnalités de protection qui reflète les capacités de Microsoft Excel, vous permettant de sécuriser vos données au niveau du fichier, du classeur et de la feuille de calcul.

{{% alert color="primary" %}}
Aspose.Cells for Node.js via C++ offre une large gamme de fonctionnalités de protection, du niveau fichier au niveau des données, similaires à MS Excel. Ces capacités incluent le chiffrement des fichiers avec un mot de passe, l'application d'un accès en lecture seule via un mot de passe de modification, la protection de la structure du classeur, la protection des feuilles de calcul et la signature numérique des classeurs.
{{% /alert %}}

## Chiffrer et déchiffrer les fichiers Excel
Un mot de passe défini sur un fichier Excel empêche les utilisateurs non autorisés d'ouvrir ou de visualiser le contenu du classeur. Pour chiffrer un classeur, affectez une chaîne de mot de passe à `workbook.getSettings().setPassword()`, puis enregistrez le classeur. Aspose.Cells écrit le fichier sous forme chiffrée. Pour ouvrir un classeur chiffré en vue de son déchiffrement, instanciez un objet `LoadOptions`, définissez `loadOptions.setPassword()` avec le même mot de passe que celui utilisé lors du chiffrement, puis transmettez-le au constructeur `Workbook`. Aspose.Cells applique le mot de passe fourni de manière transparente, afin que le reste de votre code puisse interagir avec le contenu déchiffré comme si le fichier était un classeur ordinaire.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
let cell = sheet.getCells().get("A1");
cell.putValue("Confidential Data");
workbook.getSettings().setPassword("OpenPassword123");
workbook.save("encrypted.xlsx");
let loadOptions = new AsposeCells.LoadOptions();
loadOptions.setPassword("OpenPassword123");
let decryptedWorkbook = new AsposeCells.Workbook("encrypted.xlsx", loadOptions);
console.log("Decrypted cell A1 value: " + decryptedWorkbook.getWorksheets().get(0).getCells().get("A1").getStringValue());
```

## Protection en lecture seule (mot de passe de modification)
Excel prend en charge deux couches distinctes de mots de passe. La première est un mot de passe d'ouverture, qui chiffre le fichier lui-même et qui est abordé dans la section précédente. La seconde est un mot de passe de modification, qui n'empêche pas les utilisateurs d'ouvrir le classeur ; Excel recommande plutôt d'ouvrir le fichier en mode lecture seule, sauf si le mot de passe de modification est fourni. Configurez ce comportement dans Aspose.Cells via `workbook.getSettings().getWriteProtection()`. Définissez sa propriété `password` avec le mot de passe de modification et sa propriété `author` pour identifier l'auteur de la protection. Utilisez la méthode `writeProtection.validatePassword(string)` pour vérifier si un mot de passe de modification fourni est correct, en retournant `true` en cas de correspondance et `false` sinon.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
// Écrire une valeur d'exemple dans la cellule A1 de la première feuille de calcul
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data");
// Configurer la protection en écriture : définir le mot de passe de modification et l'auteur
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd");
workbook.getSettings().getWriteProtection().setAuthor("AuthorName");
// Enregistrer le classeur pour que la protection en écriture soit persistante
workbook.save("WriteProtectedWorkbook.xlsx");
// Valider le mot de passe de modification en utilisant le mot de passe correct
let isCorrectValid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd");
console.log("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
// Valider le mot de passe de modification en utilisant un mot de passe incorrect pour démontrer l'autre branche
let isWrongValid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd");
console.log("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## Protéger et déprotéger la structure du classeur
La protection de la structure du classeur empêche les autres utilisateurs d'afficher les feuilles de calcul masquées, d'ajouter de nouvelles feuilles de calcul, de déplacer des feuilles de calcul, de supprimer des feuilles de calcul, de masquer des feuilles de calcul ou de renommer des feuilles de calcul. L'état protégé s'applique à la structure des feuilles et non au contenu des cellules à l'intérieur de celles-ci. Pour appliquer la protection de la structure, appelez `workbook.protect(ProtectionType.Structure, "password")`. Pour supprimer la protection, appelez `workbook.unprotect("password")` et fournissez le mot de passe correct. La valeur d'énumération `ProtectionType.Structure` est utilisée ici et se distingue des autres types de protection tels que `ProtectionType.Windows`.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
// Ajouter une deuxième feuille de calcul
workbook.getWorksheets().add();
// Écrire une valeur d'exemple dans la cellule A1 de la première feuille de calcul
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data");
// Protéger la structure du classeur
workbook.protect(AsposeCells.ProtectionType.Structure, "StructPwd");
// Enregistrer le classeur sous structure_protected.xlsx
let filePath = "structure_protected.xlsx";
workbook.save(filePath);
// Recharger le fichier dans une nouvelle instance de Workbook
let loadedWorkbook = new AsposeCells.Workbook(filePath);
// Supprimer la protection de la structure
loadedWorkbook.unprotect("StructPwd");
// Afficher le message de confirmation
console.log("Structure protection has been successfully removed from the workbook.");
```

## Protéger et déprotéger les feuilles de calcul
La protection de la feuille de calcul verrouille les cellules d'une feuille de calcul contre toute modification accidentelle ou délibérée. Les utilisateurs ne peuvent pas modifier les cellules verrouillées sans fournir le mot de passe. Il s'agit de la protection généralement utilisée pour sécuriser les formules, les en-têtes ou les zones de saisie de données désignées dans les feuilles de calcul partagées. Pour protéger une feuille de calcul, appelez `worksheet.protect(ProtectionType.All, "password")`. L'utilisation de `ProtectionType.All` active toutes les options de protection disponibles, telles que la sélection de cellules verrouillées, la mise en forme des cellules, l'insertion de lignes et de colonnes, ainsi que la suppression de lignes et de colonnes. Pour supprimer la protection, appelez `worksheet.unprotect("password")` avec le mot de passe correct. Un contrôle plus fin est disponible en combinant d'autres types de protection tels que `Contents`, `Objects` et `Scenarios` à l'aide de l'opérateur OR bit à bit.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
sheet.getCells().get("A1").putValue("Sample Data");
sheet.protect(AsposeCells.ProtectionType.All, "SheetPwd");
workbook.save("sheet_protected.xlsx");
let workbookReloaded = new AsposeCells.Workbook("sheet_protected.xlsx");
let sheetReloaded = workbookReloaded.getWorksheets().get(0);
sheetReloaded.unprotect("SheetPwd");
console.log("Worksheet protection removed successfully.");
```

## Ajouter et valider les signatures numériques
Une signature numérique garantit aux destinataires que le contenu du classeur est authentique et qu'il n'a pas été modifié depuis sa signature. Aspose.Cells prend en charge les signatures numériques via l'espace de noms `Aspose.Cells.DigitalSignatures`. Le flux de travail typique charge un fichier de certificat `.pfx` à l'aide des utilitaires cryptographiques de Node.js, l'enveloppe dans un `Aspose.Cells.DigitalSignatures.DigitalSignature`, ajoute la signature à une `DigitalSignatureCollection`, puis applique la collection au classeur via `workbook.addDigitalSignature(digitalSignatureCollection)`. La propriété `digitalSignature.comments` peut enregistrer le contexte de la signature, tel que l'heure et l'objectif de la signature. Toute modification apportée au classeur après la signature invalide la signature, de sorte qu'une étape de validation côté réception peut détecter toute falsification.

```javascript
const AsposeCells = require("aspose.cells.node");
let signature = new AsposeCells.DigitalSignature("signature.pfx", "pfx-password", "Signed by Aspose.Cells", new Date());
let signatures = new AsposeCells.DigitalSignatureCollection();
signatures.add(signature);
let workbook = new AsposeCells.Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value");
workbook.addDigitalSignature(signatures);
workbook.save("signed_workbook.xlsx");
console.log("The workbook has been digitally signed.");
```

## Articles connexes
- [Chiffrer et déchiffrer des fichiers Excel](/cells/fr/nodejs-cpp/encrypt-and-decrypt-excel-files/)
- [Protéger et déprotéger la structure du classeur](/cells/fr/nodejs-cpp/protect-and-unprotect-workbook-structure/)
- [Protéger et déprotéger une feuille de calcul](/cells/fr/nodejs-cpp/protect-and-unprotect-worksheets/)
- [Protéger ou déprotéger par mot de passe le classeur partagé](/cells/fr/nodejs-cpp/password-protect-or-unprotect-the-shared-workbook/)
- [Attribuer et valider des signatures numériques](/cells/fr/nodejs-cpp/assign-and-validate-digital-signatures/)
- [Vérifier le mot de passe de modification à l'aide d'Aspose.Cells](/cells/fr/nodejs-cpp/check-password-to-modify-using-aspose-cells/)
- [Détecter le format de fichier des fichiers Office Open XML chiffrés - OOXML](/cells/fr/nodejs-cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Chiffrement des fichiers Excel](/cells/fr/nodejs-cpp/encrypting-excel-files/)
- [Comment détecter un format de fichier et vérifier si le fichier est chiffré](/cells/fr/nodejs-cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="nodejs-cpp" >}}