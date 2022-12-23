---
title: Cells'de Değer Bulun
type: docs
weight: 20
url: /tr/net/find-value-in-cells/
---
## **Aspose.Cells - Cells'de Değer Bulun**
Microsoft Excel'de, kullanıcılar belirli verileri içeren hücreleri arayabilir. Örneğin, tıklama**Düzenlemek**ve sonra**Bulmak**Ara iletişim kutusunu açar. Kullanıcılar bir değer girer ve tıklar**Tamam**onu aramak için Excel, eşleşen alanları vurgular.

**C#**

{{< highlight "cs" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Finding the cell containing the specified formula

Cells cells = worksheet.Cells;

//Instantiate FindOptions

FindOptions findOptions = new FindOptions();

//Finding the cell containing a string value that starts with "Or"

findOptions.LookAtType = LookAtType.StartWith;

Cell cell = cells.Find("SH", null, findOptions);

//Printing the name of the cell found after searching worksheet

Console.WriteLine("Name of the cell containing String: " + cell.Name);

{{< /highlight >}}
## **Çalışan Kodu İndir**
 İndirmek**Cells'de Değer Bulun** aşağıda belirtilen sosyal kodlama sitelerinden herhangi birini oluşturun:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Find.Value.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Veri Bul veya Ara](/cells/tr/net/find-or-search-data/).

{{% /alert %}}
