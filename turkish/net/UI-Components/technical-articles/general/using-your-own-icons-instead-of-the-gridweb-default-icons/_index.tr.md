---
title: GridWeb in Varsayılan Simgeleri Yerine Kendi Simgelerinizi Kullanma
type: docs
weight: 10
url: /tr/net/aspose-cells-gridweb/use-your-own-icons-instead-of-the-default-icons/
keywords: GridWeb, simge, simgeler
description: Bu makale, GridWeb de simgelerin nasıl kullanılacağını açıklar.
---

{{% alert color="primary" %}} 

Bazı durumlarda, Aspose.Cells.GridWeb kontrolünün varsayılan simgeleri yerine kendi simgelerinizi (resimler) kullanmak isteyebilirsiniz. Bu makale, bunu nasıl yapılacağını açıklar.

{{% /alert %}} 

Denetimin varsayılan simgeleri, URL dizinine "/acw_client/" yerleştirilir. Dosya yolu varsayılan olarak "C:\Program Files\Aspose\Aspose.Cells for .NET\acw_client" olabilir. O klasörde submit.gif, save.gif vb. gibi dosyalar bulabilirsiniz. Bu resimleri kendi resimlerinizle değiştirmek istiyorsanız, web uygulamanızın web.config dosyasına bir yapılandırma bölümü ekleyin.

**XML**

{{< highlight csharp >}}

 <appSettings>

 <add key="Aspose.Cells.GridWeb.acw_client_path" value="/acw_client/" />

</appSettings>



{{< /highlight >}}

Bu yapılandırmanın yalnızca denetim resimlerin yolunu etkilediğini ve denetim istemci komut dosyalarının yolunu etkilemediğini fark etmiş olabilirsiniz. Örneğin, GridWeb kontrolü ile sayfanızı çalıştırırsanız ve tarayıcıda kaynak dosyasını kontrol ederseniz, kontrolün DIV öğesinin acw_client _path özelliğinin yine “/yourApp/webform1.aspx/” (örneğin) dediğini görebilirsiniz. Bazı durumlarda, istemci komut dosyası yolunu yeniden tanımlamanız gerekebilir. Denetimin, yeniden tanımlanan resim yolunu istemci komut dosyası yol olarak kullanması için, appSettings bölümüne başka bir yapılandırma ayarı ekleyin
**XML**

{{< highlight csharp >}}

 <add key="Aspose.Cells.GridWeb.force_script_path" value="true" />



{{< /highlight >}}

{{% alert color="primary" %}} 

Bu yapılandırma sadece lisanslı denetimle etkili olur.

{{% /alert %}}
