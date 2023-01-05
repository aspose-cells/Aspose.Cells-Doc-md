---
title: Créer un nouveau classeur
type: docs
weight: 20
url: /fr/net/create-new-workbook/
---
## **Aspose.Cells - Créer un nouveau classeur**
La classe Workbook est disponible pour une utilisation simple

**C#**

{{< highlight "cs" >}}

 Workbook workbook = new Workbook(); // Creating a Workbook object

workbook.Save("test.xlsx", SaveFormat.Xlsx); //Workbooks can be saved in many formats

{{< /highlight >}}
## **NPOI - HSSF XSSF - Créer un nouveau classeur**
Créez un nouveau classeur à l'aide de la classe Workbook et enregistrez-le à l'aide de FileOutputStream.

**C#**

{{< highlight "cs" >}}

 IWorkbook workbook = new XSSFWorkbook();

workbook.CreateSheet("Sheet A1");

workbook.CreateSheet("Sheet A2");

workbook.CreateSheet("Sheet A3");

FileStream sw = File.Create("test.xlsx");

workbook.Write(sw);

sw.Close();

{{< /highlight >}}
## **Télécharger le code d'exécution**
 Télécharger**Créer un nouveau classeur** forment l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Create.New.Workbook.Aspose.Cells.zip)
