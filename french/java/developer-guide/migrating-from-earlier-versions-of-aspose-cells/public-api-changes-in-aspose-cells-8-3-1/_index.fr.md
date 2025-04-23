---
title: Modifications de l API publique dans Aspose.Cells 8.3.1
type: docs
weight: 120
url: /fr/java/public-api-changes-in-aspose-cells-8-3-1/
---

{{% alert color="primary" %}} 

Ce document décrit les modifications apportées à l'API Aspose.Cells de la version 8.3.0 à la version 8.3.1 qui pourraient intéresser les développeurs de modules/applications.

{{% /alert %}} 
## **APIs ajoutées**
### **Ajout de la propriété DataLabels.ShowCellRange**
Le getter/setter de la propriété ShowCellRange a été ajouté à la classe DataLabels afin de reproduire la fonctionnalité d'Excel pour formater les étiquettes de données du graphique en cours d'exécution. Veuillez noter qu'Excel fournit cette fonctionnalité en suivant les étapes suivantes. 

1. Sélectionnez les étiquettes de données de la série et cliquez avec le bouton droit pour ouvrir le menu contextuel.
1. Cliquez sur **Format des étiquettes de données…** et il affichera **Options de l'étiquette**.
1. Cochez ou décochez la case à cocher **L'étiquette contient - Valeur à partir des cellules**.

Le code d'exemple ci-dessous accède aux étiquettes de données de la série du graphique, puis définit la méthode DataLabels.setShowCellRange() sur true pour reproduire la fonctionnalité d'Excel **L'étiquette contient - Valeur à partir des cellules**.

**Java**

{{< highlight csharp >}}

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

Veuillez consulter l'article [Affichage de la plage de cellules en tant que étiquettes de données](/cells/fr/java/showing-cell-range-as-the-data-labels/) pour plus d'informations.

{{% /alert %}} 

### **Méthodes ajoutées Cell.getTable & ListObject.putCellValue**
Les méthodes Cell.getTable & ListObject.putCellValue ont été ajoutées avec Aspose.Cells for Java 8.3.1 afin de faciliter l'accès des utilisateurs à ListObject à partir d'une cellule et d'ajouter des valeurs à l'intérieur en utilisant les décalages de ligne et de colonne. Le code d'exemple suivant charge la feuille de calcul source et ajoute des valeurs à l'intérieur de la table.

**Java**

{{< highlight csharp >}}

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

Veuillez consulter l'article [Accéder à un tableau à partir d'une cellule et ajouter des valeurs à l'intérieur en utilisant des décalages de ligne et de colonne](/cells/fr/java/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/) pour plus d'informations.

{{% /alert %}} 

### **Méthodes ajoutées OdsSaveOptions.isStrictSchema11 & OdsSaveOptions.setStrictSchema11**
Les méthodes isStrictSchema11 & setStrictSchema11 ont été ajoutées à la classe OdsSaveOptions afin de permettre aux développeurs de sauvegarder la feuille de calcul dans un format conforme à la spécification ODF v1.2. La valeur par défaut de la propriété setStrictSchema11 est fausse, cela signifie que, à partir de la version 8.3.1 des API Aspose.Cells, les fichiers ODS seront enregistrés par défaut au format ODF version 1.2.

Le code snippet fourni ci-dessous enregistre le fichier ODS au format ODF 1.2.

**Java**

{{< highlight csharp >}}

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

Veuillez consulter l'article [Sauvegarder un fichier ODS dans les spécifications ODF 1.1 et 1.2](/cells/fr/java/save-ods-file-in-odf-1-1-and-1-2-specifications/) pour plus d'informations.

{{% /alert %}} 

### **Méthode ajoutée SparklineCollection.add**
Les API Aspose.Cells ont exposé la méthode SparklineCollection.add(String dataRange, int row, int column) pour spécifier la plage de données et l'emplacement du groupe de mini-graphiques. Veuillez noter qu'Excel propose la même fonctionnalité avec les étapes suivantes. 

1. Sélectionnez la cellule contenant votre mini-graphique.
1. Sélectionnez **Modifier les données du mini-graphique** dans la section **Conception**.
1. Choisissez **Modifier l'emplacement et les données du groupe**.
1. Spécifiez **Plage de données** & **Emplacement**.

Le code d'exemple suivant charge la feuille de calcul source, accède au premier groupe de mini-graphiques et ajoute de nouvelles plages de données et des emplacements pour le groupe de mini-graphiques. 

**Java**

{{< highlight csharp >}}

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

Veuillez consulter l'article [Copier un mini-graphique en spécifiant la plage de données et l'emplacement du groupe de mini-graphiques](/cells/fr/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/) pour plus d'informations.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
