---
title: Aspose.Cells'i kullanarak Çalışma Kitabının Sekmelerini Görüntüleme ve Gizleme
type: docs
weight: 50
url: /tr/java/display-and-hide-tabs-of-workbook-using-aspose-cells/
---
## **Aspose.Cells - Çalışma Kitabının Sekmelerini Görüntüle ve Gizle**
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir Çalışma Kitabı sınıfı sağlar. Workbook sınıfı, bir Excel dosyasını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Geliştiriciler, bir Excel dosyasındaki sekmelerin görünürlüğünü kontrol etmek için Workbook sınıfının setShowTabs yöntemini kullanabilir.

**Java**

{{< highlight "java" >}}

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
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDisplayAndHideTabs.java)

