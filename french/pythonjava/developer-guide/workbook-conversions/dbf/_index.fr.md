---
title: Lecture et écriture des fichiers DBF
description: Aspose.Cells est une bibliothèque Python via Java permettant de travailler avec des fichiers de feuille de calcul, qui prend en charge la lecture et l’écriture de fichiers dBASE III et IV (DBF). Cet article explique comment importer des données depuis des fichiers DBF et exporter des données vers ces fichiers à l’aide d’Aspose.Cells, notamment les détails du format de fichier, les fonctionnalités prises en charge et des exemples étape par étape.
linktitle: Lecture et écriture de DBF
url: /fr/python-java/reading-and-writing-dbf-files/
keywords: Aspose.Cells, bibliothèque Python via Java, DBF, dBASE, lire DBF, écrire DBF, importer DBF, exporter DBF, format de fichier, .dbf
type: docs
weight: 200
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells prend entièrement en charge la lecture et l’écriture des fichiers DBF (dBASE). Vous pouvez charger des fichiers dBASE III et dBASE IV existants dans un objet `Workbook`, manipuler les données à l’aide de l’API Aspose.Cells riche, puis enregistrer le classeur au format DBF afin de l’utiliser avec des applications de base de données héritées.
{{% /alert %}}

## **Introduction**
Le DBF (fichier de base de données) est un ancien format de fichier de base de données introduit à l’origine par dBASE au début des années 1980. Malgré l’ancienneté de ce format, les fichiers DBF restent largement utilisés dans de nombreux secteurs pour stocker des données structurées, notamment dans la comptabilité, les SIG et d’autres applications spécialisées. Aspose.Cells vous permet d’intégrer ces fichiers hérités de manière transparente aux flux de travail modernes de traitement des feuilles de calcul Python via Java.
La bibliothèque prend en charge la lecture et l’écriture des fichiers DBF, ce qui vous permet de :
- Importer des données depuis des fichiers DBF existants vers des objets `Workbook` Aspose.Cells afin de les traiter ultérieurement ou de les convertir vers d’autres formats.
- Créer de nouveaux fichiers DBF à partir de zéro ou en transformant des données provenant d’autres formats de feuille de calcul.
- Conserver les définitions de champs, les types de données et les structures d’enregistrements lors du transfert de données depuis et vers le format DBF.
Les fichiers DBF peuvent également être ouverts directement dans Microsoft Excel et dans d’autres applications de feuille de calcul, ce qui en fait un pont pratique entre les systèmes hérités et les outils de traitement des feuilles de calcul modernes.

## **Versions et fonctionnalités DBF prises en charge**
Aspose.Cells prend en charge les versions suivantes du format DBF :
- **dBASE III** — La variante originale et la plus largement prise en charge du format DBF.
- **dBASE IV** — Une version étendue qui prend en charge des types de données supplémentaires et des tailles de champ plus importantes.

### Fonctionnalités prises en charge
La bibliothèque fournit une prise en charge complète des opérations suivantes :
- Lecture des données DBF dans un objet `Workbook`, avec conservation de tous les enregistrements et de toutes les définitions de champs.
- Écriture des données du classeur dans le format DBF en vue de leur export vers des applications compatibles avec dBASE.
- Gestion des types de données courants utilisés dans les fichiers DBF, notamment les champs de caractère, numériques, de date et logiques.
- Conservation des définitions de champs, telles que le nom, le type et la longueur des champs, lors des opérations de lecture et d’écriture.

### Limites et considérations
Lors de l’utilisation de fichiers DBF, tenez compte des limites suivantes :
- Le nombre maximal de champs par fichier est de **128**.
- La taille maximale d’un enregistrement est de **4000 octets**.
- Les noms de champs sont limités à **10 caractères**, doivent être en majuscules et ne peuvent contenir aucune espace.
- Les valeurs de date des fichiers DBF sont stockées au format `YYYYMMDD`.
- L’encodage de caractères peut varier selon l’application source (généralement Windows-1252 ou des pages de code OEM).

## **Lecture d’un fichier DBF**
Aspose.Cells simplifie le chargement de données depuis un fichier DBF dans un objet `Workbook`. La bibliothèque utilise la classe `LoadOptions` pour spécifier le format source, ce qui garantit une interprétation correcte des données pendant le processus de chargement.

### Lecture d’un fichier DBF avec Aspose.Cells
Pour lire un fichier DBF, vous devez créer une instance de `LoadOptions`, définir sa propriété `LoadFormat` sur `LoadFormat.DBF`, puis la transmettre au constructeur `Workbook` avec le chemin du fichier. Une fois le fichier chargé, les données sont accessibles via la collection `Worksheets`, ce qui vous permet de parcourir les cellules, d’en extraire les valeurs ou de manipuler les données selon vos besoins.
L’exemple suivant montre comment charger un fichier DBF existant dans Aspose.Cells, accéder à sa première feuille de calcul et lire les valeurs des cellules.

```python
import jpype
import os
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, LoadOptions, LoadFormat, SaveFormat
dataDir = "Data/"
filePath = os.path.join(dataDir, "example.dbf")
loadOptions = LoadOptions(LoadFormat.DBF)
workbook = Workbook(filePath, loadOptions)
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
sb = []
maxRow = cells.getMaxDataRow()
maxCol = cells.getMaxDataColumn()
for i in range(maxRow + 1):
    for j in range(maxCol + 1):
        cell = cells.get(i, j)
        value = cell.getStringValue()
        sb.append("|" + value)
    sb.append("|" + "\n")
print("".join(sb))
outputPath = os.path.join(dataDir, "output.xlsx")
workbook.save(outputPath, SaveFormat.XLSX)
print("DBF file loaded successfully. Converted XLSX saved at: " + outputPath)
jpype.shutdownJVM()
```

{{% alert color="primary" %}}
Vous pouvez ouvrir directement les fichiers DBF dans Microsoft Excel en sélectionnant le fichier dans la boîte de dialogue Ouvrir. Excel considère le fichier DBF comme une feuille de calcul et affiche ses enregistrements dans une disposition tabulaire. Cette méthode est utile pour vérifier rapidement les données après les avoir lues ou écrites avec Aspose.Cells.
{{% /alert %}}

## **Écriture d’un fichier DBF**
L’écriture de données dans un fichier DBF suit un processus similaire à celui de l’enregistrement dans tout autre format de feuille de calcul avec Aspose.Cells. Vous créez ou chargez un `Workbook`, renseignez la feuille de calcul avec des données, puis appelez la méthode `Save` en spécifiant `SaveFormat.DBF` comme format cible.

### Écriture d’un fichier DBF avec Aspose.Cells
Pour créer un fichier DBF, suivez ces étapes :
1. Créez une nouvelle instance de `Workbook`.
2. Accédez à la première feuille de calcul de la collection `Worksheets`.
3. Renseignez la feuille de calcul avec vos données, notamment les en-têtes dans la première ligne et les enregistrements dans les lignes suivantes.
4. Appelez la méthode `Workbook.save`, en transmettant le chemin du fichier et `SaveFormat.DBF` comme paramètres.
L’exemple suivant montre comment créer un nouveau fichier DBF à partir de zéro. Il renseigne une feuille de calcul avec des données d’exemple contenant différents types de données (chaînes, nombres et dates) afin d’illustrer la manière dont les types de champs sont traités lors de l’export vers le format DBF.

```python
import jpype
import os
import jpype.imports
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, SaveFormat
import java.time as _jt
import java.util as _ju
outputDir = "C:\\Output\\"
filePath = os.path.join(outputDir, "output.dbf")
if not os.path.exists(outputDir):
    os.makedirs(outputDir, exist_ok=True)
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
# En-têtes de colonnes
cells.get(0, 0).putValue("ID")
cells.get(0, 1).putValue("Name")
cells.get(0, 2).putValue("Department")
cells.get(0, 3).putValue("Salary")
cells.get(0, 4).putValue("HireDate")
# Ligne de données 1
cells.get(1, 0).putValue(101)
cells.get(1, 1).putValue("John Smith")
cells.get(1, 2).putValue("Engineering")
cells.get(1, 3).putValue(75000.50)
cells.get(1, 4).putValue(_jt.LocalDate.of(2020, 3, 15))
# Ligne de données 2
cells.get(2, 0).putValue(102)
cells.get(2, 1).putValue("Jane Doe")
cells.get(2, 2).putValue("Marketing")
cells.get(2, 3).putValue(68000.75)
cells.get(2, 4).putValue(_jt.LocalDate.of(2019, 7, 22))
# Ligne de données 3
cells.get(3, 0).putValue(103)
cells.get(3, 1).putValue("Bob Johnson")
cells.get(3, 2).putValue("Finance")
cells.get(3, 3).putValue(82000.00)
cells.get(3, 4).putValue(_jt.LocalDate.of(2021, 1, 10))
# Ligne de données 4
cells.get(4, 0).putValue(104)
cells.get(4, 1).putValue("Alice Brown")
cells.get(4, 2).putValue("Human Resources")
cells.get(4, 3).putValue(71000.25)
cells.get(4, 4).putValue(_jt.LocalDate.of(2018, 11, 5))
# Ligne de données 5
cells.get(5, 0).putValue(105)
cells.get(5, 1).putValue("Charlie Wilson")
cells.get(5, 2).putValue("Operations")
cells.get(5, 3).putValue(79500.80)
cells.get(5, 4).putValue(_jt.LocalDate.of(2022, 5, 30))
# Définir les largeurs des colonnes pour une meilleure lisibilité
worksheet.getCells().setColumnWidth(0, 8)
worksheet.getCells().setColumnWidth(1, 20)
worksheet.getCells().setColumnWidth(2, 20)
worksheet.getCells().setColumnWidth(3, 12)
worksheet.getCells().setColumnWidth(4, 14)
workbook.save(filePath, SaveFormat.DBF)
jpype.shutdownJVM()
```

{{% alert color="primary" %}}
Lors de l’écriture de données dans un fichier DBF, veillez à ce que vos données respectent les limites du format. Les noms de champs ne doivent pas dépasser 10 caractères et ne doivent pas contenir d’espaces. Les enregistrements dépassant 4000 octets au total ne seront pas correctement enregistrés. Les dates doivent être des valeurs de date valides pouvant être représentées au format YYYYMMDD.
{{% /alert %}}

## **Considérations relatives aux types de données et à la mise en forme**
Lors du transfert de données entre Aspose.Cells et le format DBF, il est important de comprendre comment les types de données sont associés dans les deux systèmes afin de garantir l’intégrité des données.

### Types de cellule vers types de champ DBF
Les valeurs des cellules Aspose.Cells sont automatiquement converties en types de champs DBF appropriés lors de l’enregistrement :
- Les **chaînes** sont associées aux champs de caractère (C).
- Les **valeurs numériques** (entiers et décimales) sont associées aux champs numériques (N).
- Les **valeurs de date** sont associées aux champs de date (D) au format `YYYYMMDD`.
- Les **valeurs booléennes** sont associées aux champs logiques (L).

### Encodage
Les fichiers DBF peuvent utiliser différents encodages de caractères selon l’application qui les a créés. Aspose.Cells gère l’encodage de manière transparente dans la plupart des cas. Toutefois, si vous rencontrez des problèmes d’affichage des caractères, vous devrez peut-être vérifier l’encodage du fichier source.

### Règles relatives aux noms de champs
Les noms de champs DBF doivent respecter les règles suivantes :
- Longueur maximale de 10 caractères.
- Doivent commencer par une lettre.
- Ne peuvent contenir ni espaces ni caractères spéciaux.
- Sont stockés en majuscules, quelle que soit la casse utilisée dans la saisie.

### Vérification du résultat
Après avoir écrit un fichier DBF, vous pouvez vérifier le résultat en l’ouvrant dans Microsoft Excel ou dans toute application compatible avec dBASE. Les données doivent apparaître dans une disposition tabulaire, avec les noms de champs comme en-têtes de colonnes et les enregistrements renseignés conformément aux données que vous avez fournies.

## **Conversion entre DBF et d’autres formats**
L’un des cas d’utilisation les plus pratiques de la lecture et de l’écriture de fichiers DBF avec Aspose.Cells consiste à convertir des données entre le format DBF et des formats modernes de feuille de calcul tels que XLSX, XLS ou CSV. Comme Aspose.Cells prend en charge un large éventail de formats, vous pouvez facilement charger un fichier DBF et l’enregistrer dans tout autre format pris en charge, ou effectuer l’opération inverse.

{{< app/cells/assistant language="python" >}}