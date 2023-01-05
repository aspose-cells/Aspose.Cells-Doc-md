---
title: Public API Changements dans Aspose.Cells 8.9.1
type: docs
weight: 320
url: /fr/java/public-api-changes-in-aspose-cells-8-9-1/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.9.0 à 8.9.1 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les méthodes publiques nouvelles et mises à jour, les classes ajoutées et supprimées, etc., mais également une description de tout changement de comportement dans les coulisses de Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Sources de polices configurables**
Aspose.Cells for Java a exposé un certain nombre de classes pour fournir la prise en charge des sources de polices configurables pour le rendu des feuilles de calcul. Voici la liste des classes qui ont été ajoutées avec Aspose.Cells for Java 8.9.1.

1. La classe FontConfigs spécifie les paramètres de police.
1. La classe FontSourceBase est une classe de base abstraite pour les classes qui permettent à l'utilisateur de spécifier diverses sources de polices.
1. La classe FileFontSource représente le fichier de police TrueType unique stocké dans le système de fichiers.
1. La classe FolderFontSource représente le dossier qui contient les fichiers de police TrueType.
1. La classe MemoryFontSource représente le seul fichier de police TrueType stocké en mémoire.
1. L'énumération FontSourceType spécifie le type d'une source de police.

Avec les changements mentionnés ci-dessus en place, le Aspose.Cells for Java permet de définir les polices comme détaillé ci-dessous.

1. Définissez un dossier de polices personnalisées lors de l'utilisation de la méthode FontConfigs.setFontFolder.
1. Définissez plusieurs dossiers de polices personnalisées lors de l'utilisation de la méthode FontConfigs.setFontFolders.
1. Définissez les sources de polices à partir d'un dossier de polices personnalisé, d'un fichier de police unique ou de données de police à partir d'un tableau d'octets tout en utilisant la méthode FontConfigs.setFontSources.

Voici un scénario d'utilisation simple des méthodes susmentionnées.

**Java**

{{< highlight "csharp" >}}

 //Defining string variables to store paths to font folders & font file

String fontFolder1 = "D:/Arial";

String fontFolder2 = "D:/Calibri";

String fontFile = "D:/Arial/arial.ttf";

//Setting first font folder with setFontFolder method

//Second parameter directs the API to search the sub folders for font files

FontConfigs.setFontFolder(fontFolder1, true);

//Setting both font folders with setFontFolders method

//Second parameter prohibits the API to search the sub folders for font files

FontConfigs.setFontFolders(new String[]{ fontFolder1, fontFolder2 }, false);

//Defining FolderFontSource

FolderFontSource sourceFolder = new FolderFontSource(fontFolder1, false);

//Defining FileFontSource

FileFontSource sourceFile = new FileFontSource(fontFile);

//Defining MemoryFontSource

byte[]bytes = Files.readAllBytes(new File(fontFile).toPath());

MemoryFontSource sourceMemory = new MemoryFontSource(bytes);

//Setting font sources

FontConfigs.setFontSources(new FontSourceBase[]{ sourceFolder, sourceFile, sourceMemory});

{{< /highlight >}}

{{% alert color="primary" %}} 

 Les deux méthodes FontConfigs.setFontFolder et FontConfigs.setFontFolders acceptent un deuxième paramètre de type booléen. Passer true comme deuxième paramètre dirigera les API Aspose.Cells pour rechercher les sous-dossiers pour les fichiers de polices.

{{% /alert %}} 

Aspose.Cells for Java permet également de configurer la substitution de police. Ce mécanisme est utile lorsqu'une police requise n'est pas disponible sur la machine où la conversion doit avoir lieu. Les utilisateurs peuvent fournir une liste de noms de polices comme alternative à la police requise à l'origine. Pour ce faire, les API Aspose.Cells ont exposé la méthode FontConfigs.setFontSubstitutes qui accepte 2 paramètres. Le premier paramètre est de type string, qui doit être le nom de la police à remplacer. Le deuxième paramètre est un tableau de type string. Les utilisateurs peuvent fournir une liste de noms de polices en remplacement du nom de police d'origine (spécifié dans le premier paramètre).

Voici un scénario d'utilisation simple de la méthode FontConfigs.SetFontSubstitutes.

**Java**

{{< highlight "csharp" >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[]{ "Times New Roman", "Calibri" });

{{< /highlight >}}

Le Aspose.Cells for Java a également fourni des moyens de recueillir des informations sur les sources et les substitutions qui ont été définies.

1. La méthode FontConfigs.getFontSources renvoie un tableau de type FontSourceBase contenant la liste des sources de polices spécifiées. Si aucune source n'a été définie, la méthode FontConfigs.getFontSources renverra un tableau vide.
1. La méthode FontConfigs.getFontSubstitutes accepte un paramètre de type chaîne permettant de spécifier le nom de la police pour laquelle une substitution a été définie. Dans le cas où aucune substitution n'a été définie pour le nom de police spécifié, la méthode FontConfigs.getFontSubstitutes renverra null.

{{% alert color="primary" %}} 

 Pour plus de détails sur FontConfigs, veuillez consulter l'article sur[Configuration des polices pour le rendu des feuilles de calcul](/cells/fr/java/configuring-fonts-for-rendering-spreadsheets/).

{{% /alert %}} 
### **Ajout de l'interface IFilePathProvider et de la propriété HtmlSaveOptions.FilePathProvider**
Aspose.Cells for Java 8.9.1 permet d'obtenir/de définir IFilePathProvider pour exporter des feuilles de calcul vers des fichiers HTML séparés. Ces nouvelles API sont utiles dans les scénarios où les liens hypertexte d'une feuille de calcul pointent vers un emplacement dans une autre feuille de calcul, où l'exigence de l'application est de rendre chaque feuille de calcul pour séparer le fichier HTML. L'implémentation de IFilePathProvider permet de conserver intacts les hyperliens susmentionnés, qu'ils pointent vers un emplacement dans un fichier HTML distinct.

Voici le scénario d'utilisation simple de la propriété HtmlSaveOptions.FilePathProvider.

**Java**

{{< highlight "csharp" >}}

 // Charger une feuille de calcul dans une instance de Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

// Enregistrez chaque feuille de travail pour séparer le fichier HTML

 pour (int je = 0; je< book.getWorksheets().getCount(); i++)

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

 Pour plus de détails sur cette amélioration, veuillez consulter l'article sur[Implémentation de l'interface IFilePathProvider](/cells/fr/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/).

{{% /alert %}} 
### **Ajout de la propriété CopyOptions.ReferToDestinationSheet et de la surcharge pour la méthode Cells.copyRows**
Aspose.Cells for Java API a exposé la propriété CopyOptions.ReferToDestinationSheet de type booléen ainsi qu'une surcharge de la méthode Cells.copyRows afin de faciliter l'opération de copie des lignes lorsque les lignes à copier contiennent également un graphique et sa source de données. Les développeurs peuvent utiliser ces nouvelles API pour faire pointer la source de données du graphique vers les feuilles de calcul source ou de destination.

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

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

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article sur[Contrôler la source de données du graphique lors de la copie de lignes](/cells/fr/java/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/).

{{% /alert %}} 
### **Ajout de la propriété CalculationOptions.Recursive**
Aspose.Cells for Java 8.9.1 a exposé la propriété de type booléen CalculationOptions.Recursive. La définition de la propriété CalculationOptions.Recursive sur true et la transmission de l'objet à la méthode Workbook.calculateFormula ordonnent aux API Aspose.Cells de calculer les cellules dépendantes de manière récursive lors du calcul de cellules qui dépendent d'autres cellules.

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

 //Load a sample spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Initialize CalculationOptions & set Recursive property to true

CalculationOptions options = new CalculationOptions();

options.setRecursive(true);

//Recalculate formulas

book.calculateFormula(options);

{{< /highlight >}}

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article sur[Optimiser le temps de calcul](/cells/fr/java/decrease-the-calculation-time-of-cell-calculate-method/).

{{% /alert %}}
## **API obsolètes**
### **Propriété CellsHelper.FontDir obsolète**
Il est conseillé d'utiliser la méthode FontConfigs.setFontFolder(String, boolean) avec dossier récursif à false à la place.
### **Propriété CellsHelper.FontDirs obsolète**
Utilisez la méthode FontConfigs.setFontFolders(String[], boolean) avec le dossier récursif à false à la place.
### **Propriété CellsHelper.FontFiles obsolète**
Utilisez plutôt la méthode FontConfigs.setFontSources(FontSourceBase[]).
