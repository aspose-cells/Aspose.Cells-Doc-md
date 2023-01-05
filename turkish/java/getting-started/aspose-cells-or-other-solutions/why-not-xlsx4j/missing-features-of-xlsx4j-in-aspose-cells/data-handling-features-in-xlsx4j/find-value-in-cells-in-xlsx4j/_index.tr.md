---
title: xlsx4j'de Cells'de Değer Bulun
type: docs
weight: 30
url: /tr/java/find-value-in-cells-in-xlsx4j/
---
## **Aspose.Cells - Cells'de Değer Bulun**
Microsoft Excel'de, kullanıcılar belirli verileri içeren hücreleri arayabilir. Örneğin, tıklama**Düzenlemek**ve sonra**Bulmak**Ara iletişim kutusunu açar. Kullanıcılar bir değer girer ve tıklar**Tamam**onu aramak için Excel, eşleşen alanları vurgular.

**Java**

{{< highlight "java" >}}

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
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/findvalueincells/AsposeFindValueInCells.java)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Veri Bul veya Ara](/cells/tr/java/find-or-search-data).

{{% /alert %}}
