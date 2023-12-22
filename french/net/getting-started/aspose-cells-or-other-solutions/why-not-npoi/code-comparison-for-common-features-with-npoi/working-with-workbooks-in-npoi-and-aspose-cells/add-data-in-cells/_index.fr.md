---
title: Ajouter des données dans Cells
type: docs
weight: 10
url: /fr/net/add-data-in-cells/
description: Cet article explique comment ajouter des données dans Cells à l'aide des API Aspose.Cells for .NET.
keywords: C# Add Data in Cells, C# Insert Data to Worksheet, C# Set Data of Cell.
---
##  **Comment ajouter des données dans Cells en utilisant Aspose.Cells for .NET**
Aspose.Cells fournit une classe, Workbook, qui représente un fichier Excel Microsoft. La classe Workbook contient un WorksheetCollection qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe Worksheet. La classe Worksheet fournit une collection Cells. Chaque article de la collection Cells représente un objet de la classe Cell.

**C#**

{{< highlight "cs" >}}

 //Instanciation d'un objet Workbook

Classeur workbook = new Workbook();

//Accès à la feuille de calcul ajoutée dans le fichier Excel

Feuille de calcul feuille de calcul = workbook.Worksheets[0];

entier x = 1 ;

pour (int je = 1; je<= 15; i++)

{

    for (int j = 0; j < 15; j++)

    {

        worksheet.Cells[i, j].Value = x++;

    }

}

workbook.Save("test.xlsx");


{{< /highlight >}}
##  **NPOI HSSF XSSF - Ajouter des données dans Cells**
Dans NPOI, row.createCell(1).setCellValue peut être utilisé pour ajouter des données dans des cellules.

**C#**

{{< highlight "cs" >}}

 Classeur IWorkbook = new XSSFWorkbook();

ISheet sheet1 = workbook.CreateSheet("Sheet1");

sheet1.CreateRow(0).CreateCell(0).SetCellValue("Ceci est un échantillon");

entier x = 1 ;

pour (int je = 1; je<= 15; i++)

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
##  **Télécharger le code d'exécution**
 Télécharger**Ajouter des données dans Cells** formez l’un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Add.Data.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Pour plus de détails, visitez[Ajout de données au Cells](/cells/fr/net/add-data-in-cells/).

{{% /alert %}}
