---
title: Alt Toplamları Hesapla
type: docs
weight: 10
url: /tr/net/calculate-sub-totals/
---
## **Aspose.Cells - Alt Toplamları Hesapla**
Bir e-tablodaki yinelenen değerler için otomatik olarak ara toplamlar oluşturabilirsiniz. Aspose.Cells, elektronik tablolara programlı olarak ara toplamlar eklemenize yardımcı olan API özelliklerini sağlar.

**C#**

{{< highlight "cs" >}}

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

cells.Subtotal(ca, 0, ConsolidationFunction.Sum, new int[]{ 1 });

//Save the excel file

workbook.Save("AsposeTotal.xls"); 

{{< /highlight >}}
## **Çalışan Kodu İndir**
 İndirmek**Alt Toplamları Hesapla** aşağıda belirtilen sosyal kodlama sitelerinden herhangi birini oluşturun:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Calculate.Sub.Totals.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Ara Toplamlar Oluşturma](/cells/tr/net/creating-subtotals/).

{{% /alert %}}
