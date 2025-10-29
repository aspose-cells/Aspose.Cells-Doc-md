---
title: Configuration des polices pour le rendu des feuilles de calcul avec JavaScript via C++
linktitle: Configuration des polices pour le rendu des feuilles de calcul
type: docs
weight: 10
url: /fr/javascript-cpp/configuring-fonts-for-rendering-spreadsheets/
description: Apprenez à configurer les polices pour le rendu des feuilles de calcul en utilisant Aspose.Cells for JavaScript via C++. Assurez vous que les polices sont disponibles pour une conversion optimale.
---

## **Scénarios d'utilisation possibles**

Les API Aspose.Cells offrent la possibilité de rendre les feuilles de calcul en formats image ainsi que de les convertir en formats PDF et XPS. Pour maximiser la fidélité de la conversion, il est nécessaire que les polices utilisées dans la feuille de calcul soient disponibles dans le répertoire par défaut des polices du système d'exploitation. Si les polices requises ne sont pas présentes, les API Aspose.Cells tenteront de les remplacer par celles disponibles.

## **Sélection des polices**

Voici le processus suivi par les API Aspose.Cells en arrière-plan.

1. L'API tente de trouver les polices sur le système de fichiers correspondant exactement au nom de police utilisé dans la feuille de calcul.
1. Si l'API ne parvient pas à trouver les polices portant le même nom exact, elle tente d'utiliser la police par défaut spécifiée dans la propriété [**DefaultStyle.font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) du classeur.
1. Si l'API ne parvient pas à localiser la police définie dans la propriété [**DefaultStyle.font**](https://reference.aspose.com/cells/javascript-cpp/style/#font--) du classeur, elle tente d'utiliser la police spécifiée dans la propriété [**PdfSaveOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#defaultFont--) ou [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--).
1. Si l'API ne parvient pas à localiser la police définie dans [**PdfSaveOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#defaultFont--) ou [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--), elle tente d'utiliser la police spécifiée dans [**FontConfigs.defaultFontName**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#defaultFontName--).
1. Si l'API ne parvient pas à localiser la police définie dans [**FontConfigs.defaultFontName**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#defaultFontName--), elle tente de sélectionner les polices les plus adaptées parmi toutes les polices disponibles.
1. Enfin, si l'API ne trouve pas de polices sur le système de fichiers, elle rend la feuille de calcul en utilisant Arial.

## **Définir des dossiers de polices personnalisés**

Les API Aspose.Cells recherchent dans le répertoire par défaut des polices du système d'exploitation les polices requises. Si celles-ci ne sont pas disponibles dans le répertoire, les API recherchent dans les répertoires personnalisés (définis par l'utilisateur). La classe [**FontConfigs**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs) offre plusieurs méthodes pour définir des répertoires de polices personnalisés, comme détaillé ci-dessous.

1. [**FontConfigs.fontFolder(string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolder-string-boolean-): Cette méthode est utile s'il n'y a qu'un seul dossier à définir.
1. [**FontConfigs.fontFolders(string[], boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolders-stringarray-boolean-): Cette méthode est utile lorsque les polices résident dans des dossiers multiples et que l'utilisateur souhaite définir tous les dossiers séparément plutôt que de combiner toutes les polices dans un seul dossier.
1. [**FontConfigs.fontSources(FontSourceBase[])**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources-fontsourcebasearray-): Ce mécanisme est utile lorsque l'utilisateur souhaite charger des polices à partir de dossiers multiples ou d'un seul fichier de police ou de données de police à partir d'un tableau d'octets.

{{% alert color="primary" %}}

Les deux méthodes [**FontConfigs.fontFolder(string, boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolder-string-boolean-) et [**FontConfigs.fontFolders(string[], boolean)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontFolders-stringarray-boolean-) acceptent un deuxième paramètre de type Boolean. Passer **true** en tant que deuxième paramètre dirigera les API Aspose.Cells pour rechercher les sous-dossiers des fichiers de polices.

{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Font Configuration Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Font Configuration Example</h1>
        <p>Select an Excel file (optional) and font resources to configure Aspose.Cells font sources in the browser.</p>

        <label>Excel File (optional):</label>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <br/><br/>

        <label>Font File (.ttf/.otf) (optional):</label>
        <input type="file" id="fontFileInput" accept=".ttf,.otf" />
        <br/><br/>

        <label>Font Folder (optional, select a folder):</label>
        <input type="file" id="fontFolderInput" webkitdirectory directory multiple />
        <br/><br/>

        <button id="runExample">Configure Fonts</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const fontFileInput = document.getElementById('fontFileInput');
            const fontFolderInput = document.getElementById('fontFolderInput');
            const resultDiv = document.getElementById('result');

            // Basic validation: ensure at least one font resource is provided (file or folder)
            if (!fontFileInput.files.length && !fontFolderInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select at least one font file or a font folder.</p>';
                return;
            }

            // Defining string variables to store paths/names to font folders & font file
            // (In browser environment we use simple names or uploaded file names)
            const fontFolder1 = "Arial";
            const fontFolder2 = "Calibri";
            const fontFile = "arial.ttf";

            // Setting first font folder (converted from setFontFolder)
            AsposeCells.FontConfigs.fontFolder = fontFolder1;
            // Preserve the subfolder-search flag from original API call as a separate property
            AsposeCells.FontConfigs.fontFolderSearchSubFolders = true;

            // Setting both font folders (converted from setFontFolders)
            AsposeCells.FontConfigs.fontFolders = [fontFolder1, fontFolder2];
            // Preserve the subfolder-search flag as a separate property
            AsposeCells.FontConfigs.fontFoldersSearchSubFolders = false;

            // Defining FolderFontSource
            const sourceFolder = new AsposeCells.FolderFontSource(fontFolder1, false);

            // Defining FileFontSource
            const sourceFile = new AsposeCells.FileFontSource(fontFile);

            // Defining MemoryFontSource
            let memoryFontBytes = new Uint8Array([]);
            if (fontFileInput.files.length) {
                const ff = fontFileInput.files[0];
                const arrayBuffer = await ff.arrayBuffer();
                memoryFontBytes = new Uint8Array(arrayBuffer);
            } else if (fontFolderInput.files.length) {
                // If a folder was provided, try to find a .ttf/.otf inside it and use the first found
                const files = Array.from(fontFolderInput.files);
                const fontCandidate = files.find(f => f.name.toLowerCase().endsWith('.ttf') || f.name.toLowerCase().endsWith('.otf'));
                if (fontCandidate) {
                    const arrayBuffer = await fontCandidate.arrayBuffer();
                    memoryFontBytes = new Uint8Array(arrayBuffer);
                }
            }
            const sourceMemory = new AsposeCells.MemoryFontSource(memoryFontBytes);

            // Setting font sources (converted from setFontSources)
            AsposeCells.FontConfigs.fontSources = [sourceFolder, sourceFile, sourceMemory];

            // Provide feedback to the user
            resultDiv.innerHTML = '<p style="color: green;">Font configuration applied successfully.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Veuillez utiliser l'une des méthodes mentionnées ci-dessus au début de l'application, c'est-à-dire; avant d'appeler d'autres objets des APIs Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Si toutes les méthodes mentionnées ci-dessus sont utilisées pour définir les sources de polices, seuls les derniers réglages prendront effet.

{{% /alert %}}

## **Mécanisme de substitution de polices**

Les API Aspose.Cells offrent également la possibilité de spécifier la police de substitution pour le rendu. Ce mécanisme est utile lorsque la police requise n'est pas disponible sur la machine où la conversion doit avoir lieu. Les utilisateurs peuvent fournir une liste de noms de police en alternative à la police initialement requise. Pour cela, les API Aspose.Cells exposent la méthode [**FontConfigs.fontSubstitutes(string, string[])**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-stringarray-) qui accepte deux paramètres. Le premier est de type **string**, qui doit être le nom de la police à substituer. Le second est un tableau de type **string**, dans lequel les utilisateurs peuvent fournir une liste de noms de police de substitution pour la police originale (spécifiée dans le premier paramètre).

Voici un scénario d'utilisation simple.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Substituting the Arial font with Times New Roman & Calibri
            // Converted from: AsposeCells.FontConfigs.setFontSubstitutes("Arial", ["Times New Roman", "Calibri"]);
            AsposeCells.FontConfigs.fontSubstitutes = { "Arial": ["Times New Roman", "Calibri"] };

            // Saving the (possibly modified) workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the processed file.</p>';
        });
    </script>
</html>
```

## **Collecte d'informations**

En complément des méthodes mentionnées ci-dessus, les API Aspose.Cells offrent également des moyens de recueillir des informations sur les sources et remplacements qui ont été configurés.

1. La méthode [**FontConfigs.fontSources**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources--) retourne un tableau de type [**FontSourceBase**](https://reference.aspose.com/cells/javascript-cpp/fontsourcebase) contenant la liste des sources de police spécifiées. Si aucune source n'a été configurée, la méthode [**FontConfigs.fontSources**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSources--) renverra un tableau vide.
1. La méthode [**FontConfigs.fontSubstitutes(string)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-) accepte un paramètre de type **string** permettant de spécifier le nom de la police pour laquelle une substitution a été définie. Si aucune substitution n'a été configurée pour ce nom de police, la méthode [**FontConfigs.fontSubstitutes(string)**](https://reference.aspose.com/cells/javascript-cpp/fontconfigs/#fontSubstitutes-string-) renverra null.

## **Sujets avancés**
- [Définir la police par défaut lors du rendu de la feuille de calcul en images](/cells/fr/javascript-cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [Définir la propriété DefaultFont des PdfSaveOptions et ImageOrPrintOptions pour avoir la priorité](/cells/fr/javascript-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Formats de police pris en charge](/cells/fr/javascript-cpp/supported-font-formats/)
- [Feuille de calcul vers Image - Définir le format de pixel pour l'image rendue](/cells/fr/javascript-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
