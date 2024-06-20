---
title: Changements dans l API publique dans Aspose.Cells 8.9.0
type: docs
weight: 310
url: /fr/java/public-api-changes-in-aspose-cells-8-9-0/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.8.3 à la 8.9.0 qui pourraient intéresser les développeurs de modules/applications. Il comprend non seulement les nouvelles méthodes publiques, les classes ajoutées et supprimées, mais aussi une description de tout changement dans le comportement en coulisse dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Propriété HtmlSaveOptions.DefaultFontName ajoutée**
Aspose.Cells for Java 8.9.0 a exposé la propriété DefaultFontName pour la classe HtmlSaveOptions qui permet de spécifier le nom de police par défaut lors du rendu des feuilles de calcul au format HTML. La police par défaut ne sera utilisée que si la police du style n'existe pas. La valeur par défaut de la propriété HtmlSaveOptions.DefaultFontName est nulle, ce qui signifie que l'API Aspose.Cells for Java utilisera la police universelle qui a la même famille que la police d'origine.

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article sur [Définir la police par défaut pour le rendu de feuilles de calcul au format HTML](/cells/fr/java/set-default-font-while-rendering-spreadsheet-to/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**Java**

{{< highlight csharp >}}

 //Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set default font name for Html rendering

options.setDefaultFontName("Arial");

//Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.save(dir + "output.html", options);

{{< /highlight >}}
### **Propriété ajoutée ImageOrPrintOptions.DefaultFont**
Aspose.Cells for Java 8.9.0 permet de définir le nom de police par défaut pour la classe ImageOrPrintOptions en exposant la propriété DefaultFont. Ladite propriété peut être utilisée lorsque les caractères Unicode dans la feuille de calcul ne sont pas définis avec la police correcte dans le style de cellule et que ces caractères peuvent apparaître comme des blocs dans les images résultantes. 

{{% alert color="primary" %}} 

Définissez la propriété DefaultFont sur MingLiu ou MS Gothic pour afficher des caractères Unicode. Si ladite propriété n'est pas définie, Aspose.Cells utilisera la police par défaut du système pour afficher les caractères Unicode. 

{{% /alert %}} {{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article sur [Définir la police par défaut pour le rendu de feuilles de calcul dans les formats d'image](/cells/fr/java/set-default-font-while-rendering-spreadsheet-to-images/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**Java**

{{< highlight csharp >}}

 //Create an instance of ImageOrPrintOptions

ImageOrPrintOptions options = new ImageOrPrintOptions();

//Set default font name for image rendering

options.setDefaultFont("Arial");

//Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Access the worksheet to be rendered

Worksheet sheet = book.getWorksheets().get(0);

//Create an instance of SheetRender

SheetRender render = new SheetRender(sheet, options);

//Save spreadsheet to image

render.toImage(0, dir + "output.png");

{{< /highlight >}}
### **Propriété PivotTable.Excel2003Compatible ajoutée**
L'API Aspose.Cells for Java a exposé la propriété Excel2003Compatible de type booléen pour la classe PivotTable qui permet de spécifier si le PivotTable est compatible avec Excel 2003 à des fins de rafraîchissement. La valeur par défaut de la propriété Excel2003Compatible est true, ce qui signifie qu'une chaîne doit être inférieure ou égale à 255 caractères. Si la chaîne est supérieure à 255 caractères, elle sera tronquée. Si elle est définie sur false, la restriction susmentionnée ne sera pas imposée.

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article sur [Compatibilité pour Excel 2003 pour la actualisation des tableaux croisés dynamiques](/cells/fr/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Access the desired Pivot Table from the spreadsheet

PivotTable pivot = book.getWorksheets().get(0).getPivotTables().get(0);

//Set Excel 2003 compatibility to false

pivot.setExcel2003Compatible(false);

//Refresh & recalculate Pivot Table

pivot.refreshData();

pivot.calculateData();

{{< /highlight >}}
