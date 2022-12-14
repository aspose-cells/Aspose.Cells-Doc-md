---
title: Public API Changements dans Aspose.Cells 8.9.0
type: docs
weight: 310
url: /fr/java/public-api-changes-in-aspose-cells-8-9-0/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.8.3 à 8.9.0 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les méthodes publiques nouvelles et mises à jour, les classes ajoutées et supprimées, etc., mais également une description de tout changement de comportement dans les coulisses de Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Ajout de la propriété HtmlSaveOptions.DefaultFontName**
Aspose.Cells for Java 8.9.0 a exposé la propriété DefaultFontName pour la classe HtmlSaveOptions qui permet de spécifier le nom de la police par défaut lors du rendu des feuilles de calcul au format HTML. La police par défaut sera utilisée uniquement lorsque la police de style n'existe pas. La valeur par défaut de la propriété HtmlSaveOptions.DefaultFontName est null, ce qui signifie que Aspose.Cells for Java API utilisera la police universelle qui a la même famille que la police d'origine.

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article sur[Définition de la police par défaut pour le rendu des feuilles de calcul au format HTML](/cells/fr/java/set-default-font-while-rendering-spreadsheet-to/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set default font name for Html rendering

options.setDefaultFontName("Arial");

//Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.save(dir + "output.html", options);

{{< /highlight >}}
### **Ajout de la propriété ImageOrPrintOptions.DefaultFont**
Aspose.Cells for Java 8.9.0 permet de définir le nom de police par défaut pour la classe ImageOrPrintOptions en exposant la propriété DefaultFont. Ladite propriété peut être utilisée lorsque les caractères Unicode de la feuille de calcul ne sont pas définis avec la police correcte dans le style de cellule. Par conséquent, ces caractères peuvent apparaître sous forme de blocs dans les images résultantes.

{{% alert color="primary" %}} 

 Définissez la propriété DefaultFont sur MingLiu ou MS Gothic pour afficher les caractères Unicode. Si ladite propriété n'est pas définie, Aspose.Cells utilisera la police par défaut du système pour afficher les caractères Unicode.

{{% /alert %}} {{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article sur[Définition de la police par défaut pour le rendu des feuilles de calcul dans des formats d'image](/cells/fr/java/set-default-font-while-rendering-spreadsheet-to-images/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

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
### **Ajout de la propriété PivotTable.Excel2003Compatible**
Aspose.Cells for Java API a exposé la propriété Excel2003Compatible de type booléen pour la classe PivotTable qui permet de spécifier si le tableau croisé dynamique est compatible avec Excel 2003 à des fins de rafraîchissement. La valeur par défaut de la propriété Excel2003Compatible est true, ce qui signifie qu'une chaîne doit être inférieure ou égale à 255 caractères. Si la chaîne est supérieure à 255 caractères, elle sera tronquée. Si elle est fausse, la restriction susmentionnée ne sera pas imposée.

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article sur[Compatibilité pour Excel 2003 pour l'actualisation des tableaux croisés dynamiques](/cells/fr/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

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
