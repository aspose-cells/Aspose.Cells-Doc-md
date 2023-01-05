---
title: GridWeb Varsayılan Simgeleri Yerine Kendi Simgelerinizi Kullanma
type: docs
weight: 10
url: /tr/net/using-your-own-icons-instead-of-the-gridweb-default-icons/
---
{{% alert color="primary" %}} 

Bazen Aspose.Cells.GridWeb kontrolünün varsayılan simgeleri yerine kendi simgelerinizi (resimlerinizi) kullanmak isteyebilirsiniz. Bu makalede bunun nasıl yapılacağı açıklanmaktadır.

{{% /alert %}} 

Denetimin varsayılan simgeleri "/acw" URL yolunda bulunur_client/". Dosya yolu şu şekilde olabilir: "C:\Program Files\Aspose\Aspose.Cells for .NET\acw_client" varsayılan olarak. Bu klasörde send.gif, save.gif vb. dosyaları bulabilirsiniz. Bu resimleri kendi resimlerinizle değiştirmek isterseniz, web uygulamanızın web.config dosyasına bir config bölümü ekleyin.

**xml**

{{< highlight "csharp" >}}

 <appSettings>

 <add key="Aspose.Cells.GridWeb.acw_client_path" value="/acw_client/" />

</appSettings>



{{< /highlight >}}

Bu yapılandırmanın yalnızca kontrol görüntüleri yolunu etkilediğini ve kontrolün istemci-komut dosyaları yolunu etkilemediğini fark etmiş olabilirsiniz. Örneğin, sayfanızı GridWeb kontrolü ile çalıştırırsanız ve tarayıcıda kaynak dosyayı kontrol ederseniz, acw'nin_ müşteri_grid'in DIV öğesinin path özelliği hala "/yourApp/webform1.aspx/" diyor. Bazı durumlarda, istemci komut dosyası yolunu yeniden tanımlamanız gerekebilir. Denetimi, yeniden tanımlanmış görüntü yolunu istemci-komut dosyası yolu olarak kullanmaya zorlamak için, appSettings bölümünde başka bir yapılandırma ayarı ekleyin.
**xml**

{{< highlight "csharp" >}}

 <add key="Aspose.Cells.GridWeb.force_script_path" value="true" />



{{< /highlight >}}

{{% alert color="primary" %}} 

Bu yapılandırma, yalnızca lisanslı kontrol ile geçerli olacaktır.

{{% /alert %}}
