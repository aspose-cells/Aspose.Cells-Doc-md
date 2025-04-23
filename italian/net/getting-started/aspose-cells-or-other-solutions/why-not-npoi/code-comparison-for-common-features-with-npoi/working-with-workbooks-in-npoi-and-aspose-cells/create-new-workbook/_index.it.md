---
title: Crea un Nuovo Workbook
type: docs
weight: 20
url: /it/net/create-new-workbook/
---

## **Aspose.Cells - Crea un Nuovo Workbook**
La classe Workbook è disponibile per un uso semplice

**C#**

{{< highlight cs >}}

 Workbook workbook = new Workbook(); // Creating a Workbook object

workbook.Save("test.xlsx", SaveFormat.Xlsx); //Workbooks can be saved in many formats

{{< /highlight >}}
## **NPOI - HSSF XSSF - Crea un Nuovo Workbook**
Crea un nuovo Workbook usando la classe Workbook e salva usando FileOutputStream.

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
## **Scarica il codice in esecuzione**
Scarica **Crea un Nuovo Workbook** da uno dei siti di codifica sociale menzionati di seguito:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Create.New.Workbook.Aspose.Cells.zip)
{{< app/cells/assistant language="csharp" >}}
