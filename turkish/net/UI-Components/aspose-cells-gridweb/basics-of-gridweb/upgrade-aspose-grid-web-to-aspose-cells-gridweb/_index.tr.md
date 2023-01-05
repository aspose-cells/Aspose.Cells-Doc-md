---
title: Aspose.Grid.Web'i Aspose.Cells.GridWeb'e yükseltin
type: docs
weight: 30
url: /tr/net/upgrade-aspose-grid-web-to-aspose-cells-gridweb/
---
{{% alert color="primary" %}}

Yükseltmeyi kolaylaştırmak için, özellikle eski Aspose.Grid.Web'i kullanmış ve birleştirilmiş Aspose.Cells.GridWeb'e yükseltmesi gereken mevcut kullanıcılar için kritik bilgileri açıklayan bir belge tutuyoruz.

 Bunların kısa notlar olması amaçlanmıştır ve kitabın bölümlerine bakarak daha fazla bilgi bulabilmeniz gerekir.[Geliştirici Kılavuzu](/cells/tr/net/developer-guide/).

{{% /alert %}}

## **Aspose.Cells.GridWeb'e yükseltme**

 Aspose.Grid.Web kullanıcıları, yükseltme yaptıklarında yeni Aspose.Cells.GridWeb'i kullanırken sorunlarla karşılaşabilirler. Aspose.Grid.Web'in yeniden adlandırıldığına ve Aspose.Cells'in bir parçası haline geldiğine dikkat edilmelidir, bu nedenle kontrolün eski sürümlerine devam etmeyeceğiz veya bu sürümlerde değişiklik yapmayacağız.

En son Aspose.Cells.GridWeb bileşenine yükseltmek zor değil.

{{% alert color="primary" %}}

API'de üyeler, yapılar, numaralandırmalar vb. ile sınıflar aynı kaldığından birkaç değişiklik vardır. Değişikliklerin çoğu, kontrolün ad alanlarında ve diğer etiketlerde veya niteliklerde yapılmıştır.

{{% /alert %}}

Aşağıda, şimdi değiştirilen ad alanları listesi ve diğer nitelikler/etiketler yer almaktadır:

1. Aspose.Grid.Web ad alanı, Aspose.Cells.GridWeb olarak yeniden adlandırıldı.
1. Aspose.Grid.Web.Data ad alanı, Aspose.Cells.GridWeb.Data olarak yeniden adlandırıldı.
1. Aspose.Grid.Web.Design ad alanı, Aspose.Cells.GridWeb.Design olarak yeniden adlandırıldı.
1. Aspose.Grid.Formula ad alanı, Aspose.Cells.GridFormula olarak yeniden adlandırıldı ve bileşenin son sürümleriyle, söz konusu ad alanı genel API'den tamamen kaldırıldı.
1. agw:GridWeb etiketi, aspx biçiminde acw:GridWeb olarak değiştirildi.
1. Eski Aspose.Grid.Web istemci yolu, agw_istemci, acw olarak değişti_Aspose.Cells.GridWeb için istemci.
1.  Web.config dosyasındaki istemci yolu ayarı, örneğin:

{{< highlight "java" >}}

 <appSettings> 

    <add key="aspose.grid.web.agw_client_path" value="/agw_client/" />

    <add key="aspose.grid.web.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}

 olarak değişti

{{< highlight "java" >}}

 <appSettings>

    <add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

    <add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}
