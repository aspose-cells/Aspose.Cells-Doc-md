---
title: Aspose.Grid.Web i Aspose.Cells.GridWeb e Yükselt
type: docs
weight: 30
url: /tr/net/aspose-cells-gridweb/upgrade-aspose-grid-web-to-aspose-cells-gridweb/
keywords: GridWeb 
description: Bu makale, GridWeb in nasıl yükseltileceğini tanıtmaktadır.
---

{{% alert color="primary" %}}

Yükseltmeyi kolaylaştırmak için, mevcut kullanıcılar için kritik bilgileri açıklayan bir belge sağlıyoruz, özellikle eski Aspose.Grid.Web kullananlar ve Aspose.Cells.GridWeb'a yükseltme yapması gerekenler için.

Bu kısa notlar olması amaçlanmıştır ve [Geliştirici Kılavuzu](/cells/tr/net/aspose-cells-gridweb/developer-guide/) bölümlerine bakarak daha fazla bilgi bulmanız gerektiğini düşünüyoruz.

{{% /alert %}}

## **Aspose.Cells.GridWeb'e Yükseltme**

Aspose.Grid.Web kullanıcıları, Aspose.Cells.GridWeb'e yükselttiklerinde yeni sorunlarla karşılaşabilirler. Aspose.Grid.Web'in adının değiştiği ve Aspose.Cells'in bir parçası haline geldiği unutulmamalıdır, bu nedenle kontrolün eski sürümlerine devam etmeyeceğiz veya değişiklikler yapmayacağız. 

En yeni Aspose.Cells.GridWeb bileşenine yükseltmek zor değildir.

{{% alert color="primary" %}}

Sınıfların, yapılar, numaralandırmalar vb. üyeleriyle ilgili bazı değişiklikler yapılmış olmasına rağmen, API'de birkaç değişiklik bulunmaktadır. Çoğu değişiklik, kontrolün ad uzayları ve diğer etiketler veya özniteliklerine yapılmıştır.

{{% /alert %}}

Aşağıdaki, şu anda değiştirilmiş olan ad uzayları listesi ve diğer öznitelikler/etiketler listesidir:

1. Aspose.Grid.Web ad uzayı Aspose.Cells.GridWeb olarak değiştirildi.
1. Aspose.Grid.Web.Data ad uzayı Aspose.Cells.GridWeb.Data olarak değiştirildi.
1. Aspose.Grid.Web.Design ad uzayı Aspose.Cells.GridWeb.Design olarak değiştirildi.
1. Aspose.Grid.Formula ad uzayı Aspose.Cells.GridFormula olarak değiştirildi ve bileşenin en son sürümleriyle, söz konusu ad uzayı tamamen genel API'den kaldırıldı.
1. aspx formunda tag agw:GridWeb, acw:GridWeb olarak değiştirildi.
1. Eski Aspose.Grid.Web istemci yolu, agw_client, Aspose.Cells.GridWeb için acw_client olarak değiştirildi.
1. Örneğin web.config dosyasında istemci yol ayarı: 

{{< highlight java >}}

 <appSettings> 

    <add key="aspose.grid.web.agw_client_path" value="/agw_client/" />

    <add key="aspose.grid.web.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}

olarak değiştirildi 

{{< highlight java >}}

 <appSettings>

    <add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

    <add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}
