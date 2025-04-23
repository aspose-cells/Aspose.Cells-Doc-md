---
title: Çalışma Kitaplarının Kaydırma Çubuklarını Göster ve Gizle
type: docs
weight: 40
url: /tr/java/display-and-hide-scrollbars-of-workbooks/
---

## **Aspose.Cells - İş Kitaplarının Kaydırma Çubuklarını Göster ve Gizle**
Aspose.Cells bir Excel dosyasını temsil eden **Workbook** sınıfını sağlar. **Workbook** sınıfı, Excel dosyasını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Ancak, Excel dosyasındaki kaydırma çubuklarının görünürlüğünü kontrol etmek için geliştiriciler, **Workbook** sınıfının **setVScrollBarVisible** ve **setHScrollBarVisible** yöntemlerini kullanabilir.

**Java**

{{< highlight java >}}

 //Instantiating a Excel object by excel file path

Workbook workbook = new Workbook(dataDir + "book1.xls");

//Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(false);

//Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeSrollbarsHide.xls");

// ===============================================================

//Displaying the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(true);

//Displaying the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(true);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeDisplaySrollbars.xls");


{{< /highlight >}}
## **Çalışan Kodu İndir**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDisplayAndHideScrollbars.java)
{{< app/cells/assistant language="java" >}}
