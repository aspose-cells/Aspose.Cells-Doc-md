---
title: Public API Changements dans Aspose.Cells 8.6.2
type: docs
weight: 210
url: /fr/net/public-api-changes-in-aspose-cells-8-6-2/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.6.1 à 8.6.2 qui peuvent intéresser les développeurs de modules/applications. Il comprend non seulement des méthodes publiques nouvelles et mises à jour, des classes ajoutées, mais également une description de tout changement de comportement en coulisse dans Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Prise en charge du rappel avec des marqueurs intelligents**
 Cette version de Aspose.Cells for .NET API a exposé la propriété WorkbookDesigner.CallBack et l'interface ISmartMarkerCallBack qui, ensemble, permettent de[obtenir les notifications concernant la référence de cellule et/ou le marqueur intelligent en cours de traitement](/cells/fr/net/getting-notifications-while-merging-data-with-smart-markers/). Le morceau de code suivant illustre l'utilisation de l'interface ISmartMarkerCallBack pour définir une nouvelle classe qui gère le rappel de la méthode WorkbookDesigner.Process.

**C#**

{{< highlight "csharp" >}}

 class SmartMarkerCallBack : ISmartMarkerCallBack

{

    Workbook workbook;

    internal SmartMarkerCallBack(Workbook workbook)

    {

        this.workbook = workbook;

    }

    public void Process(int sheetIndex, int rowIndex, int colIndex, string tableName, string columnName)

    {

        Console.WriteLine("Processing Cell : " + workbook.Worksheets[sheetIndex].Name + "!" + CellsHelper.CellIndexToName(rowIndex, colIndex));

        Console.WriteLine("Processing Marker : " + tableName + "." + columnName);

    }

}

{{< /highlight >}}



Le reste du processus comprend le chargement de la feuille de calcul du concepteur contenant les marqueurs intelligents avec WorkbookDesigner et son traitement en définissant la source de données. Cependant, pour activer les notifications, il est nécessaire de définir la propriété WorkbookDesigner.CallBack avant d'appeler la méthode WorkbookDesigner.Process, comme illustré ci-dessous.

**C#**

{{< highlight "csharp" >}}

 //Loading the designer spreadsheet in an instance of Workbook

Workbook workbook = new Workbook(inputFilePath);

//Loading the instance of Workbook in an instance of WorkbookDesigner

WorkbookDesigner designer = new WorkbookDesigner(workbook);

//Set the WorkbookDesigner.CallBack property to an instance of newly created class

designer.CallBack = new SmartMarkerCallBack(workbook);

//Set the data source 

designer.SetDataSource(table);

//Process the Smart Markers in the designer spreadsheet

designer.Process(false);

{{< /highlight >}}


### **Méthode Chart.ToPdf ajouté**
 Aspose.Cells for .NET 8.6.2 a exposé la méthode Chart.ToPdf qui peut être utilisée pour[rendre directement la forme du graphique au format PDF](/cells/fr/net/convert-an-excel-chart-to-image/). Ladite méthode accepte actuellement un paramètre de type chaîne comme emplacement de chemin de fichier pour stocker le fichier résultant sur le disque.

Voici le scénario d'utilisation simple.

**C#**

{{< highlight "csharp" >}}

 //Load spreadsheet containing charts

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first chart inside the worksheet

Chart chart = worksheet.Charts[0];

//Save the chart in PDF format

chart.ToPdf(outputFilePath);

{{< /highlight >}}


### **Méthode Workbook.RemoveUnusedStyles ajouté**
 Aspose.Cells for .NET 8.6.2 a exposé la méthode Workbook.RemoveUnusedStyles qui peut être utilisée pour[supprimer tous les objets Style inutilisés du pool de styles](/cells/fr/net/remove-unused-styles-inside-the-workbook/).

Voici le scénario d'utilisation simple.

**C#**

{{< highlight "csharp" >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.RemoveUnusedStyles();

{{< /highlight >}}


### **Propriété Cells.Style ajouté**
La propriété Cells.Style peut être utilisée pour accéder au style de la feuille de calcul représentant le style par défaut.

Voici le scénario d'utilisation simple.

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.Worksheets[0].Cells.Style;

{{< /highlight >}}


### **Événements ajoutés pour GridWeb**
Aspose.Cells.GridWeb for .NET 8.6.2 a exposé les deux nouveaux événements suivants.

1. AjaxCallFinished : se déclenche lorsque la mise à jour AJAX du contrôle est terminée. (EnableAJAX doit être défini sur true).
1. CellModifiedOnAjax : se déclenche lorsque la cellule est modifiée dans l'appel AJAX.
