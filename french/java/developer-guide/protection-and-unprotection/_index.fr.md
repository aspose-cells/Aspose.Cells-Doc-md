---
title: Chiffrer, déchiffrer, protéger et désactiver la protection des fichiers Excel
linktitle: Chiffrement et protection
description: Cette section explique comment chiffrer et déchiffrer des fichiers Excel et protéger les données Excel, en abordant le chiffrement des fichiers, la protection en lecture seule, la protection de la structure du classeur, la protection des feuilles de calcul et les signatures numériques à l'aide de code Java
keywords: Aspose.Cells, Java, chiffrer, déchiffrer, mot de passe, protéger, déprotéger, protection du classeur, protection de la feuille de calcul, lecture seule, signature numérique
type: docs
weight: 68
url: /fr/java/protect-and-unprotect/
alias: [/java/security-features/]
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Les classeurs Excel stockent souvent des informations financières, professionnelles ou personnelles sensibles qui doivent être protégées contre tout accès non autorisé. Aspose.Cells for Java fournit un ensemble complet de fonctionnalités de protection qui reflètent les capacités de Microsoft Excel, ce qui vous permet de sécuriser vos données au niveau du fichier, du classeur et de la feuille de calcul.

{{% alert color="primary" %}}
Aspose.Cells for Java offre un large éventail de fonctionnalités de protection, du niveau du fichier jusqu'au niveau des données, similaires à celles de MS Excel. Ces fonctionnalités comprennent le chiffrement des fichiers avec un mot de passe, l'imposition d'un accès en lecture seule à l'aide d'un mot de passe de modification, la protection de la structure du classeur, la protection des feuilles de calcul et la signature numérique des classeurs.
{{% /alert %}}

## Chiffrer et déchiffrer des fichiers Excel
Un mot de passe associé à un fichier Excel empêche les utilisateurs non autorisés d'ouvrir ou d'afficher le contenu du classeur. Pour chiffrer un classeur, attribuez une chaîne de caractères à `Workbook.Settings.Password` (accessible via `workbook.getSettings().setPassword(...)`), puis enregistrez le classeur. Aspose.Cells écrit le fichier sous forme chiffrée. Pour ouvrir un classeur chiffré et le déchiffrer, instanciez un objet `LoadOptions`, définissez `LoadOptions.Password` (via `loadOptions.setPassword(...)`) avec le même mot de passe que celui utilisé lors du chiffrement, puis transmettez cet objet au constructeur `Workbook`. Aspose.Cells applique de manière transparente le mot de passe fourni afin que le reste de votre code puisse interagir avec le contenu déchiffré comme si le fichier était un classeur ordinaire.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cell cell = sheet.getCells().get("A1");
cell.putValue("Confidential Data");
workbook.getSettings().setPassword("OpenPassword123");
workbook.save("encrypted.xlsx");
LoadOptions loadOptions = new LoadOptions();
loadOptions.setPassword("OpenPassword123");
Workbook decryptedWorkbook = new Workbook("encrypted.xlsx", loadOptions);
System.out.println("Decrypted cell A1 value: " + decryptedWorkbook.getWorksheets().get(0).getCells().get("A1").getStringValue());
```

## Protection en lecture seule (mot de passe de modification)
Excel prend en charge deux couches de mots de passe distinctes. La première est un mot de passe d'ouverture, qui chiffre le fichier lui-même et a été décrit dans la section précédente. La seconde est un mot de passe de modification, qui n'empêche pas les utilisateurs d'ouvrir le classeur ; Excel leur recommande plutôt d'ouvrir le fichier en lecture seule, sauf si le mot de passe de modification est fourni. Configurez ce comportement dans Aspose.Cells via `Workbook.Settings.WriteProtection` (accessible via `workbook.getSettings().getWriteProtection()`). Définissez sa propriété `Password` (via `writeProtection.setPassword(...)`) avec le mot de passe de modification et sa propriété `Author` (via `writeProtection.setAuthor(...)`) afin d'indiquer qui a appliqué la protection. Utilisez la méthode `WriteProtection.validatePassword(String)` pour vérifier si un mot de passe de modification fourni est correct ; elle retourne `true` en cas de correspondance et `false` dans le cas contraire.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data");
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd");
workbook.getSettings().getWriteProtection().setAuthor("AuthorName");
workbook.save("WriteProtectedWorkbook.xlsx");
boolean isCorrectValid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd");
System.out.println("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
boolean isWrongValid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd");
System.out.println("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## Protéger et déprotéger la structure du classeur
La protection de la structure du classeur empêche les autres utilisateurs d'afficher les feuilles de calcul masquées, d'ajouter de nouvelles feuilles de calcul, de déplacer des feuilles de calcul, de supprimer des feuilles de calcul, de masquer des feuilles de calcul ou de renommer des feuilles de calcul. L'état protégé s'applique à la structure des feuilles de calcul plutôt qu'au contenu des cellules de chaque feuille de calcul. Pour appliquer la protection de la structure, appelez `workbook.protect(ProtectionType.STRUCTURE, "password")`. Pour supprimer la protection, appelez `workbook.unprotect("password")` et fournissez le mot de passe correct. La valeur d'énumération `ProtectionType.STRUCTURE` est utilisée ici et se distingue d'autres types de protection tels que `ProtectionType.WINDOWS`.

```java
import com.aspose.cells.*;
// Créer un nouveau classeur
Workbook workbook = new Workbook();
// Ajouter une deuxième feuille de calcul
workbook.getWorksheets().add();
// Écrire une valeur d'exemple dans la cellule A1 de la première feuille de calcul
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data");
// Protéger la structure du classeur
workbook.protect(ProtectionType.STRUCTURE, "StructPwd");
// Enregistrer le classeur sous structure_protected.xlsx
String filePath = "structure_protected.xlsx";
workbook.save(filePath);
// Recharger le fichier dans une nouvelle instance de classeur
Workbook loadedWorkbook = new Workbook(filePath);
// Supprimer la protection de la structure
loadedWorkbook.unprotect("StructPwd");
// Afficher le message de confirmation
System.out.println("Structure protection has been successfully removed from the workbook.");
```

## Protéger et déprotéger les feuilles de calcul
La protection d'une feuille de calcul verrouille les cellules de cette feuille afin d'empêcher toute modification accidentelle ou délibérée. Les utilisateurs ne peuvent pas modifier les cellules verrouillées sans fournir le mot de passe. Il s'agit du type de protection généralement utilisé pour protéger les formules, les en-têtes ou les zones de saisie de données désignées dans les feuilles de calcul partagées. Pour protéger une feuille de calcul, appelez `worksheet.protect(ProtectionType.ALL, "password")`. L'utilisation de `ProtectionType.ALL` active toutes les options de protection disponibles, telles que la sélection des cellules verrouillées, la mise en forme des cellules, l'insertion de lignes et de colonnes et la suppression de lignes et de colonnes. Pour supprimer la protection, appelez `worksheet.unprotect("password")` avec le mot de passe correct. Un contrôle plus précis est disponible en combinant d'autres types de protection tels que `CONTENTS`, `OBJECTS` et `SCENARIOS` à l'aide de l'opérateur OU au niveau des bits.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
sheet.getCells().get("A1").putValue("Sample Data");
sheet.protect(ProtectionType.ALL, "SheetPwd", "SheetPwd");
workbook.save("sheet_protected.xlsx");
Workbook workbookReloaded = new Workbook("sheet_protected.xlsx");
Worksheet sheetReloaded = workbookReloaded.getWorksheets().get(0);
sheetReloaded.unprotect("SheetPwd");
System.out.println("Worksheet protection removed successfully.");
```

## Ajouter et valider des signatures numériques
Une signature numérique garantit aux destinataires que le contenu du classeur est authentique et n'a pas été modifié depuis qu'elle a été appliquée. Aspose.Cells prend en charge les signatures numériques via le package `com.aspose.cells.DigitalSignatures`. Le flux de travail typique consiste à charger un fichier de certificat `.pfx` à l'aide des API de sécurité Java (telles que `java.security.KeyStore` et `java.security.cert.X509Certificate`), à l'encapsuler dans un `com.aspose.cells.DigitalSignatures.DigitalSignature`, à ajouter la signature à une `DigitalSignatureCollection`, puis à appliquer la collection au classeur via `workbook.addDigitalSignature(DigitalSignatureCollection)`. La propriété `DigitalSignature.getComments()` permet de consigner un contexte de signature, tel que l'heure de la signature et sa finalité. Toute modification apportée au classeur après la signature invalide cette dernière ; une étape de validation du côté du destinataire peut donc détecter toute falsification.

```java
import com.aspose.cells.*;
import java.io.FileInputStream;
import java.security.KeyStore;
KeyStore pfxKeyStore = KeyStore.getInstance("PKCS12");
pfxKeyStore.load(new FileInputStream("signature.pfx"), "pfx-password".toCharArray());
DigitalSignature signature = new DigitalSignature(pfxKeyStore, "pfx-password", "Signed by Aspose.Cells", new DateTime());
DigitalSignatureCollection signatures = new DigitalSignatureCollection();
signatures.add(signature);
Workbook workbook = new Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value");
workbook.addDigitalSignature(signatures);
workbook.save("signed_workbook.xlsx");
System.out.println("The workbook has been digitally signed.");
```

## Articles connexes
- [Chiffrer et déchiffrer des fichiers Excel](/cells/fr/java/encrypt-and-decrypt-excel-files/)
- [Protéger et déprotéger la structure du classeur](/cells/fr/java/protect-and-unprotect-workbook-structure/)
- [Protéger et déprotéger une feuille de calcul](/cells/fr/java/protect-and-unprotect-worksheet/)
- [Protéger ou déprotéger par mot de passe le classeur partagé](/cells/fr/java/password-protect-or-unprotect-the-shared-workbook/)
- [Attribuer et valider des signatures numériques](/cells/fr/java/assign-and-validate-digital-signatures/)
- [Détecter le format des fichiers Office Open XML (OOXML) chiffrés](/cells/fr/java/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Comment détecter le format d'un fichier et vérifier s'il est chiffré](/cells/fr/java/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="java" >}}