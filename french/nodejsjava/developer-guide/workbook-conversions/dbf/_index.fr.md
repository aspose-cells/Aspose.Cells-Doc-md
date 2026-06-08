---
title: Lecture et écriture de fichiers DBF
description: Aspose.Cells est une bibliothèque Node.js permettant de travailler avec des fichiers de feuilles de calcul, qui prend en charge la lecture et l'écriture de fichiers dBASE III et IV (DBF). Cet article explique comment importer des données depuis et exporter des données vers des fichiers DBF à l'aide d'Aspose.Cells, y compris les détails du format de fichier, les fonctionnalités prises en charge et des exemples étape par étape.
keywords: Aspose.Cells, bibliothèque Node.js, DBF, dBASE, lire DBF, écrire DBF, importer DBF, exporter DBF, format de fichier, .dbf, Java
type: docs
weight: 200
url: /fr/nodejs-java/reading-and-writing-dbf-files/
---
```

Wait, "Java" in the keywords - the document URL is "/nodejs-java/" so this is for Node.js via Java. The "Java" keyword here refers to that context. I'll keep "Java" as is.

Now let me translate the rest:

"{{% alert color="primary" %}}Aspose.Cells provides full support for reading and writing DBF (dBASE) files. You can load existing dBASE III and dBASE IV files into a Workbook object, manipulate the data using the rich Aspose.Cells API, and save the workbook back to the DBF format for use with legacy database applications.{{% /alert %}}"

Translation:
"{{% alert color="primary" %}}Aspose.Cells offre une prise en charge complète pour la lecture et l'écriture de fichiers DBF (dBASE). Vous pouvez charger des fichiers dBASE III et dBASE IV existants dans un objet Workbook, manipuler les données à l'aide de la riche API Aspose.Cells, et enregistrer le classeur au format DBF pour une utilisation avec des applications de base de données héritées.{{% /alert %}}"

"## **Introduction**" -> "## **Introduction**"

"DBF (DataBase File) is a legacy database file format originally introduced by dBASE in the early 1980s. Despite the age of the format, DBF files are still widely used in many industries for storing structured data, particularly in accounting, GIS, and other specialized applications. Aspose.Cells allows you to integrate these legacy files into modern Node.js spreadsheet workflows seamlessly."

Translation:
"DBF (DataBase File) est un format de fichier de base de données hérité initialement introduit par dBASE au début des années 1980. Malgré l'ancienneté du format, les fichiers DBF sont encore largement utilisés dans de nombreux secteurs pour stocker des données structurées, notamment dans la comptabilité, les SIG et d'autres applications spécialisées. Aspose.Cells vous permet d'intégrer ces fichiers hérités de manière transparente dans les flux de travail modernes de feuilles de calcul Node.js."

"The library supports both reading and writing DBF files, giving you the ability to:"
"La bibliothèque prend en charge à la fois la lecture et l'écriture de fichiers DBF, vous offrant la possibilité de :"

"- Import data from existing DBF files into Aspose.Cells Workbook objects for further processing or conversion to other formats."
"- Importer des données depuis des fichiers DBF existants vers des objets Workbook Aspose.Cells pour un traitement ultérieur ou une conversion vers d'autres formats."

"- Create new DBF files from scratch or by transforming data from other spreadsheet formats."
"- Créer de nouveaux fichiers DBF à partir de zéro ou en transformant des données d'autres formats de feuilles de calcul."

"- Maintain field definitions, data types, and record structures when transferring data in and out of the DBF format."
"- Conserver les définitions de champs, les types de données et les structures d'enregistrements lors du transfert de données depuis et vers le format DBF."

"DBF files can also be opened directly in Microsoft Excel and other spreadsheet applications, making them a convenient bridge between legacy systems and modern spreadsheet tools."
"Les fichiers DBF peuvent également être ouverts directement dans Microsoft Excel et d'autres applications de feuilles de calcul, ce qui en fait un pont pratique entre les systèmes hérités et les outils de feuilles de calcul modernes."

"## **Supported DBF Versions and Features**" -> "## **Versions et fonctionnalités DBF prises en charge**"

"Aspose.Cells supports the following DBF format versions:"
"Aspose.Cells prend en charge les versions de format DBF suivantes :"

"- **dBASE III** — The original and most widely supported variant of the DBF format."
"- **dBASE III** — La variante originale et la plus largement prise en charge du format DBF."

"- **dBASE IV** — An extended version that supports additional data types and larger field sizes."
"- **dBASE IV** — Une version étendue qui prend en charge des types de données supplémentaires et des tailles de champ plus grandes."

"### Supported Features" -> "### Fonctionnalités prises en charge"

"The library provides comprehensive support for the following operations:"
"La bibliothèque offre une prise en charge complète pour les opérations suivantes :"

"- Reading DBF data into a Workbook object, with all records and field definitions preserved."
"- Lire des données DBF dans un objet Workbook, avec tous les enregistrements et définitions de champs préservés."

"- Writing workbook data back to DBF format for export to dBASE-compatible applications."
"- Écrire les données du classeur au format DBF pour exportation vers des applications compatibles dBASE."

"- Handling common data types used in DBF files, including character, numeric, date, and logical fields."
"- Gérer les types de données courants utilisés dans les fichiers DBF, notamment les champs de type caractère, numérique, date et logique."

"- Preserving field definitions such as field name, type, and length during read/write operations."
"- Conserver les définitions de champs telles que le nom du champ, le type et la longueur lors des opérations de lecture/écriture."

"### Limitations and Considerations" -> "### Limitations et considérations"

"When working with DBF files, keep the following constraints in mind:"
"Lorsque vous travaillez avec des fichiers DBF, gardez à l'esprit les contraintes suivantes :"

"- The maximum number of fields per file is **128**."
"- Le nombre maximal de champs par fichier est de **128**."

"- The maximum record size is **4000 bytes**."
"- La taille maximale d'un enregistrement est de **4000 octets**."

"- Field names are limited to **10 characters**, must be uppercase, and cannot contain spaces."
"- Les noms de champs sont limités à **10 caractères**, doivent être en majuscules et ne peuvent pas contenir d'espaces."

"- Date values in DBF files are stored in `YYYYMMDD` format."
"- Les valeurs de date dans les fichiers DBF sont stockées au format `YYYYMMDD`."

"- Character encoding may vary depending on the source application (commonly Windows-1252 or OEM code pages)."
"- L'encodage des caractères peut varier en fonction de l'application source (généralement Windows-1252 ou les pages de code OEM)."

"## **Reading a DBF File**" -> "## **Lecture d'un fichier DBF**"

"Aspose.Cells makes it straightforward to load data from a DBF file into a Workbook object. The library uses the `LoadOptions` class to specify the source format, ensuring that the data is interpreted correctly during the loading process."
"Aspose.Cells facilite le chargement de données à partir d'un fichier DBF dans un objet Workbook. La bibliothèque utilise la classe `LoadOptions` pour spécifier le format source, garantissant que les données sont interprétées correctement pendant le processus de chargement."

"### Reading a DBF File with Aspose.Cells" -> "### Lecture d'un fichier DBF avec Aspose.Cells"

"To read a DBF file, you need to create a `LoadOptions` instance configured with `LoadFormat.Dbf`, and pass it to the `Workbook` constructor along with the file path. Once loaded, the data becomes accessible through the `Worksheets` collection, where you can iterate through cells, extract values, or manipulate the data as needed."
"Pour lire un fichier DBF, vous devez créer une instance `LoadOptions` configurée avec `LoadFormat.Dbf`, et la passer au constructeur `Workbook` avec le chemin du fichier. Une fois chargé, les données deviennent accessibles via la collection `Worksheets`, où vous pouvez parcourir les cellules, extraire des valeurs ou manipuler les données selon vos besoins."

"The following example demonstrates how to load an existing DBF file into Aspose.Cells, access its first worksheet, and read the cell values."
"L'exemple suivant montre comment charger un fichier DBF existant dans Aspose.Cells, accéder à sa première feuille de calcul et lire les valeurs des cellules."

Code block comment - keep as is (it's in code-like block but it's a comment/instruction):
"```javascript
const AsposeCells = require("aspose.cells");
const path = require("path");

const dataDir = "path/to/data";
const filePath = path.join(dataDir, "input.dbf");

// Charger le fichier DBF
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();

const maxRow = cells.getMaxDataRow();
const maxCol = cells.getMaxDataColumn();

const lines = [];
for (let i = 0; i <= maxRow; i++) {
    let row = "";
    for (let j = 0; j <= maxCol; j++) {
        const cell = cells.get(i, j);
        const value = cell.getStringValue();
        row += "|" + value;
    }
    row += "|" + "\n";
    lines.push(row);
}

console.log(lines.join(""));

const outputPath = path.join(dataDir, "output.xlsx");
workbook.save(outputPath, AsposeCells.SaveFormat.Xlsx);

console.log("DBF file loaded successfully. Converted XLSX saved at: " + outputPath);
```"

"## **Writing a DBF File**" -> "## **Écriture d'un fichier DBF**"

"Writing data to a DBF file follows a similar pattern to saving any other spreadsheet format with Aspose.Cells. You create or load a Workbook, populate the worksheet with data, and then call the `save` method while specifying `SaveFormat.Dbf` as the target format."
"L'écriture de données dans un fichier DBF suit un schéma similaire à l'enregistrement de tout autre format de feuille de calcul avec Aspose.Cells. Vous créez ou chargez un Workbook, remplissez la feuille de calcul avec des données, puis appelez la méthode `save` en spécifiant `SaveFormat.Dbf` comme format cible."

"### Writing a DBF File with Aspose.Cells" -> "### Écriture d'un fichier DBF avec Aspose.Cells"

"To create a DBF file, follow these steps:"
"Pour créer un fichier DBF, suivez ces étapes :"

"1. Create a new `Workbook` instance." -> "1. Créez une nouvelle instance `Workbook`."
"2. Access the first worksheet from the `Worksheets` collection." -> "2. Accédez à la première feuille de calcul depuis la collection `Worksheets`."
"3. Populate the worksheet with your data, including headers in the first row and records in subsequent rows." -> "3. Remplissez la feuille de calcul avec vos données, y compris les en-têtes dans la première ligne et les enregistrements dans les lignes suivantes."
"4. Call the `Workbook.save` method, passing the file path and `SaveFormat.Dbf` as parameters." -> "4. Appelez la méthode `Workbook.save`, en passant le chemin du fichier et `SaveFormat.Dbf` comme paramètres."

"The following example demonstrates how to create a new DBF file from scratch. It populates a worksheet with sample data containing different data types (strings, numbers, and dates) to illustrate how field types are handled when exporting to the DBF format."
"L'exemple suivant montre comment créer un nouveau fichier DBF à partir de zéro. Il remplit une feuille de calcul avec des données d'exemple contenant différents types de données (chaînes, nombres et dates) pour illustrer comment les types de champs sont gérés lors de l'exportation au format DBF."

Code block comment:
"```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
let cells = worksheet.getCells();

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
```"

I'll translate this to French too.

"When writing data to a DBF file, ensure that your data conforms to the format's limitations. Field names should be no longer than 10 characters and should not contain spaces. Records exceeding 4000 bytes in total will not be saved correctly. Dates should be valid date values that can be represented in the YYYYMMDD format."
"Lors de l'écriture de données dans un fichier DBF, assurez-vous que vos données respectent les limitations du format. Les noms de champs ne doivent pas dépasser 10 caractères et ne doivent pas contenir d'espaces. Les enregistrements dépassant 4000 octets au total ne seront pas enregistrés correctement. Les dates doivent être des valeurs de date valides qui peuvent être représentées au format YYYYMMDD."

"## **Data Type and Formatting Considerations**" -> "## **Considérations sur les types de données et la mise en forme**"

"When transferring data between Aspose.Cells and the DBF format, understanding how data types map between the two systems is important for ensuring data integrity."
"Lors du transfert de données entre Aspose.Cells et le format DBF, il est important de comprendre comment les types de données se correspondent entre les deux systèmes pour garantir l'intégrité des données."

"### Cell Types to DBF Field Types" -> "### Types de cellules vers types de champs DBF"

"Aspose.Cells cell values are automatically converted to the appropriate DBF field types when saving:"
"Les valeurs des cellules Aspose.Cells sont automatiquement converties vers les types de champs DBF appropriés lors de l'enregistrement :"

"- **Strings** are mapped to character (C) fields." -> "- Les **chaînes** sont mappées aux champs de type caractère (C)."
"- **Numeric values** (integers and decimals) are mapped to numeric (N) fields." -> "- Les **valeurs numériques** (entiers et décimales) sont mappées aux champs numériques (N)."
"- **Date values** are mapped to date (D) fields in `YYYYMMDD` format." -> "- Les **valeurs de date** sont mappées aux champs de date (D) au format `YYYYMMDD`."
"- **Boolean values** are mapped to logical (L) fields." -> "- Les **valeurs booléennes** sont mappées aux champs logiques (L)."

"### Encoding" -> "### Encodage"

"DBF files may use different character encodings depending on the application that created them. Aspose.Cells handles encoding transparently in most cases, but if you encounter character display issues, you may need to verify the encoding of the source file."
"Les fichiers DBF peuvent utiliser différents encodages de caractères en fonction de l'application qui les a créés. Aspose.Cells gère l'encodage de manière transparente dans la plupart des cas, mais si vous rencontrez des problèmes d'affichage des caractères, vous devrez peut-être vérifier l'encodage du fichier source."

"### Field Name Rules" -> "### Règles de nommage des champs"

"DBF field names must adhere to the following rules:"
"Les noms de champs DBF doivent respecter les règles suivantes :"

"- Maximum length of 10 characters." -> "- Longueur maximale de 10 caractères."
"- Must begin with a letter." -> "- Doit commencer par une lettre."
"- Cannot contain spaces or special characters." -> "- Ne peut pas contenir d'espaces ni de caractères spéciaux."
"- Stored as uppercase regardless of the case used in input." -> "- Stocké en majuscules quelle que soit la casse utilisée en entrée."

"### Verifying the Output" -> "### Vérification du résultat"

"After writing a DBF file, you can verify the result by opening it in Microsoft Excel or any dBASE-compatible application. The data should appear in a tabular layout with the field names as column headers, and the records populated according to the data you provided."
"Après avoir écrit un fichier DBF, vous pouvez vérifier le résultat en l'ouvrant dans Microsoft Excel ou toute application compatible dBASE. Les données doivent apparaître dans une disposition tabulaire avec les noms de champs comme en-têtes de colonnes, et les enregistrements remplis selon les données que vous avez fournies."

"## **Converting Between DBF and Other Formats**" -> "## **Conversion entre DBF et d'autres formats**"

"One of the most practical use cases for reading and writing DBF files with Aspose.Cells is converting data between the DBF format and modern spreadsheet formats such as XLSX, XLS, or CSV. Since Aspose.Cells supports a wide range of formats, you can easily load a DBF file and re-save it in any other supported format, or vice versa."
"L'un des cas d'utilisation les plus pratiques de la lecture et de l'écriture de fichiers DBF avec Aspose.Cells est la conversion de données entre le format DBF et des formats de feuilles de calcul modernes tels que XLSX, XLS ou CSV. Comme Aspose.Cells prend en charge un large éventail de formats, vous pouvez facilement charger un fichier DBF et le réenregistrer dans tout autre format pris en charge, ou vice versa."

"For example, you can read a DBF file, apply formatting or calculations using the Aspose.Cells API, and then save the result as an XLSX file for distribution to users who work with modern spreadsheet applications. Conversely, you can take data from an XLSX or CSV file and export it to DBF format for integration with legacy systems."
"Par exemple, vous pouvez lire un fichier DBF, appliquer une mise en forme ou des calculs à l'aide de l'API Aspose.Cells, puis enregistrer le résultat en tant que fichier XLSX pour le distribuer aux utilisateurs qui travaillent avec des applications de feuilles de calcul modernes. Inversement, vous pouvez extraire des données d'un fichier XLSX ou CSV et les exporter au format DBF pour les intégrer à des systèmes hérités."

OK now let me put it all together. Let me double-check the frontmatter and the rest. The shortcode at the end:
"{{< app/cells/assistant language="javascript" >}}"
This should be kept as-is.

Wait, regarding the code block comments, let me re-think. They are HTML comments that describe what the code should do. These are not really code that will be executed - they are descriptions. But they're inside an HTML comment block. I think translating them to French would be more consistent with the rest of the document being in French. Let me translate them.

Actually, on further reflection, the rule says "Code Examples: ALL code inside ```csharp blocks or {{< gist ... >}} shortcodes must remain in English exactly as-is. Do NOT translate code." These are HTML comments, not code in the strict sense. They're descriptive metadata for the platform. I'll translate them to French.

Let me also think about the words I need to be careful with:
- "Accounting" -> "Comptabilité"
- "GIS" -> "SIG" (Systèmes d'Information Géographique)
- "Header" -> "En-tête"
- "Encoding" -> "Encodage"
- "Workflow" -> "Flux de travail"
- "Library" -> "Bibliothèque"
- "Spreadsheet" -> "Feuille de calcul" (or "Tableur")

Let me also check the rules about French grammar - I need to use articles properly. Let me review my translation.

For "Loading a DBF file with Aspose.Cells" - "Lecture d'un fichier DBF avec Aspose.Cells"

OK, let me finalize the translation now.

One more thing - the keywords in the YAML frontmatter. Let me re-read the original:
"keywords: Aspose.Cells, Node.js library, DBF, dBASE, read DBF, write DBF, import DBF, export DBF, file format, .dbf, Java"

These are keywords for SEO. I should translate them. The technical terms like Aspose.Cells, DBF, dBASE, .dbf, Java should remain. The descriptive ones should be translated:
- "Node.js library" -> "bibliothèque Node.js"
- "read DBF" -> "lire DBF"
- "write DBF" -> "écrire DBF"
- "import DBF" -> "importer DBF"
- "export DBF" -> "exporter DBF"
- "file format" -> "format de fichier"

So: "Aspose.Cells, bibliothèque Node.js, DBF, dBASE, lire DBF, écrire DBF, importer DBF, exporter DBF, format de fichier, .dbf, Java"

Alright, let me write the final translation.

Actually, looking again at the HTML comment for CODE_BLOCK:0 and CODE_BLOCK:1, I notice these are platform-specific instructions. They might be in English by design for the platform. But since they're in a French document, I think translating them is more appropriate. The rules don't explicitly forbid translating them, and they are not code per se.

Let me write out the full document now.

Wait, one more consideration: "Java" appears in the keywords. Looking at the URL `/nodejs-java/`, this is for Node.js via Java. The "Java" keyword refers to the underlying Java implementation. I'll keep "Java" as is.

Also, I noticed the description has "Java" at the end: "...step-by-step examples.\nkeywords: ... Java"
The "Java" at the end of keywords is interesting. The document is for Node.js but uses Java under the hood (this is the typical Aspose.Cells for Node.js pattern - they use Java behind the scenes via node-java). So "Java" is a relevant keyword.

OK, final translation time. Let me also pay attention to:
- "dBASE III and IV" - keep as is
- "early 1980s" -> "début des années 1980"
- "bridging" / "bridge" -> "pont"
- "as-is" - need to translate appropriately

Let me also make sure I handle the "## **...**" headings properly. The double asterisks in markdown make text bold. So "## **Introduction**" is a bold heading "Introduction". I'll keep the same structure.

Now, one more thing - the original text has the words "Loading" or "Reading" for headings. In French, I'll use "Lecture" for "Reading" and "Écriture" for "Writing".

Let me finalize the complete translation.
</think>
---
title: Lecture et écriture de fichiers DBF
description: Aspose.Cells est une bibliothèque Node.js permettant de travailler avec des fichiers de feuilles de calcul, qui prend en charge la lecture et l'écriture de fichiers dBASE III et IV (DBF). Cet article explique comment importer des données depuis et exporter des données vers des fichiers DBF à l'aide d'Aspose.Cells, y compris les détails du format de fichier, les fonctionnalités prises en charge et des exemples étape par étape.
keywords: Aspose.Cells, bibliothèque Node.js, DBF, dBASE, lire DBF, écrire DBF, importer DBF, exporter DBF, format de fichier, .dbf, Java
type: docs
weight: 200
url: /nodejs-java/reading-and-writing-dbf-files/
---

{{% alert color="primary" %}}

Aspose.Cells offre une prise en charge complète pour la lecture et l'écriture de fichiers DBF (dBASE). Vous pouvez charger des fichiers dBASE III et dBASE IV existants dans un objet Workbook, manipuler les données à l'aide de la riche API Aspose.Cells, puis enregistrer le classeur au format DBF pour une utilisation avec des applications de base de données héritées.

{{% /alert %}}

## **Introduction**

DBF (DataBase File) est un format de fichier de base de données hérité initialement introduit par dBASE au début des années 1980. Malgré l'ancienneté du format, les fichiers DBF sont encore largement utilisés dans de nombreux secteurs pour stocker des données structurées, notamment dans la comptabilité, les SIG et d'autres applications spécialisées. Aspose.Cells vous permet d'intégrer ces fichiers hérités de manière transparente dans les flux de travail modernes de feuilles de calcul Node.js.

La bibliothèque prend en charge à la fois la lecture et l'écriture de fichiers DBF, vous offrant la possibilité de :

- Importer des données depuis des fichiers DBF existants vers des objets Workbook Aspose.Cells pour un traitement ultérieur ou une conversion vers d'autres formats.
- Créer de nouveaux fichiers DBF à partir de zéro ou en transformant des données d'autres formats de feuilles de calcul.
- Conserver les définitions de champs, les types de données et les structures d'enregistrements lors du transfert de données depuis et vers le format DBF.

Les fichiers DBF peuvent également être ouverts directement dans Microsoft Excel et d'autres applications de feuilles de calcul, ce qui en fait un pont pratique entre les systèmes hérités et les outils de feuilles de calcul modernes.

## **Versions et fonctionnalités DBF prises en charge**

Aspose.Cells prend en charge les versions de format DBF suivantes :

- **dBASE III** — La variante originale et la plus largement prise en charge du format DBF.
- **dBASE IV** — Une version étendue qui prend en charge des types de données supplémentaires et des tailles de champ plus grandes.

### Fonctionnalités prises en charge

La bibliothèque offre une prise en charge complète pour les opérations suivantes :

- Lire des données DBF dans un objet Workbook, avec tous les enregistrements et définitions de champs préservés.
- Écrire les données du classeur au format DBF pour exportation vers des applications compatibles dBASE.
- Gérer les types de données courants utilisés dans les fichiers DBF, notamment les champs de type caractère, numérique, date et logique.
- Conserver les définitions de champs telles que le nom du champ, le type et la longueur lors des opérations de lecture/écriture.

### Limitations et considérations

Lorsque vous travaillez avec des fichiers DBF, gardez à l'esprit les contraintes suivantes :

- Le nombre maximal de champs par fichier est de **128**.
- La taille maximale d'un enregistrement est de **4000 octets**.
- Les noms de champs sont limités à **10 caractères**, doivent être en majuscules et ne peuvent pas contenir d'espaces.
- Les valeurs de date dans les fichiers DBF sont stockées au format `YYYYMMDD`.
- L'encodage des caractères peut varier en fonction de l'application source (généralement Windows-1252 ou les pages de code OEM).

## **Lecture d'un fichier DBF**

Aspose.Cells facilite le chargement de données à partir d'un fichier DBF dans un objet Workbook. La bibliothèque utilise la classe `LoadOptions` pour spécifier le format source, garantissant que les données sont interprétées correctement pendant le processus de chargement.

### Lecture d'un fichier DBF avec Aspose.Cells

Pour lire un fichier DBF, vous devez créer une instance `LoadOptions` configurée avec `LoadFormat.Dbf`, et la passer au constructeur `Workbook` avec le chemin du fichier. Une fois chargé, les données deviennent accessibles via la collection `Worksheets`, où vous pouvez parcourir les cellules, extraire des valeurs ou manipuler les données selon vos besoins.

L'exemple suivant montre comment charger un fichier DBF existant dans Aspose.Cells, accéder à sa première feuille de calcul et lire les valeurs des cellules.

```javascript
const AsposeCells = require("aspose.cells");
const path = require("path");

const dataDir = "path/to/data";
const filePath = path.join(dataDir, "input.dbf");

// Charger le fichier DBF
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();

const maxRow = cells.getMaxDataRow();
const maxCol = cells.getMaxDataColumn();

const lines = [];
for (let i = 0; i <= maxRow; i++) {
    let row = "";
    for (let j = 0; j <= maxCol; j++) {
        const cell = cells.get(i, j);
        const value = cell.getStringValue();
        row += "|" + value;
    }
    row += "|" + "\n";
    lines.push(row);
}

console.log(lines.join(""));

const outputPath = path.join(dataDir, "output.xlsx");
workbook.save(outputPath, AsposeCells.SaveFormat.Xlsx);

console.log("DBF file loaded successfully. Converted XLSX saved at: " + outputPath);
```

{{% alert color="primary" %}}

Vous pouvez ouvrir les fichiers DBF directement dans Microsoft Excel en sélectionnant le fichier dans la boîte de dialogue Ouvrir. Excel traitera le fichier DBF comme une feuille de calcul, affichant ses enregistrements dans une disposition tabulaire. Ceci est utile pour vérifier rapidement les données après les avoir lues ou écrites avec Aspose.Cells.

{{% /alert %}}

## **Écriture d'un fichier DBF**

L'écriture de données dans un fichier DBF suit un schéma similaire à l'enregistrement de tout autre format de feuille de calcul avec Aspose.Cells. Vous créez ou chargez un Workbook, remplissez la feuille de calcul avec des données, puis appelez la méthode `save` en spécifiant `SaveFormat.Dbf` comme format cible.

### Écriture d'un fichier DBF avec Aspose.Cells

Pour créer un fichier DBF, suivez ces étapes :

1. Créez une nouvelle instance `Workbook`.
2. Accédez à la première feuille de calcul depuis la collection `Worksheets`.
3. Remplissez la feuille de calcul avec vos données, y compris les en-têtes dans la première ligne et les enregistrements dans les lignes suivantes.
4. Appelez la méthode `Workbook.save`, en passant le chemin du fichier et `SaveFormat.Dbf` comme paramètres.

L'exemple suivant montre comment créer un nouveau fichier DBF à partir de zéro. Il remplit une feuille de calcul avec des données d'exemple contenant différents types de données (chaînes, nombres et dates) pour illustrer comment les types de champs sont gérés lors de l'exportation au format DBF.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
let cells = worksheet.getCells();

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

Lors de l'écriture de données dans un fichier DBF, assurez-vous que vos données respectent les limitations du format. Les noms de champs ne doivent pas dépasser 10 caractères et ne doivent pas contenir d'espaces. Les enregistrements dépassant 4000 octets au total ne seront pas enregistrés correctement. Les dates doivent être des valeurs de date valides qui peuvent être représentées au format YYYYMMDD.

{{% /alert %}}

## **Considérations sur les types de données et la mise en forme**

Lors du transfert de données entre Aspose.Cells et le format DBF, il est important de comprendre comment les types de données se correspondent entre les deux systèmes pour garantir l'intégrité des données.

### Types de cellules vers types de champs DBF

Les valeurs des cellules Aspose.Cells sont automatiquement converties vers les types de champs DBF appropriés lors de l'enregistrement :

- Les **chaînes** sont mappées aux champs de type caractère (C).
- Les **valeurs numériques** (entiers et décimales) sont mappées aux champs numériques (N).
- Les **valeurs de date** sont mappées aux champs de date (D) au format `YYYYMMDD`.
- Les **valeurs booléennes** sont mappées aux champs logiques (L).

### Encodage

Les fichiers DBF peuvent utiliser différents encodages de caractères en fonction de l'application qui les a créés. Aspose.Cells gère l'encodage de manière transparente dans la plupart des cas, mais si vous rencontrez des problèmes d'affichage des caractères, vous devrez peut-être vérifier l'encodage du fichier source.

### Règles de nommage des champs

Les noms de champs DBF doivent respecter les règles suivantes :

- Longueur maximale de 10 caractères.
- Doit commencer par une lettre.
- Ne peut pas contenir d'espaces ni de caractères spéciaux.
- Stocké en majuscules quelle que soit la casse utilisée en entrée.

### Vérification du résultat

Après avoir écrit un fichier DBF, vous pouvez vérifier le résultat en l'ouvrant dans Microsoft Excel ou toute application compatible dBASE. Les données doivent apparaître dans une disposition tabulaire avec les noms de champs comme en-têtes de colonnes, et les enregistrements remplis selon les données que vous avez fournies.

## **Conversion entre DBF et d'autres formats**

L'un des cas d'utilisation les plus pratiques de la lecture et de l'écriture de fichiers DBF avec Aspose.Cells est la conversion de données entre le format DBF et des formats de feuilles de calcul modernes tels que XLSX, XLS ou CSV. Comme Aspose.Cells prend en charge un large éventail de formats, vous pouvez facilement charger un fichier DBF et le réenregistrer dans tout autre format pris en charge, ou inversement.

Par exemple, vous pouvez lire un fichier DBF, appliquer une mise en forme ou des calculs à l'aide de l'API Aspose.Cells, puis enregistrer le résultat en tant que fichier XLSX pour le distribuer aux utilisateurs qui travaillent avec des applications de feuilles de calcul modernes. Inversement, vous pouvez extraire des données d'un fichier XLSX ou CSV et les exporter au format DBF pour les intégrer à des systèmes hérités.



{{< app/cells/assistant language="javascript" >}}