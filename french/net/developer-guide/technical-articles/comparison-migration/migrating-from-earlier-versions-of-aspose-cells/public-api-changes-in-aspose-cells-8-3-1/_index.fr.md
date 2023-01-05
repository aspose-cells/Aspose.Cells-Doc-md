---
title: Public API Changements dans Aspose.Cells 8.3.1
type: docs
weight: 110
url: /fr/net/public-api-changes-in-aspose-cells-8-3-1/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 8.3.0 à 8.3.1 qui peuvent intéresser les développeurs de modules/applications.

{{% /alert %}} 
## **API ajoutées**
### **Propriété DataLabels.ShowCellRange ajoutée**
 La propriété ShowCellRange a été ajoutée à la classe DataLabels afin d'imiter la fonctionnalité Excel de formatage des étiquettes de données du graphique au moment de l'exécution. Veuillez noter qu'Excel fournit cette fonctionnalité à travers les étapes suivantes.

1. Sélectionnez les étiquettes de données de la série et cliquez avec le bouton droit pour ouvrir le menu contextuel.
1.  Clique le**Formater les étiquettes de données...** et ça montrera**Options d'étiquette**.
1.  Cochez ou décochez la case**L'étiquette contient - Valeur à partir de Cells**.

 L'exemple de code ci-dessous accède aux étiquettes de données de la série de graphiques, puis définit la méthode DataLabels.ShowCellRange sur true pour imiter la fonctionnalité d'Excel de**L'étiquette contient - Valeur à partir de Cells**.

**C#**

{{< highlight "csharp" >}}

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

{{< highlight "csharp" >}}



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

 Veuillez vérifier l'article[Affichage de la plage Cell comme étiquettes de données](http://aspose.com/docs/display/cellsnet/Showing+Cell+Range+as+the+Data+Labels) pour plus d'informations.

{{% /alert %}} 

### **Méthodes Cell.GetTable & ListObject.PutCellValue ajoutées**
Les méthodes Cell.GetTable & ListObject.PutCellValue ont été ajoutées avec Aspose.Cells for .NET 8.3.1 afin de faciliter aux utilisateurs l'accès à ListObject à partir d'une cellule et d'y ajouter des valeurs à l'aide des décalages de ligne et de colonne. L'exemple de code suivant charge la feuille de calcul source et ajoute des valeurs dans le tableau.

**C#**

{{< highlight "csharp" >}}

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

{{< highlight "csharp" >}}

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

 Veuillez vérifier l'article[Accéder au tableau à partir de Cell et y ajouter des valeurs à l'aide des décalages de ligne et de colonne](http://aspose.com/docs/display/cellsnet/Accessing+Table+from+Cell+and+Adding+Values+inside+it+using+Row+and+Column+Offsets) pour plus d'informations.

{{% /alert %}} 

### **Propriété OdsSaveOptions.IsStrictSchema11 ajoutée**
La propriété IsStrictSchema11 a été ajoutée à la classe OdsSaveOptions afin de permettre aux développeurs d'enregistrer la feuille de calcul dans un format conforme à la spécification ODF v1.2. La valeur par défaut de la propriété IsStrictSchema11 est false, ce qui signifie qu'à partir de la version 8.3.1 des API Aspose.Cells, les fichiers ODS seront enregistrés au format ODF version 1.2 par défaut.

L'extrait de code fourni ci-dessous enregistre le fichier ODS au format ODF 1.2.

**C#**

{{< highlight "csharp" >}}

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

{{< highlight "csharp" >}}

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

 Veuillez vérifier l'article[Enregistrer le fichier ODS dans les spécifications ODF 1.1 et 1.2](http://aspose.com/docs/display/cellsnet/Save+ODS+file+in+ODF+1.1+and+1.2+Specifications) pour plus d'informations.

{{% /alert %}} 

### **Méthode SparklineCollection.Add Ajouté**
 Aspose.Cells Les API ont exposé la méthode SparklineCollection.Add(string dataRange, int row, int column) pour spécifier la plage de données et l'emplacement du groupe Sparkline. Veuillez noter qu'Excel fournit la même fonctionnalité via les étapes suivantes.

1. Sélectionnez la cellule contenant votre Sparkline.
1.  Sélectionner**Modifier les données du Sparkline** section à l'intérieur du**Concevoir** languette
1.  Choisir**Modifier l'emplacement et les données du groupe**.
1.  Spécifier**Plage de données** & **Lieu**.

 L'exemple de code suivant charge la feuille de calcul source, accède au premier groupe de graphiques sparkline et ajoute de nouvelles plages de données et de nouveaux emplacements pour le groupe de graphiques sparkline.

**C#**

{{< highlight "csharp" >}}

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

{{< highlight "csharp" >}}

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

 Veuillez vérifier l'article[Copier Sparkline en spécifiant la plage de données et l'emplacement du groupe Sparkline](http://aspose.com/docs/display/cellsnet/Copy+Sparkline+by+Specifying+Data+Range+and+Location+of+Sparkline+Group) pour plus d'informations.

{{% /alert %}}
