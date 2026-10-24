---
title: Protéger et déprotéger
linktitle: Protection
description: Cette section explique comment chiffrer et déchiffrer des fichiers Excel et protéger les données Excel, couvrant le chiffrement des fichiers, la protection en lecture seule, la protection de la structure du classeur, la protection des feuilles de calcul et les signatures numériques à l'aide de code Python
keywords: Aspose.Cells, Python via Java, chiffrer, déchiffrer, mot de passe, protéger, déprotéger, protection du classeur, protection de la feuille de calcul, lecture seule, signature numérique, Python
type: docs
weight: 68
url: /fr/python-java/protect-and-unprotect/
alias: [/python-java/security-features/]
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Les classeurs Excel contiennent souvent des informations financières, commerciales ou personnelles sensibles qui doivent être protégées contre tout accès non autorisé. Aspose.Cells for Python via Java offre un ensemble complet de fonctionnalités de protection qui reflète les capacités de Microsoft Excel, vous permettant de sécuriser vos données au niveau du fichier, du classeur et de la feuille de calcul.

{{% alert color="primary" %}}
Aspose.Cells for Python via Java offre un large éventail de fonctionnalités de protection, du niveau du fichier au niveau des données, similaires à celles de MS Excel. Ces capacités incluent le chiffrement des fichiers avec un mot de passe, l'application d'un accès en lecture seule via un mot de passe de modification, la protection de la structure du classeur, la protection des feuilles de calcul et la signature numérique des classeurs.
{{% /alert %}}

## Chiffrer et déchiffrer des fichiers Excel
Un mot de passe défini sur un fichier Excel empêche les utilisateurs non autorisés d'ouvrir ou de consulter le contenu du classeur. Pour chiffrer un classeur, attribuez une chaîne de mot de passe à `workbook.getSettings().setPassword(...)`, puis enregistrez le classeur. Aspose.Cells écrit le fichier sous forme chiffrée. Pour ouvrir un classeur chiffré en vue de son déchiffrement, instanciez un objet `LoadOptions`, définissez le mot de passe via `load_options.setPassword(...)` avec le même mot de passe utilisé lors du chiffrement, et transmettez-le au constructeur `Workbook`. Aspose.Cells applique le mot de passe fourni de manière transparente afin que le reste de votre code puisse interagir avec le contenu déchiffré comme si le fichier était un classeur normal.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cell, LoadOptions
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cell = sheet.getCells().get("A1")
cell.putValue("Confidential Data")
workbook.getSettings().setPassword("OpenPassword123")
workbook.save("encrypted.xlsx")
load_options = LoadOptions()
load_options.setPassword("OpenPassword123")
decrypted_workbook = Workbook("encrypted.xlsx", load_options)
print("Decrypted cell A1 value: " + decrypted_workbook.getWorksheets().get(0).getCells().get("A1").getStringValue())
jpype.shutdownJVM()
```

## Protection en lecture seule (mot de passe de modification)
Excel prend en charge deux couches distinctes de mots de passe. La première est un mot de passe d'ouverture, qui chiffre le fichier lui-même et est traité dans la section précédente. La seconde est un mot de passe de modification, qui n'empêche pas les utilisateurs d'ouvrir le classeur ; Excel recommande plutôt d'ouvrir le fichier en mode lecture seule, sauf si le mot de passe de modification est fourni. Configurez ce comportement dans Aspose.Cells via `workbook.getSettings().getWriteProtection()`. Définissez le mot de passe via `setPassword(...)` avec le mot de passe de modification et l'auteur via `setAuthor(...)` pour identifier qui a appliqué la protection. Utilisez la méthode `writeProtection.validatePassword(String)` pour vérifier si un mot de passe de modification fourni est correct, en retournant `true` en cas de correspondance et `false` sinon.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# Créer un nouveau classeur à partir de zéro
workbook = Workbook()
# Écrire une valeur d'exemple dans la cellule A1 de la première feuille de calcul
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data")
# Configurer la protection en écriture : définir le mot de passe de modification et l'auteur
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd")
workbook.getSettings().getWriteProtection().setAuthor("AuthorName")
# Enregistrer le classeur pour que la protection en écriture soit conservée
workbook.save("WriteProtectedWorkbook.xlsx")
# Valider le mot de passe de modification en utilisant le mot de passe correct
is_correct_valid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd")
print("ValidatePassword(\"ModifyPwd\") returned: " + str(is_correct_valid))
# Valider le mot de passe de modification en utilisant un mot de passe incorrect pour démontrer l'autre branche
is_wrong_valid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd")
print("ValidatePassword(\"WrongPwd\") returned: " + str(is_wrong_valid))
jpype.shutdownJVM()
```

## Protéger et déprotéger la structure du classeur
La protection de la structure du classeur empêche d'autres utilisateurs d'afficher les feuilles de calcul masquées, d'ajouter de nouvelles feuilles de calcul, de déplacer des feuilles de calcul, de supprimer des feuilles de calcul, de masquer des feuilles de calcul ou de renommer des feuilles de calcul. L'état protégé s'applique à la structure des feuilles plutôt qu'au contenu des cellules à l'intérieur de chaque feuille. Pour appliquer la protection de la structure, appelez `workbook.protect(ProtectionType.STRUCTURE, "password")`. Pour supprimer la protection, appelez `workbook.unprotect("password")` et fournissez le mot de passe correct. La valeur d'énumération `ProtectionType.STRUCTURE` est utilisée ici et est distincte des autres types de protection tels que `ProtectionType.WINDOWS`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, ProtectionType
# Créer un nouveau classeur
workbook = Workbook()
# Ajouter une deuxième feuille de calcul
workbook.getWorksheets().add()
# Écrire une valeur d'exemple dans la cellule A1 de la première feuille de calcul
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data")
# Protéger la structure du classeur
workbook.protect(ProtectionType.STRUCTURE, "StructPwd")
# Enregistrer le classeur sous structure_protected.xlsx
file_path = "structure_protected.xlsx"
workbook.save(file_path)
# Recharger le fichier dans une nouvelle instance de Workbook
loaded_workbook = Workbook(file_path)
# Supprimer la protection de structure
loaded_workbook.unprotect("StructPwd")
# Afficher le message de confirmation
print("Structure protection has been successfully removed from the workbook.")
jpype.shutdownJVM()
```

## Protéger et déprotéger les feuilles de calcul
La protection de la feuille de calcul verrouille les cellules d'une feuille de calcul contre les modifications accidentelles ou délibérées. Les utilisateurs ne peuvent pas modifier les cellules verrouillées sans fournir le mot de passe. C'est la protection classique utilisée pour protéger les formules, les en-têtes ou les zones de saisie de données désignées dans les feuilles de calcul partagées. Pour protéger une feuille de calcul, appelez `worksheet.protect(ProtectionType.ALL, "password")`. L'utilisation de `ProtectionType.ALL` active toutes les options de protection disponibles, telles que la sélection de cellules verrouillées, la mise en forme des cellules, l'insertion de lignes et de colonnes, et la suppression de lignes et de colonnes. Pour supprimer la protection, appelez `worksheet.unprotect("password")` avec le mot de passe correct. Un contrôle plus fin est disponible en combinant d'autres types de protection tels que `ProtectionType.CONTENTS`, `ProtectionType.OBJECTS` et `ProtectionType.SCENARIOS` à l'aide de l'opérateur bit à bit OR.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, ProtectionType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sample Data")
worksheet.protect(ProtectionType.ALL, "SheetPwd", None)
workbook.save("sheet_protected.xlsx")
workbook_reloaded = Workbook("sheet_protected.xlsx")
sheet_reloaded = workbook_reloaded.getWorksheets().get(0)
sheet_reloaded.unprotect("SheetPwd")
print("Worksheet protection removed successfully.")
jpype.shutdownJVM()
```

## Ajouter et valider des signatures numériques
Une signature numérique garantit aux destinataires que le contenu du classeur est authentique et n'a pas été modifié depuis sa signature. Aspose.Cells prend en charge les signatures numériques via l'espace de noms `Aspose.Cells.DigitalSignatures`. Le flux de travail typique charge un fichier de certificat `.pfx` via `java.security.KeyStore`, l'enrobe dans une `Aspose.Cells.DigitalSignatures.DigitalSignature`, ajoute la signature à une `DigitalSignatureCollection`, et applique la collection au classeur via `workbook.addDigitalSignature(digitalSignatureCollection)`. La propriété `digitalSignature.getComments()` peut enregistrer le contexte de signature, tel que l'heure et l'objectif de la signature. Toute modification apportée au classeur après la signature invalide la signature, de sorte qu'une étape de validation côté réception peut détecter toute falsification.

```python
import jpype
import jpype.imports
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, DigitalSignature, DigitalSignatureCollection
from java.security import KeyStore
from java.io import FileInputStream
from java.util import Date
# Charger le certificat depuis un fichier PFX en utilisant Java KeyStore
key_store = KeyStore.getInstance("PKCS12")
fis = FileInputStream("signature.pfx")
key_store.load(fis, "pfx-password")
fis.close()
# Obtenir le certificat
alias = key_store.aliases().nextElement()
certificate = key_store.getCertificate(alias)
# Créer une signature numérique
signature = DigitalSignature(certificate, "Signed by Aspose.Cells", Date())
signatures = DigitalSignatureCollection()
signatures.add(signature)
# Créer le classeur et ajouter la signature
workbook = Workbook()
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value")
workbook.addDigitalSignature(signatures)
workbook.save("signed_workbook.xlsx")
print("The workbook has been digitally signed.")
jpype.shutdownJVM()
```

## Articles connexes
- [Chiffrer et déchiffrer des fichiers Excel](/cells/fr/python-java/encrypt-and-decrypt-excel-files/)
- [Protéger et déprotéger la structure du classeur](/cells/fr/python-java/protect-and-unprotect-workbook-structure/)
- [Protéger et déprotéger une feuille de calcul](/cells/fr/python-java/protect-and-unprotect-worksheet/)
- [Vérifier le mot de passe de modification à l'aide d'Aspose.Cells](/cells/fr/python-java/check-password-to-modify-using-aspose-cells/)

{{< app/cells/assistant language="python" >}}