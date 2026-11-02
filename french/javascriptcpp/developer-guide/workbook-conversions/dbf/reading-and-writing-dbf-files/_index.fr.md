---
title: Lecture et écriture de fichiers DBF
linktitle: Lecture et écriture de fichiers DBF
description: Aspose.Cells est une bibliothèque JavaScript via C++ permettant de traiter des fichiers de feuille de calcul. Elle prend en charge la lecture et l’écriture de fichiers dBASE III et IV (DBF). Cet article explique comment importer des données depuis des fichiers DBF et exporter des données vers ces fichiers à l’aide d’Aspose.Cells, en abordant les détails du format de fichier, les fonctionnalités prises en charge et des exemples pas à pas.
keywords: Aspose.Cells, bibliothèque JavaScript via C++, DBF, dBASE, lire DBF, écrire DBF, importer DBF, exporter DBF, format de fichier, .dbf
type: docs
weight: 200
url: /fr/javascript-cpp/reading-and-writing-dbf-files/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells prend entièrement en charge la lecture et l’écriture de fichiers DBF (dBASE). Vous pouvez charger des fichiers dBASE III et dBASE IV existants dans un objet Workbook, manipuler les données à l’aide de l’API Aspose.Cells, riche en fonctionnalités, puis enregistrer le classeur au format DBF afin de l’utiliser avec des applications de base de données héritées.
{{% /alert %}}

## **Introduction**
Le format DBF (DataBase File) est un ancien format de base de données mis au point à l’origine par dBASE au début des années 1980. Malgré l’âge de ce format, les fichiers DBF restent largement utilisés dans de nombreux secteurs pour stocker des données structurées, notamment dans la comptabilité, les SIG et d’autres applications spécialisées. Aspose.Cells vous permet d’intégrer fluement ces fichiers hérités aux flux de travail modernes de traitement des feuilles de calcul.
La bibliothèque prend en charge la lecture et l’écriture de fichiers DBF, ce qui vous permet de :
- Importer des données depuis des fichiers DBF existants dans des objets Workbook d’Aspose.Cells, en vue de leur traitement ultérieur ou de leur conversion vers d’autres formats.
- Créer de nouveaux fichiers DBF à partir de zéro ou en transformant des données provenant d’autres formats de feuille de calcul.
- Conserver les définitions de champs, les types de données et les structures d’enregistrements lors des transferts de données depuis et vers le format DBF.
Les fichiers DBF peuvent également être ouverts directement dans Microsoft Excel et dans d’autres applications de gestion des feuilles de calcul, ce qui fait d’eux un pont pratique entre les systèmes hérités et les outils modernes de gestion des feuilles de calcul.

## **Versions et fonctionnalités DBF prises en charge**
Aspose.Cells prend en charge les versions suivantes du format DBF :
- **dBASE III** — La variante originale et la plus largement prise en charge du format DBF.
- **dBASE IV** — Une version étendue qui prend en charge des types de données supplémentaires et des tailles de champ plus importantes.

### Fonctionnalités prises en charge
La bibliothèque fournit une prise en charge complète des opérations suivantes :
- Lire des données DBF dans un objet Workbook, en conservant tous les enregistrements et toutes les définitions de champs.
- Écrire les données du classeur au format DBF pour les exporter vers des applications compatibles avec dBASE.
- Traiter les types de données courants utilisés dans les fichiers DBF, notamment les champs de type caractère, numérique, date et logique.
- Conserver les définitions de champs, telles que le nom, le type et la longueur du champ, pendant les opérations de lecture et d’écriture.

### Limites et considérations
Lors de l’utilisation de fichiers DBF, tenez compte des contraintes suivantes :
- Le nombre maximal de champs par fichier est de **128**.
- La taille maximale d’un enregistrement est de **4000 octets**.
- Les noms de champs sont limités à **10 caractères**, doivent être en majuscules et ne peuvent pas contenir d’espaces.
- Les valeurs de date des fichiers DBF sont stockées au format `YYYYMMDD`.
- L’encodage des caractères peut varier selon l’application source (généralement Windows-1252 ou des pages de code OEM).

## **Lecture d’un fichier DBF**
Aspose.Cells simplifie le chargement des données d’un fichier DBF dans un objet Workbook. La bibliothèque utilise la classe `LoadOptions` pour spécifier le format source, ce qui garantit une interprétation correcte des données lors du chargement.

### Lecture d’un fichier DBF avec Aspose.Cells
Pour lire un fichier DBF, vous devez créer une instance de `LoadOptions`, définir sa propriété `loadFormat` sur `LoadFormat.Dbf`, puis la transmettre au constructeur `Workbook` avec le chemin du fichier. Une fois chargé, les données sont accessibles via la collection `Worksheets`, où vous pouvez parcourir les cellules, extraire les valeurs ou manipuler les données selon vos besoins.
L’exemple suivant montre comment charger un fichier DBF existant à l’aide d’Aspose.Cells, accéder à sa première feuille de calcul et lire les valeurs des cellules.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".dbf" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select a DBF file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const fileData = new Uint8Array(await file.arrayBuffer());
                const loadOptions = new LoadOptions(AsposeCells.LoadFormat.Dbf);
                const workbook = new Workbook(fileData, loadOptions);
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                const maxRow = cells.maxDataRow;
                const maxCol = cells.maxDataColumn;
                const lines = [];
                for (let i = 0; i <= maxRow; i++) {
                    let line = "";
                    for (let j = 0; j <= maxCol; j++) {
                        const cell = cells.get(i, j);
                        const value = cell.stringValue;
                        line += "|" + value;
                    }
                    line += "|";
                    lines.push(line);
                }
                const output = document.createElement('pre');
                output.textContent = lines.join("\n");
                result.replaceChildren(output);
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                const message = document.createElement('p');
                message.style.color = "green";
                message.textContent = "DBF file loaded successfully. Converted XLSX saved as output.xlsx.";
                result.appendChild(message);
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

{{% alert color="primary" %}}
Vous pouvez ouvrir des fichiers DBF directement dans Microsoft Excel en sélectionnant le fichier dans la boîte de dialogue Ouvrir. Excel traitera le fichier DBF comme une feuille de calcul et affichera ses enregistrements sous forme de tableau. Cette méthode est utile pour vérifier rapidement les données après leur lecture ou leur écriture avec Aspose.Cells.
{{% /alert %}}

## **Écriture d’un fichier DBF**
L’écriture de données dans un fichier DBF suit un processus similaire à celui de l’enregistrement d’un classeur dans n’importe quel autre format de feuille de calcul avec Aspose.Cells. Vous créez ou chargez un objet Workbook, remplissez la feuille de calcul de données, puis appelez la méthode `save` en spécifiant `SaveFormat.Dbf` comme format cible.

### Écriture d’un fichier DBF avec Aspose.Cells
Pour créer un fichier DBF, procédez comme suit :
1. Créez une nouvelle instance de `Workbook`.
2. Accédez à la première feuille de calcul de la collection `Worksheets`.
3. Remplissez la feuille de calcul avec vos données, notamment les en-têtes dans la première ligne et les enregistrements dans les lignes suivantes.
4. Appelez la méthode `Workbook.save`, en transmettant le chemin du fichier et `SaveFormat.Dbf` comme paramètres.
L’exemple suivant montre comment créer un nouveau fichier DBF à partir de zéro. Il remplit une feuille de calcul avec des données d’exemple de différents types (chaînes, nombres et dates) afin d’illustrer la gestion des types de champs lors de l’exportation au format DBF.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            // En-têtes de colonnes
            cells.get(0, 0).value = "ID";
            cells.get(0, 1).value = "Name";
            cells.get(0, 2).value = "Department";
            cells.get(0, 3).value = "Salary";
            cells.get(0, 4).value = "HireDate";
            // Ligne de données 1
            cells.get(1, 0).value = 101;
            cells.get(1, 1).value = "John Smith";
            cells.get(1, 2).value = "Engineering";
            cells.get(1, 3).value = 75000.50;
            cells.get(1, 4).value = new Date(2020, 2, 15);
            // Ligne de données 2
            cells.get(2, 0).value = 102;
            cells.get(2, 1).value = "Jane Doe";
            cells.get(2, 2).value = "Marketing";
            cells.get(2, 3).value = 68000.75;
            cells.get(2, 4).value = new Date(2019, 6, 22);
            // Ligne de données 3
            cells.get(3, 0).value = 103;
            cells.get(3, 1).value = "Bob Johnson";
            cells.get(3, 2).value = "Finance";
            cells.get(3, 3).value = 82000.00;
            cells.get(3, 4).value = new Date(2021, 0, 10);
            // Ligne de données 4
            cells.get(4, 0).value = 104;
            cells.get(4, 1).value = "Alice Brown";
            cells.get(4, 2).value = "Human Resources";
            cells.get(4, 3).value = 71000.25;
            cells.get(4, 4).value = new Date(2018, 10, 5);
            // Ligne de données 5
            cells.get(5, 0).value = 105;
            cells.get(5, 1).value = "Charlie Wilson";
            cells.get(5, 2).value = "Operations";
            cells.get(5, 3).value = 79500.80;
            cells.get(5, 4).value = new Date(2022, 4, 30);
            // Définir les largeurs des colonnes pour une meilleure lisibilité
            cells.setColumnWidth(0, 8);
            cells.setColumnWidth(1, 20);
            cells.setColumnWidth(2, 20);
            cells.setColumnWidth(3, 12);
            cells.setColumnWidth(4, 14);
            const outputData = workbook.save(AsposeCells.SaveFormat.Dbf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.dbf";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
Lors de l’écriture de données dans un fichier DBF, veillez à ce que vos données respectent les limitations du format. Les noms de champs doivent être composés d’au plus 10 caractères et ne doivent pas contenir d’espaces. Les enregistrements dont la taille totale dépasse 4000 octets ne seront pas correctement enregistrés. Les dates doivent être valides et pouvoir être représentées au format YYYYMMDD.
{{% /alert %}}

## **Considérations relatives aux types de données et à la mise en forme**
Lors du transfert de données entre Aspose.Cells et le format DBF, il est important de comprendre la correspondance des types de données entre les deux systèmes afin de garantir l’intégrité des données.

### Conversion des types de cellules en types de champs DBF
Les valeurs stockées dans les cellules sont automatiquement converties en types de champs DBF appropriés lors de l’enregistrement :
- **Les chaînes** sont associées à des champs de type caractère (C).
- **Les valeurs numériques** (nombres entiers et décimaux) sont associées à des champs numériques (N).
- **Les valeurs de date** sont associées à des champs de type date (D) au format `YYYYMMDD`.
- **Les valeurs booléennes** sont associées à des champs de type logique (L).

### Encodage
Les fichiers DBF peuvent utiliser différents encodages de caractères selon l’application qui les a créés. Aspose.Cells gère automatiquement l’encodage dans la plupart des cas, mais si vous rencontrez des problèmes d’affichage des caractères, vous devrez peut-être vérifier l’encodage du fichier source.

### Règles relatives aux noms de champs
Les noms de champs DBF doivent respecter les règles suivantes :
- Longueur maximale de 10 caractères.
- Doivent commencer par une lettre.
- Ne peuvent contenir ni espaces ni caractères spéciaux.
- Sont stockés en majuscules, indépendamment de la casse utilisée lors de la saisie.

### Vérification du résultat
Après avoir écrit un fichier DBF, vous pouvez vérifier le résultat en l’ouvrant dans Microsoft Excel ou toute application compatible avec dBASE. Les données doivent apparaître sous forme de tableau, avec les noms de champs comme en-têtes de colonnes et les enregistrements renseignés conformément aux données fournies.

## **Conversion entre DBF et d’autres formats**
Parmi les cas d’utilisation les plus pratiques de la lecture et de l’écriture de fichiers DBF avec Aspose.Cells figure la conversion de données entre le format DBF et des formats modernes de feuilles de calcul tels que XLSX, XLS ou CSV. Comme Aspose.Cells prend en charge un large éventail de formats, vous pouvez charger un fichier DBF puis l’enregistrer dans n’importe quel autre format pris en charge, ou effectuer l’opération inverse.

{{< app/cells/assistant language="javascript-cpp" >}}