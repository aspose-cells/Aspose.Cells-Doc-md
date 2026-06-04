---
title: Lecture et écriture de fichiers DBF
description: Aspose.Cells for Node.js via C++ est une bibliothèque permettant de travailler avec des fichiers de feuilles de calcul, qui prend en charge la lecture et l'écriture de fichiers dBASE III et IV (DBF). Cet article explique comment importer des données depuis et exporter des données vers des fichiers DBF à l'aide d'Aspose.Cells, y compris les détails du format de fichier, les fonctionnalités prises en charge et des exemples étape par étape.
keywords: Aspose.Cells, Node.js via C++, DBF, dBASE, lire DBF, écrire DBF, importer DBF, exporter DBF, format de fichier, .dbf
type: docs
weight: 200
url: /fr/nodejs-cpp/reading-and-writing-dbf-files/
---

{{% alert color="primary" %}}

Aspose.Cells offre une prise en charge complète pour la lecture et l'écriture de fichiers DBF (dBASE). Vous pouvez charger des fichiers dBASE III et dBASE IV existants dans un objet Workbook, manipuler les données à l'aide de la riche API Aspose.Cells, puis enregistrer le classeur au format DBF pour l'utiliser avec des applications de base de données héritées.

{{% /alert %}}

## **Introduction**

Le format DBF (DataBase File) est un format de fichier de base de données hérité introduit à l'origine par dBASE au début des années 1980. Malgré l'ancienneté du format, les fichiers DBF sont encore largement utilisés dans de nombreux secteurs pour stocker des données structurées, notamment dans la comptabilité, les SIG et d'autres applications spécialisées. Aspose.Cells vous permet d'intégrer ces fichiers hérités de manière transparente dans les workflows modernes de feuilles de calcul Node.js via C++.

La bibliothèque prend en charge à la fois la lecture et l'écriture des fichiers DBF, vous offrant la possibilité de :

- Importer des données depuis des fichiers DBF existants dans des objets Workbook d'Aspose.Cells pour un traitement ultérieur ou une conversion vers d'autres formats.
- Créer de nouveaux fichiers DBF à partir de zéro ou en transformant des données provenant d'autres formats de feuilles de calcul.
- Conserver les définitions de champs, les types de données et les structures d'enregistrements lors du transfert de données vers et depuis le format DBF.

Les fichiers DBF peuvent également être ouverts directement dans Microsoft Excel et d'autres applications de feuilles de calcul, ce qui en fait un pont pratique entre les systèmes hérités et les outils de feuilles de calcul modernes.

## **Versions et fonctionnalités DBF prises en charge**

Aspose.Cells prend en charge les versions de format DBF suivantes :

- **dBASE III** — La variante originale et la plus largement prise en charge du format DBF.
- **dBASE IV** — Une version étendue qui prend en charge des types de données supplémentaires et des tailles de champ plus importantes.

### Fonctionnalités prises en charge

La bibliothèque offre une prise en charge complète pour les opérations suivantes :

- Lecture des données DBF dans un objet Workbook, avec tous les enregistrements et définitions de champs préservés.
- Écriture des données du classeur au format DBF pour l'exportation vers des applications compatibles dBASE.
- Gestion des types de données courants utilisés dans les fichiers DBF, notamment les champs de type caractère, numérique, date et logique.
- Conservation des définitions de champs telles que le nom du champ, le type et la longueur lors des opérations de lecture/écriture.

### Limitations et considérations

Lorsque vous travaillez avec des fichiers DBF, gardez à l'esprit les contraintes suivantes :

- Le nombre maximum de champs par fichier est **128**.
- La taille maximale d'un enregistrement est **4000 octets**.
- Les noms de champs sont limités à **10 caractères**, doivent être en majuscules et ne peuvent pas contenir d'espaces.
- Les valeurs de date dans les fichiers DBF sont stockées au format `YYYYMMDD`.
- L'encodage des caractères peut varier selon l'application source (généralement Windows-1252 ou les pages de code OEM).

## **Lecture d'un fichier DBF**

Aspose.Cells facilite le chargement des données d'un fichier DBF dans un objet Workbook. La bibliothèque utilise la classe `LoadOptions` pour spécifier le format source, garantissant que les données sont interprétées correctement pendant le processus de chargement.

### Lecture d'un fichier DBF avec Aspose.Cells

Pour lire un fichier DBF, vous devez créer une instance de `LoadOptions`, définir sa propriété `LoadFormat` sur `LoadFormat.Dbf`, et la passer au constructeur `Workbook` avec le chemin du fichier. Une fois chargé, les données deviennent accessibles via la collection `Worksheets`, où vous pouvez parcourir les cellules, extraire des valeurs ou manipuler les données selon vos besoins.

L'exemple suivant montre comment charger un fichier DBF existant dans Aspose.Cells, accéder à sa première feuille de calcul et lire les valeurs des cellules.

```javascript
let sb = "";

const maxRow = cells.getMaxDataRow();
const maxCol = cells.getMaxDataColumn();

for (let i = 0; i <= maxRow; i++)
{
    for (let j = 0; j <= maxCol; j++)
    {
        const cell = cells.get(i, j);
        const value = cell.getStringValue();
        sb += "|" + value;
    }
    sb += "|" + "\n";
}

console.log(sb);

const outputPath = path.join(dataDir, "output.xlsx");
workbook.save(outputPath, AsposeCells.SaveFormat.Xlsx);

console.log("DBF file loaded successfully. Converted XLSX saved at: " + outputPath);
```

{{% alert color="primary" %}}

Vous pouvez ouvrir les fichiers DBF directement dans Microsoft Excel en sélectionnant le fichier dans la boîte de dialogue Ouvrir. Excel traitera le fichier DBF comme une feuille de calcul, affichant ses enregistrements dans une disposition tabulaire. Cela est utile pour vérifier rapidement les données après les avoir lues ou écrites avec Aspose.Cells.

{{% /alert %}}

## **Écriture d'un fichier DBF**

L'écriture de données dans un fichier DBF suit un modèle similaire à l'enregistrement de tout autre format de feuille de calcul avec Aspose.Cells. Vous créez ou chargez un Workbook, remplissez la feuille de calcul avec des données, puis appelez la méthode `save` tout en spécifiant `SaveFormat.Dbf` comme format cible.

### Écriture d'un fichier DBF avec Aspose.Cells

Pour créer un fichier DBF, procédez comme suit :

1. Créez une nouvelle instance de `Workbook`.
2. Accédez à la première feuille de calcul à partir de la collection `Worksheets`.
3. Remplissez la feuille de calcul avec vos données, en incluant les en-têtes dans la première ligne et les enregistrements dans les lignes suivantes.
4. Appelez la méthode `workbook.save`, en passant le chemin du fichier et `SaveFormat.Dbf` comme paramètres.

L'exemple suivant montre comment créer un nouveau fichier DBF à partir de zéro. Il remplit une feuille de calcul avec des données d'exemple contenant différents types de données (chaînes, nombres et dates) pour illustrer la façon dont les types de champs sont gérés lors de l'exportation au format DBF.

```javascript
const AsposeCells = require("aspose.cells");
const path = require("path");
const fs = require("fs");

const outputDir = "C:\\Output\\";
const filePath = path.join(outputDir, "output.dbf");

if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
}

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();

// En-têtes de colonnes
cells.get(0, 0).putValue("ID");
cells.get(0, 1).putValue("Name");
cells.get(0, 2).putValue("Department");
cells.get(0, 3).putValue("Salary");
cells.get(0, 4).putValue("HireDate");

// Ligne de données 1
cells.get(1, 0).putValue(101);
cells.get(1, 1).putValue("John Smith");
cells.get(1, 2).putValue("Engineering");
cells.get(1, 3).putValue(75000.50);
cells.get(1, 4).putValue(new Date(2020, 2, 15));

// Ligne de données 2
cells.get(2, 0).putValue(102);
cells.get(2, 1).putValue("Jane Doe");
cells.get(2, 2).putValue("Marketing");
cells.get(2, 3).putValue(68000.75);
cells.get(2, 4).putValue(new Date(2019, 6, 22));

// Ligne de données 3
cells.get(3, 0).putValue(103);
cells.get(3, 1).putValue("Bob Johnson");
cells.get(3, 2).putValue("Finance");
cells.get(3, 3).putValue(82000.00);
cells.get(3, 4).putValue(new Date(2021, 0, 10));

// Ligne de données 4
cells.get(4, 0).putValue(104);
cells.get(4, 1).putValue("Alice Brown");
cells.get(4, 2).putValue("Human Resources");
cells.get(4, 3).putValue(71000.25);
cells.get(4, 4).putValue(new Date(2018, 10, 5));

// Ligne de données 5
cells.get(5, 0).putValue(105);
cells.get(5, 1).putValue("Charlie Wilson");
cells.get(5, 2).putValue("Operations");
cells.get(5, 3).putValue(79500.80);
cells.get(5, 4).putValue(new Date(2022, 4, 30));

// Définir la largeur des colonnes pour une meilleure lisibilité
worksheet.getCells().setColumnWidth(0, 8);
worksheet.getCells().setColumnWidth(1, 20);
worksheet.getCells().setColumnWidth(2, 20);
worksheet.getCells().setColumnWidth(3, 12);
worksheet.getCells().setColumnWidth(4, 14);

workbook.save(filePath, AsposeCells.SaveFormat.Dbf);
```

{{% alert color="primary" %}}

Lors de l'écriture de données dans un fichier DBF, assurez-vous que vos données sont conformes aux limitations du format. Les noms de champs ne doivent pas dépasser 10 caractères et ne doivent pas contenir d'espaces. Les enregistrements dépassant 4000 octets au total ne seront pas enregistrés correctement. Les dates doivent être des valeurs de date valides pouvant être représentées au format AAAAMMJJ.

{{% /alert %}}

## **Considérations sur les types de données et la mise en forme**

Lors du transfert de données entre Aspose.Cells et le format DBF, il est important de comprendre comment les types de données sont mappés entre les deux systèmes pour garantir l'intégrité des données.

### Types de cellules vers types de champs DBF

Les valeurs des cellules d'Aspose.Cells sont automatiquement converties vers les types de champs DBF appropriés lors de l'enregistrement :

- Les **chaînes** sont mappées vers les champs de type caractère (C).
- Les **valeurs numériques** (entiers et décimales) sont mappées vers les champs numériques (N).
- Les **valeurs de date** sont mappées vers les champs de date (D) au format `AAAAMMJJ`.
- Les **valeurs booléennes** sont mappées vers les champs logiques (L).

### Encodage

Les fichiers DBF peuvent utiliser différents encodages de caractères selon l'application qui les a créés. Aspose.Cells gère l'encodage de manière transparente dans la plupart des cas, mais si vous rencontrez des problèmes d'affichage des caractères, vous devrez peut-être vérifier l'encodage du fichier source.

### Règles de nommage des champs

Les noms de champs DBF doivent respecter les règles suivantes :

- Longueur maximale de 10 caractères.
- Doivent commencer par une lettre.
- Ne peuvent pas contenir d'espaces ni de caractères spéciaux.
- Stockés en majuscules quelle que soit la casse utilisée en entrée.

### Vérification du résultat

Après avoir écrit un fichier DBF, vous pouvez vérifier le résultat en l'ouvrant dans Microsoft Excel ou toute application compatible dBASE. Les données doivent apparaître dans une disposition tabulaire avec les noms de champs comme en-têtes de colonnes, et les enregistrements remplis en fonction des données que vous avez fournies.

## **Conversion entre DBF et d'autres formats**

L'un des cas d'utilisation les plus pratiques pour la lecture et l'écriture de fichiers DBF avec Aspose.Cells est la conversion de données entre le format DBF et les formats de feuilles de calcul modernes tels que XLSX, XLS ou CSV. Comme Aspose.Cells prend en charge un large éventail de formats, vous pouvez facilement charger un fichier DBF et l'enregistrer à nouveau dans tout autre format pris en charge, ou vice versa.

Par exemple, vous pouvez lire un fichier DBF, appliquer une mise en forme ou des calculs à l'aide de l'API Aspose.Cells, puis enregistrer le résultat sous forme de fichier XLSX pour le distribuer aux utilisateurs qui travaillent avec des applications de feuilles de calcul modernes. Inversement, vous pouvez prendre des données d'un fichier XLSX ou CSV et les exporter au format DBF pour les intégrer dans des systèmes hérités.



{{< app/cells/assistant language="javascript" >}}