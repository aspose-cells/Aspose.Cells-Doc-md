---
title: Public API Changements dans Aspose.Cells 8.8.1
type: docs
weight: 270
url: /fr/net/public-api-changes-in-aspose-cells-8-8-1/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.8.0 à 8.8.1 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les méthodes publiques nouvelles et mises à jour, les classes ajoutées et supprimées, etc., mais également une description de tout changement de comportement dans les coulisses de Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Filtrer les données pour le chargement**
Aspose.Cells for .NET 8.8.1 a exposé l'énumération LoadDataFilterOptions avec la propriété LoadOptions.LoadDataFilterOptions qui peut être utilisée pour spécifier le type de données qui doit être chargé lors de la création du classeur à partir d'un fichier de modèle. Le filtrage des données chargées peut améliorer les performances à des fins particulières, en particulier lors de l'utilisation des API LightCells.

L'énumération LoadDataFilterOptions fournit les sélections suivantes.

1. Tout pour tout charger depuis la feuille de calcul.
1. Aucun pour ne rien charger de la feuille de calcul.
1. CellBlank charge les cellules dont les valeurs sont vides.
1. CellBool charge les cellules dont les valeurs sont booléennes.
1. CellData charge les données des cellules, y compris les valeurs, les formules et le formatage.
1. CellError charge les cellules dont les valeurs sont erronées.
1. CellNumeric charge les cellules dont les valeurs sont numériques (y compris la date et l'heure).
1. CellString charge les cellules dont les valeurs sont text/string.
1. CellValue charge uniquement les valeurs de cellule (tous types).
1. Chart charge uniquement les graphiques.
1. ConditionalFormatting charge uniquement les règles de mise en forme conditionnelle.
1. DataValidation charge uniquement les règles de validation des données.
1. DocumentProperties charge uniquement les propriétés du document.
1. Formule charge les formules incluant les noms définis.
1. MergedArea charge uniquement les cellules fusionnées.
1. Tableau croisé dynamique charge les tableaux croisés dynamiques.
1. Paramètres charge uniquement les paramètres du classeur et de la feuille de calcul.
1. Forme charge uniquement les formes.
1. Style charge la mise en forme des cellules.
1. Le tableau charge les tableaux/listes d'objets Excel.

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur[Filtrer les données pour le chargement](/cells/fr/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

var options = new LoadOptions(LoadFormat.Xlsx);

//Set LoadDataFilterOptions to load only shapes

options.LoadDataFilterOptions = LoadDataFilterOptions.Shape;

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

var book = new Workbook(filePath, options);

{{< /highlight >}}


### **Convertir directement le graphique en PDF**
Aspose.Cells Les API ont déjà fourni la possibilité de rendre des graphiques au format PDF tout en utilisant la méthode Chart.ToPdf. Avec cette version, le API a exposé une autre version surchargée de ladite méthode qui pourrait accepter une instance de Stream, permettant aux utilisateurs d'enregistrer le PDF du graphique dans une instance de MemoryStream.

Voici le scénario d'utilisation simple.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook and load an existing spreadsheet with a chart

var workbook = new Workbook(filePath);

//Access first worksheet containing a chart

var worksheet = workbook.Worksheets[0];

//Access first chart from the worksheet

var chart = worksheet.Charts[0];

//Save the chart to PDF as Stream

using (MemoryStream stream = new MemoryStream())

{

    chart.ToPdf(stream);

}

{{< /highlight >}}


### **Ajout de la propriété WorkbookSettings.PaperSize**
Aspose.Cells for .NET 8.8.1 a exposé la propriété WorkbookSettings.PaperSize afin de définir la taille du papier d'impression par défaut pour l'ensemble de la feuille de calcul. La propriété WorkbookSettings.PaperSize accepte une valeur de l'énumération PaperSizeType qui contient les tailles prédéfinies pour les types de papier d'impression les plus largement utilisés.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access WorkbookSettings from the Workbook

var settings = book.Settings;

//Set the default printing paper size for the Workbook

settings.PaperSize = PaperSizeType.PaperA4;

{{< /highlight >}}


### **Ajout de la propriété Shape.TextBody**
Cette version de Aspose.Cells for .NET API a exposé le Shape.TextBody afin de manipuler les aspects du texte dans une forme. L'extrait de code suivant utilise ladite propriété pour définir l'effet d'ombre du texte dans un TextBox.

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur[Définition de l'effet d'ombre pour le texte](/cells/fr/net/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**C#**

{{< highlight "csharp" >}}

 //Créer une instance de Workbook

var livre = nouveau classeur();

// Accéder à la première feuille de calcul du classeur

var feuille = livre. Feuilles de travail [0] ;

//Ajouter un TextBox à la ShapeCollection

var textBox = feuille.Shapes.AddTextBox(2, 0, 2, 0, 100, 400);

//Définir le texte du TextBox

textBox.Text = "Ce texte a les paramètres suivants.\n\nEffets de texte > Ombre > Décalage en bas" ;

// Définir l'effet d'ombre pour le texte

 pour (int je = 0; je< textBox.TextBody.Count; i++)

{

    textBox.TextBody[i].ShapeFont.FillFormat.ShadowEffect.PresetType = PresetShadowType.OffsetBottom;

}

{{< /highlight >}}


### **Ajout de la méthode Worksheet.CalculateFormula(string formula, CalculationOptions opts)**
Aspose.Cells for .NET 8.8.1 a exposé une autre surcharge pour la méthode CalculateFormula qui offre la possibilité de calculer une formule donnée directement avec des options personnalisées.

{{% alert color="primary" %}} 

 Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur[Calcul direct de la fonction personnalisée](/cells/fr/net/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 
### **Ajout de la méthode GridCell.CreateValidation**
Aspose.Cells.GridWeb a fourni la possibilité d'ajouter directement la règle de validation à une seule cellule tout en utilisant la méthode GridCell.CreateValidation. Ladite méthode nécessite 2 paramètres. Le premier est de type GridValidationType qui détermine le type de validation, tandis que le second paramètre (isRequied) est de type Boolean.



**C#**

{{< highlight "csharp" >}}

 //Access first worksheet

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B3

GridCell cell = sheet.Cells["B3"];

//Add validation inside the GridCell

//Any value which is not between 20 and 40 will cause error in a GridCell

GridValidation val = cell.CreateValidation(GridValidationType.WholeNumber, true);

val.Formula1 = "=20";

val.Formula2 = "=40";

val.Operator = GridOperatorType.Between;

val.ShowError = true;

val.ShowInput = true;

{{< /highlight >}}


### **Ajout de la méthode GridCell.RemoveValidation**
Aspose.Cells.GridWeb a également fourni la possibilité de supprimer la règle de validation des données d'un GridCell tout en utilisant la méthode GridCell.RemoveValidation.
## **API obsolètes**
### **Propriété Shape.TextFrame obsolète**
Il est conseillé d'utiliser la propriété Shape.TextBody.TextAlignment à la place.
