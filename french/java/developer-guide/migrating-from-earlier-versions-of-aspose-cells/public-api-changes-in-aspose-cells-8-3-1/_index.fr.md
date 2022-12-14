---
title: Public API Changements dans Aspose.Cells 8.3.1
type: docs
weight: 120
url: /fr/java/public-api-changes-in-aspose-cells-8-3-1/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.3.0 à 8.3.1 qui peuvent intéresser les développeurs de modules/applications.

{{% /alert %}} 
## **API ajoutées**
### **Propriété DataLabels.ShowCellRange ajoutée**
Le getter/setter pour la propriété ShowCellRange a été ajouté à la classe DataLabels afin d'imiter la fonctionnalité d'Excel de formatage des étiquettes de données du graphique au moment de l'exécution. Veuillez noter qu'Excel fournit cette fonctionnalité à travers les étapes suivantes.

1. Sélectionnez les étiquettes de données de la série et cliquez avec le bouton droit pour ouvrir le menu contextuel.
1.  Clique le**Formater les étiquettes de données...** et ça montrera**Options d'étiquette**.
1.  Cochez ou décochez la case**L'étiquette contient - Valeur à partir de Cells**.

 L'exemple de code ci-dessous accède aux étiquettes de données de la série de graphiques, puis définit la méthode DataLabels.setShowCellRange () sur true pour imiter la fonctionnalité d'Excel de**L'étiquette contient - Valeur à partir de Cells**.

**Java**

{{< highlight "csharp" >}}

 //Create workbook from the source spreadsheet containing an existing chart

Workbook workbook = new Workbook("sample.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the chart inside the worksheet

Chart chart = worksheet.getCharts().get(0);

//Check the "Label Contains - Value From Cells"

DataLabels dataLabels = chart.getNSeries().get(0).getDataLabels();

dataLabels.setShowCellRange(true);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

 Veuillez vérifier l'article[Affichage de la plage Cell comme étiquettes de données](/cells/fr/java/showing-cell-range-as-the-data-labels/) pour plus d'informations.

{{% /alert %}} 

### **Méthodes Cell.getTable & ListObject.putCellValue ajoutées**
Les méthodes Cell.getTable & ListObject.putCellValue ont été ajoutées avec Aspose.Cells for Java 8.3.1 afin de faciliter aux utilisateurs l'accès à ListObject à partir d'une cellule et d'y ajouter des valeurs à l'aide des décalages de ligne et de colonne. L'exemple de code suivant charge la feuille de calcul source et ajoute des valeurs dans le tableau.

**Java**

{{< highlight "csharp" >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cell D5 which lies inside the table

Cell cell = worksheet.getCells().get("D5");

//Put value inside the cell D5

cell.putValue("D5 Data");

//Access the Table from this cell

ListObject table = cell.getTable();

//Add some value using Row and Column Offset

table.putCellValue(2, 2, "Offset [2,2]");

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

 Veuillez vérifier l'article[Accéder au tableau à partir de Cell et y ajouter des valeurs à l'aide des décalages de ligne et de colonne](/cells/fr/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/) pour plus d'informations.

{{% /alert %}} 

### **Méthodes OdsSaveOptions.isStrictSchema11 & OdsSaveOptions.setStrictSchema11 ajoutées**
Les méthodes isStrictSchema11 & setStrictSchema11 ont été ajoutées à la classe OdsSaveOptions afin de permettre aux développeurs d'enregistrer la feuille de calcul dans un format conforme à la spécification ODF v1.2. La valeur par défaut de la propriété setStrictSchema11 est false, ce qui signifie qu'à partir de la version 8.3.1 des API Aspose.Cells, les fichiers ODS seront enregistrés au format ODF version 1.2 par défaut.

L'extrait de code fourni ci-dessous enregistre le fichier ODS au format ODF 1.2.

**Java**

{{< highlight "csharp" >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Put some value in cell A1

Cell cell = worksheet.getCells().get("A1");

cell.putValue("Welcome to Aspose!");

//Save ODS in ODF 1.2 version which is default

OdsSaveOptions options = new OdsSaveOptions();

workbook.save("ODF1.2.ods", options);

//Save ODS in ODF 1.1 version

options.setStrictSchema11(true);

workbook.save("ODF1.1.ods", options);

{{< /highlight >}}

{{% alert color="primary" %}} 

 Veuillez vérifier l'article[Enregistrer le fichier ODS dans les spécifications ODF 1.1 et 1.2](/cells/fr/java/save-ods-file-in-odf-1-1-and-1-2-specifications/) pour plus d'informations.

{{% /alert %}} 

### **Méthode SparklineCollection.add ajoutée**
 Aspose.Cells Les API ont exposé la méthode SparklineCollection.add(String dataRange, int row, int column) pour spécifier la plage de données et l'emplacement du groupe Sparkline. Veuillez noter qu'Excel fournit la même fonctionnalité via les étapes suivantes.

1. Sélectionnez la cellule contenant votre Sparkline.
1.  Sélectionner**Modifier les données du Sparkline** section à l'intérieur du**Concevoir** languette
1.  Choisir**Modifier l'emplacement et les données du groupe**.
1. Spécifier**Plage de données** & **Emplacement**.

 L'exemple de code suivant charge la feuille de calcul source, accède au premier groupe de graphiques sparkline et ajoute de nouvelles plages de données et de nouveaux emplacements pour le groupe de graphiques sparkline.

**Java**

{{< highlight "csharp" >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first sparkline group

SparklineGroup group = worksheet.getSparklineGroupCollection().get(0);

//Add Data Ranges and Locations inside this sparkline group

group.getSparklineCollection().add("D5:O5", 4, 15);

group.getSparklineCollection().add("D6:O6", 5, 15);

group.getSparklineCollection().add("D7:O7", 6, 15);

group.getSparklineCollection().add("D8:O8", 7, 15);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

 Veuillez vérifier l'article[Copier Sparkline en spécifiant la plage de données et l'emplacement du groupe Sparkline](/cells/fr/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/) pour plus d'informations.

{{% /alert %}}
