---
title: Public API Changements dans Aspose.Cells 16.11.0
type: docs
weight: 360
url: /fr/java/public-api-changes-in-aspose-cells-16-11-0/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 16.10.0 à 16.11.0 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les méthodes publiques nouvelles et mises à jour, les classes ajoutées et supprimées, etc., mais également une description de tout changement de comportement dans les coulisses de Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Prise en charge des paramètres de globalisation**
Aspose.Cells 16.11.0 a exposé la classe GlobalizationSettings avec la propriété WorkbookSettings.GlobalizationSettings afin de forcer les API Aspose.Cells à utiliser des étiquettes personnalisées pour les sous-totaux. La classe GlobalizationSettings a les méthodes suivantes qui peuvent être remplacées dans l'implémentation personnalisée pour donner les noms souhaités aux étiquettes**Total** & **Total**.

- GlobalizationSettings.getTotalName : obtient le nom total de la fonction.
- GlobalizationSettings.getGrandTotalName : obtient le nom du total général de la fonction.

Voici une classe personnalisée simple qui étend la classe GlobalizationSettings et remplace ses méthodes susmentionnées pour renvoyer des étiquettes personnalisées pour la fonction de consolidation Moyenne.

**Java**

{{< highlight "csharp" >}}

 public class CustomSettings extends GlobalizationSettings

{    

    public String getTotalName(int functionType)

    {

    	 switch (functionType)

         {

             case ConsolidationFunction.AVERAGE:

                 return "AVG";

             default:

                return super.getTotalName(functionType);

         }

    }

    public String getGrandTotalName(int functionType)

    {

    	 switch (functionType)

         {

             case ConsolidationFunction.AVERAGE:

                 return "GRAND AVG";

             default:

            	 return super.getGrandTotalName(functionType);

         }



    }

}

{{< /highlight >}}

L'extrait de code suivant charge une feuille de calcul existante et ajoute le sous-total de type Moyenne aux données déjà disponibles dans la feuille de calcul. La classe CustomSettings et ses méthodes getTotalName & getGrandTotalName seront appelées au moment de l'ajout de Subtotal à la feuille de calcul.

**Java**

{{< highlight "csharp" >}}

 //Loads an existing spreadsheet containing some data

Workbook book = new Workbook(dir + "sample.xlsx");

//Assigns the GlobalizationSettings property of the WorkbookSettings class

//to the class created in first step

book.getSettings().setGlobalizationSettings(new CustomSettings());

//Accesses the 1st worksheet from the collection which contains data

//Data resides in the cell range A2:B9

Worksheet sheet = book.getWorksheets().get(0);

//Adds SubTotal of type Average to the worksheet

sheet.getCells().subtotal(CellArea.createCellArea("A2", "B9"), 0, ConsolidationFunction.AVERAGE, new int[]{ 0,1 });

//Calculates Formulas

book.calculateFormula();

//Auto fits all columns

sheet.autoFitColumns();

//Saves the workbook on disc

book.save(dir + "output.xlsx");

{{< /highlight >}}

La classe GlobalizationSettings propose également la méthode getOtherName qui est utile pour obtenir le nom des étiquettes "Autre" pour les camemberts. Voici un scénario d'utilisation simple de la méthode GlobalizationSettings.getOtherName.

**Java**

{{< highlight "csharp" >}}

 public class CustomSettings extends GlobalizationSettings

{ 

	public String getOtherName()

	{

		String language = Locale.getDefault().getLanguage();

		System.out.println(language);

		switch (language)

		{

			case "en":

				return "Other";

			case "fr":

				return "Autre";

			case "de":

				return "Andere";

			//Do other cases

			default:

				return super.getOtherName();

		}

	}

}

{{< /highlight >}}

L'extrait de code suivant charge une feuille de calcul existante contenant un graphique à secteurs et affiche le graphique en image tout en utilisant la classe CustomSettings créée ci-dessus.

**Java**

{{< highlight "csharp" >}}

 //Loads an existing spreadsheet containing a pie chart

Workbook book = new Workbook(dir + "sample.xlsx");

//Assigns the GlobalizationSettings property of the WorkbookSettings class

//to the class created in first step

book.getSettings().setGlobalizationSettings(new CustomSettings());

//Accesses the 1st worksheet from the collection which contains pie chart

Worksheet sheet = book.getWorksheets().get(0);

//Accesses the 1st chart from the collection

Chart chart = sheet.getCharts().get(0);

//Refreshes the chart

chart.calculate();

//Renders the chart to image

chart.toImage(dir + "output.png", new ImageOrPrintOptions());

{{< /highlight >}}
### **Classe CellsFactory ajoutée**
Aspose.Cells 16.11.0 a exposé la classe CellsFactory qui a actuellement une méthode, c'est-à-dire ; créerStyle. La méthode CellsFactory.createStyle peut être utilisée pour créer une instance de la classe Style sans l'ajouter au pool de styles de classeur.

Voici un scénario d'utilisation simple de la méthode CellsFactory.createStyle.

**Java**

{{< highlight "csharp" >}}

 //Initializes the CellsFactory class

CellsFactory factory = new CellsFactory();

//Creates an instance of Style

Style style = factory.createStyle();

{{< /highlight >}}
### **Ajout de la propriété Workbook.AbsolutePath**
Aspose.Cells 16.11.0 a exposé la propriété Workbook.AbsolutePath permettant d'obtenir ou de définir le chemin absolu du classeur stocké dans le fichier workbook.xml. Cette propriété est utile lors de la mise à jour des liens externes uniquement.
### **Ajout de la méthode GridHyperlinkCollection.getHyperlink**
Aspose.Cells.GridWeb 16.11.0 a exposé la méthode getHyperlink à la classe GridHyperlinkCollection qui permet d'obtenir l'instance de GridHyperlink en transmettant une instance GridCell ou une paire d'entiers correspondant aux indices de colonne de ligne.

{{% alert color="primary" %}} 

Si aucun lien hypertexte n'a été trouvé sur la cellule spécifiée, la méthode getHyperlink renverra null.

{{% /alert %}} 

Voici un scénario d'utilisation simple de la méthode getHyperlink.

**Java**

{{< highlight "csharp" >}}

 //Gets the active worksheet from the collection

GridWorksheet sheet = gridWeb1.getWorkSheets().get(gridWeb1.getActiveSheetIndex());

//Accesses the GridHyperlinkCollection

GridHyperlinkCollection links = sheet.getHyperlinks();

//Gets hyperlink from cell A1

GridHyperlink link = links.getHyperlink(sheet.getCells().get("A1"));

//Gets hyperlink from cell D1

link = links.getHyperlink(0, 3);

{{< /highlight >}}
## **API obsolètes**
### **Constructeur de style obsolète**
Veuillez utiliser la méthode cellsFactory.createStyle comme alternative.
## **API supprimées**
### **Méthode Cell.getConditionalStyle supprimée**
Veuillez utiliser la méthode Cell.getConditionalFormattingResult à la place.
### **Méthode Cells.getMaxDataRowInColumn(int column) supprimée**
Veuillez utiliser la méthode Cells.getLastDataRow(int) comme alternative.
### **Propriété PageSetup.Draft supprimée**
Il est conseillé d'utiliser à la place la propriété PageSetup.PrintDraft.
### **Propriété AutoFilter.FilterColumnCollection supprimée**
Veuillez envisager d'utiliser la propriété AutoFilter.FilterColumns pour atteindre le même objectif.
### **Propriété TickLabels.Rotation supprimée**
Veuillez utiliser la propriété TickLabels.RotationAngle à la place.
