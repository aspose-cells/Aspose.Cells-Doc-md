---
title: Modifications de l API publique dans Aspose.Cells 8.9.1
type: docs
weight: 310
url: /fr/net/public-api-changes-in-aspose-cells-8-9-1/
---

{{% alert color="primary" %}} 

Ce document décrit les modifications apportées à l'API Aspose.Cells de la version 8.9.0 à la version 8.9.1 qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement les nouvelles méthodes publiques et mises à jour, les classes ajoutées et supprimées, etc., mais aussi une description de toute modification du comportement en arrière-plan dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Sources de police configurables**
Aspose.Cells for .NET a exposé un certain nombre de classes pour prendre en charge les sources de police configurables pour le rendu de feuilles de calcul. Voici la liste des classes qui ont été ajoutées avec Aspose.Cells for .NET 8.9.1.

1. La classe FontConfigs spécifie les paramètres de police.
1. La classe FontSourceBase est une classe de base abstraite pour les classes qui permettent à l'utilisateur de spécifier différentes sources de police.
1. La classe FileFontSource représente le fichier de police TrueType unique stocké dans le système de fichiers.
1. La classe FolderFontSource représente le dossier qui contient des fichiers de police TrueType.
1. La classe MemoryFontSource représente le fichier de police TrueType unique stocké en mémoire.
1. L'énumération FontSourceType spécifie le type d'une source de police.

Avec les modifications mentionnées ci-dessus en place, le Aspose.Cells for .NET permet de définir les polices comme détaillé ci-dessous.

1. Définir un dossier de police personnalisé tout en utilisant la méthode FontConfigs.SetFontFolder.
1. Définir plusieurs dossiers de police personnalisés tout en utilisant la méthode FontConfigs.SetFontFolders.
1. Définir les sources de police à partir d'un dossier de police personnalisé, d'un seul fichier de police ou de données de police à partir d'un tableau d'octets tout en utilisant la méthode FontConfigs.SetFontSources.

Voici un scénario d'utilisation simple des méthodes mentionnées ci-dessus.

**C#**

{{< highlight csharp >}}

 // Defining string variables to store paths to font folders & font file

string fontFolder1 = "D:/Arial";

string fontFolder2 = "D:/Calibri";

string fontFile = "D:/Arial/arial.ttf";

// Setting first font folder with SetFontFolder method

// Second parameter directs the API to search the subfolders for font files

FontConfigs.SetFontFolder(fontFolder1, true);

// Setting both font folders with SetFontFolders method

// Second parameter prohibits the API to search the subfolders for font files

FontConfigs.SetFontFolders(new string[] { fontFolder1, fontFolder2 }, false);

// Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

// Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

// Defining MemoryFontSource

MemoryFontSource sourceMemory = new MemoryFontSource(System.IO.File.ReadAllBytes(fontFile));

//Setting font sources

FontConfigs.SetFontSources(new FontSourceBase[] { sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

Les méthodes FontConfigs.SetFontFolder et FontConfigs.SetFontFolders acceptent toutes deux un deuxième paramètre de type booléen. En passant true comme deuxième paramètre, les API Aspose.Cells rechercheront les sous-dossiers des fichiers de polices.

{{% /alert %}} 

Aspose.Cells for .NET permet également de configurer la substitution des polices. Ce mécanisme est utile lorsque la police requise n'est pas disponible sur la machine où la conversion doit avoir lieu. Les utilisateurs peuvent fournir une liste de noms de police en tant qu'alternative à la police initialement requise. Pour ce faire, les API Aspose.Cells ont exposé la méthode FontConfigs.SetFontSubstitutes qui accepte 2 paramètres. Le premier paramètre est de type chaîne, qui devrait être le nom de la police à remplacer. Le deuxième paramètre est un tableau de type chaîne. Les utilisateurs peuvent fournir une liste de noms de police en substitution au nom de police original (spécifié dans le premier paramètre).

Voici un scénario d'utilisation simple de la méthode FontConfigs.SetFontSubstitutes.

**C#**

{{< highlight csharp >}}

 // Substituting the Arial font with Times New Roman & Calibri

FontConfigs.SetFontSubstitutes("Arial", new string[] { "Times New Roman", "Calibri" });

{{< /highlight >}}



Le Aspose.Cells for .NET a également fourni des moyens pour rassembler des informations sur les sources et les substitutions qui ont été définies.

1. La méthode FontConfigs.GetFontSources renvoie un tableau de type FontSourceBase contenant la liste des sources de polices spécifiées. Si aucune source n'a été définie, la méthode FontConfigs.GetFontSources renverra un tableau vide.
1. La méthode FontConfigs.GetFontSubstitutes accepte un paramètre de type chaîne permettant de spécifier le nom de la police pour laquelle une substitution a été définie. Si aucune substitution n'a été définie pour le nom de police spécifié, la méthode FontConfigs.GetFontSubstitutes renverra null.

{{% alert color="primary" %}} 

Pour plus de détails sur FontConfigs, veuillez consulter l'article sur [Configuration des polices pour le rendu des feuilles de calcul](/cells/fr/net/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **Ajout de l'interface IFilePathProvider et de la propriété HtmlSaveOptions.FilePathProvider**
Aspose.Cells for .NET 8.9.1 permet d'obtenir/définir l'IFilePathProvider pour exporter les feuilles de calcul vers des fichiers HTML séparés. Ces nouvelles API sont utiles dans les scénarios où les liens hypertexte dans une feuille de calcul pointent vers un emplacement dans une autre feuille de calcul, et où l'exigence de l'application est de rendre chaque feuille de calcul dans un fichier HTML séparé. La mise en œuvre de l'IFilePathProvider permet de conserver les liens hypertexte susmentionnés, indépendamment du fait qu'ils pointent vers un emplacement dans un fichier HTML résultant séparé.

Voici un scénario d'utilisation simple de la propriété HtmlSaveOptions.FilePathProvider.

**C#**

{{< highlight csharp >}}

 // Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Save each Worksheet to separate HTML file

for (int i = 0; i < book.Worksheets.Count; i++)

{

    book.Worksheets.ActiveSheetIndex = i;

    // Create an instance of HtmlSaveOptions & set FilePathProvider property

    var options = new HtmlSaveOptions

    {

        ExportActiveWorksheetOnly = true,

        FilePathProvider = new FilePathProvider()

    };

    // Write HTML file to disc

    book.Save(dir + string.Format(@"sheet{0}.html", i), options);

}

{{< /highlight >}}



Voici comment mettre en œuvre l'interface IFilePathProvider.

**C#**

{{< highlight csharp >}}

 public class FilePathProvider : IFilePathProvider

{

    public FilePathProvider()

    {

    }

    /// <summary>

    /// Gets the full path of the file by Worksheet name when exporting Worksheet to html separately.

    /// So the references among the Worksheets can be exported correctly.

    /// </summary>

    /// <param name="sheetName">Worksheet name</param>

    /// <returns>the full path of the file</returns>

    public string GetFullName(string sheetName)

    {

        if ("Sheet2".Equals(sheetName))

        {

            return "sheet1.html";

        }

        else if ("Sheet3".Equals(sheetName))

        {

            return "sheet2.html";

        }

        return "";

    }

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Pour plus de détails sur cet ajout, veuillez consulter l'article sur [Mise en œuvre de l'interface IFilePathProvider](/cells/fr/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **Ajout de la propriété CopyOptions.ReferToDestinationSheet & Overload pour la méthode Cells.CopyRows**
L'API Aspose.Cells for .NET a exposé la propriété CopyOptions.ReferToDestinationSheet de type booléen ainsi qu'une surcharge de la méthode Cells.CopyRows afin de faciliter l'opération de copie de lignes lorsque les lignes à copier contiennent également un graphique et sa source de données. Les développeurs peuvent utiliser ces nouvelles API pour pointer la source de données du graphique vers les feuilles de calcul source ou de destination.

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the worksheet containing the chart & its data source

var source = book.Worksheets[0];

// Add a new worksheet to the collection

var destination = book.Worksheets[book.Worksheets.Add()];

// Initialize CopyOptions and set its ReferToDestinationSheet property to true

CopyOptions options = new CopyOptions();

options.ReferToDestinationSheet = true;

// Copy the rows

destination.Cells.CopyRows(source.Cells, 0, 0, source.Cells.MaxDisplayRange.RowCount, options);

// Save the result on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article sur [Contrôler la source de données du graphique lors de la copie de lignes](/cells/fr/net/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **Ajout de la propriété CalculationOptions.Recursive**
Aspose.Cells for .NET 8.9.1 a exposé la propriété CalculationOptions.Recursive de type booléen. En définissant la propriété CalculationOptions.Recursive sur true et en passant l'objet à la méthode Workbook.CalculateFormula, les API Aspose.Cells calculeront les cellules dépendantes de manière récursive lors du calcul des cellules qui dépendent d'autres cellules.

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

 // Load a sample spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Initialize CalculationOptions & set Recursive property to true

var options = new CalculationOptions();

options.Recursive = true;

// Recalculate formulas

book.CalculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article sur [Optimiser le temps de calcul](/cells/fr/net/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **APIs obsolètes**
### **Propriété CellsHelper.FontDir obsolète**
Il est conseillé d'utiliser la méthode FontConfigs.SetFontFolder(string, bool) avec l'option récursive définie sur false à la place.
### **Propriété CellsHelper.FontDirs obsolète**
Utilisez la méthode FontConfigs.SetFontFolders(string[], bool) avec l'option récursive définie sur false à la place.
### **Propriété CellsHelper.FontFiles obsolète**
Utilisez la méthode FontConfigs.SetFontSources(FontSourceBase[]) à la place.
{{< app/cells/assistant language="csharp" >}}
