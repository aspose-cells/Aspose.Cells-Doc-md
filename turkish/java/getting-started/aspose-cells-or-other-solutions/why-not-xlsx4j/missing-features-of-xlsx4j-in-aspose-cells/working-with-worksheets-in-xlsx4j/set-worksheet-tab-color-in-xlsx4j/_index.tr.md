---
title: xlsx4j deki İş Kitabı Sekme Rengini Ayarla
type: docs
weight: 60
url: /tr/java/set-worksheet-tab-color-in-xlsx4j/
---

## **Aspose.Cells - Çalışma Sayfası Sekmesi Rengi Ayarlama**
Aspose.Cells, bireysel çalışma sayfası sekmelerinin rengini değiştirmenize olanak tanır, böylece onları geri kalanından ayırt edebilirsiniz. Örneğin, Giderleri kırmızı, Satışları yeşil, Varlıkları mavi vb. yapabilirsiniz.
### **Microsoft Excel ile Çalışma Sayfası Sekmesi Rengini Ayarlama**
1. Mevcut çalışma sayfasının altındaki sekme sayfasında bir sekmeye sağ tıklayın.
1. **Sekme rengi**'ni seçin.
1. Paletten bir renk seçin.
1. **Tamam**'ı tıklayın.

**Java**

{{< highlight java >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook(dataDir + "workbook.xls");

//Get the first worksheet in the book

Worksheet worksheet = workbook.getWorksheets().get(0);

//Set the tab color

worksheet.setTabColor(Color.getRed());

//Save the Excel file

workbook.save(dataDir + "AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/settabcolor/AsposeSetWorksheetTabColor.java)

{{% alert color="primary" %}} 

Daha fazla bilgi için [Çalışma Sayfası Sekme Rengini Ayarlama](/java/set-worksheet-tab-color)'ı ziyaret edin.

{{% /alert %}}
