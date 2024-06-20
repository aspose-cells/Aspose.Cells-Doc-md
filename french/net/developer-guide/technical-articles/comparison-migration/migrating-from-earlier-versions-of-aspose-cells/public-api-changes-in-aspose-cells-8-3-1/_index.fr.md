---
title: Modifications de l API publique dans Aspose.Cells 8.3.1
type: docs
weight: 110
url: /fr/net/public-api-changes-in-aspose-cells-8-3-1/
---

{{% alert color="primary" %}} 

Ce document décrit les modifications apportées à l'API Aspose.Cells de la version 8.3.0 à la version 8.3.1 qui pourraient intéresser les développeurs de modules/applications.

{{% /alert %}} 
## **APIs ajoutées**
### **Ajout de la propriété DataLabels.ShowCellRange**
La propriété ShowCellRange a été ajoutée à la classe DataLabels afin de reproduire la fonctionnalité de formatage des étiquettes de données du graphique dans Excel à l'exécution. Veuillez noter qu'Excel propose cette fonctionnalité grâce aux étapes suivantes. 

1. Sélectionnez les étiquettes de données de la série et cliquez avec le bouton droit pour ouvrir le menu contextuel.
1. Cliquez sur **Format des étiquettes de données…** et il affichera **Options de l'étiquette**.
1. Cochez ou décochez la case à cocher **L'étiquette contient - Valeur à partir des cellules**.

Le code d'exemple ci-dessous accède aux étiquettes de données de la série de graphiques, puis définit la méthode DataLabels.ShowCellRange sur true pour imiter la fonctionnalité **Label Contains - Value From Cells** d'Excel.

**C#**

{{< highlight csharp >}}

 //Create workbook from the source Excel file

Workbook workbook = new Workbook("sample.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the chart inside the worksheet

Chart chart = worksheet.Charts[0];

//Check the "Label Contains - Value From Cells"

DataLabels dataLabels = chart.NSeries[0].DataLabels;

dataLabels.ShowCellRange = true;

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}

**VB.NET**

{{< highlight csharp >}}



'Create workbook from the source Excel file

Dim m_workbook As Workbook = New Workbook("sample.xlsx")

'Access the first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Access the chart inside the worksheet

Dim m_chart As Chart = m_worksheet.Charts(0)

'Check the "Label Contains - Value From Cells"

Dim m_dataLabels As DataLabels = m_chart.NSeries(0).DataLabels

m_dataLabels.ShowCellRange = True

'Save the workbook

m_workbook.Save("output.xlsx")


{{< /highlight >}}

{{% alert color="primary" %}} 

Veuillez consulter l'article [Afficher la plage de cellules en tant qu'étiquettes de données](http://aspose.com/docs/display/cellsnet/Showing+Cell+Range+as+the+Data+Labels) pour plus d'informations.

{{% /alert %}} 

### **Méthodes Cell.GetTable & ListObject.PutCellValue ajoutées**
Les méthodes Cell.GetTable & ListObject.PutCellValue ont été ajoutées avec Aspose.Cells for .NET 8.3.1 afin de permettre aux utilisateurs d'accéder à l'objet ListObject à partir d'une cellule et d'ajouter des valeurs à l'intérieur à l'aide des décalages de ligne et de colonne. Le code d'échantillon suivant charge la feuille de calcul source et ajoute des valeurs à l'intérieur de la table.

**C#**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access cell D5 which lies inside the table

Cell cell = worksheet.Cells["D5"];

//Put value inside the cell D5

cell.PutValue("D5 Data");

//Access the Table from this cell

ListObject table = cell.GetTable();

//Add some value using Row and Column Offset

table.PutCellValue(2, 2, "Offset [2,2]");

//Save the workbook

workbook.Save("output.xlsx");


{{< /highlight >}}

**VB.NET**

{{< highlight csharp >}}

 'Create workbook from source Excel file

Dim m_workbook As Workbook = New Workbook("source.xlsx")

'Access first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Access cell D5 which lies inside the table

Dim m_cell As Cell = m_worksheet.Cells("D5")

'Put value inside the cell D5

m_cell.PutValue("D5 Data")

'Access the Table from this cell

Dim table As ListObject = m_cell.GetTable()

'Add some value using Row and Column Offset

table.PutCellValue(2, 2, "Offset [2,2]")

'Save the workbook

m_workbook.Save("output.xlsx")


{{< /highlight >}}

{{% alert color="primary" %}} 

Veuillez consulter l'article [Accéder à la table depuis une cellule et ajouter des valeurs à l'intérieur en utilisant des décalages de lignes et de colonnes](http://aspose.com/docs/display/cellsnet/Accessing+Table+from+Cell+and+Adding+Values+inside+it+using+Row+and+Column+Offsets) pour plus d'informations.

{{% /alert %}} 

### **Propriété OdsSaveOptions.IsStrictSchema11 ajoutée**
La propriété IsStrictSchema11 a été ajoutée à la classe OdsSaveOptions afin de permettre aux développeurs de sauvegarder la feuille de calcul conformément à la spécification ODF v1.2. La valeur par défaut de la propriété IsStrictSchema11 est faux, ce qui signifie que, à partir de la version 8.3.1 des API Aspose.Cells, les fichiers ODS seront sauvegardés par défaut au format ODF version 1.2.

Le code snippet fourni ci-dessous enregistre le fichier ODS au format ODF 1.2.

**C#**

{{< highlight csharp >}}

 //Create workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Put some value in cell A1

Cell cell = worksheet.Cells["A1"];

cell.PutValue("Welcome to Aspose!");

//Save ODS in ODF 1.2 version which is default

OdsSaveOptions options = new OdsSaveOptions();

workbook.Save("ODF1.2.ods", options);

//Save ODS in ODF 1.1 version

options.IsStrictSchema11 = true;

workbook.Save("ODF1.1.ods", options);


{{< /highlight >}}

**VB.NET**

{{< highlight csharp >}}

 'Create workbook 

Dim m_workbook As Workbook = New Workbook()

'Access first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Put some value in cell A1

Dim m_cell As Cell = m_worksheet.Cells("A1")

m_cell.PutValue("Welcome to Aspose!")

'Save ODS in ODF 1.2 version which is default

Dim options As OdsSaveOptions = New OdsSaveOptions()

m_workbook.Save("ODF1.2.ods", options)

'Save ODS in ODF 1.1 version

options.IsStrictSchema11 = True

m_workbook.Save("ODF1.1.ods", options)

{{< /highlight >}}

{{% alert color="primary" %}} 

Veuillez consulter l'article [Enregistrer un fichier ODS aux spécifications ODF 1.1 et 1.2](http://aspose.com/docs/display/cellsnet/Save+ODS+file+in+ODF+1.1+and+1.2+Specifications) pour plus d'informations.

{{% /alert %}} 

### **Méthode SparklineCollection.Add ajoutée**
Les API Aspose.Cells ont exposé la méthode SparklineCollection.Add(string dataRange, int row, int column) pour spécifier la Plage de Données et l'Emplacement du Groupe de Sparklines. Veuillez noter qu'Excel offre la même fonctionnalité par les étapes suivantes. 

1. Sélectionnez la cellule contenant votre mini-graphique.
1. Sélectionnez **Modifier les données du mini-graphique** dans la section **Conception**.
1. Choisissez **Modifier l'emplacement et les données du groupe**.
1. Spécifiez **Plage de données** & **Emplacement**.

Le code d'exemple suivant charge la feuille de calcul source, accède au premier groupe de mini-graphiques et ajoute de nouvelles plages de données et des emplacements pour le groupe de mini-graphiques. 

**C#**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the first sparkline group

SparklineGroup group = worksheet.SparklineGroupCollection[0];

//Add Data Ranges and Locations inside this sparkline group

group.SparklineCollection.Add("D5:O5", 4, 15);

group.SparklineCollection.Add("D6:O6", 5, 15);

group.SparklineCollection.Add("D7:O7", 6, 15);

group.SparklineCollection.Add("D8:O8", 7, 15);

//Save the workbook

workbook.Save("output.xlsx");


{{< /highlight >}}

**VB.NET**

{{< highlight csharp >}}

 'Create workbook from source Excel file

Dim m_workbook As Workbook = New Workbook("source.xlsx")

'Access first worksheet

Dim m_worksheet As Worksheet = m_workbook.Worksheets(0)

'Access the first sparkline group

Dim group As SparklineGroup = m_worksheet.SparklineGroupCollection(0)

'Add Data Ranges and Locations inside this sparkline group

group.SparklineCollection.Add("D5:O5", 4, 15)

group.SparklineCollection.Add("D6:O6", 5, 15)

group.SparklineCollection.Add("D7:O7", 6, 15)

group.SparklineCollection.Add("D8:O8", 7, 15)

'Save the workbook

m_workbook.Save("output.xlsx")


{{< /highlight >}}

{{% alert color="primary" %}} 

Veuillez vérifier l'article [Copiez Sparkline en spécifiant la plage de données et l'emplacement du groupe de sparkline](http://aspose.com/docs/display/cellsnet/Copy+Sparkline+by+Specifying+Data+Range+and+Location+of+Sparkline+Group) pour plus d'informations.

{{% /alert %}}
