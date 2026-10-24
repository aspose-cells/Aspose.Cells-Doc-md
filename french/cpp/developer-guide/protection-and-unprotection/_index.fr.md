---
title: Protéger et déprotéger avec C++
linktitle: Chiffrement et protection
description: Cette section explique comment chiffrer et déchiffrer des fichiers Excel et protéger les données Excel, couvrant le chiffrement de fichiers, la protection en lecture seule, la protection de la structure du classeur, la protection des feuilles de calcul et les signatures numériques à l'aide de code C++
keywords: Aspose.Cells, Aspose.Cells for C++, chiffrer, déchiffrer, mot de passe, protéger, déprotéger, protection du classeur, protection de la feuille de calcul, lecture seule, signature numérique, C++
type: docs
weight: 68
url: /fr/cpp/protect-and-unprotect/
alias: [/cpp/security-features/]
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Les classeurs Excel contiennent souvent des informations financières, commerciales ou personnelles sensibles qui doivent être protégées contre tout accès non autorisé. Aspose.Cells for C++ offre un ensemble complet de fonctionnalités de protection qui reflète les capacités de Microsoft Excel, vous permettant de sécuriser vos données au niveau du fichier, du classeur et de la feuille de calcul.

{{% alert color="primary" %}}
Aspose.Cells for C++ propose une large gamme de fonctionnalités de protection, du niveau du fichier au niveau des données, similaires à celles de MS Excel. Ces capacités incluent le chiffrement des fichiers avec un mot de passe, l'application d'un accès en lecture seule via un mot de passe de modification, la protection de la structure du classeur, la protection des feuilles de calcul et la signature numérique des classeurs.
{{% /alert %}}

## Chiffrer et déchiffrer des fichiers Excel
Un mot de passe défini sur un fichier Excel empêche les utilisateurs non autorisés d'ouvrir ou de consulter le contenu du classeur. Pour chiffrer un classeur, attribuez une chaîne de mot de passe à `workbook.GetSettings().SetPassword()`, puis enregistrez le classeur. Aspose.Cells écrit le fichier sous forme chiffrée. Pour ouvrir un classeur chiffré en vue de le déchiffrer, instanciez un objet `LoadOptions`, définissez `LoadOptions.SetPassword()` sur le même mot de passe que celui utilisé lors du chiffrement, puis transmettez-le au constructeur `Workbook`. Aspose.Cells applique le mot de passe fourni de manière transparente, de sorte que le reste de votre code puisse interagir avec le contenu déchiffré comme s'il s'agissait d'un classeur ordinaire.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cell cell = sheet.GetCells().Get(u"A1");
    cell.PutValue(u"Confidential Data");
    workbook.GetSettings().SetPassword(U16String("OpenPassword123"));
    workbook.Save(u"encrypted.xlsx");
    LoadOptions loadOptions;
    loadOptions.SetPassword(U16String("OpenPassword123"));
    Workbook decryptedWorkbook(u"encrypted.xlsx", loadOptions);
    U16String cellValue = decryptedWorkbook.GetWorksheets().Get(0).GetCells().Get(u"A1").GetStringValue();
    std::cout << "Decrypted cell A1 value: " << cellValue.ToUtf8() << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Protection en lecture seule (mot de passe de modification)
Excel prend en charge deux couches distinctes de mots de passe. La première est un mot de passe d'ouverture, qui chiffre le fichier lui-même et qui est traité dans la section précédente. La seconde est un mot de passe de modification, qui n'empêche pas les utilisateurs d'ouvrir le classeur ; au lieu de cela, Excel recommande d'ouvrir le fichier en mode lecture seule, sauf si le mot de passe de modification est fourni. Configurez ce comportement dans Aspose.Cells via `workbook.GetSettings().GetWriteProtection()`. Définissez sa propriété `Password` sur le mot de passe de modification et sa propriété `Author` pour identifier l'auteur de la protection. Utilisez la méthode `WriteProtection.ValidatePassword()` pour vérifier si un mot de passe de modification fourni est correct, en renvoyant `true` en cas de correspondance et `false` dans le cas contraire.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    Cell a1 = cells.Get(u"A1");
    a1.PutValue(u"Sample Data");
    workbook.GetSettings().GetWriteProtection().SetPassword(u"ModifyPwd");
    workbook.GetSettings().GetWriteProtection().SetAuthor(u"AuthorName");
    workbook.Save(u"WriteProtectedWorkbook.xlsx");
    bool isCorrectValid = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"ModifyPwd");
    std::cout << "ValidatePassword(\"ModifyPwd\") returned: " << (isCorrectValid ? "True" : "False") << std::endl;
    bool isWrongValid = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"WrongPwd");
    std::cout << "ValidatePassword(\"WrongPwd\") returned: " << (isWrongValid ? "True" : "False") << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Protéger et déprotéger la structure du classeur
La protection de la structure du classeur empêche les autres utilisateurs de consulter les feuilles de calcul masquées, d'ajouter de nouvelles feuilles de calcul, de déplacer des feuilles de calcul, de supprimer des feuilles de calcul, de masquer des feuilles de calcul ou de renommer des feuilles de calcul. L'état protégé s'applique à la structure des feuilles plutôt qu'au contenu des cellules à l'intérieur de chaque feuille. Pour appliquer la protection de la structure, appelez `workbook.Protect(ProtectionType::Structure, "password")`. Pour supprimer la protection, appelez `workbook.Unprotect("password")` et fournissez le mot de passe correct. La valeur d'énumération `ProtectionType::Structure` est utilisée ici et est distincte des autres types de protection tels que `ProtectionType::Windows`.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Créer un nouveau classeur
    Workbook workbook;
    // Ajouter une deuxième feuille de calcul
    workbook.GetWorksheets().Add();
    // Écrire une valeur d'exemple dans la cellule A1 de la première feuille de calcul
    workbook.GetWorksheets().Get(0).GetCells().Get(0, 0).PutValue(u"Sample Data");
    // Protéger la structure du classeur
    workbook.Protect(ProtectionType::Structure, u"StructPwd");
    // Enregistrer le classeur sous structure_protected.xlsx
    U16String filePath = u"structure_protected.xlsx";
    workbook.Save(filePath);
    // Recharger le fichier dans une nouvelle instance de classeur
    Workbook loadedWorkbook(filePath);
    // Supprimer la protection de la structure
    loadedWorkbook.Unprotect(u"StructPwd");
    // Afficher le message de confirmation
    std::cout << "Structure protection has been successfully removed from the workbook." << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Protéger et déprotéger les feuilles de calcul
La protection d'une feuille de calcul verrouille les cellules d'une feuille de calcul contre les modifications accidentelles ou délibérées. Les utilisateurs ne peuvent pas modifier les cellules verrouillées sans fournir le mot de passe. Il s'agit de la protection typique utilisée pour protéger les formules, les en-têtes ou les zones de saisie de données désignées dans les feuilles de calcul partagées. Pour protéger une feuille de calcul, appelez `worksheet.Protect(ProtectionType::All, "password")`. L'utilisation de `ProtectionType::All` active toutes les options de protection disponibles, telles que la sélection des cellules verrouillées, la mise en forme des cellules, l'insertion de lignes et de colonnes, ainsi que la suppression de lignes et de colonnes. Pour supprimer la protection, appelez `worksheet.Unprotect("password")` avec le mot de passe correct. Un contrôle plus fin est disponible en combinant d'autres types de protection tels que `Contents`, `Objects` et `Scenarios` à l'aide de l'opérateur OR au niveau du bit.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Sample Data");
    sheet.Protect(ProtectionType::All, u"SheetPwd");
    workbook.Save(u"sheet_protected.xlsx");
    Workbook workbookReloaded(u"sheet_protected.xlsx");
    Worksheet sheetReloaded = workbookReloaded.GetWorksheets().Get(0);
    sheetReloaded.Unprotect(u"SheetPwd");
    std::cout << "Worksheet protection removed successfully.\n";
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Ajouter et valider des signatures numériques
Une signature numérique garantit aux destinataires que le contenu du classeur est authentique et n'a pas été modifié depuis sa signature. Aspose.Cells offre une prise en charge des signatures numériques via l'espace de noms `Aspose::Cells::DigitalSignatures`. Le flux de travail typique consiste à charger un fichier de certificat `.pfx`, à l'envelopper dans un objet `Aspose::Cells::DigitalSignatures::DigitalSignature`, à ajouter la signature à un `DigitalSignatureCollection`, puis à appliquer la collection au classeur via `workbook.AddDigitalSignature(DigitalSignatureCollection)`. La propriété `DigitalSignature.GetComments()` peut enregistrer le contexte de la signature, tel que l'heure et l'objectif de la signature. Toute modification apportée au classeur après la signature invalide celle-ci ; une étape de validation côté destinataire permet donc de détecter toute altération.

```cpp
#include "Aspose.Cells.h"
#include <chrono>
#include <ctime>
using namespace Aspose::Cells;
using namespace Aspose::Cells::DigitalSignatures;
int main() {
    Aspose::Cells::Startup();
    std::time_t t = std::time(nullptr);
    std::tm tm{};
    localtime_s(&tm, &t);
    Date currentDate{0};
    currentDate.year = tm.tm_year + 1900;
    currentDate.month = tm.tm_mon + 1;
    currentDate.day = tm.tm_mday;
    currentDate.hour = tm.tm_hour;
    currentDate.minute = tm.tm_min;
    currentDate.second = tm.tm_sec;
    DigitalSignature signature(u"signature.pfx", u"pfx-password", u"Signed by Aspose.Cells", currentDate);
    DigitalSignatureCollection signatures;
    signatures.Add(signature);
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Sample Value");
    workbook.AddDigitalSignature(signatures);
    workbook.Save(u"signed_workbook.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Articles connexes
- [Chiffrer et déchiffrer des fichiers Excel](/cells/fr/cpp/encrypt-and-decrypt-excel-files/)
- [Protéger et déprotéger la structure du classeur](/cells/fr/cpp/protect-and-unprotect-workbook-structure/)
- [Protéger et déprotéger une feuille de calcul](/cells/fr/cpp/protect-and-unprotect-worksheets/)
- [Protéger ou déprotéger par mot de passe le classeur partagé](/cells/fr/cpp/password-protect-or-unprotect-the-shared-workbook/)
- [Vérifier le mot de passe de modification à l'aide d'Aspose.Cells](/cells/fr/cpp/check-password-to-modify-using-aspose-cells/)
- [Détecter le format de fichier des fichiers Office Open XML - OOXML chiffrés](/cells/fr/cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Chiffrement des fichiers Excel](/cells/fr/cpp/encrypting-excel-files/)
- [Comment détecter un format de fichier et vérifier si le fichier est chiffré](/cells/fr/cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="cpp" >}}