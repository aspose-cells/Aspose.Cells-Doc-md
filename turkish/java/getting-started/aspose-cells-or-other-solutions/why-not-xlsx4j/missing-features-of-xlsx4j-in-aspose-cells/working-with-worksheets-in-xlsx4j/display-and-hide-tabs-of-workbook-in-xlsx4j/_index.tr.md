---
title: xlsx4j deki İş Kitabının Sekmelerini Göster ve Gizle
type: docs
weight: 40
url: /tr/java/display-and-hide-tabs-of-workbook-in-xlsx4j/
---

## **Aspose.Cells - İş Kitabının Sekmelerini Göster ve Gizle**
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir **Workbook** sınıfını sağlar. Workbook sınıfı, Excel dosyasını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Bir Excel dosyasındaki sekmelerin görünürlüğünü kontrol etmek için geliştiriciler, Workbook sınıfının **setShowTabs** yöntemini kullanabilir.

**Java**

{{< highlight java >}}

 //Instantiating a Workbook object by excel file path

Workbook workbook = new Workbook(dataDir + "book1.xls");

//Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(false);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeHideTabs.xls");

// ===============================================================

//Displaying the tabs of the Excel file

workbook.getSettings().setShowTabs(true);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeDisplayTabs.xls");

{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/displayandhidetabs/AsposeDisplayAndHideTabs.java)
