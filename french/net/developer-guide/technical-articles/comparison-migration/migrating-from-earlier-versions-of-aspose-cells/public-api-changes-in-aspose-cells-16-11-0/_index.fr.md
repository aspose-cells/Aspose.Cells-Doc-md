---
title: Changements d API public dans Aspose.Cells 16.11.0
type: docs
weight: 350
url: /fr/net/public-api-changes-in-aspose-cells-16-11-0/
---

{{% alert color="primary" %}} 

Ce document décrit les modifications apportées à l'API Aspose.Cells de la version 16.10.0 à la version 16.11.0 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les nouvelles méthodes publiques et mises à jour, les classes ajoutées et supprimées, etc., mais aussi une description de tout changement dans le comportement en coulisses dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Prise en charge des paramètres de globalisation**
Aspose.Cells 16.11.0 a exposé la classe GlobalizationSettings ainsi que la propriété WorkbookSettings.GlobalizationSettings afin d'obliger les API Aspose.Cells à utiliser des libellés personnalisés pour les sous-totaux. La classe GlobalizationSettings possède les méthodes suivantes qui peuvent être remplacées dans l'implémentation personnalisée pour donner des noms désirés aux libellés **Total** & **Total général**.

- GlobalizationSettings.GetTotalName: Obtient le nom total de la fonction.
- GlobalizationSettings.GetGrandTotalName: Obtient le nom du grand total de la fonction.

Voici une simple classe personnalisée qui étend la classe GlobalizationSettings et remplace ses méthodes susmentionnées pour renvoyer des libellés personnalisés pour la fonction de consolidation Average.

**C#**

{{< highlight csharp >}}

 class CustomSettings : GlobalizationSettings

{

    public override string GetTotalName(ConsolidationFunction functionType)

    {

        switch (functionType)

        {

            case ConsolidationFunction.Average:

                return "AVG";

            default:

                return base.GetTotalName(functionType);

        }

    }

    public override string GetGrandTotalName(ConsolidationFunction functionType)

    {

        switch (functionType)

        {

            case ConsolidationFunction.Average:

                return "GRD AVG";

            default:

                return base.GetGrandTotalName(functionType);

        }

    }

}

{{< /highlight >}}



Le code suivant charge une feuille de calcul existante et ajoute le sous-total de type Moyenne sur les données déjà disponibles dans la feuille de calcul. La classe CustomSettings et ses méthodes GetTotalName & GetGrandTotalName seront appelées au moment d'ajouter le sous-total à la feuille de calcul.

**C#**

{{< highlight csharp >}}

 // Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

// Assigns the GlobalizationSettings property of the WorkbookSettings class

// to the class created in first step

book.Settings.GlobalizationSettings = new Cells.CustomSettings();

// Accesses the 1st worksheet from the collection which contains data

// Data resides in the cell range A2:B9

Worksheet sheet = book.Worksheets[0];

// Adds SubTotal of type Average to the worksheet

sheet.Cells.Subtotal(CellArea.CreateCellArea("A2", "B9"), 0, ConsolidationFunction.Average, new int[] { 0,1 });

// Calculates Formulas

book.CalculateFormula();

// Auto fits all columns

sheet.AutoFitColumns();

// Saves the workbook on disc

book.Save(dir + "output.xlsx");

{{< /highlight >}}



La classe GlobalizationSettings offre également la méthode GetOtherName qui est utile pour obtenir le nom des libellés "Autre" pour les graphiques circulaires. Voici un scénario d'utilisation simple de la méthode GlobalizationSettings.GetOtherName.

**C#**

{{< highlight csharp >}}

 class CustomSettings : GlobalizationSettings

{

    public override string GetOtherName()

    {

        int lcid = System.Globalization.CultureInfo.CurrentCulture.LCID;

        switch (lcid)

        {

            case 1033:

                return "Other";

            case 1036:

                return "Autre";

            case 1031:

                return "Andere";

            //Do other case

            default:

                return base.GetOtherName();

        }

    }

}

{{< /highlight >}}



L'extrait suivant charge une feuille de calcul existante contenant un diagramme circulaire, et rend le diagramme en image en utilisant la classe CustomSettings créée ci-dessus.

**C#**

{{< highlight csharp >}}

 // Loads an existing spreadsheet containing a pie chart

Workbook book = new Workbook(dir + "sample.xlsx");

// Assigns the GlobalizationSettings property of the WorkbookSettings class

// to the class created in first step

book.Settings.GlobalizationSettings = new Cells.CustomSettings();

// Accesses the 1st worksheet from the collection which contains pie chart

Worksheet sheet = book.Worksheets[0];

// Accesses the 1st chart from the collection

Chart chart = sheet.Charts[0];

// Refreshes the chart

chart.Calculate();

// Renders the chart to image

chart.ToImage(dir + "output.png", new ImageOrPrintOptions());

{{< /highlight >}}


### **Classe CellsFactory ajoutée**
Aspose.Cells 16.11.0 a exposé la classe CellsFactory qui a actuellement une méthode, c'est-à-dire; CreateStyle. La méthode CellsFactory.CreateStyle peut être utilisée pour créer une instance de la classe Style sans l'ajouter au pool de styles du classeur.

Voici un scénario d'utilisation simple de la méthode CellsFactory.CreateStyle.

**C#**

{{< highlight csharp >}}

 // Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

// Creates an instance of Style

Style style = factory.CreateStyle();

{{< /highlight >}}


### **Propriété Workbook.AbsolutePath ajoutée**
Aspose.Cells 16.11.0 a exposé la propriété Workbook.AbsolutePath qui permet d'obtenir ou de définir le chemin absolu du classeur stocké dans le fichier workbook.xml. Cette propriété est utile lors de la mise à jour des liens externes uniquement.
### **Méthode GridHyperlinkCollection.GetHyperlink ajoutée**
Aspose.Cells.GridWeb 16.11.0 a exposé la méthode GetHyperlink de la classe GridHyperlinkCollection qui permet d'obtenir l'instance de GridHyperlink en passant soit une instance de GridCell, soit une paire d'entiers correspondant aux indices des lignes et colonnes.

{{% alert color="primary" %}} 

Dans le cas où aucun lien hypertexte n'a été trouvé sur la cellule spécifiée, la méthode GetHyperlink renverrait null.

{{% /alert %}} 

Voici un scénario d'utilisation simple de la méthode GetHyperlink.

**C#**

{{< highlight csharp >}}

 // Gets the active worksheet from the collection

GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];

// Accesses the GridHyperlinkCollection

GridHyperlinkCollection links = sheet.Hyperlinks;

// Gets hyperlink from cell A1

GridHyperlink link = links.GetHyperlink(sheet.Cells["A1"]);

// Gets hyperlink from cell D1

link = links.GetHyperlink(0, 3);

{{< /highlight >}}
## **APIs obsolètes**
### **Constructeur de style obsolète**
Veuillez utiliser la méthode cellsFactory.CreateStyle comme alternative.
## **APIs supprimées**
### **Méthode Cell.GetConditionalStyle supprimée**
Veuillez utiliser la méthode Cell.GetConditionalFormattingResult à la place.
### **Méthode Deleted Cells.MaxDataRowInColumn(int column)**
Veuillez utiliser la méthode Cells.GetLastDataRow(int) comme solution de remplacement.
### **Propriété PageSetup.Draft supprimée**
Il est conseillé d'utiliser la propriété PageSetup.PrintDraft à la place.
### **Propriété AutoFilter.FilterColumnCollection supprimée**
Veuillez envisager d'utiliser la propriété AutoFilter.FilterColumns pour atteindre le même objectif.
### **Propriété TickLabels.Rotation supprimée**
Veuillez utiliser la propriété TickLabels.RotationAngle à la place.
