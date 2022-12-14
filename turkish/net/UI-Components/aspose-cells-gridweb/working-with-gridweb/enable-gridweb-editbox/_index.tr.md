---
title: GridWeb EditBox'ı Etkinleştir
type: docs
weight: 110
url: /tr/net/enable-gridweb-editbox/
---
{{% alert color="primary" %}} 

GridWeb'in Düzenleme Kutusu, verileri/formülleri hücrelere görmek/girmek veya kopyalamak için kullanabileceğiniz, kontrolün üst kısmında işlenen bir araç çubuğudur. Ayrıca düzenlemekte olduğunuz hücrenin adını da gösterir. Çerçeveye tıkladıktan sonra veya veri yazmaya başladığınızda veya eşittir (=) sembolü yazdığınızda, Düzenleme Kutusu aktif olacaktır.

{{% /alert %}} 
## **Aspose.Cells.GridWeb'in Düzenleme Kutusunu Ayarlama**
GridWeb denetimi, geliştiricilerin araç çubuğunu açmak için bunu "True" olarak atayabilecekleri ShowCellEditBox özelliğini sağlar. Özniteliğin varsayılan değeri Yanlış'tır. Değerini "True" olarak ayarladığınızda, GridWeb kontrolünün üstünde Düzenleme Kutusu görünecektir.

{{% alert color="primary" %}} 

 Bu özelliği etkinleştirmek için, "jquery.js" dosyasını projenize aktarmanız ve çalışması için .aspx sayfalarınıza başvurmanız gerekir. jQuery arşivini adresinden indirebilirsiniz.<https://jqueryui.com/download/all/> ve kütüphane dosyalarını projedeki bazı klasörlere koyun ve kütüphane dosyasına şu şekilde referans ekleyin:<script> .aspx web formunuzda aşağıdaki gibi etiketleyin. En son jQuery sürümlerinin tümü tamam.

{{< highlight "csharp" >}}

 <head id="Head1" runat="server">

  <title>Untitled Page</title>

  <script type="text/javascript" src="/jquery/jquery.js"></script>

</head>



{{< /highlight >}}

{{% /alert %}} 

**Edit Box ile GridWeb kontrolü** 

![yapılacaklar:resim_alternatif_Metin](enable-gridweb-editbox_1.png)
### **Örnek**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-DisplayCellEditBox.aspx-DisplayCellEditBox.cs" >}}
