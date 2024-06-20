---
title: Yalnızca DLL Kullanımı
type: docs
weight: 20
url: /tr/reportingservices/using-dll-only/
---

## Yalnızca DLL kullanarak Aspose.Cells for Reporting Services'ü nasıl yükleyebilirsiniz:

- Aspose.Cells for Reporting Services [indirme sayfası](https://downloads.aspose.com/cells/reportingservices)'na gidin ve en son sürümü ve kurulu belgeleri içeren **Aspose.Cells for Reporting Services (zip)** arşivini indirin.
   - Aspose.Cells.ReportingServices.DLLs_xx.xx.zip içinde 7 farklı versiyonunda Aspose.Cells.ReprotingSerivces.dll bulunmaktadır. Bunlar farklı Microsoft rapor sunucusu ürünlerini desteklemektedir.
       - SSRS2005 klasöründeki Aspose.Cells.ReportingServices.dll, Microsoft SQL Server 2005 Raporlama Hizmetleri'ni destekler.
       - SSRS2008 klasöründeki Aspose.Cells.ReportingServices.dll, Microsoft SQL Server 2008 Raporlama Hizmetleri'ni destekler.
       - SSRS2008R2 klasöründeki Aspose.Cells.ReportingServices.dll, Microsoft SQL Server 2008R2/2012/2014 Raporlama Hizmetleri'ni destekler.
       - SSRS2016 klasöründeki Aspose.Cells.ReportingServices.dll, Microsoft SQL Server 2016/2017/2019 Raporlama Hizmetleri'ni destekler.

- Arşivi sabit diskinizdeki bir dizine açın.

- Aspose.Cells for Reporting Services Rapor Tasarımcısını yükleyin:
   - **Aspose.Cells.ReportingServices.Client.dll**'yi Regasm.exe aracılığıyla kaydedin.
   - Excel'de Aspose.Cells for Reporting Services eklentisini ekleyin.

- Microsoft SQL Server Raporlama Hizmetleri bileşeni için Aspose.Cells for Reporting Services'ü yükleyin:
   - **Aspose.Cells.ReportingServices.dll**'yi ${Microsoft SQL Server Raporlama Hizmetleri kurulum klasörü}\ReportServer\bin klasörüne koyun. 
   - Aspose.Cells for Reporting Services dönüştürücü uzantılarını ekleyin:  
      - **${Microsoft SQL Server Raporlama Hizmetleri kurulum klasörü}\ReportServer\rsreportserver.config**'i açın.
      - Add the following lines into the <Render>……</Render> element: 
{{< highlight xml >}}

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
   - Aspose.Cells for Reporting Services'nün yürütme izinlerini ekleyin:
      - **${Microsoft SQL Server Raporlama Hizmetleri kurulum klasörü}\ReportServer\rssrvpolicy.config**'i açın ve
      - Add the following as the last item in the second to the outer <CodeGroup> element (which should be <CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. "> ): 

{{< highlight xml >}}

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

## Aspose.Cells for Reporting Services'ün başarıyla yüklendiğini doğrulayın:
   1. Open the Report Manager and check the list of available export types for a report. (Launch Report Manager by opening a browser and type the Report Manager URL into the address bar. (By default, the URL is http://<ComputerName>/Reports).
   1. Sunucudaki raporlardan birini seçin ve **Biçim Seç** listesini açın.
      Aspose.Cells for Reporting Services tarafından sağlanan dışa aktarma biçimlerinin listesini görmelisiniz.
   1. **XLS - Aspose.Cells aracılığıyla Excel Çalışma Kitabı**'nı seçin.
   1. **Dışa Aktar**'ı tıklayın.
      Rapor seçilen formatta oluşturulur.
   1. İstemciye gönderin ve uygun bir uygulamada açın. Bu durumda rapor Microsoft Excel'de açılır.

Tebrikler, Aspose.Cells for Reporting Services'ü başarıyla yüklediniz ve bir Microsoft Excel dosyası olarak rapor oluşturdunuz!


Aspose.Cells.ReportingServices.DLLs_xx.xx.zip içinde 7 farklı versiyonunda Aspose.Cells.ReprotingSerivces.dll bulunmaktadır. Bunlar farklı Microsoft rapor sunucusu ürünlerini desteklemektedir. 
