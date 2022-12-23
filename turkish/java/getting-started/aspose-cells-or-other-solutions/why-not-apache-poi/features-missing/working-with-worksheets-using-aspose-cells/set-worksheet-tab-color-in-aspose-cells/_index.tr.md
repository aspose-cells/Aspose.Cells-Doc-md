---
title: Aspose.Cells'de Çalışma Sayfası Sekme Rengini Ayarla
type: docs
weight: 90
url: /tr/java/set-worksheet-tab-color-in-aspose-cells/
---
## **Aspose.Cells - Çalışma Sayfası Sekme Rengini Ayarla**
Aspose.Cells, tek tek çalışma sayfası sekmelerinin rengini değiştirerek diğerlerinden öne çıkmalarını sağlar. Örneğin, Giderleri kırmızı, Satışları yeşil, Varlıkları mavi vb. yapabilirsiniz.
#### **Microsoft Excel ile Çalışma Sayfası Sekme Rengini Ayarlama**
1. Geçerli çalışma sayfasının altındaki sekme sayfasındaki bir sekmeyi sağ tıklayın.
1. Seçme**Sekme rengi**.
1. Paletten bir renk seçin.
1. Tıklamak**Tamam**.

**Java**

{{< highlight "java" >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook(dataPath + "workbook.xls");

//Get the first worksheet in the book

Worksheet worksheet = workbook.getWorksheets().get(0);

//Set the tab color

worksheet.setTabColor(Color.getRed());

//Save the Excel file

workbook.save(dataPath + "AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **Çalışan Kodu İndir**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/SetWorksheetTabColor.java)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Çalışma Sayfası Sekme Rengini Ayarla](/java/set-worksheet-tab-color).

{{% /alert %}}
