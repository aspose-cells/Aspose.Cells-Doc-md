---
title: Yalnızca DLL Kullanımı
type: docs
weight: 20
url: /tr/reportingservices/using-dll-only/
---
## Yalnızca DLL kullanılarak Aspose.Cells for Reporting Services nasıl kurulur:

-  Aspose.Cells for Reporting Services'i ziyaret edin[indirme sayfası](https://downloads.aspose.com/cells/reportingservices) ve indir**Aspose.Cells for Reporting Services (zip)** bileşenin en son sürümünü ve yüklü belgeleri içeren arşiv.
 - Aspose.Cells.ReportingServices.DLLs_xx.xx.zip içinde 7 çeşit Aspose.Cells.ReprotingSerivces.dll sürümü vardır. Farklı Microsoft rapor sunucusu ürünlerini desteklerler.
 - SSRS2005 klasöründeki Aspose.Cells.ReportingServices.dll Microsoft SQL Server 2005 Raporlama Hizmetlerini destekler.
 - SSRS2008 klasöründeki Aspose.Cells.ReportingServices.dll Microsoft SQL Server 2008 Raporlama Hizmetlerini destekler.
 - SSRS2008R2 klasöründeki Aspose.Cells.ReportingServices.dll Microsoft SQL Server 2008R2/2012/2014 Raporlama Servislerini destekler.
 - SSRS2016 klasöründeki Aspose.Cells.ReportingServices.dll Microsoft SQL Server 2016/2017/2019 Raporlama Servislerini destekler.
   
- Arşivi, sabit sürücünüzdeki bir dizine paketinden çıkarın.

- Aspose.Cells for Reporting Services Rapor Tasarımcısını yükleyin:
 - Kayıt ol**Aspose.Cells.ReportingServices.Client.dll** Regasm.exe yardımcı programını kullanarak.
 - Excel'de Aspose.Cells for Reporting Services eklentisini ekleyin.
   
- Microsoft SQL Server Reporting Services için Aspose.Cells for Reporting Services'i yükleyin hizmetler bileşeni:
 - Koy**Aspose.Cells.ReportingServices.dll** ${Microsoft SQL Server Reporting Services kurulum klasörü}\ReportServer\bin klasörüne.
 - Aspose.Cells for Reporting Services işleyici uzantılarını ekleyin:
 - Açık**${Microsoft SQL Server Raporlama Hizmetleri kurulum klasörü}\ReportServer\rsreportserver.config**
 - Aşağıdaki satırları içine ekleyin<Render>……</Render> eleman:
{{< highlight "xml" >}}

 <Render>

...

<!--Start here.-->

<Extension Name="ACXLS" Type="Aspose.Cells.ReportingServices.XlsRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACXLSX" Type="Aspose.Cells.ReportingServices.Excel2007XlsxRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACXLSX(Data Only)" Type="Aspose.Cells.ReportingServices.Excel2007SimpleXlsxRenderer,Aspose.Cells.ReportingServices"/>

<Extension Name="ACXLSB" Type="Aspose.Cells.ReportingServices.XlsbRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACXLSM" Type="Aspose.Cells.ReportingServices.Excel2007XlsmRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACXML" Type="Aspose.Cells.ReportingServices.SpreadsheetMLRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACHTML" Type="Aspose.Cells.ReportingServices.HtmlRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACCSV" Type="Aspose.Cells.ReportingServices.CSVRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACODS" Type="Aspose.Cells.ReportingServices.ODSRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACTXT" Type="Aspose.Cells.ReportingServices.TabDelimitedRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACXPS" Type="Aspose.Cells.ReportingServices.XpsRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACMD" Type="Aspose.Cells.ReportingServices.MarkdownRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACTIFF" Type="Aspose.Cells.ReportingServices.TIFFRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACPDF" Type="Aspose.Cells.ReportingServices.PDFRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACPNG" Type="Aspose.Cells.ReportingServices.PNGRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACJPG" Type="Aspose.Cells.ReportingServices.JPGRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACEMF" Type="Aspose.Cells.ReportingServices.EMFRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACDIF" Type="Aspose.Cells.ReportingServices.DifRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACSVG" Type="Aspose.Cells.ReportingServices.SvgRenderer,Aspose.Cells.ReportingServices" />

<Extension Name="ACJSON" Type="Aspose.Cells.ReportingServices.JsonRenderer,Aspose.Cells.ReportingServices" />
<!--End here.-->

</Render>

{{< /highlight >}}
 - Yürütmek için Aspose.Cells for Reporting Services izinlerini ekleyin:
 - Açık**${Microsoft SQL Server Raporlama Hizmetleri kurulum klasörü}\ReportServer\rssrvpolicy.config** ve bir
 - Dışa ikincideki son öğe olarak aşağıdakini ekleyin<CodeGroup> eleman (olması gereken<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. "> ): 

{{< highlight "xml" >}}

 <CodeGroup>

...

<CodeGroup>

...

<!--Start here.-->

<CodeGroup class="UnionCodeGroup" version="1" PermissionSetName="FullTrust" Name="Aspose.Cells_for_Reporting_Services" Description="This code group grants full trust to the Aspose.Cells for Reporting Services assembly.">

<IMembershipCondition class="StrongNameMembershipCondition" version="1" PublicKeyBlob="00240000048000009400000006020000002400005253413100040000010001002780c08eaa89aedfb00b1b96137cca3e15f32826e0e4fd1da3c98d1e3968a03a019aa7b7228b151f6e5dae4dcb00f98479770f507626b04e786e5e93ec3757c1cc4ed1ac4b72c7649c4438e9d3a5f44d8b7522043686a2e8c2a495e04b917e0505d3201015c828e3c15afc8a46ab78293574b9e0475df68627bbabc5b564addd" />

</CodeGroup>

<!--End here.-->

</CodeGroup>

</CodeGroup>

{{< /highlight >}}

## Aspose.Cells for Reporting Services'in başarıyla yüklendiğini doğrulayın:
1. Rapor Yöneticisini açın ve bir rapor için mevcut dışa aktarma türleri listesini kontrol edin. (Bir tarayıcı açarak Rapor Yöneticisi'ni başlatın ve adres çubuğuna Rapor Yöneticisi URL'sini yazın. (Varsayılan olarak, URL http:// şeklindedir.)<ComputerName>/Raporlar).
 1. Sunucudaki raporlardan birini seçin ve**Format Seç** liste.
 Aspose.Cells for Reporting Services tarafından sağlanan dışa aktarma biçimlerinin listesini görmelisiniz.
 1. Seçin**XLS – Aspose.Cells aracılığıyla Excel Çalışma Kitabı**.
 1. tıklayın**İhracat**.
 Rapor seçilen formatta oluşturulur.
 1. İstemciye gönderin ve uygun bir uygulamada açın. Bu durumda rapor Microsoft Excel'de açılır.

Tebrikler, Aspose.Cells for Reporting Services'i başarıyla yüklediniz ve Microsoft Excel dosyası olarak bir rapor oluşturdunuz!


 Aspose.Cells.ReportingServices.DLLs_xx.xx.zip dosyasında 7 çeşit Aspose.Cells.ReprotingSerivces.dll sürümü vardır. Farklı Microsoft rapor sunucusu ürünlerini desteklerler.