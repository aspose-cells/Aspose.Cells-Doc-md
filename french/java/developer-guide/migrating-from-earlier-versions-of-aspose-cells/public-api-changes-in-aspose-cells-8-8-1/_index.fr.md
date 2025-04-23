---
title: Changements apportés à l API publique dans Aspose.Cells 8.8.1
type: docs
weight: 280
url: /fr/java/public-api-changes-in-aspose-cells-8-8-1/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 8.8.0 à la 8.8.1 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement de nouvelles méthodes publiques, des classes ajoutées et supprimées, etc., mais aussi une description de tout changement de comportement en arrière-plan dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Filtrer les données à charger**
Aspose.Cells for Java 8.8.1 a exposé l'énumération LoadDataFilterOptions ainsi que la propriété LoadOptions.LoadDataFilterOptions qui peut être utilisée pour spécifier le type de données à charger lors de la construction du classeur à partir d'un fichier modèle. Filtrer les données chargées peut améliorer les performances à des fins spéciales, notamment lors de l'utilisation des API LightCells.

L'énumération LoadDataFilterOptions propose les sélections suivantes.

1. TOUT pour charger tout à partir de la feuille de calcul.
1. AUCUN pour ne rien charger à partir de la feuille de calcul.
1. CELL_BLANK charge les cellules dont les valeurs sont vides.
1. CELL_BOOL charge les cellules dont les valeurs sont booléennes.
1. CELL_DATA charge les données des cellules, y compris les valeurs, les formules et la mise en forme.
1. CELL_ERROR charge les cellules dont les valeurs sont des erreurs.
1. CELL_NUMERIC charge les cellules dont les valeurs sont numériques (y compris les dates et heures).
1. CELL_STRING charge les cellules dont les valeurs sont du texte/une chaîne de caractères.
1. CELL_VALUE charge uniquement les valeurs des cellules (tous types).
1. CHART ne charge que les graphiques.
1. CONDITIONAL_FORMATTING ne charge que les règles de formatage conditionnel.
1. DATA_VALIDATION ne charge que les règles de validation des données.
1. DOCUMENT_PROPERTIES ne charge que les propriétés du document.
1. FORMULA charge les formules y compris les noms définis.
1. MERGED_AREA ne charge que les cellules fusionnées.
1. PIVOT_TABLE charge les tableaux croisés dynamiques.
1. SETTINGS ne charge que les paramètres de classeur et de feuille de calcul.
1. SHAPE ne charge que les formes.
1. STYLE charge la mise en forme des cellules.
1. TABLE charge les tableaux Excel/objets de liste.

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur [Filtrer les données à charger](/cells/fr/java/filtrer-le-type-de-données-lors-du-chargement-du-classeur-à-partir-du-fichier-modèle/).

{{% /alert %}} 

Voici le scénario d'utilisation simple.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

LoadOptions options = new LoadOptions(LoadFormat.XLSX);

//Set LoadDataFilterOptions to load only shapes

options.setLoadDataFilterOptions(LoadDataFilterOptions.SHAPE);

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

Workbook book = new Workbook(filePath, options);

{{< /highlight >}}
### **Convertir directement le graphique en PDF**
Les API Aspose.Cells ont déjà fourni la possibilité de rendre les graphiques en PDF tout en utilisant la méthode Chart.toPdf. Avec cette version, l'API a exposé une autre version surchargée de ladite méthode qui pourrait accepter une instance de OutputStream, permettant aux utilisateurs de sauvegarder le PDF du graphique dans une instance de ByteArrayOutputStream.

Voici le scénario d'utilisation simple.

**Java**

{{< highlight csharp >}}

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
Aspose.Cells for Java 8.8.1 a exposé la propriété WorkbookSettings.PaperSize afin de définir la taille par défaut du papier d'impression pour la feuille de calcul entière. La propriété WorkbookSettings.PaperSize accepte une valeur de l'énumération PaperSizeType qui contient les tailles prédéfinies pour les types de papier d'impression les plus couramment utilisés.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook();

//Access WorkbookSettings from the Workbook

WorkbookSettings settings = book.getSettings();

//Set the default printing paper size for the Workbook

settings.setPaperSize(PaperSizeType.PAPER_A_4);

{{< /highlight >}}
### **Propriété Shape.TextBody ajoutée**
Cette version de l'API Aspose.Cells for Java a exposé le Shape.TextBody afin de manipuler les aspects du texte dans les formes. L'extrait suivant utilise ladite propriété pour définir l'effet d'ombre du texte dans une zone de texte.

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur [Définition de l'effet d'ombre pour le texte](/cells/fr/java/setting-shadow-of-text-effects-of-shape-or-textbox/).

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet of the Workbook

Worksheet sheet = book.getWorksheets().get(0);

//Add a TextBox to the ShapeCollection

int index = sheet.getTextBoxes().add(2, 2, 100, 400);

TextBox textBox = sheet.getTextBoxes().get(index);

//Set the text of the TextBox

textBox.setText("This text has the following settings.\n\nText Effects > Shadow > Offset Bottom");

//Set shadow effect for text

for (int i = 0; i < textBox.getTextBody().getCount(); i++)

{

  textBox.getTextBody().get(i).getShapeFont().getFillFormat().getShadowEffect().setPresetType(PresetShadowType.OFFSET_BOTTOM);

}

{{< /highlight >}}
### **Méthode Worksheet.calculateFormula(string formule, CalculationOptions opts) ajoutée**
Aspose.Cells for Java 8.8.1 a ajouté une autre surcharge pour la méthode Worksheet.calculateFormula qui permet de calculer une formule donnée directement avec des options personnalisées.

{{% alert color="primary" %}} 

Pour plus de détails sur cette fonctionnalité, veuillez consulter l'article détaillé sur [Calcul direct de fonction personnalisée](/cells/fr/java/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/).

{{% /alert %}} 
### **Méthode GridCell.createValidation ajoutée**
Aspose.Cells.GridWeb offre la possibilité d'ajouter directement la règle de validation à une seule cellule en utilisant la méthode GridCell.createValidation. Cette méthode nécessite 2 paramètres. Le premier est de type GridValidationType qui détermine le type de validation, tandis que le deuxième paramètre (isRequied) est de type booléen.

**Java**

{{< highlight csharp >}}

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
### **Méthode GridCell.removeValidation ajoutée**
Aspose.Cells.GridWeb a également fourni la possibilité de supprimer la règle de validation des données d'une GridCell en utilisant la méthode GridCell.removeValidation.
## **APIs obsolètes**
### **Propriété Shape.TextFrame rendue obsolète**
Il est conseillé d'utiliser la propriété Shape.TextBody.TextAlignment à la place.
{{< app/cells/assistant language="java" >}}
