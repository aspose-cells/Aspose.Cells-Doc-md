---
title: Modifications de l API publique dans Aspose.Cells 8.9.1
type: docs
weight: 320
url: /fr/java/public-api-changes-in-aspose-cells-8-9-1/
---

{{% alert color="primary" %}} 

Ce document décrit les modifications apportées à l'API Aspose.Cells de la version 8.9.0 à la version 8.9.1 qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement les nouvelles méthodes publiques et mises à jour, les classes ajoutées et supprimées, etc., mais aussi une description de toute modification du comportement en arrière-plan dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Sources de police configurables**
Aspose.Cells for Java a exposé un certain nombre de classes pour prendre en charge les sources de polices configurables pour le rendu des feuilles de calcul. Voici la liste des classes qui ont été ajoutées avec Aspose.Cells for Java 8.9.1.

1. La classe FontConfigs spécifie les paramètres de police.
1. La classe FontSourceBase est une classe de base abstraite pour les classes qui permettent à l'utilisateur de spécifier différentes sources de police.
1. La classe FileFontSource représente le fichier de police TrueType unique stocké dans le système de fichiers.
1. La classe FolderFontSource représente le dossier qui contient des fichiers de police TrueType.
1. La classe MemoryFontSource représente le fichier de police TrueType unique stocké en mémoire.
1. L'énumération FontSourceType spécifie le type d'une source de police.

Avec les modifications mentionnées ci-dessus en place, le Aspose.Cells for Java permet de définir les polices comme détaillé ci-dessous.

1. Définissez un dossier de polices personnalisé tout en utilisant la méthode FontConfigs.setFontFolder.
1. Définir plusieurs dossiers de polices personnalisés tout en utilisant la méthode FontConfigs.setFontFolders.
1. Définir les sources de polices à partir d'un dossier de polices personnalisé, un seul fichier de police ou des données de police à partir d'un tableau d'octets tout en utilisant la méthode FontConfigs.setFontSources.

Voici un scénario d'utilisation simple des méthodes mentionnées ci-dessus.

**Java**

{{< highlight csharp >}}

 //Defining string variables to store paths to font folders & font file

String fontFolder1 = "D:/Arial";

String fontFolder2 = "D:/Calibri";

String fontFile = "D:/Arial/arial.ttf";

//Setting first font folder with setFontFolder method

//Second parameter directs the API to search the sub folders for font files

FontConfigs.setFontFolder(fontFolder1, true);

//Setting both font folders with setFontFolders method

//Second parameter prohibits the API to search the sub folders for font files

FontConfigs.setFontFolders(new String[] { fontFolder1, fontFolder2 }, false);

//Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

//Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

//Defining MemoryFontSource

byte[] bytes = Files.readAllBytes(new File(fontFile).toPath());

MemoryFontSource sourceMemory = new MemoryFontSource(bytes);

//Setting font sources

FontConfigs.setFontSources(new FontSourceBase[] { sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

Les méthodes FontConfigs.setFontFolder et FontConfigs.setFontFolders acceptent toutes deux un deuxième paramètre de type booléen. En passant true comme deuxième paramètre, les API Aspose.Cells rechercheront les sous-dossiers pour les fichiers de polices. 

{{% /alert %}} 

Aspose.Cells for Java permet également de configurer le remplacement de police. Ce mécanisme est utile lorsque la police requise n'est pas disponible sur la machine où la conversion doit avoir lieu. Les utilisateurs peuvent fournir une liste de noms de police en tant qu'alternative à la police originellement requise. Afin de réaliser cela, les API Aspose.Cells ont exposé la méthode FontConfigs.setFontSubstitutes qui accepte 2 paramètres. Le premier paramètre est de type chaîne, qui doit être le nom de la police qui doit être remplacée. Le deuxième paramètre est un tableau de type chaîne. Les utilisateurs peuvent fournir une liste de noms de polices comme substitution au nom de police original (spécifié dans le premier paramètre).

Voici un scénario d'utilisation simple de la méthode FontConfigs.SetFontSubstitutes.

**Java**

{{< highlight csharp >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[] { "Times New Roman", "Calibri" });

{{< /highlight >}}

Le Aspose.Cells for Java a également fourni des moyens de recueillir des informations sur les sources et les substitutions qui ont été définies.

1. La méthode FontConfigs.getFontSources renvoie un tableau de type FontSourceBase contenant la liste des sources de polices spécifiées. Dans le cas où aucune source n'a été définie, la méthode FontConfigs.getFontSources renverra un tableau vide.
1. La méthode FontConfigs.getFontSubstitutes accepte un paramètre de type chaîne permettant de spécifier le nom de la police pour laquelle une substitution a été définie. Dans le cas où aucune substitution n'a été définie pour le nom de police spécifié, la méthode FontConfigs.getFontSubstitutes renverra null.

{{% alert color="primary" %}} 

Pour plus de détails sur FontConfigs, veuillez consulter l'article sur [Configuration des polices pour le rendu des feuilles de calcul](/cells/fr/java/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **Ajout de l'interface IFilePathProvider et de la propriété HtmlSaveOptions.FilePathProvider**
Aspose.Cells for Java 8.9.1 permet d'obtenir/définir IFilePathProvider pour exporter les feuilles de calcul vers des fichiers HTML séparés. Ces nouvelles API sont utiles dans les scénarios où les liens hypertexte dans une feuille de calcul pointent vers un emplacement dans une autre feuille de calcul, où l'application doit rendre chaque feuille de calcul dans un fichier HTML séparé. La mise en œuvre de IFilePathProvider permet de conserver les liens hypertexte susmentionnés intacts, peu importe le fait qu'ils pointent vers un emplacement dans un fichier HTML résultant séparé.

Voici un scénario d'utilisation simple de la propriété HtmlSaveOptions.FilePathProvider.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Save each Worksheet to separate  HTML file

for (int i = 0; i < book.getWorksheets().getCount(); i++)

{

	book.getWorksheets().setActiveSheetIndex(i);

	//Create an instance of HtmlSaveOptions & set FilePathProvider property

	HtmlSaveOptions options = new HtmlSaveOptions();

	options.setExportActiveWorksheetOnly(true);

	options.setFilePathProvider(new IFilePathProvider() 

	{ 

		public String getFullName(String sheetName)

		{

		    if ("Sheet2".equals(sheetName))

		    {

		        return "sheet1.html";

		    }

		    else if ("Sheet3".equals(sheetName))

		    {

		        return "sheet2.html";

		    }



		    return "";

		}

	});



	 //Write HTML file to disc

	 book.save(dir + "sheet"+ i +".html", options);

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Pour plus de détails sur cette amélioration, veuillez consulter l'article sur [Implémentation de l'interface IFilePathProvider](/cells/fr/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **Ajout de la propriété CopyOptions.ReferToDestinationSheet et de la surcharge pour la méthode Cells.copyRows**
L'API Aspose.Cells for Java a exposé la propriété CopyOptions.ReferToDestinationSheet de type booléen ainsi que la surcharge de la méthode Cells.copyRows afin de faciliter l'opération de copie de lignes lorsque les lignes à copier contiennent également un graphique et sa source de données. Les développeurs peuvent utiliser ces nouvelles API pour pointer la source de données du graphique vers les feuilles de calcul source ou de destination.

Voici le scénario d'utilisation simple.

**Java**

{{< highlight csharp >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Access the worksheet containing the chart & its data source

Worksheet source = book.getWorksheets().get(0);

//Add a new worksheet to the collection

Worksheet destination = book.getWorksheets().get(book.getWorksheets().add());

//Initialize CopyOptions and set its ReferToDestinationSheet property to true

CopyOptions options = new CopyOptions();

options.setReferToDestinationSheet(true);

//Copy the rows

destination.getCells().copyRows(source.getCells(), 0, 0, source.getCells().getMaxDisplayRange().getRowCount(), options);

//Save the result on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article sur [Contrôler la source de données du graphique lors de la copie de lignes](/cells/fr/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **Ajout de la propriété CalculationOptions.Recursive**
Aspose.Cells for Java 8.9.1 a exposé la propriété booléenne CalculationOptions.Recursive. Définir la propriété CalculationOptions.Recursive sur true et passer l'objet à la méthode Workbook.calculateFormula dirige les API Aspose.Cells pour calculer de manière récursive les cellules dépendantes lors du calcul des cellules qui dépendent d'autres cellules.

Voici le scénario d'utilisation simple.

**Java**

{{< highlight csharp >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Initialize CalculationOptions & set Recursive property to true

CalculationOptions options = new CalculationOptions();

options.setRecursive(true);

//Recalculate formulas

book.calculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article sur [Optimiser le temps de calcul](/cells/fr/java/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **APIs obsolètes**
### **Propriété CellsHelper.FontDir obsolète**
Il est conseillé d'utiliser la méthode FontConfigs.setFontFolder(String, boolean) avec une récursivité de dossier à false à la place.
### **Propriété CellsHelper.FontDirs obsolète**
Utilisez la méthode FontConfigs.setFontFolders(String[], boolean) avec la récursivité de dossier à false à la place.
### **Propriété CellsHelper.FontFiles obsolète**
Utilisez la méthode FontConfigs.setFontSources(FontSourceBase[]) à la place.
{{< app/cells/assistant language="java" >}}
