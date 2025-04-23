---
title: Changements dans l API publique dans Aspose.Cells 8.9.0
type: docs
weight: 300
url: /fr/net/public-api-changes-in-aspose-cells-8-9-0/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.8.3 à la 8.9.0 qui pourraient intéresser les développeurs de modules/applications. Il comprend non seulement les nouvelles méthodes publiques, les classes ajoutées et supprimées, mais aussi une description de tout changement dans le comportement en coulisse dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Propriété HtmlSaveOptions.DefaultFontName ajoutée**
Aspose.Cells for .NET 8.9.0 a exposé la propriété DefaultFontName pour la classe HtmlSaveOptions qui permet de spécifier le nom de la police par défaut lors du rendu des feuilles de calcul au format HTML. La police par défaut ne sera utilisée que lorsque la police de style n'existe pas. La valeur par défaut de la propriété HtmlSaveOptions.DefaultFontName est null, ce qui signifie que l'API Aspose.Cells for .NET utilisera la police universelle qui a la même famille que la police d'origine.

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article sur [Définir la police par défaut pour le rendu des feuilles de calcul au format HTML](/cells/fr/net/définir-la-police-par-défaut-lors-du-rendu-des-feuilles-de-calcul/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

 // Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set default font name for Html rendering

options.DefaultFontName = "Arial";

// Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **Propriété ajoutée ImageOrPrintOptions.DefaultFont**
Aspose.Cells for .NET 8.9.0 permet de définir le nom de la police par défaut pour la classe ImageOrPrintOptions en exposant la propriété DefaultFont. Cette propriété peut être utilisée lorsque les caractères Unicode dans la feuille de calcul ne sont pas définis avec la bonne police dans le style de cellule, donc ces caractères peuvent apparaître comme des blocs dans les images résultantes.

{{% alert color="primary" %}} 

Définissez la propriété DefaultFont sur MingLiu ou MS Gothic pour afficher des caractères Unicode. Si ladite propriété n'est pas définie, Aspose.Cells utilisera la police par défaut du système pour afficher les caractères Unicode.

{{% /alert %}} {{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article sur [Définir la police par défaut pour le rendu des feuilles de calcul dans des formats d'image](/cells/fr/net/définir-la-police-par-défaut-lors-du-rendu-des-feuilles-de-calcul-en-images/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

 // Create an instance of ImageOrPrintOptions

var options = new ImageOrPrintOptions();

// Set default font name for image rendering

options.DefaultFont = "Arial";

// Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the worksheet to be rendered

var sheet = book.Worksheets[0];

// Create an instance of SheetRender

var render = new SheetRender(sheet, options);

// Save spreadsheet to image

render.ToImage(0, dir + "output.png");

{{< /highlight >}}


### **Propriété ajoutée PivotTable.IsExcel2003Compatible**
L'API Aspose.Cells for .NET a exposé la propriété de type booléen IsExcel2003Compatible pour la classe PivotTable qui permet de spécifier si le tableau croisé dynamique est compatible avec Excel 2003 à des fins de rafraîchissement. La valeur par défaut de la propriété IsExcel2003Compatible est true, ce qui signifie qu'une chaîne doit être inférieure ou égale à 255 caractères. Si la chaîne est supérieure à 255 caractères, elle sera tronquée. Si elle est définie sur false, la restriction susmentionnée ne sera pas appliquée.

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article sur [Compatibilité pour Excel 2003 pour Actualiser les Tableaux Croisés Dynamiques](https://docs.aspose.com/cells/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**C#**

{{< highlight csharp >}}

 // Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the desired Pivot Table from the spreadsheet

var pivot = book.Worksheets[0].PivotTables[0];

// Set Excel 2003 compatibility to false

pivot.IsExcel2003Compatible = false;

// Refresh & recalculate Pivot Table

pivot.RefreshData();

pivot.CalculateData();

{{< /highlight >}}


### **Méthode GridWeb.GetVersion ajoutée**
Aspose.Cells.GridWeb pour .NET 8.9.0 a exposé la méthode d'usine {GetVersion}} qui renvoie la version de sortie du composant GridWeb.
{{< app/cells/assistant language="csharp" >}}
