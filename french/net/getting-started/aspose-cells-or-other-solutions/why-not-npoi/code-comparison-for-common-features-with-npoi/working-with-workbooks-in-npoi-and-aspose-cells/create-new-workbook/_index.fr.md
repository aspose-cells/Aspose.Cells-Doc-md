---
title: Créer un nouveau classeur
type: docs
weight: 20
url: /fr/net/create-new-workbook/
---

## **Aspose.Cells - Créer un nouveau classeur**
La classe Workbook est disponible pour un usage simple

**C#**

{{< highlight cs >}}

 Workbook workbook = new Workbook(); // Creating a Workbook object

workbook.Save("test.xlsx", SaveFormat.Xlsx); //Workbooks can be saved in many formats

{{< /highlight >}}
## **NPOI - HSSF XSSF - Créer un nouveau classeur**
Créer un nouveau classeur en utilisant la classe Workbook et enregistrer en utilisant FileOutputStream.

**C#**

{{< highlight cs >}}

 IWorkbook workbook = new XSSFWorkbook();

workbook.CreateSheet("Sheet A1");

workbook.CreateSheet("Sheet A2");

workbook.CreateSheet("Sheet A3");

FileStream sw = File.Create("test.xlsx");

workbook.Write(sw);

sw.Close();

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**
Téléchargez **Créer un nouveau classeur** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Create.New.Workbook.Aspose.Cells.zip)
{{< app/cells/assistant language="csharp" >}}
