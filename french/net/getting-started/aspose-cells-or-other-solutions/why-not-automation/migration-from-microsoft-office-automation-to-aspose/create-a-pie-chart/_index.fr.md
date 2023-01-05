---
title: Créer un graphique à secteurs
type: docs
weight: 110
url: /fr/net/create-a-pie-chart/
---
{{% alert color="primary" %}}

Les graphiques présentent les données d'une manière facile à comprendre. Les utilisateurs qui travaillent avec Microsoft Excel peuvent créer un certain nombre de graphiques différents et les personnaliser. Les mêmes fonctionnalités sont disponibles pour les développeurs qui travaillent avec Aspose.Cells for .NET.

{{% /alert %}}

## **Création d'un graphique à secteurs**

Cet article compare la création d'un graphique à secteurs à l'aide d'Office Automation et de VSTO à l'utilisation de Aspose.Cells for .NET. Les étapes de création d'un graphique à secteurs sont les suivantes :

1. Création d'un classeur et d'une feuille de calcul.
1. Ajout de données d'exemple.
1. Tableau des produits de référence.
1. Ajout d'un graphique à secteurs, définition de la plage de données et du titre du graphique.
1. Enregistrement de la feuille de calcul.

 Les exemples de code de cet article montrent comment ajouter un graphique à secteurs avec[VSTO](/cells/fr/net/create-a-pie-chart/) , en utilisant C# ou Visual Basic, par rapport à la création d'un avec[Aspose.Cells](/cells/fr/net/create-a-pie-chart/), en utilisant à nouveau C# ou Visual Basic.

### **Création d'un graphique à secteurs avec VSTO**

Les exemples de code qui suivent montrent comment ajouter un graphique à secteurs à une feuille de calcul à l'aide de VSTO.

**C#**

{{< highlight "csharp" >}}

 void PieChart()

{

    //Access a Vsto Worksheet

    Microsoft.Office.Tools.Excel.Worksheet sheet = this;

    //Add sample data for pie chart

    //Add headings in A1 and B1

    sheet.Cells[1, 1] = "Products";

    sheet.Cells[1, 2] = "Users";



    //Add data from A2 till B4

    sheet.Cells[2, 1] = "Aspose.Cells";

    sheet.Cells[2, 2] = 10000;

    sheet.Cells[3, 1] = "Aspose.Slides";

    sheet.Cells[3, 2] = 8000;

    sheet.Cells[4, 1] = "Aspose.Words";

    sheet.Cells[4, 2] = 12000;

    //Chart reference

    Microsoft.Office.Tools.Excel.Chart productsChart;

    //Add a Pie Chart

    productsChart = sheet.Controls.AddChart(0, 105, 330, 200, "ProductUsers");

    productsChart.ChartType = Microsoft.Office.Interop.Excel.XlChartType.xlPie;

    //Set chart title

    productsChart.HasTitle = true;

    productsChart.ChartTitle.Text = "Users";

    //Gets the cells that define the data to be charted.

    Microsoft.Office.Interop.Excel.Range chartRange = sheet.get_Range("A2", "B4");

    productsChart.SetSourceData(chartRange, missing);

    //Access the Active workbook from Vsto sheet

    Microsoft.Office.Interop.Excel.Workbook workbook= sheet.Application.ActiveWorkbook;

    //Save the copy of workbook as OutputVsto.xlsx

    workbook.SaveCopyAs("C:\\Downloads\\OutputVsto.xlsx");

}



{{< /highlight >}}

**Un camembert créé avec VSTO** 

![tâche : image_autre_texte](create-a-pie-chart_1.png)

### **Création d'un graphique à secteurs avec Aspose.Cells for .NET**

Les exemples de code qui suivent montrent comment ajouter un graphique à secteurs à une feuille de calcul à l'aide de Aspose.Cells.

**C#**

{{< highlight "csharp" >}}

 private void PieChart()

{

    //Create Aspose.Cells Workbook

    Workbook workbook = new Workbook();

    //Access Aspose.Cells Worksheet

    Worksheet sheet = workbook.Worksheets[0];

    //Add sample data for pie chart

    //Add headings in A1 and B1

    sheet.Cells["A1"].PutValue("Products");

    sheet.Cells["B1"].PutValue("Users");

    //Add data from A2 till B4

    sheet.Cells["A2"].PutValue("Aspose.Cells");

    sheet.Cells["B2"].PutValue(10000);

    sheet.Cells["A3"].PutValue("Aspose.Slides");

    sheet.Cells["B3"].PutValue(8000);

    sheet.Cells["A4"].PutValue("Aspose.Words");

    sheet.Cells["B4"].PutValue(12000);

    //Chart reference

    Chart productsChart;

    //Add a Pie Chart

    int chartIdx = sheet.Charts.Add(ChartType.Pie, 7, 0, 20, 6);

    productsChart = sheet.Charts[chartIdx];

    //Gets the cells that define the data to be charted

    int seriesIdx = productsChart.NSeries.Add("=Sheet1!$B$2:$B$4", true);

    Series nSeries = productsChart.NSeries[seriesIdx];

    nSeries.XValues = "=Sheet1!$A$2:$A$4";

    //Set chart title

    productsChart.Title.Text = "Users";

    //Autofit first column

    sheet.AutoFitColumn(0);

    //Save the copy of workbook as OutputAspose.xlsx

    workbook.Save("C:\\Downloads\\OutputAspose.xlsx");

}

{{< /highlight >}}

**Graphique circulaire créé avec Aspose.Cells for .NET** 

![tâche : image_autre_texte](create-a-pie-chart_2.png)
