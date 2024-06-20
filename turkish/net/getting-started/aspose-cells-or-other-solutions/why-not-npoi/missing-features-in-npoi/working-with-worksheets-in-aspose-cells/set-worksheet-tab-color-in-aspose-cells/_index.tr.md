---
title: Aspose.Cells te Çalışma Sayfası Sekmesi Rengi Ayarlama
type: docs
weight: 20
url: /tr/net/set-worksheet-tab-color-in-aspose-cells/
---

## **Aspose.Cells - Çalışma Sayfası Sekmesi Rengi Ayarlama**
Aspose.Cells, bireysel çalışma sayfası sekmelerinin rengini değiştirmenize olanak tanır, böylece onları geri kalanından ayırt edebilirsiniz. Örneğin, Giderleri kırmızı, Satışları yeşil, Varlıkları mavi vb. yapabilirsiniz.
### **Microsoft Excel ile Çalışma Sayfası Sekmesi Rengini Ayarlama**
1. Mevcut çalışma sayfasının altındaki sekme sayfasında bir sekmeye sağ tıklayın.
1. **Sekme rengi**'ni seçin.
1. Paletten bir renk seçin.
1. **Tamam**'ı tıklayın.

**C#**

{{< highlight cs >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook("../../data/test.xlsx");

//Get the first worksheet in the book

Worksheet worksheet = workbook.Worksheets[0];

//Set the tab color

worksheet.TabColor = Color.Red;

//Save the Excel file

workbook.Save("AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **Çalışan Kodu İndir**
Çalışma Sayfası Sekmesi Rengi Ayarlama'yı indirin herhangi aşağıda belirtilen sosyal kodlama sitelerinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Worksheet.Tab.Color.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Daha fazla bilgi için [Çalışma Sayfası Sekmesi Rengi Ayarlama](/cells/tr/net/set-worksheet-tab-color/) adresini ziyaret edin.

{{% /alert %}}
