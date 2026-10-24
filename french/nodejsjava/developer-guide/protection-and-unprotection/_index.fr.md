---
title: Protéger et déprotéger
linktitle: Chiffrement et protection
description: Cette section explique comment chiffrer et déchiffrer des fichiers Excel et protéger les données Excel à l'aide de code JavaScript. Elle présente le chiffrement des fichiers, la protection en lecture seule, la protection de la structure du classeur, la protection des feuilles de calcul et les signatures numériques.
keywords: Aspose.Cells, Node.js via Java, chiffrer, déchiffrer, mot de passe, protéger, déprotéger, protection du classeur, protection de la feuille de calcul, lecture seule, signature numérique, JavaScript
type: docs
weight: 68
url: /fr/nodejs-java/protect-and-unprotect/
alias: [/nodejs-java/security-features/]
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Les classeurs Excel stockent souvent des informations financières, commerciales ou personnelles sensibles qui doivent être protégées contre tout accès non autorisé. Aspose.Cells for Node.js via Java propose un ensemble complet de fonctionnalités de protection qui reflète les capacités de Microsoft Excel, vous permettant de sécuriser vos données au niveau du fichier, au niveau du classeur et au niveau de la feuille de calcul.

{{% alert color="primary" %}}
Aspose.Cells for Node.js via Java offre une vaste gamme de fonctionnalités de protection, du niveau du fichier au niveau des données, comparables à celles de Microsoft Excel. Ces fonctionnalités comprennent le chiffrement des fichiers avec un mot de passe, l'imposition d'un accès en lecture seule au moyen d'un mot de passe de modification, la protection de la structure du classeur, la protection des feuilles de calcul et la signature numérique des classeurs.
{{% /alert %}}

## Chiffrer et déchiffrer les fichiers Excel
Un mot de passe défini sur un fichier Excel empêche les utilisateurs non autorisés d'ouvrir ou de consulter le contenu du classeur. Pour chiffrer un classeur, utilisez `workbook.getSettings().setPassword(...)` pour définir une chaîne de caractères comme mot de passe, puis enregistrez le classeur. Aspose.Cells écrit le fichier sous forme chiffrée. Pour ouvrir un classeur chiffré en vue de son déchiffrement, instanciez un objet `LoadOptions`, appelez `loadOptions.setPassword(...)` avec le même mot de passe que celui utilisé lors du chiffrement, puis transmettez cet objet au constructeur `Workbook`. Aspose.Cells applique de manière transparente le mot de passe fourni, afin que le reste de votre code puisse interagir avec le contenu déchiffré comme si le fichier était un classeur ordinaire.

```javascript
const AsposeCells = require("aspose.cells");
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
Excel prend en charge deux couches de mots de passe distinctes. La première est un mot de passe d'ouverture, qui chiffre le fichier lui-même et est traité dans la section précédente. La seconde est un mot de passe de modification, qui n'empêche pas les utilisateurs d'ouvrir le classeur ; Excel recommande plutôt d'ouvrir le fichier en mode lecture seule, sauf si le mot de passe de modification est fourni. Configurez ce comportement dans Aspose.Cells à l'aide de `workbook.getSettings().getWriteProtection()`. Affectez le mot de passe de modification à la propriété `Password` et le nom de la personne ayant appliqué la protection à la propriété `Author`. Utilisez la méthode `writeProtection.validatePassword(string)` pour vérifier le mot de passe de modification fourni. Elle retourne `true` en cas de correspondance et `false` dans le cas contraire.

```javascript
const AsposeCells = require("aspose.cells");
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
La protection de la structure du classeur empêche les autres utilisateurs d'afficher les feuilles de calcul masquées, d'ajouter de nouvelles feuilles de calcul ou de déplacer, de supprimer, de masquer ou de renommer des feuilles de calcul. L'état de protection concerne la structure des feuilles de calcul, et non le contenu des cellules qu'elles contiennent. Pour appliquer cette protection, appelez `workbook.protect(ProtectionType.Structure, "password")`. Pour supprimer la protection, appelez `workbook.unprotect("password")` et fournissez le mot de passe correct. La valeur d'énumération `ProtectionType.Structure` est utilisée ici ; elle se distingue des autres types de protection, tels que `ProtectionType.Windows`.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
// Ajouter une deuxième feuille de calcul
workbook.getWorksheets().add();
// Écrire une valeur d'exemple dans la cellule A1 de la première feuille de calcul
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data");
// Protéger la structure du classeur
workbook.protect(AsposeCells.ProtectionType.STRUCTURE, "StructPwd");
// Enregistrer le classeur sous structure_protected.xlsx
let filePath = "structure_protected.xlsx";
workbook.save(filePath);
// Recharger le fichier dans une nouvelle instance de classeur
let loadedWorkbook = new AsposeCells.Workbook(filePath);
// Supprimer la protection de la structure
loadedWorkbook.unprotect("StructPwd");
// Afficher le message de confirmation
console.log("Structure protection has been successfully removed from the workbook.");
```

## Protéger et déprotéger les feuilles de calcul
La protection de la feuille de calcul verrouille les cellules d'une feuille de calcul contre toute modification accidentelle ou délibérée. Les utilisateurs ne peuvent pas modifier les cellules verrouillées sans fournir le mot de passe. Il s'agit de la protection généralement utilisée pour protéger les formules, les en-têtes ou les zones de saisie de données prévues dans les feuilles de calcul partagées. Pour protéger une feuille de calcul, appelez `worksheet.protect(ProtectionType.All, "password")`. L'utilisation de `ProtectionType.All` active toutes les options de protection disponibles, telles que la sélection des cellules verrouillées, la mise en forme des cellules, l'insertion de lignes et de colonnes, ainsi que la suppression de lignes et de colonnes. Pour supprimer la protection, appelez `worksheet.unprotect("password")` avec le mot de passe correct. Pour obtenir un contrôle plus précis, combinez d'autres types de protection, tels que `Contents`, `Objects` et `Scenarios`, à l'aide de l'opérateur OU bit à bit.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
sheet.getCells().get("A1").putValue("Sample Data");
sheet.protect(AsposeCells.ProtectionType.ALL, "SheetPwd");
workbook.save("sheet_protected.xlsx");
let workbookReloaded = new AsposeCells.Workbook("sheet_protected.xlsx");
let sheetReloaded = workbookReloaded.getWorksheets().get(0);
sheetReloaded.unprotect("SheetPwd");
console.log("Worksheet protection removed successfully.");
```

## Ajouter et valider les signatures numériques
Une signature numérique atteste aux destinataires l'authenticité du contenu du classeur et garantit qu'il n'a pas été modifié depuis la signature du classeur. Aspose.Cells prend en charge les signatures numériques via des classes telles que `AsposeCells.DigitalSignature` et `AsposeCells.DigitalSignatureCollection`. Le flux typique crée un `AsposeCells.DigitalSignature` directement à partir d'un fichier de certificat `.pfx` avec son mot de passe et ses commentaires de signature, ajoute la signature à une `DigitalSignatureCollection`, puis applique la collection au classeur via `workbook.addDigitalSignature(DigitalSignatureCollection)`. La propriété `DigitalSignature.Comments` peut consigner le contexte de signature, par exemple l'heure de signature et sa finalité. Toute modification apportée au classeur après la signature invalide celle-ci. Une étape de validation du côté du destinataire peut donc détecter toute altération.

```javascript
const AsposeCells = require("aspose.cells");
let signature = new AsposeCells.DigitalSignature("signature.pfx", "pfx-password", "Signed by Aspose.Cells", new Date());
let signatures = new AsposeCells.DigitalSignatureCollection();
signatures.add(signature);
let workbook = new AsposeCells.Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value");
workbook.addDigitalSignature(signatures);
workbook.save("signed_workbook.xlsx");
console.log("The workbook has been digitally signed.");
```

{{< app/cells/assistant language="nodejs-java" >}}