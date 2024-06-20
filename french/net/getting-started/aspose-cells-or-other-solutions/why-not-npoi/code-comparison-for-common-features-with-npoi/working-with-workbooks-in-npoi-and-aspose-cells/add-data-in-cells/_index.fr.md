---
title: Ajouter des données dans les cellules
type: docs
weight: 10
url: /fr/net/add-data-in-cells/
description: Cet article explique comment ajouter des données dans les cellules à l aide des API Aspose.Cells for .NET.
keywords: C# Ajouter des données dans les cellules, C# Insérer des données dans la feuille de calcul, C# Définir les données de la cellule.
---


## **Comment ajouter des données dans les cellules à l'aide de Aspose.Cells for .NET**
Aspose.Cells fournit une classe, Workbook, qui représente un fichier Microsoft Excel. La classe Workbook contient une collection de feuilles de calcul qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par la classe Worksheet. La classe Worksheet fournit une collection de cellules. Chaque élément dans la collection de cellules représente un objet de la classe Cell

**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Accessing the added worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

int x = 1;

for (int i = 1; i <= 15; i++)

{

    for (int j = 0; j < 15; j++)

    {

        worksheet.Cells[i, j].Value = x++;

    }

}

workbook.Save("test.xlsx");


{{< /highlight >}}
## **NPOI HSSF XSSF - Ajouter des données dans les cellules**
Dans NPOI, row.createCell(1).setCellValue peut être utilisé pour ajouter des données dans les cellules.

**C#**

{{< highlight cs >}}

 IWorkbook workbook = new XSSFWorkbook();

ISheet sheet1 = workbook.CreateSheet("Sheet1");

sheet1.CreateRow(0).CreateCell(0).SetCellValue("This is a Sample");

int x = 1;

for (int i = 1; i <= 15; i++)

{

	IRow row = sheet1.CreateRow(i);

	for (int j = 0; j < 15; j++)

	{

		row.CreateCell(j).SetCellValue(x++);

	}

}

FileStream sw = File.Create("test.xlsx");

workbook.Write(sw);

sw.Close();

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Ajouter des données dans les cellules** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Add.Data.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Ajout de données aux cellules](/cells/fr/net/add-data-in-cells/).

{{% /alert %}}
