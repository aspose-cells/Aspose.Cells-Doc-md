---
title: Public API Changements dans Aspose.Cells 8.7.0
type: docs
weight: 240
url: /fr/java/public-api-changes-in-aspose-cells-8-7-0/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.6.3 à 8.7.0 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les méthodes publiques nouvelles et mises à jour, les classes ajoutées et supprimées, etc., mais également une description de tout changement de comportement dans les coulisses de Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Prise en charge de l'optimisation PDF**
 Les API Aspose.Cells offrent déjà la possibilité de convertir des feuilles de calcul en PDF. Avec cette version du API, les utilisateurs peuvent désormais[optimiser la taille du PDF résultant](/cells/fr/java/save-excel-into-pdf-with-standard-or-minimum-size/)aussi bien. Aspose.Cells for Java 8.7.0 a exposé la propriété PdfSaveOptions.OptimizationType avec l'énumération PdfOptimizationType afin de permettre aux utilisateurs de choisir l'algorithme d'optimisation souhaité lors de l'exportation de feuilles de calcul au format PDF. Il existe 2 valeurs possibles pour la propriété PdfSaveOptions.OptimizationType comme détaillé ci-dessous.

1. PdfOptimizationType.MINIMUM_SIZE : la qualité est compromise pour la taille du fichier résultant.
1. PdfOptimizationType.STANDARD : la qualité n'est pas compromise, la taille du fichier résultant sera donc importante.

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of PdfSaveOptions

PdfSaveOptions pdfSaveOptions = new PdfSaveOptions();

//Set the OptimizationType property to desired value

pdfSaveOptions.setOptimizationType(PdfOptimizationType.MINIMUM_SIZE);

//Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook(inFilePath);

//Save the spreadsheet in PDF format while passing the instance of PdfSaveOptions

book.save(outFilePath, pdfSaveOptions);

{{< /highlight >}}
### **Détection d'un projet VBA signé numériquement**
 La propriété VbaProject.isSigned nouvellement exposée peut être utilisée pour[détecter si le projet VBA dans un classeur est signé numériquement](/cells/fr/java/check-if-vba-code-is-signed/). La propriété VbaProject.isSigned est de type booléen, qui renvoie true si le projet VBA est signé numériquement et vice versa.

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

VbaProject vbaProject = book.getVbaProject();

//Check if VbaProject is digitally signed

if (vbaProject.isSigned())

{

	System.out.println("VbaProject is digitally signed");

}

else

{

	System.out.println("VbaProject is not digitally signed");

}

{{< /highlight >}}
### **Méthode Protection.verifyPassword ajoutée**
Aspose.Cells Les API ont amélioré la classe Protection en introduisant la méthode verifyPassword qui permet de spécifier un mot de passe en tant qu'instance de String et[vérifie si le même mot de passe a été utilisé pour protéger la feuille de travail](/cells/fr/java/verify-password-used-to-protect-the-worksheet/). La méthode Protection.verifyPassword renvoie true si le mot de passe spécifié correspond au mot de passe utilisé pour protéger la feuille de calcul donnée, et false si le mot de passe spécifié ne correspond pas. Le morceau de code suivant utilise la méthode Protection.verifyPassword conjointement avec le champ Protection.isProtectedWithPassword pour détecter la protection par mot de passe et vérifie le mot de passe.

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load a spreadsheet

Workbook book = new Workbook(inFilePath);

//Access the protected Worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Check if Worksheet is password protected

if (sheet.getProtection().isProtectedWithPassword())

{

  //Verify the password used to protect the Worksheet

  if (sheet.getProtection().verifyPassword("password"))

  {

	  System.out.println("Specified password has matched");

  }

  else

  {

	  System.out.println("Specified password has not matched");

  }

}

{{< /highlight >}}
### **Propriété Protection.isProtectedWithPassword ajoutée**
 Cette version de Aspose.Cells for Java a également exposé le champ Protection.isProtectedWithPassword qui peut être utile dans[détecter si une feuille de travail est protégée par un mot de passe ou non](/cells/fr/java/detect-if-worksheet-is-password-protected/).

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(inFilePath);

//Access the desired Worksheet via its index or name

Worksheet sheet = book.getWorksheets().get(0);

//Access Protection module of desired Worksheet

Protection protection = sheet.getProtection();

//Check if Worksheet is password protected

if (protection.isProtectedWithPassword())

{

	System.out.println("Worksheet is password protected");

}

else

{

	System.out.println("Worksheet is not password protected");

}

{{< /highlight >}}
### **Propriété ColorScale.Is3ColorScale ajoutée**
 Aspose.Cells for Java 8.7.0 a exposé la propriété ColorScale.Is3ColorScale qui peut être utilisée pour[créer un format conditionnel d'échelle à 2 couleurs](/cells/fr/java/adding-2-color-scale-and-3-color-scale-conditional-formattings/). Ladite propriété est de type booléen avec la valeur par défaut true, ce qui signifie que le format conditionnel sera de 3-Color Scale par défaut. Toutefois, le fait de définir la propriété ColorScale.Is3ColorScale sur false générera un format conditionnel d'échelle à 2 couleurs.

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook();

//Access the Worksheet to which conditional formatting rule has to be added

Worksheet sheet = book.getWorksheets().get(0);

//Add FormatConditions to the collection

int index = sheet.getConditionalFormattings().add();

//Access newly added formatConditionCollection via its index

FormatConditionCollection formatConditionCollection = sheet.getConditionalFormattings().get(index);

//Create a CellArea on which conditional formatting rule will be applied

CellArea cellArea = CellArea.createCellArea("A1", "A5");

//Add conditional formatted cell range

formatConditionCollection.addArea(cellArea);

//Add format condition of type ColorScale

index = formatConditionCollection.addCondition(FormatConditionType.COLOR_SCALE);

//Access newly added format condition via its index

FormatCondition formatCondition = formatConditionCollection.get(index);

//Set Is3ColorScale to false in order to generate a 2-Color Scale format

formatCondition.getColorScale().setIs3ColorScale(false);

//Set other necessary properties

{{< /highlight >}}
### **Propriété TxtLoadOptions.HasFormula ajoutée**
 Aspose.Cells for Java 8.7.0 a fourni un support pour[identifier et analyser les formules lors du chargement de fichiers CSV/TXT ayant des données simples délimitées](/cells/fr/java/load-or-import-csv-file-with-formulas/). La propriété TxtLoadOptions.HasFormula nouvellement exposée, lorsqu'elle est définie sur true, ordonne au API d'analyser les formules du fichier délimité d'entrée et de les définir sur les cellules pertinentes sans nécessiter de traitement supplémentaire.

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of TxtLoadOptions

TxtLoadOptions options = new TxtLoadOptions();

//Set HasFormula property to true

options.setHasFormula(true);

//Set the Separator property as desired

options.setSeparator(',');

//Load the CSV/TXT file using the instance of TxtLoadOptions

Workbook book = new Workbook(inFilePath, options);

//Calculate formulas in order to get the calculated values of formula in CSV

book.calculateFormula();

//Write result in any of the supported formats

book.save(outFilePath);

{{< /highlight >}}
### **Propriété DataLabels.ResizeShapeToFitText ajoutée**
 Une autre fonctionnalité utile que Aspose.Cells for Java 8.7.0 a exposée est la propriété DataLabels.ResizeShapeToFitText qui peut activer le[redimensionner la forme pour l'adapter au texte](/cells/fr/java/resize-chart-s-data-label-shape-to-fit-text/) fonctionnalité de l'application Excel pour les étiquettes de données du graphique.

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook containing the Chart

Workbook book = new Workbook(inFilePath);

//Access the Worksheet that contains the Chart

Worksheet sheet = book.getWorksheets().get(0);

//Access the desired Chart via its index or name

Chart chart = sheet.getCharts().get(0);

//Access the DataLabels of desired NSeries

DataLabels labels = chart.getNSeries().get(0).getDataLabels();

//Set ResizeShapeToFitText property to true

labels.setResizeShapeToFitText(true);

//Calculate Chart

chart.calculate();

{{< /highlight >}}
## **API supprimées**
### **Propriété Workbook.SaveOptions supprimé**
La propriété Workbook.SaveOptions a été marquée comme obsolète il y a quelque temps. Avec cette version, il a été complètement supprimé du public API, il est donc conseillé d'utiliser la méthode Workbook.save(Stream, SaveOptions) ou Workbook.save(string, SaveOptions) comme alternative.
