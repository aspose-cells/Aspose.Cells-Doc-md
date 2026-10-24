---
title: Protéger et déprotéger
linktitle: Protéger et déprotéger
description: Cette section explique comment chiffrer et déchiffrer des fichiers Excel et protéger les données Excel, couvrant le chiffrement des fichiers, la protection en lecture seule, la protection de la structure du classeur, la protection des feuilles de calcul et les signatures numériques à l'aide de code C#
keywords: Aspose.Cells, .NET, chiffrer, déchiffrer, mot de passe, protéger, déprotéger, protection du classeur, protection de la feuille de calcul, lecture seule, signature numérique, C#
type: docs
weight: 68
url: /fr/net/protect-and-unprotect/
alias: [/net/security-features/]
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Les classeurs Excel contiennent souvent des informations sensibles, financières, commerciales ou personnelles qui doivent être protégées contre tout accès non autorisé. Aspose.Cells for .NET offre un ensemble complet de fonctionnalités de protection qui reflète les capacités de Microsoft Excel, vous permettant de sécuriser vos données au niveau du fichier, du classeur et de la feuille de calcul.

{{% alert color="primary" %}}
Aspose.Cells for .NET propose une large gamme de fonctionnalités de protection, du niveau du fichier au niveau des données, similaires à celles de MS Excel. Ces capacités comprennent le chiffrement des fichiers avec un mot de passe, l'application d'un accès en lecture seule via un mot de passe de modification, la protection de la structure du classeur, la protection des feuilles de calcul et la signature numérique des classeurs.
{{% /alert %}}

## Chiffrer et déchiffrer des fichiers Excel
Un mot de passe défini sur un fichier Excel empêche les utilisateurs non autorisés d'ouvrir ou de consulter le contenu du classeur. Pour chiffrer un classeur, attribuez une chaîne de mot de passe à `Workbook.Settings.Password`, puis enregistrez le classeur. Aspose.Cells écrit le fichier sous forme chiffrée. Pour ouvrir un classeur chiffré en vue de le déchiffrer, instanciez un objet `LoadOptions`, définissez `LoadOptions.Password` avec le même mot de passe que celui utilisé lors du chiffrement, puis transmettez-le au constructeur `Workbook`. Aspose.Cells applique le mot de passe fourni de manière transparente afin que le reste de votre code puisse interagir avec le contenu déchiffré comme s'il s'agissait d'un classeur classique.

```csharp
using System;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cell cell = sheet.Cells["A1"];
cell.PutValue("Confidential Data");
workbook.Settings.Password = "OpenPassword123";
workbook.Save("encrypted.xlsx");
LoadOptions loadOptions = new LoadOptions();
loadOptions.Password = "OpenPassword123";
Workbook decryptedWorkbook = new Workbook("encrypted.xlsx", loadOptions);
Console.WriteLine("Decrypted cell A1 value: " + decryptedWorkbook.Worksheets[0].Cells["A1"].StringValue);
```

## Protection en lecture seule (mot de passe de modification)
Excel prend en charge deux niveaux de mot de passe distincts. Le premier est un mot de passe d'ouverture, qui chiffre le fichier lui-même et qui est abordé dans la section précédente. Le second est un mot de passe de modification, qui n'empêche pas les utilisateurs d'ouvrir le classeur ; Excel recommande plutôt d'ouvrir le fichier en mode lecture seule sauf si le mot de passe de modification est fourni. Configurez ce comportement dans Aspose.Cells via `Workbook.Settings.WriteProtection`. Définissez sa propriété `Password` avec le mot de passe de modification et sa propriété `Author` pour identifier l'auteur de la protection. Utilisez la méthode `WriteProtection.ValidatePassword(string)` pour vérifier si un mot de passe de modification fourni est correct, en retournant `true` en cas de correspondance et `false` dans le cas contraire.

```csharp
using System;
using Aspose.Cells;
// Créer un nouveau classeur à partir de zéro
Workbook workbook = new Workbook();
// Écrire une valeur d'exemple dans la cellule A1 de la première feuille de calcul
workbook.Worksheets[0].Cells["A1"].PutValue("Sample Data");
// Configurer la protection en écriture : définir le mot de passe pour modifier et l'auteur
workbook.Settings.WriteProtection.Password = "ModifyPwd";
workbook.Settings.WriteProtection.Author = "AuthorName";
// Enregistrer le classeur pour que la protection en écriture soit persistée
workbook.Save("WriteProtectedWorkbook.xlsx");
// Valider le mot de passe pour modifier en utilisant le bon mot de passe
bool isCorrectValid = workbook.Settings.WriteProtection.ValidatePassword("ModifyPwd");
Console.WriteLine("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
// Valider le mot de passe pour modifier en utilisant un mot de passe incorrect pour démontrer l'autre branche
bool isWrongValid = workbook.Settings.WriteProtection.ValidatePassword("WrongPwd");
Console.WriteLine("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## Protéger et déprotéger la structure du classeur
La protection de la structure du classeur empêche d'autres utilisateurs d'afficher les feuilles de calcul masquées, d'ajouter de nouvelles feuilles de calcul, de déplacer des feuilles de calcul, de supprimer des feuilles de calcul, de masquer des feuilles de calcul ou de renommer des feuilles de calcul. L'état protégé s'applique à la structure des feuilles et non au contenu des cellules à l'intérieur de celles-ci. Pour appliquer la protection de la structure, appelez `workbook.Protect(ProtectionType.Structure, "password")`. Pour supprimer la protection, appelez `workbook.Unprotect("password")` et fournissez le mot de passe correct. La valeur d'énumération `ProtectionType.Structure` est utilisée ici et se distingue des autres types de protection tels que `ProtectionType.Windows`.

```csharp
using System;
using Aspose.Cells;
// Créer un nouveau classeur
Workbook workbook = new Workbook();
// Ajouter une deuxième feuille de calcul
workbook.Worksheets.Add();
// Écrire une valeur d'exemple dans la cellule A1 de la première feuille de calcul
workbook.Worksheets[0].Cells[0, 0].PutValue("Sample Data");
// Protéger la structure du classeur
workbook.Protect(ProtectionType.Structure, "StructPwd");
// Enregistrer le classeur sous structure_protected.xlsx
string filePath = "structure_protected.xlsx";
workbook.Save(filePath);
// Recharger le fichier dans une nouvelle instance de Workbook
Workbook loadedWorkbook = new Workbook(filePath);
// Supprimer la protection de la structure
loadedWorkbook.Unprotect("StructPwd");
// Afficher le message de confirmation
Console.WriteLine("Structure protection has been successfully removed from the workbook.");
```

## Protéger et déprotéger les feuilles de calcul
La protection de la feuille de calcul verrouille les cellules d'une feuille de calcul contre toute modification accidentelle ou délibérée. Les utilisateurs ne peuvent pas modifier les cellules verrouillées sans fournir le mot de passe. Il s'agit de la protection classique utilisée pour protéger les formules, les en-têtes ou les zones de saisie de données désignées dans les feuilles de calcul partagées. Pour protéger une feuille de calcul, appelez `worksheet.Protect(ProtectionType.All, "password")`. L'utilisation de `ProtectionType.All` active toutes les options de protection disponibles, telles que la sélection des cellules verrouillées, la mise en forme des cellules, l'insertion de lignes et de colonnes et la suppression de lignes et de colonnes. Pour supprimer la protection, appelez `worksheet.Unprotect("password")` avec le mot de passe correct. Un contrôle plus fin est disponible en combinant d'autres types de protection tels que `Contents`, `Objects` et `Scenarios` à l'aide de l'opérateur OR bit à bit.

```csharp
using System;
using Aspose.Cells;
var workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
sheet.Cells["A1"].PutValue("Sample Data");
sheet.Protect(ProtectionType.All, "SheetPwd");
workbook.Save("sheet_protected.xlsx");
var workbookReloaded = new Workbook("sheet_protected.xlsx");
Worksheet sheetReloaded = workbookReloaded.Worksheets[0];
sheetReloaded.Unprotect("SheetPwd");
Console.WriteLine("Worksheet protection removed successfully.");
```

## Ajouter et valider des signatures numériques
Une signature numérique garantit aux destinataires que le contenu du classeur est authentique et qu'il n'a pas été modifié depuis sa signature. Aspose.Cells prend en charge les signatures numériques via l'espace de noms `Aspose.Cells.DigitalSignatures`. Le flux de travail classique charge un fichier de certificat `.pfx` via `System.Security.Cryptography.X509Certificates.X509Certificate2`, l'enveloppe dans un `Aspose.Cells.DigitalSignatures.DigitalSignature`, ajoute la signature à un `DigitalSignatureCollection`, puis applique la collection au classeur via `Workbook.AddDigitalSignature(DigitalSignatureCollection)`. La propriété `DigitalSignature.Comments` peut enregistrer le contexte de signature, tel que l'heure et l'objet de la signature. Toute modification apportée au classeur après la signature invalide cette dernière ; une étape de validation côté destinataire permet donc de détecter toute falsification.

```csharp
using System;
using System.IO;
using System.Security.Cryptography.X509Certificates;
using Aspose.Cells;
using Aspose.Cells.DigitalSignatures;
X509Certificate2 certificate = new X509Certificate2("signature.pfx", "pfx-password");
DigitalSignature signature = new DigitalSignature(certificate, "Signed by Aspose.Cells", DateTime.Now);
DigitalSignatureCollection signatures = new DigitalSignatureCollection();
signatures.Add(signature);
Workbook workbook = new Workbook();
workbook.Worksheets[0].Cells["A1"].PutValue("Sample Value");
workbook.AddDigitalSignature(signatures);
workbook.Save("signed_workbook.xlsx");
Console.WriteLine("The workbook has been digitally signed.");
```

## Articles connexes
- [Chiffrer et déchiffrer des fichiers Excel](/cells/fr/net/encrypt-and-decrypt-excel-files/)
- [Protéger et déprotéger la structure du classeur](/cells/fr/net/protect-and-unprotect-workbook-structure/)
- [Protéger et déprotéger la feuille de calcul](/cells/fr/net/protect-and-unprotect-worksheets/)
- [Protéger par mot de passe ou déprotéger le classeur partagé](/cells/fr/net/password-protect-or-unprotect-the-shared-workbook/)
- [Attribuer et valider des signatures numériques](/cells/fr/net/assign-and-validate-digital-signatures/)
- [Vérifier le mot de passe de modification à l'aide d'Aspose.Cells](/cells/fr/net/check-password-to-modify-using-aspose-cells/)
- [Détecter le format de fichier des fichiers chiffrés Office Open XML - OOXML](/cells/fr/net/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Chiffrement des fichiers Excel](/cells/fr/net/encrypting-excel-files/)
- [Comment détecter un format de fichier et vérifier si le fichier est chiffré](/cells/fr/net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="csharp" >}}