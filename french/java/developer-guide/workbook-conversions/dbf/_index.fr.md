---
title: Lecture et écriture de fichiers DBF
description: Aspose.Cells est une bibliothèque Java pour travailler avec des fichiers de tableurs, qui prend en charge la lecture et l'écriture de fichiers dBASE III et IV (DBF). Cet article explique comment importer et exporter des données depuis et vers des fichiers DBF à l'aide d'Aspose.Cells, y compris les détails du format de fichier, les fonctionnalités prises en charge et des exemples étape par étape.
keywords: Aspose.Cells, bibliothèque Java, DBF, dBASE, lire DBF, écrire DBF, importer DBF, exporter DBF, format de fichier, .dbf
type: docs
weight: 200
url: /fr/java/reading-and-writing-dbf-files/
---

{{% alert color="primary" %}}

Aspose.Cells offre une prise en charge complète pour la lecture et l'écriture de fichiers DBF (dBASE). Vous pouvez charger des fichiers dBASE III et dBASE IV existants dans un objet Workbook, manipuler les données à l'aide de la riche API Aspose.Cells, et enregistrer le classeur au format DBF pour une utilisation avec des applications de base de données héritées.

{{% /alert %}}

## **Introduction**

DBF (DataBase File) est un format de fichier de base de données hérité initialement introduit par dBASE au début des années 1980. Malgré l'ancienneté du format, les fichiers DBF sont encore largement utilisés dans de nombreux secteurs pour stocker des données structurées, notamment dans la comptabilité, les SIG et d'autres applications spécialisées. Aspose.Cells vous permet d'intégrer ces fichiers hérités de manière transparente dans les flux de travail modernes de tableurs Java.

La bibliothèque prend en charge à la fois la lecture et l'écriture de fichiers DBF, ce qui vous offre la possibilité de :

- Importer des données à partir de fichiers DBF existants dans des objets Workbook d'Aspose.Cells pour traitement ultérieur ou conversion vers d'autres formats.
- Créer de nouveaux fichiers DBF à partir de zéro ou en transformant des données provenant d'autres formats de tableurs.
- Conserver les définitions de champs, les types de données et les structures d'enregistrements lors du transfert de données vers et depuis le format DBF.

Les fichiers DBF peuvent également être ouverts directement dans Microsoft Excel et d'autres applications de tableurs, ce qui en fait un pont pratique entre les systèmes hérités et les outils de tableurs modernes.

## **Versions et fonctionnalités DBF prises en charge**

Aspose.Cells prend en charge les versions de format DBF suivantes :

- **dBASE III** — La variante originale et la plus largement prise en charge du format DBF.
- **dBASE IV** — Une version étendue qui prend en charge des types de données supplémentaires et des tailles de champ plus grandes.

### Fonctionnalités prises en charge

La bibliothèque offre une prise en charge complète pour les opérations suivantes :

- Lecture des données DBF dans un objet Workbook, avec tous les enregistrements et définitions de champs préservés.
- Écriture des données du classeur au format DBF pour exportation vers des applications compatibles dBASE.
- Gestion des types de données courants utilisés dans les fichiers DBF, y compris les champs de caractères, numériques, de date et logiques.
- Préservation des définitions de champs telles que le nom du champ, le type et la longueur lors des opérations de lecture/écriture.

### Limitations et considérations

Lorsque vous travaillez avec des fichiers DBF, gardez à l'esprit les contraintes suivantes :

- Le nombre maximum de champs par fichier est de **128**.
- La taille maximale d'un enregistrement est de **4000 octets**.
- Les noms de champs sont limités à **10 caractères**, doivent être en majuscules et ne peuvent pas contenir d'espaces.
- Les valeurs de date dans les fichiers DBF sont stockées au format `YYYYMMDD`.
- L'encodage des caractères peut varier selon l'application source (généralement Windows-1252 ou les pages de code OEM).

## **Lecture d'un fichier DBF**

Aspose.Cells facilite le chargement des données d'un fichier DBF dans un objet Workbook. La bibliothèque utilise la classe `LoadOptions` pour spécifier le format source, garantissant que les données sont interprétées correctement pendant le processus de chargement.

### Lecture d'un fichier DBF avec Aspose.Cells

Pour lire un fichier DBF, vous devez créer une instance de `LoadOptions`, définir sa propriété `LoadFormat` sur `LoadFormat.Dbf`, et la passer au constructeur `Workbook` avec le chemin du fichier. Une fois chargées, les données deviennent accessibles via la collection `getWorksheets()`, où vous pouvez parcourir les cellules, extraire des valeurs ou manipuler les données selon vos besoins.

L'exemple suivant montre comment charger un fichier DBF existant dans Aspose.Cells, accéder à sa première feuille de calcul et lire les valeurs des cellules.

```java
import com.aspose.cells.*;
import java.io.File;

String dataDir = "Data/";
String filePath = new File(new File(dataDir), "example.dbf").getPath();

LoadOptions loadOptions = new LoadOptions(LoadFormat.DBF);

Workbook workbook = new Workbook(filePath, loadOptions);

Worksheet worksheet = workbook.getWorksheets().get(0);

Cells cells = worksheet.getCells();

StringBuilder sb = new StringBuilder();

int maxRow = cells.getMaxDataRow();
int maxCol = cells.getMaxDataColumn();

for (int i = 0; i <= maxRow; i++)
{
    for (int j = 0; j <= maxCol; j++)
    {
        Cell cell = cells.get(i, j);
        String value = cell.getStringValue();
        sb.append("|").append(value);
    }
    sb.append("|").append(System.lineSeparator());
}

System.out.println(sb.toString());

String outputPath = new File(new File(dataDir), "output.xlsx").getPath();
workbook.save(outputPath, SaveFormat.XLSX);

System.out.println("DBF file loaded successfully. Converted XLSX saved at: " + outputPath);
```

{{% alert color="primary" %}}

Vous pouvez ouvrir les fichiers DBF directement dans Microsoft Excel en sélectionnant le fichier dans la boîte de dialogue Ouvrir. Excel traitera le fichier DBF comme un tableur, affichant ses enregistrements dans une disposition tabulaire. Cela est utile pour vérifier rapidement les données après les avoir lues ou écrites avec Aspose.Cells.

{{% /alert %}}

## **Écriture d'un fichier DBF**

L'écriture de données dans un fichier DBF suit un schéma similaire à l'enregistrement de tout autre format de tableur avec Aspose.Cells. Vous créez ou chargez un Workbook, remplissez la feuille de calcul avec des données, puis appelez la méthode `save` en spécifiant `SaveFormat.Dbf` comme format cible.

### Écriture d'un fichier DBF avec Aspose.Cells

Pour créer un fichier DBF, suivez ces étapes :

1. Créez une nouvelle instance de `Workbook`.
2. Accédez à la première feuille de calcul dans la collection `getWorksheets()`.
3. Remplissez la feuille de calcul avec vos données, en incluant les en-têtes dans la première ligne et les enregistrements dans les lignes suivantes.
4. Appelez la méthode `Workbook.save`, en passant le chemin du fichier et `SaveFormat.Dbf` comme paramètres.

L'exemple suivant montre comment créer un nouveau fichier DBF à partir de zéro. Il remplit une feuille de calcul avec des données d'exemple contenant différents types de données (chaînes, nombres et dates) pour illustrer comment les types de champs sont gérés lors de l'exportation au format DBF.

```java
import com.aspose.cells.*;
import java.io.File;
import java.util.GregorianCalendar;

String outputDir = "C:\\Output\\";
String filePath = new File(new File(outputDir), "output.dbf").getPath();

if (!new File(outputDir).exists())
{
    new File(outputDir).mkdirs();
}

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();

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
cells.get(1, 4).putValue(new GregorianCalendar(2020, 2, 15).getTime());

// Ligne de données 2
cells.get(2, 0).putValue(102);
cells.get(2, 1).putValue("Jane Doe");
cells.get(2, 2).putValue("Marketing");
cells.get(2, 3).putValue(68000.75);
cells.get(2, 4).putValue(new GregorianCalendar(2019, 6, 22).getTime());

// Ligne de données 3
cells.get(3, 0).putValue(103);
cells.get(3, 1).putValue("Bob Johnson");
cells.get(3, 2).putValue("Finance");
cells.get(3, 3).putValue(82000.00);
cells.get(3, 4).putValue(new GregorianCalendar(2021, 0, 10).getTime());

// Ligne de données 4
cells.get(4, 0).putValue(104);
cells.get(4, 1).putValue("Alice Brown");
cells.get(4, 2).putValue("Human Resources");
cells.get(4, 3).putValue(71000.25);
cells.get(4, 4).putValue(new GregorianCalendar(2018, 10, 5).getTime());

// Ligne de données 5
cells.get(5, 0).putValue(105);
cells.get(5, 1).putValue("Charlie Wilson");
cells.get(5, 2).putValue("Operations");
cells.get(5, 3).putValue(79500.80);
cells.get(5, 4).putValue(new GregorianCalendar(2022, 4, 30).getTime());

// Définir la largeur des colonnes pour une meilleure lisibilité
worksheet.getCells().setColumnWidth(0, 8);
worksheet.getCells().setColumnWidth(1, 20);
worksheet.getCells().setColumnWidth(2, 20);
worksheet.getCells().setColumnWidth(3, 12);
worksheet.getCells().setColumnWidth(4, 14);

workbook.save(filePath, SaveFormat.DBF);
```

{{% alert color="primary" %}}

Lors de l'écriture de données dans un fichier DBF, assurez-vous que vos données respectent les limitations du format. Les noms de champs ne doivent pas dépasser 10 caractères et ne doivent pas contenir d'espaces. Les enregistrements dépassant 4000 octets au total ne seront pas enregistrés correctement. Les dates doivent être des valeurs de date valides pouvant être représentées au format YYYYMMDD.

{{% /alert %}}

## **Considérations sur les types de données et la mise en forme**

Lors du transfert de données entre Aspose.Cells et le format DBF, il est important de comprendre comment les types de données sont mappés entre les deux systèmes pour garantir l'intégrité des données.

### Types de cellules vers types de champs DBF

Les valeurs des cellules Aspose.Cells sont automatiquement converties vers les types de champs DBF appropriés lors de l'enregistrement :

- Les **chaînes** sont mappées vers des champs de caractères (C).
- Les **valeurs numériques** (entiers et décimaux) sont mappées vers des champs numériques (N).
- Les **valeurs de date** sont mappées vers des champs de date (D) au format `YYYYMMDD`.
- Les **valeurs booléennes** sont mappées vers des champs logiques (L).

### Encodage

Les fichiers DBF peuvent utiliser différents encodages de caractères selon l'application qui les a créés. Aspose.Cells gère l'encodage de manière transparente dans la plupart des cas, mais si vous rencontrez des problèmes d'affichage des caractères, vous devrez peut-être vérifier l'encodage du fichier source.

### Règles de nommage des champs

Les noms de champs DBF doivent respecter les règles suivantes :

- Longueur maximale de 10 caractères.
- Doivent commencer par une lettre.
- Ne peuvent pas contenir d'espaces ni de caractères spéciaux.
- Stockés en majuscules quelle que soit la casse utilisée en entrée.

### Vérification du résultat

Après avoir écrit un fichier DBF, vous pouvez vérifier le résultat en l'ouvrant dans Microsoft Excel ou toute application compatible dBASE. Les données doivent apparaître dans une disposition tabulaire avec les noms de champs comme en-têtes de colonnes, et les enregistrements remplis selon les données que vous avez fournies.

## **Conversion entre DBF et d'autres formats**

L'un des cas d'utilisation les plus pratiques pour la lecture et l'écriture de fichiers DBF avec Aspose.Cells est la conversion de données entre le format DBF et des formats de tableurs modernes tels que XLSX, XLS ou CSV. Puisqu'Aspose.Cells prend en charge une large gamme de formats, vous pouvez facilement charger un fichier DBF et le réenregistrer dans tout autre format pris en charge, ou vice versa.

Par exemple, vous pouvez lire un fichier DBF, appliquer une mise en forme ou des calculs à l'aide de l'API Aspose.Cells, puis enregistrer le résultat sous forme de fichier XLSX pour distribution aux utilisateurs qui travaillent avec des applications de tableurs modernes. Inversement, vous pouvez extraire des données d'un fichier XLSX ou CSV et les exporter au format DBF pour intégration avec des systèmes hérités.



{{< app/cells/assistant language="java" >}}