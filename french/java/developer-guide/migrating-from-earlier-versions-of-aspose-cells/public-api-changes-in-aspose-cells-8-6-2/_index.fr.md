---
title: Changements d API publics dans Aspose.Cells 8.6.2
type: docs
weight: 220
url: /fr/java/public-api-changes-in-aspose-cells-8-6-2/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.6.1 à la version 8.6.2 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement de nouvelles et mises à jour des méthodes publiques, des classes ajoutées, mais également une description de tout changement dans le comportement en coulisse d'Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Support pour le rappel avec les marqueurs intelligents**
Cette version de l'API Aspose.Cells for Java a exposé le champ WorkbookDesigner.CallBack et l'interface ISmartMarkerCallBack qui permettent ensemble de [recevoir les notifications sur la référence de la cellule et/ou le marqueur intelligent en cours de traitement](/cells/fr/java/getting-notifications-while-merging-data-with-smart-markers/). Le morceau de code suivant démontre l'utilisation de l'interface ISmartMarkerCallBack pour définir une nouvelle classe qui gère le rappel pour la méthode WorkbookDesigner.process. 

**Java**

{{< highlight csharp >}}

 public class SmartMarkerCallBack implements ISmartMarkerCallBack 

{

	Workbook workbook;

	SmartMarkerCallBack(Workbook workbook)

	{

	    this.workbook = workbook;

	}



	@Override

	public void process(int sheetIndex, int rowIndex, int colIndex, String tableName, String columnName)

	{

	    System.out.println("Processing Cell : " + workbook.getWorksheets().get(sheetIndex).getName() + "!" + CellsHelper.cellIndexToName(rowIndex, colIndex));

	    System.out.println("Processing Marker : " + tableName + "." + columnName);

	}

}

{{< /highlight >}}

Le reste du processus consiste à charger la feuille de calcul du concepteur contenant les marqueurs intelligents avec WorkbookDesigner ou en créer une à partir de zéro et la traiter en définissant la source de données. Cependant, pour activer les notifications, il est nécessaire de définir la propriété WorkbookDesigner.CallBack avant d'appeler la méthode WorkbookDesigner.process comme démontré ci-dessous.

**Java**

{{< highlight csharp >}}

 //Instantiate a new Workbook designer

WorkbookDesigner report = new WorkbookDesigner();

//Get the first worksheet of the workbook

Worksheet sheet = report.getWorkbook().getWorksheets().get(0);

//Set the Variable Array marker to a cell

//You may also place this Smart Marker into a template file manually using Excel and then open this file via WorkbookDesigner 

sheet.getCells().get("A1").putValue("&=$VariableArray");

//Set the data source for the marker(s)

report.setDataSource("VariableArray", new String[] { "English", "Arabic", "Hindi", "Urdu", "French" });

//Set the CallBack property

report.setCallBack(new SmartMarkerCallBack(report.getWorkbook()));

//Process the markers

report.process(false);

{{< /highlight >}}
### **Ajout de la méthode Chart.toPdf**
Aspose.Cells for Java 8.6.2 a exposé la méthode Chart.toPdf qui peut être utilisée pour rendre directement la forme du graphique au format PDF. La méthode en question accepte actuellement un paramètre de type String en tant qu'emplacement du fichier pour stocker le fichier résultant sur le disque.

Voici le scénario d'utilisation simple.

**Java**

{{< highlight csharp >}}

 //Load spreadsheet containing charts

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first chart inside the worksheet

Chart chart = worksheet.getCharts().get(0);

//Save the chart in PDF format

chart.toPdf(outputFilePath);

{{< /highlight >}}
### **Ajout de la méthode Workbook.removeUnusedStyles**
Aspose.Cells for Java 8.6.2 a exposé la méthode Workbook.removeUnusedStyles qui peut être utilisée pour [supprimer tous les objets de style inutilisés de la pool de styles](/cells/fr/java/remove-unused-styles-inside-the-workbook/). 

Voici le scénario d'utilisation simple.

**Java**

{{< highlight csharp >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.removeUnusedStyles();

{{< /highlight >}}
### **Ajout de la propriété Cells.Style**
La propriété Cells.Style peut être utilisée pour accéder au style pour la feuille de calcul représentant le style par défaut.

Voici le scénario d'utilisation simple.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.getWorksheets().get(0).getCells().getStyle();

{{< /highlight >}}
### **Événements ajoutés pour GridWeb**
Aspose.Cells.GridWeb for Java 8.6.2 a exposé les deux nouveaux événements suivants.

1. AjaxCallFinished: Se déclenche lorsque la mise à jour AJAX du contrôle est terminée. (EnableAJAX doit être défini sur true).
1. CellModifiedOnAjax: Se déclenche lorsque la cellule est modifiée dans l'appel AJAX.
{{< app/cells/assistant language="java" >}}
