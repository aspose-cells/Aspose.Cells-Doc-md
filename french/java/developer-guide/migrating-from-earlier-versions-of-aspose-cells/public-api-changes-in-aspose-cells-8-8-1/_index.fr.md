﻿---
title: Public API Changements dans Aspose.Cells 8.8.1
type: docs
weight: 280
url: /fr/java/public-api-changes-in-aspose-cells-8-8-1/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.8.0 à 8.8.1 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les méthodes publiques nouvelles et mises à jour, les classes ajoutées et supprimées, etc., mais également une description de tout changement de comportement dans les coulisses de Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Filtrer les données pour le chargement**
Aspose.Cells for Java 8.8.1 a exposé l'énumération LoadDataFilterOptions avec la propriété LoadOptions.LoadDataFilterOptions qui peut être utilisée pour spécifier le type de données qui doit être chargé lors de la création du classeur à partir d'un fichier de modèle. Le filtrage des données chargées peut améliorer les performances à des fins particulières, en particulier lors de l'utilisation des API LightCells.

L'énumération LoadDataFilterOptions fournit les sélections suivantes.

1. ALL pour tout charger depuis la feuille de calcul.
1. NONE pour ne rien charger de la feuille de calcul.
1. CELL_BLANK charge les cellules dont les valeurs sont vides.
1. CELL_BOOL charge les cellules dont les valeurs sont booléennes.
1. CELL_DATA charge les données des cellules, y compris les valeurs, les formules et le formatage.
1. CELL_ERROR charge les cellules dont les valeurs sont erronées.
1. CELL_NUMERIC charge les cellules dont les valeurs sont numériques (y compris la date et l'heure).
1. CELL_STRING charge les cellules dont les valeurs sont text/string.
1. CELL_VALUE charge uniquement les valeurs de cellule (tous types).
1. CHART charge uniquement les graphiques.
1. CONDITIONAL_FORMATTING charge uniquement les règles de mise en forme conditionnelle.
1. DATA_VALIDATION charge uniquement les règles de validation des données.
1. DOCUMENT_PROPERTIES charge uniquement les propriétés du document.
1. FORMULA charge les formules incluant les noms définis.
1. MERGED_AREA charge uniquement les cellules fusionnées.
1. PIVOT_TABLE charge les tableaux croisés dynamiques.
1. PARAMÈTRES charge uniquement les paramètres du classeur et de la feuille de calcul.
1. SHAPE charge uniquement les formes.
1. STYLE charge le formatage des cellules.
1. TABLE charge les tableaux/listes d'objets Excel.

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur[Filtrer les données pour le chargement](/cells/fr/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

LoadOptions options = new LoadOptions(LoadFormat.XLSX);

//Set LoadDataFilterOptions to load only shapes

options.setLoadDataFilterOptions(LoadDataFilterOptions.SHAPE);

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

Workbook book = new Workbook(filePath, options);

{{< /highlight >}}
### **Convertir directement le graphique en PDF**
Les API Aspose.Cells ont déjà fourni la possibilité de rendre des graphiques à PDF tout en utilisant la méthode Chart.toPdf. Avec cette version, le API a exposé une autre version surchargée de ladite méthode qui pourrait accepter une instance de OutputStream, permettant aux utilisateurs d'enregistrer le PDF du graphique dans une instance de ByteArrayOutputStream.

Voici le scénario d'utilisation simple.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet with a chart

Workbook workbook = new Workbook(filePath);

//Access first worksheet containing a chart

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first chart from the worksheet

Chart chart = worksheet.getCharts().get(0);

//Save the chart to PDF as Stream

ByteArrayOutputStream outStream = new ByteArrayOutputStream();

chart.toPdf(outStream);

{{< /highlight >}}
### **Ajout de la propriété WorkbookSettings.PaperSize**
Aspose.Cells for Java 8.8.1 a exposé la propriété WorkbookSettings.PaperSize afin de définir la taille du papier d'impression par défaut pour l'ensemble de la feuille de calcul. La propriété WorkbookSettings.PaperSize accepte une valeur de l'énumération PaperSizeType qui contient les tailles prédéfinies pour les types de papier d'impression les plus largement utilisés.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook();

//Access WorkbookSettings from the Workbook

WorkbookSettings settings = book.getSettings();

//Set the default printing paper size for the Workbook

settings.setPaperSize(PaperSizeType.PAPER_A_4);

{{< /highlight >}}
### **Ajout de la propriété Shape.TextBody**
Cette version de Aspose.Cells for Java API a exposé le Shape.TextBody afin de manipuler les aspects du texte dans une forme. L'extrait de code suivant utilise ladite propriété pour définir l'effet d'ombre du texte dans un TextBox.

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur[Définition de l'effet d'ombre pour le texte](/cells/fr/java/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**Java**

{{< highlight "csharp" >}}

 //Créer une instance de Workbook

Livre de classeur = nouveau classeur ();

// Accéder à la première feuille de calcul du classeur

Feuille de calcul = book.getWorksheets().get(0);

//Ajouter un TextBox à la ShapeCollection

index int = feuille.getTextBoxes().add(2, 2, 100, 400);

TextBox textBox = feuille.getTextBoxes().get(index);

//Définir le texte du TextBox

textBox.setText("Ce texte a les paramètres suivants.\n\nEffets de texte > Ombre > Décalage en bas");

// Définir l'effet d'ombre pour le texte

 pour (int je = 0; je< textBox.getTextBody().getCount(); i++)

{

  textBox.getTextBody().get(i).getShapeFont().getFillFormat().getShadowEffect().setPresetType(PresetShadowType.OFFSET_BOTTOM);

}

{{< /highlight >}}
### **Ajout de la méthode Worksheet.calculateFormula(string formula, CalculationOptions opts)**
Aspose.Cells for Java 8.8.1 a exposé une autre surcharge pour la méthode Worksheet.calculateFormula qui permet de calculer directement une formule donnée avec des options personnalisées.

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur[Calcul direct de la fonction personnalisée](/cells/fr/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 
### **Ajout de la méthode GridCell.createValidation**
Aspose.Cells.GridWeb a fourni la possibilité d'ajouter directement la règle de validation à une seule cellule tout en utilisant la méthode GridCell.createValidation. Ladite méthode nécessite 2 paramètres. Le premier est de type GridValidationType qui détermine le type de validation, tandis que le second paramètre (isRequied) est de type Boolean.

**Java**

{{< highlight "csharp" >}}

 //Access first worksheet

GridWorksheet sheet = gridweb.getWorkSheets().get(0);

//Access cell B3

GridCell cell = sheet.getCells().get("B3");

//Add validation inside the GridCell

//Any value which is not between 20 and 40 will cause error in a GridCell

GridValidation val = cell.createValidation(GridValidationType.WHOLE_NUMBER, true);

val.setFormula1("=20");

val.setFormula2("=40");

val.setOperator(OperatorType.BETWEEN);

val.setShowError(true);

val.setShowInput(true);

{{< /highlight >}}
### **Ajout de la méthode GridCell.removeValidation**
Aspose.Cells.GridWeb a également fourni la possibilité de supprimer la règle de validation des données d'un GridCell tout en utilisant la méthode GridCell.removeValidation.
## **API obsolètes**
### **Propriété Shape.TextFrame obsolète**
Il est conseillé d'utiliser la propriété Shape.TextBody.TextAlignment à la place.
