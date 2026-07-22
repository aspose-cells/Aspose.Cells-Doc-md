---
title: Lecture et écriture de fichiers DBF
linktitle: Lecture et écriture de fichiers
description: Aspose.Cells est une bibliothèque .NET pour travailler avec des fichiers de feuilles de calcul, qui prend en charge la lecture et l'écriture de fichiers dBASE III et IV (DBF). Cet article explique comment importer des données depuis et exporter des données vers des fichiers DBF à l'aide d'Aspose.Cells, y compris les détails du format de fichier, les fonctionnalités prises en charge et des exemples étape par étape.
keywords: Aspose.Cells, bibliothèque .NET, DBF, dBASE, lire DBF, écrire DBF, importer DBF, exporter DBF, format de fichier, .dbf
type: docs
weight: 200
url: /fr/net/reading-and-writing-dbf-files/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells offre une prise en charge complète pour la lecture et l'écriture de fichiers DBF (dBASE). Vous pouvez charger des fichiers dBASE III et dBASE IV existants dans un objet Workbook, manipuler les données à l'aide de la riche API Aspose.Cells, et enregistrer le classeur au format DBF pour une utilisation avec des applications de base de données héritées.

{{% /alert %}}

## **Introduction**

DBF (DataBase File) est un format de fichier de base de données hérité initialement introduit par dBASE au début des années 1980. Malgré l'ancienneté du format, les fichiers DBF sont toujours largement utilisés dans de nombreux secteurs pour stocker des données structurées, notamment dans la comptabilité, les SIG et d'autres applications spécialisées. Aspose.Cells vous permet d'intégrer de manière transparente ces fichiers hérités dans les flux de travail de feuilles de calcul .NET modernes.

La bibliothèque prend en charge la lecture et l'écriture de fichiers DBF, vous donnant la possibilité de :

- Importer des données depuis des fichiers DBF existants dans des objets Workbook Aspose.Cells pour un traitement ultérieur ou une conversion vers d'autres formats.
- Créer de nouveaux fichiers DBF à partir de zéro ou en transformant des données provenant d'autres formats de feuilles de calcul.
- Conserver les définitions de champs, les types de données et les structures d'enregistrements lors du transfert de données vers et depuis le format DBF.

Les fichiers DBF peuvent également être ouverts directement dans Microsoft Excel et d'autres applications de feuilles de calcul, ce qui en fait un pont pratique entre les systèmes hérités et les outils de feuilles de calcul modernes.

## **Versions et fonctionnalités DBF prises en charge**

Aspose.Cells prend en charge les versions de format DBF suivantes :

- **dBASE III** — La variante originale et la plus largement prise en charge du format DBF.
- **dBASE IV** — Une version étendue qui prend en charge des types de données supplémentaires et des tailles de champ plus grandes.

### Fonctionnalités prises en charge

La bibliothèque offre une prise en charge complète des opérations suivantes :

- Lecture de données DBF dans un objet Workbook, avec tous les enregistrements et définitions de champs conservés.
- Écriture des données du classeur au format DBF pour l'exportation vers des applications compatibles dBASE.
- Gestion des types de données courants utilisés dans les fichiers DBF, y compris les champs de caractères, numériques, de date et logiques.
- Conservation des définitions de champs telles que le nom, le type et la longueur du champ lors des opérations de lecture/écriture.

### Limitations et considérations

Lorsque vous travaillez avec des fichiers DBF, gardez à l'esprit les contraintes suivantes :

- Le nombre maximum de champs par fichier est **128**.
- La taille maximale d'un enregistrement est **4000 octets**.
- Les noms de champs sont limités à **10 caractères**, doivent être en majuscules et ne peuvent pas contenir d'espaces.
- Les valeurs de date dans les fichiers DBF sont stockées au format `YYYYMMDD`.
- L'encodage des caractères peut varier selon l'application source (généralement Windows-1252 ou des pages de code OEM).

## **Lecture d'un fichier DBF**

Aspose.Cells facilite le chargement de données depuis un fichier DBF dans un objet Workbook. La bibliothèque utilise la classe `LoadOptions` pour spécifier le format source, garantissant que les données sont interprétées correctement pendant le processus de chargement.

### Lecture d'un fichier DBF avec Aspose.Cells

Pour lire un fichier DBF, vous devez créer une instance `LoadOptions`, définir sa propriété `LoadFormat` sur `LoadFormat.Dbf`, et la transmettre au constructeur `Workbook` avec le chemin du fichier. Une fois chargé, les données deviennent accessibles via la collection `Worksheets`, où vous pouvez itérer à travers les cellules, extraire des valeurs ou manipuler les données selon vos besoins.

L'exemple suivant montre comment charger un fichier DBF existant dans Aspose.Cells, accéder à sa première feuille de calcul et lire les valeurs des cellules.

```csharp
using System;
using System.IO;
using System.Text;
using Aspose.Cells;

string dataDir = "Data/";
string filePath = Path.Combine(dataDir, "example.dbf");

LoadOptions loadOptions = new LoadOptions(LoadFormat.Dbf);

Workbook workbook = new Workbook(filePath, loadOptions);

Worksheet worksheet = workbook.Worksheets[0];

Cells cells = worksheet.Cells;

StringBuilder sb = new StringBuilder();

int maxRow = cells.MaxDataRow;
int maxCol = cells.MaxDataColumn;

for (int i = 0; i <= maxRow; i++)
{
    for (int j = 0; j <= maxCol; j++)
    {
        Cell cell = cells[i, j];
        string value = cell.StringValue;
        sb.Append("|").Append(value);
    }
    sb.Append("|").AppendLine();
}

Console.WriteLine(sb.ToString());

string outputPath = Path.Combine(dataDir, "output.xlsx");
workbook.Save(outputPath, SaveFormat.Xlsx);

Console.WriteLine("DBF file loaded successfully. Converted XLSX saved at: " + outputPath);
```

{{% alert color="primary" %}}

Vous pouvez ouvrir des fichiers DBF directement dans Microsoft Excel en sélectionnant le fichier dans la boîte de dialogue Ouvrir. Excel traitera le fichier DBF comme une feuille de calcul, affichant ses enregistrements dans une disposition tabulaire. Cela est utile pour vérifier rapidement les données après les avoir lues ou écrites avec Aspose.Cells.

{{% /alert %}}

## **Écriture d'un fichier DBF**

L'écriture de données dans un fichier DBF suit un modèle similaire à l'enregistrement de tout autre format de feuille de calcul avec Aspose.Cells. Vous créez ou chargez un Workbook, remplissez la feuille de calcul avec des données, puis appelez la méthode `Save` en spécifiant `SaveFormat.Dbf` comme format cible.

### Écriture d'un fichier DBF avec Aspose.Cells

Pour créer un fichier DBF, suivez ces étapes :

1. Créez une nouvelle instance `Workbook`.
2. Accédez à la première feuille de calcul depuis la collection `Worksheets`.
3. Remplissez la feuille de calcul avec vos données, y compris les en-têtes dans la première ligne et les enregistrements dans les lignes suivantes.
4. Appelez la méthode `Workbook.Save`, en transmettant le chemin du fichier et `SaveFormat.Dbf` comme paramètres.

L'exemple suivant montre comment créer un nouveau fichier DBF à partir de zéro. Il remplit une feuille de calcul avec des exemples de données contenant différents types de données (chaînes, nombres et dates) pour illustrer comment les types de champs sont gérés lors de l'exportation au format DBF.

```csharp
using System;
using System.IO;
using Aspose.Cells;

string outputDir = @"C:\Output\";
string filePath = Path.Combine(outputDir, "output.dbf");

if (!Directory.Exists(outputDir))
{
    Directory.CreateDirectory(outputDir);
}

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;

// En-têtes de colonnes
cells[0, 0].PutValue("ID");
cells[0, 1].PutValue("Name");
cells[0, 2].PutValue("Department");
cells[0, 3].PutValue("Salary");
cells[0, 4].PutValue("HireDate");

// Ligne de données 1
cells[1, 0].PutValue(101);
cells[1, 1].PutValue("John Smith");
cells[1, 2].PutValue("Engineering");
cells[1, 3].PutValue(75000.50);
cells[1, 4].PutValue(new DateTime(2020, 3, 15));

// Ligne de données 2
cells[2, 0].PutValue(102);
cells[2, 1].PutValue("Jane Doe");
cells[2, 2].PutValue("Marketing");
cells[2, 3].PutValue(68000.75);
cells[2, 4].PutValue(new DateTime(2019, 7, 22));

// Ligne de données 3
cells[3, 0].PutValue(103);
cells[3, 1].PutValue("Bob Johnson");
cells[3, 2].PutValue("Finance");
cells[3, 3].PutValue(82000.00);
cells[3, 4].PutValue(new DateTime(2021, 1, 10));

// Ligne de données 4
cells[4, 0].PutValue(104);
cells[4, 1].PutValue("Alice Brown");
cells[4, 2].PutValue("Human Resources");
cells[4, 3].PutValue(71000.25);
cells[4, 4].PutValue(new DateTime(2018, 11, 5));

// Ligne de données 5
cells[5, 0].PutValue(105);
cells[5, 1].PutValue("Charlie Wilson");
cells[5, 2].PutValue("Operations");
cells[5, 3].PutValue(79500.80);
cells[5, 4].PutValue(new DateTime(2022, 5, 30));

// Définir la largeur des colonnes pour une meilleure lisibilité
worksheet.Cells.SetColumnWidth(0, 8);
worksheet.Cells.SetColumnWidth(1, 20);
worksheet.Cells.SetColumnWidth(2, 20);
worksheet.Cells.SetColumnWidth(3, 12);
worksheet.Cells.SetColumnWidth(4, 14);

workbook.Save(filePath, SaveFormat.Dbf);
```

{{% alert color="primary" %}}

Lors de l'écriture de données dans un fichier DBF, assurez-vous que vos données respectent les limitations du format. Les noms de champs ne doivent pas dépasser 10 caractères et ne doivent pas contenir d'espaces. Les enregistrements dépassant 4000 octets au total ne seront pas enregistrés correctement. Les dates doivent être des valeurs de date valides pouvant être représentées au format AAAAMMJJ.

{{% /alert %}}

## **Considérations sur les types de données et la mise en forme**

Lors du transfert de données entre Aspose.Cells et le format DBF, il est important de comprendre comment les types de données correspondent entre les deux systèmes pour garantir l'intégrité des données.

### Types de cellules vers types de champs DBF

Les valeurs des cellules Aspose.Cells sont automatiquement converties vers les types de champs DBF appropriés lors de l'enregistrement :

- Les **chaînes** sont mappées vers les champs de type caractère (C).
- Les **valeurs numériques** (entiers et décimales) sont mappées vers les champs numériques (N).
- Les **valeurs de date** sont mappées vers les champs de date (D) au format `YYYYMMDD`.
- Les **valeurs booléennes** sont mappées vers les champs logiques (L).

### Encodage

Les fichiers DBF peuvent utiliser différents encodages de caractères selon l'application qui les a créés. Aspose.Cells gère l'encodage de manière transparente dans la plupart des cas, mais si vous rencontrez des problèmes d'affichage des caractères, vous devrez peut-être vérifier l'encodage du fichier source.

### Règles de nommage des champs

Les noms de champs DBF doivent respecter les règles suivantes :

- Longueur maximale de 10 caractères.
- Doit commencer par une lettre.
- Ne peut pas contenir d'espaces ou de caractères spéciaux.
- Stockés en majuscules quelle que soit la casse utilisée en entrée.

### Vérification du résultat

Après avoir écrit un fichier DBF, vous pouvez vérifier le résultat en l'ouvrant dans Microsoft Excel ou toute application compatible dBASE. Les données doivent apparaître dans une disposition tabulaire avec les noms de champs comme en-têtes de colonnes, et les enregistrements remplis selon les données que vous avez fournies.

## **Conversion entre DBF et d'autres formats**

L'un des cas d'utilisation les plus pratiques pour la lecture et l'écriture de fichiers DBF avec Aspose.Cells est la conversion de données entre le format DBF et des formats de feuilles de calcul modernes tels que XLSX, XLS ou CSV. Comme Aspose.Cells prend en charge une large gamme de formats, vous pouvez facilement charger un fichier DBF et l'enregistrer dans tout autre format pris en charge, ou vice versa.

Par exemple, vous pouvez lire un fichier DBF, appliquer une mise en forme ou des calculs à l'aide de l'API Aspose.Cells, puis enregistrer le résultat sous forme de fichier XLSX pour distribution aux utilisateurs qui travaillent avec des applications de feuilles de calcul modernes. Inversement, vous pouvez extraire des données d'un fichier XLSX ou CSV et les exporter au format DBF pour intégration avec des systèmes hérités.

{{< app/cells/assistant language="csharp" >}}