---
title: Aspose.Cells Kullanarak Hücrelerde Değer Bulma
type: docs
weight: 10
url: /tr/java/find-value-in-cells-using-aspose-cells/
---

## **Aspose.Cells - Hücrelerde Değer Bul**
Microsoft Excel'de kullanıcılar belirli veriler içeren hücreleri arayabilir. Örneğin, **Düzenle**'ye tıkladıktan sonra **Bul** açılır iletişim kutusunu açarlar. Kullanıcılar bir değer girer ve aramak için **Tamam**'a tıklarlar. Excel eşleşen alanları vurgular.

**Java**

{{< highlight java >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

//Finding the cell containing the specified formula

Cells cells = worksheet.getCells();

//Instantiate FindOptions

FindOptions findOptions = new FindOptions();

//Finding the cell containing a string value that starts with "Or"

findOptions.setLookAtType(LookAtType.START_WITH);

Cell cell = cells.find("SH",null,findOptions);

//Printing the name of the cell found after searching worksheet

System.out.println("Name of the cell containing String: " + cell.getName());

{{< /highlight >}}
## **Çalışan Kodu İndir**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/search/AsposeFindCellsWithString.java)

{{% alert color="primary" %}} 

Daha fazla bilgi için [Veri Bulma veya Arama](/cells/tr/java/find-or-search-data)'yı ziyaret edin.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
