---
title: Hücrelerde Değer Bul
type: docs
weight: 20
url: /tr/net/find-value-in-cells/
---

## **Aspose.Cells - Hücrelerde Değer Bul**
Microsoft Excel'de kullanıcılar belirli veriler içeren hücreleri arayabilir. Örneğin, **Düzenle**'ye tıkladıktan sonra **Bul** açılır iletişim kutusunu açarlar. Kullanıcılar bir değer girer ve aramak için **Tamam**'a tıklarlar. Excel eşleşen alanları vurgular.

**C#**

{{< highlight cs >}}

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
Herhangi aşağıdaki sosyal kodlama sitelerinden **Hücrelerde Değer Bul** indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Find.Value.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Daha fazla ayrıntı için [Veri Bulma veya Arama](/cells/tr/net/find-or-search-data/) ziyaret edin.

{{% /alert %}}
