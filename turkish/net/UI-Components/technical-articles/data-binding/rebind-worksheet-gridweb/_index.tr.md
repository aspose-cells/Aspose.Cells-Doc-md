---
title: Çalışma Sayfası GridWeb'i Yeniden Bağla
type: docs
weight: 50
url: /tr/net/rebind-worksheet-gridweb/
---
{{% alert color="primary" %}} 

 Bir çalışma sayfasını bir veri kümesine bağladığınızda

 IDE'de Çalışma Sayfaları Tasarımcısı, APSX'te bir çalışma sayfası etiketi oluşturulacak

 dosya. Şöyle görünebilir:

**xml**

{{< highlight "csharp" >}}

 <acw:Worksheet DataMember="Products" BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True" DataSource='<%# dataSet11 %>'>



{{< /highlight >}}

 GridWeb1.DataBind() veya WebWorksheet.DataBind()'i çağırdığınızda, çalışma sayfası dataSet11'deki verilerle doldurulacaktır.

 Bazen çalışma sayfasını yeniden ciltlemek isteyebilirsiniz:

**C#]**

{{< highlight "csharp" >}}

 private void Button1_Click(object sender, System.EventArgs e)

{

    GridWeb1.WebWorksheets[0].Cells.Clear();

    // Load data to the dataSet11.

    LoadData(dataSet11);

    GridWeb1.WebWorksheets[0].DataBind();

}



{{< /highlight >}}

**VB**

{{< highlight "csharp" >}}

 Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As 

System.EventArgs) Handles Button1.Click

    GridWeb1.WebWorksheets(0).Cells.Clear()

    ' Load data to the dataSet11.

    LoadData(dataSet11)

    GridWeb1.WebWorksheets(0).DataBind()

End Sub



{{< /highlight >}}

Çalışma zamanında worksheet.DataSource özelliğini değiştirseniz bile çalışma sayfası her zaman dataSet11'e bağlanır. Bunun nedeni, sayfanın her zaman çalışma sayfasının ASPX dosyasındaki etiketindeki DataSource bağlama bilgilerini kullanmasıdır. Çalışma zamanında sayfayı başka bir veri kaynağına bağlamak için, ASPC dosyasındaki çalışma sayfası etiketindeki veri kaynağı bağlama bilgilerini kaldırın. Etiketi şu şekilde düzenleyin:

**xml**

{{< highlight "csharp" >}}

 <acw:Worksheet BindStartRow="2" Name="Products" 

EnableCreateBindColumnHeader="True">



{{< /highlight >}}

DataBind yöntemini çağırmadan önce worksheet.DataSource ve worksheet.DataMember özelliklerini belirtin.

{{% /alert %}}
