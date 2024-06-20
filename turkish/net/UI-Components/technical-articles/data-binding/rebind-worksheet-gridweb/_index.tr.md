---
title: Worksheet GridWeb ini Yeniden Bağlama
type: docs
weight: 50
url: /tr/net/aspose-cells-gridweb/rebind-worksheet-gridweb/
keywords: GridWeb, yeniden bağlama
description: Bu makale, GridWeb de çalışsheet in nasıl yeniden bağlanacağını tanıtır.
---

{{% alert color="primary" %}} 

Bir veri kümesiyle çalışsheet'i bağladığınızda IDE içindeki Worksheets Designer, APSX dosyasında bir çalışsheet etiketi oluşturur. 

Ve şöyle görünebilir: 

GridWeb1.DataBind() veya WebWorksheet.DataBind() çağırdığınızda, worksheet, dataSet11'deki verilerle doldurulur. 

**XML**

{{< highlight csharp >}}

 <acw:Worksheet DataMember="Products" BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True" DataSource='<%# dataSet11 %>'>



{{< /highlight >}}

Bazen çalışsheet'i yeniden bağlamak isteyebilirsiniz: 

Veri kaynağı özelliğini Runtime'da değiştirmenize rağmen, çalışsheet her zaman APSX dosyasındaki etiketteki veri kaynağı bağlama bilgisini kullanır. Levhasını Runtime'da başka bir veri kaynağına bağlamak için, ASPC dosyasındaki veri kaynağı bağlama bilgisini kaldırın. Etiketi şuna göre düzenleyin: 

**C#]**

{{< highlight csharp >}}

 private void Button1_Click(object sender, System.EventArgs e)

{

    GridWeb1.WorkSheets[0].Cells.Clear();

    // Load data to the dataSet11.

    LoadData(dataSet11);

    GridWeb1.WorkSheets[0].DataBind();

}



{{< /highlight >}}

**VB**

{{< highlight csharp >}}

 Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As 

System.EventArgs) Handles Button1.Click

    GridWeb1.WorkSheets(0).Cells.Clear()

    ' Load data to the dataSet11.

    LoadData(dataSet11)

    GridWeb1.WorkSheets(0).DataBind()

End Sub



{{< /highlight >}}

Çalışsayısı.DataSource özelliğini çalışma zamanında değiştirseniz bile, çalışsayısı.DataSource özelliğini not defteri sunucusundan geçiş bilgisi olarak kullanır. Bu, ASPX dosyasındaki çalışsayısı etiketindeki bağlama bilgisini daima kullanır. Çalışsayısını çalışma zamanında başka bir veri kaynağına bağlamak için, ASPC dosyasındaki çalışsayısı etiketindeki veri kaynağı bağlama bilgisini kaldırın. Etiketi şu şekilde düzenleyin: 

**XML**

{{< highlight csharp >}}

 <acw:Worksheet BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True">



{{< /highlight >}}

DataBind yöntemini çağırmadan önce çalışsayısı.DataSource ve çalışsayısı.DataMember özelliklerini belirtin.

{{% /alert %}}
