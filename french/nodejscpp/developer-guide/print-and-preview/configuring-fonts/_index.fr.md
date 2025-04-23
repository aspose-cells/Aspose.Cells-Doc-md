---
title: Configuration des polices pour le rendu des feuilles de calcul avec Node.js via C++
linktitle: Configuration des polices pour le rendu des feuilles de calcul
type: docs
weight: 10
url: /fr/nodejs-cpp/configuring-fonts-for-rendering-spreadsheets/
description: Apprenez comment configurer les polices pour le rendu des feuilles de calcul en utilisant Aspose.Cells for Node.js via C++. Assurez vous que les polices soient disponibles pour une fidélité de conversion optimale.
---

## **Scénarios d'utilisation possibles**

Les API Aspose.Cells offrent la possibilité de rendre les feuilles de calcul en formats image ainsi que de les convertir en formats PDF et XPS. Pour maximiser la fidélité de la conversion, il est nécessaire que les polices utilisées dans la feuille de calcul soient disponibles dans le répertoire par défaut des polices du système d'exploitation. Si les polices requises ne sont pas présentes, les API Aspose.Cells tenteront de les remplacer par celles disponibles.

## **Sélection des polices**

Voici le processus suivi par les API Aspose.Cells en arrière-plan.

1. L'API tente de trouver les polices sur le système de fichiers correspondant exactement au nom de police utilisé dans la feuille de calcul.
1. Si l'API ne parvient pas à trouver les polices portant le même nom exact, elle tente d'utiliser la police par défaut spécifiée dans la propriété [**DefaultStyle.getFont()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) du classeur.
1. Si l'API ne parvient pas à localiser la police définie dans la propriété [**DefaultStyle.getFont()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getFont--) du classeur, elle tente d'utiliser la police spécifiée dans la propriété [**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--) ou [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--).
1. Si l'API ne parvient pas à localiser la police définie dans [**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--) ou [**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--), elle tente d'utiliser la police spécifiée dans [**FontConfigs.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getDefaultFontName--).
1. Si l'API ne parvient pas à localiser la police définie dans [**FontConfigs.getDefaultFontName()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getDefaultFontName--), elle tente de sélectionner les polices les plus adaptées parmi toutes les polices disponibles.
1. Enfin, si l'API ne trouve pas de polices sur le système de fichiers, elle rend la feuille de calcul en utilisant Arial.

## **Définir des dossiers de polices personnalisés**

Les API Aspose.Cells recherchent dans le répertoire par défaut des polices du système d'exploitation les polices requises. Si celles-ci ne sont pas disponibles dans le répertoire, les API recherchent dans les répertoires personnalisés (définis par l'utilisateur). La classe [**FontConfigs**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs) offre plusieurs méthodes pour définir des répertoires de polices personnalisés, comme détaillé ci-dessous.

1. [**FontConfigs.setFontFolder(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolder-string-boolean-): Cette méthode est utile s'il n'y a qu'un seul dossier à définir.
1. [**FontConfigs.setFontFolders(string[], boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolders-stringarray-boolean-): Cette méthode est utile lorsque les polices résident dans des dossiers multiples et que l'utilisateur souhaite définir tous les dossiers séparément plutôt que de combiner toutes les polices dans un seul dossier.
1. [**FontConfigs.setFontSources(FontSourceBase[])**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontSources-fontsourcebasearray-): Ce mécanisme est utile lorsque l'utilisateur souhaite charger des polices à partir de dossiers multiples ou d'un seul fichier de police ou de données de police à partir d'un tableau d'octets.

{{% alert color="primary" %}}

Les deux méthodes [**FontConfigs.setFontFolder(string, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolder-string-boolean-) et [**FontConfigs.setFontFolders(string[], boolean)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontFolders-stringarray-boolean-) acceptent un deuxième paramètre de type Boolean. Passer **true** en tant que deuxième paramètre dirigera les API Aspose.Cells pour rechercher les sous-dossiers des fichiers de polices.

{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Defining string variables to store paths to font folders & font file
const fontFolder1 = path.join(dataDir, "Arial");
const fontFolder2 = path.join(dataDir, "Calibri");
const fontFile = path.join(dataDir, "arial.ttf"); 

// Setting first font folder with SetFontFolder method
// Second parameter directs the API to search the subfolders for font files
AsposeCells.FontConfigs.setFontFolder(fontFolder1, true);

// Setting both font folders with SetFontFolders method
// Second parameter prohibits the API to search the subfolders for font files
AsposeCells.FontConfigs.setFontFolders([fontFolder1, fontFolder2], false);

// Defining FolderFontSource
const sourceFolder = new AsposeCells.FolderFontSource(fontFolder1, false);

// Defining FileFontSource
const sourceFile = new AsposeCells.FileFontSource(fontFile);

// Defining MemoryFontSource
const sourceMemory = new AsposeCells.MemoryFontSource(require("fs").readFileSync(fontFile));

// Setting font sources
AsposeCells.FontConfigs.setFontSources([sourceFolder, sourceFile, sourceMemory]);
```

{{% alert color="primary" %}}

Veuillez utiliser l'une des méthodes mentionnées ci-dessus au début de l'application, c'est-à-dire; avant d'appeler d'autres objets des APIs Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Si toutes les méthodes mentionnées ci-dessus sont utilisées pour définir les sources de polices, seuls les derniers réglages prendront effet.

{{% /alert %}}

## **Mécanisme de substitution de polices**

Les API Aspose.Cells offrent également la possibilité de spécifier la police de substitution pour le rendu. Ce mécanisme est utile lorsque la police requise n'est pas disponible sur la machine où la conversion doit avoir lieu. Les utilisateurs peuvent fournir une liste de noms de police en alternative à la police initialement requise. Pour cela, les API Aspose.Cells exposent la méthode [**FontConfigs.setFontSubstitutes(string, string[])**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#setFontSubstitutes-string-stringarray-) qui accepte deux paramètres. Le premier est de type **string**, qui doit être le nom de la police à substituer. Le second est un tableau de type **string**, dans lequel les utilisateurs peuvent fournir une liste de noms de police de substitution pour la police originale (spécifiée dans le premier paramètre).

Voici un scénario d'utilisation simple.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Substituting the Arial font with Times New Roman & Calibri
AsposeCells.FontConfigs.setFontSubstitutes("Arial", ["Times New Roman", "Calibri"]);
```

## **Collecte d'informations**

En complément des méthodes mentionnées ci-dessus, les API Aspose.Cells offrent également des moyens de recueillir des informations sur les sources et remplacements qui ont été configurés.

1. La méthode [**FontConfigs.getFontSources()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSources--) retourne un tableau de type [**FontSourceBase**](https://reference.aspose.com/cells/nodejs-cpp/fontsourcebase) contenant la liste des sources de police spécifiées. Si aucune source n'a été configurée, la méthode [**FontConfigs.getFontSources()**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSources--) renverra un tableau vide.
1. La méthode [**FontConfigs.getFontSubstitutes(string)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSubstitutes-string-) accepte un paramètre de type **string** permettant de spécifier le nom de la police pour laquelle une substitution a été définie. Si aucune substitution n'a été configurée pour ce nom de police, la méthode [**FontConfigs.getFontSubstitutes(string)**](https://reference.aspose.com/cells/nodejs-cpp/fontconfigs/#getFontSubstitutes-string-) renverra null.

## **Sujets avancés**
- [Définir la police par défaut lors du rendu de la feuille de calcul en images](/cells/fr/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [Définir la propriété DefaultFont des PdfSaveOptions et ImageOrPrintOptions pour avoir la priorité](/cells/fr/nodejs-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Formats de police pris en charge](/cells/fr/nodejs-cpp/supported-font-formats/)
- [Feuille de calcul vers Image - Définir le format de pixel pour l'image rendue](/cells/fr/nodejs-cpp/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
