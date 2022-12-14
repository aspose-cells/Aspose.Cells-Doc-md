---
title: Aspose.Cells'de Çalışma Sayfası Sekme Rengini Ayarla
type: docs
weight: 20
url: /tr/net/set-worksheet-tab-color-in-aspose-cells/
---
## **Aspose.Cells - Çalışma Sayfası Sekme Rengini Ayarla**
Aspose.Cells, tek tek çalışma sayfası sekmelerinin rengini değiştirerek diğerlerinden öne çıkmalarını sağlar. Örneğin, Giderleri kırmızı, Satışları yeşil, Varlıkları mavi vb. yapabilirsiniz.
### **Microsoft Excel ile Çalışma Sayfası Sekme Rengini Ayarlama**
1. Geçerli çalışma sayfasının altındaki sekme sayfasındaki bir sekmeyi sağ tıklayın.
1. Seçme**Sekme rengi**.
1. Paletten bir renk seçin.
1. Tıklamak**TAMAM**.

**C#**

{{< highlight "cs" >}}

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
 İndirmek**Çalışma Sayfası Sekme Rengini Ayarla** aşağıda belirtilen sosyal kodlama sitelerinden herhangi birini oluşturun:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Worksheet.Tab.Color.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Çalışma Sayfası Sekme Rengini Ayarla](/cells/tr/net/set-worksheet-tab-color/).

{{% /alert %}}
