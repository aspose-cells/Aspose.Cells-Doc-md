---
title: Protéger et déprotéger
linktitle: Chiffrement et protection
description: Cette section explique comment chiffrer et déchiffrer des fichiers Excel et protéger les données Excel, couvrant le chiffrement des fichiers, la protection en lecture seule, la protection de la structure du classeur, la protection des feuilles de calcul et les signatures numériques à l'aide de code Python
keywords: Aspose.Cells, Python via .NET, chiffrer, déchiffrer, mot de passe, protéger, déprotéger, protection du classeur, protection de la feuille de calcul, lecture seule, signature numérique, Python
type: docs
weight: 68
url: /fr/python-net/protect-and-unprotect/
alias: [/python-net/security-features/]
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Les classeurs Excel stockent souvent des informations financières, commerciales ou personnelles sensibles qui doivent être protégées contre tout accès non autorisé. Aspose.Cells for Python via .NET fournit un ensemble complet de fonctionnalités de protection qui reflètent les capacités de Microsoft Excel, vous permettant de sécuriser vos données au niveau du fichier, du classeur et de la feuille de calcul.

{{% alert color="primary" %}}
Aspose.Cells for Python via .NET offre une large gamme de fonctionnalités de protection, du niveau du fichier au niveau des données, similaires à MS Excel. Ces fonctionnalités incluent le chiffrement des fichiers avec un mot de passe, l'application d'un accès en lecture seule via un mot de passe de modification, la protection de la structure du classeur, la protection des feuilles de calcul et la signature numérique des classeurs.
{{% /alert %}}

## Chiffrer et déchiffrer les fichiers Excel
Un mot de passe défini sur un fichier Excel empêche les utilisateurs non autorisés d'ouvrir ou de consulter le contenu du classeur. Pour chiffrer un classeur, attribuez une chaîne de mot de passe à `workbook.settings.password`, puis enregistrez le classeur. Aspose.Cells écrit le fichier sous forme chiffrée. Pour ouvrir un classeur chiffré en vue de le déchiffrer, instanciez un objet `LoadOptions`, définissez `load_options.password` avec le même mot de passe que celui utilisé lors du chiffrement, puis transmettez-le au constructeur `Workbook`. Aspose.Cells applique le mot de passe fourni de manière transparente, de sorte que le reste de votre code puisse interagir avec le contenu déchiffré comme s'il s'agissait d'un classeur classique.

```python
import aspose.cells as ac
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cell = sheet.cells.get("A1")
cell.put_value("Confidential Data")
workbook.settings.password = "OpenPassword123"
workbook.save("encrypted.xlsx")
load_options = ac.LoadOptions()
load_options.password = "OpenPassword123"
decrypted_workbook = ac.Workbook("encrypted.xlsx", load_options)
print("Decrypted cell A1 value: " + decrypted_workbook.worksheets[0].cells.get("A1").string_value)
```

## Protection en lecture seule (mot de passe de modification)
Excel prend en charge deux couches distinctes de mots de passe. La première est un mot de passe pour ouvrir le fichier, qui chiffre le fichier lui-même et est traitée dans la section précédente. La seconde est un mot de passe de modification, qui n'empêche pas les utilisateurs d'ouvrir le classeur ; Excel recommande plutôt d'ouvrir le fichier en mode lecture seule, sauf si le mot de passe de modification est fourni. Configurez ce comportement dans Aspose.Cells via `workbook.settings.write_protection`. Définissez sa propriété `password` avec le mot de passe de modification et sa propriété `author` pour identifier l'auteur de la protection. Utilisez la méthode `write_protection.validate_password(string)` pour vérifier si un mot de passe de modification fourni est correct, en renvoyant `true` en cas de correspondance et `false` dans le cas contraire.

```python
import aspose.cells as ac
# Créer un nouveau classeur à partir de zéro
workbook = ac.Workbook()
# Écrire une valeur d'exemple dans la cellule A1 de la première feuille de calcul
workbook.worksheets[0].cells.get("A1").put_value("Sample Data")
# Configurer la protection en écriture : définir le mot de passe de modification et l'auteur
workbook.settings.write_protection.password = "ModifyPwd"
workbook.settings.write_protection.author = "AuthorName"
# Enregistrer le classeur pour que la protection en écriture soit persistante
workbook.save("WriteProtectedWorkbook.xlsx")
# Valider le mot de passe de modification en utilisant le mot de passe correct
is_correct_valid = workbook.settings.write_protection.validate_password("ModifyPwd")
print("ValidatePassword(\"ModifyPwd\") returned: " + str(is_correct_valid))
# Valider le mot de passe de modification en utilisant un mot de passe incorrect pour démontrer l'autre branche
is_wrong_valid = workbook.settings.write_protection.validate_password("WrongPwd")
print("ValidatePassword(\"WrongPwd\") returned: " + str(is_wrong_valid))
```

## Protéger et déprotéger la structure du classeur
La protection de la structure du classeur empêche les autres utilisateurs d'afficher les feuilles de calcul masquées, d'ajouter de nouvelles feuilles de calcul, de déplacer des feuilles de calcul, de supprimer des feuilles de calcul, de masquer des feuilles de calcul ou de renommer des feuilles de calcul. L'état protégé s'applique à la structure des feuilles plutôt qu'au contenu des cellules à l'intérieur d'une feuille. Pour appliquer la protection de la structure, appelez `workbook.protect(ProtectionType.STRUCTURE, "password")`. Pour supprimer la protection, appelez `workbook.unprotect("password")` et fournissez le mot de passe correct. La valeur d'énumération `ProtectionType.STRUCTURE` est utilisée ici et se distingue des autres types de protection tels que `ProtectionType.WINDOWS`.

```python
import aspose.cells as ac
# Créer un nouveau classeur
workbook = ac.Workbook()
# Ajouter une deuxième feuille de calcul
workbook.worksheets.add()
# Écrire une valeur d'exemple dans la cellule A1 de la première feuille de calcul
workbook.worksheets[0].cells.get(0, 0).put_value("Sample Data")
# Protéger la structure du classeur
workbook.protect(ac.ProtectionType.STRUCTURE, "StructPwd")
# Enregistrer le classeur sous structure_protected.xlsx
file_path = "structure_protected.xlsx"
workbook.save(file_path)
# Recharger le fichier dans une nouvelle instance de classeur
loaded_workbook = ac.Workbook(file_path)
# Supprimer la protection de la structure
loaded_workbook.unprotect("StructPwd")
# Afficher le message de confirmation
print("Structure protection has been successfully removed from the workbook.")
```

## Protéger et déprotéger les feuilles de calcul
La protection de la feuille de calcul verrouille les cellules d'une feuille de calcul contre les modifications accidentelles ou délibérées. Les utilisateurs ne peuvent pas modifier les cellules verrouillées sans fournir le mot de passe. Il s'agit de la protection classique utilisée pour protéger les formules, les en-têtes ou les zones de saisie de données désignées dans les feuilles de calcul partagées. Pour protéger une feuille de calcul, appelez `worksheet.protect(ProtectionType.ALL, "password")`. L'utilisation de `ProtectionType.ALL` active toutes les options de protection disponibles, telles que la sélection de cellules verrouillées, la mise en forme des cellules, l'insertion de lignes et de colonnes, ainsi que la suppression de lignes et de colonnes. Pour supprimer la protection, appelez `worksheet.unprotect("password")` avec le mot de passe correct. Un contrôle plus fin est disponible en combinant d'autres types de protection tels que `Contents`, `Objects` et `Scenarios` à l'aide de l'opérateur OR binaire.

```python
import aspose.cells as ac
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
sheet.cells.get("A1").put_value("Sample Data")
sheet.protect(ac.ProtectionType.ALL, "SheetPwd")
workbook.save("sheet_protected.xlsx")
workbook_reloaded = ac.Workbook("sheet_protected.xlsx")
sheet_reloaded = workbook_reloaded.worksheets[0]
sheet_reloaded.unprotect("SheetPwd")
print("Worksheet protection removed successfully.")
```

## Ajouter et valider les signatures numériques
Une signature numérique garantit aux destinataires que le contenu du classeur est authentique et n'a pas été modifié depuis sa signature. Aspose.Cells prend en charge les signatures numériques via l'espace de noms `aspose.cells.digital_signatures`. Le flux de travail classique charge un fichier de certificat `.pfx` via `System.Security.Cryptography.X509Certificates.X509Certificate2`, l'enveloppe dans un `aspose.cells.digital_signatures.DigitalSignature`, ajoute la signature à une `DigitalSignatureCollection` et applique la collection au classeur via `workbook.add_digital_signature(DigitalSignatureCollection)`. La propriété `digital_signature.comments` peut enregistrer le contexte de la signature, tel que l'heure et l'objet de la signature. Toute modification apportée au classeur après la signature invalide celle-ci, de sorte qu'une étape de validation côté destinataire peut détecter toute altération.

```python
from datetime import datetime
import aspose.cells as ac
from aspose.cells.digitalsignatures import DigitalSignature, DigitalSignatureCollection
with open("signature.pfx", "rb") as certificate_file:
    certificate = certificate_file.read()
signature = DigitalSignature(certificate, "Signed by Aspose.Cells", datetime.now())
signatures = DigitalSignatureCollection()
signatures.add(signature)
workbook = ac.Workbook()
workbook.worksheets[0].cells.get("A1").put_value("Sample Value")
workbook.add_digital_signature(signatures)
workbook.save("signed_workbook.xlsx")
print("The workbook has been digitally signed.")
```

## Articles connexes
- [Chiffrer et déchiffrer les fichiers Excel](/cells/fr/python-net/encrypt-and-decrypt-excel-files/)
- [Protéger et déprotéger la structure du classeur](/cells/fr/python-net/protect-and-unprotect-workbook-structure/)
- [Protéger et déprotéger une feuille de calcul](/cells/fr/python-net/protect-and-unprotect-worksheets/)
- [Protéger ou déprotéger par mot de passe le classeur partagé](/cells/fr/python-net/password-protect-or-unprotect-the-shared-workbook/)
- [Attribuer et valider les signatures numériques](/cells/fr/python-net/assign-and-validate-digital-signatures/)
- [Vérifier le mot de passe de modification à l'aide d'Aspose.Cells](/cells/fr/python-net/check-password-to-modify-using-aspose-cells/)
- [Détecter le format de fichier des fichiers Office Open XML - OOXML chiffrés](/cells/fr/python-net/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Chiffrement des fichiers Excel](/cells/fr/python-net/encrypting-excel-files/)
- [Comment détecter un format de fichier et vérifier si le fichier est chiffré](/cells/fr/python-net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="python-net" >}}