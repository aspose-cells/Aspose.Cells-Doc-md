---
title: Alt Toplamları Hesapla
type: docs
weight: 10
url: /tr/net/calculate-sub-totals/
---

## **Aspose.Cells - Alt Toplamları Hesapla**
Herhangi bir tekrarlanan değer için alt toplamları otomatik olarak oluşturabilirsiniz. Aspose.Cells, elektronik tablolara alt toplamlar eklemeye yardımcı olan API özellikleri sunar.

**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Get the Cells collection in the first worksheet

Cells cells = workbook.Worksheets[0].Cells;

//Create a cellarea i.e.., B3:C19

CellArea ca = new CellArea();

ca.StartRow = 2;

ca.StartColumn = 1;

ca.EndRow = 18;

ca.EndColumn = 2;

//Apply subtotal, the consolidation function is Sum and it will applied to

//Second column (C) in the list

cells.Subtotal(ca, 0, ConsolidationFunction.Sum, new int[] { 1 });

//Save the excel file

workbook.Save("AsposeTotal.xls"); 

{{< /highlight >}}
## **Çalışan Kodu İndir**
Herhangi aşağıdaki sosyal kodlama sitelerinden **Alt Toplamları Hesapla** indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Calculate.Sub.Totals.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Daha fazla ayrıntı için [Alt Toplamlar Oluşturma](/cells/tr/net/creating-subtotals/) ziyaret edin.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
