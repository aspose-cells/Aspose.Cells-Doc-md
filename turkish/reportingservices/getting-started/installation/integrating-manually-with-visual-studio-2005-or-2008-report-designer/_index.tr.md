---
title: Visual Studio 2005 veya 2008 Rapor Tasarımcısı ile El ile Entegre Etme
type: docs
weight: 30
url: /tr/reportingservices/integrating-manually-with-visual-studio-2005-or-2008-report-designer/
---

{{% alert color="primary" %}} 

Eğer MSI kurulum programı olmadan Microsoft Visual Studio Rapor Tasarımcısı için Aspose.Cells for Reporting Services'ü manuel olarak kurmak istiyorsanız lütfen aşağıdaki adımları sırayla uygulayın. Tüm gerekli kurulum ve yapılandırmayı otomatik olarak gerçekleştiren MSI kurulum programını kullanmanızı öneririz. Ancak MSI kurulum programı ile kurulum yapamazsanız, lütfen aşağıdaki yönergeleri takip edin. 
Bu bölüm, Business Intelligence Development Studio'ya yüklemek Aspose.Cells for Reporting Services'ü bir bilgisayara nasıl yükleneceğini açıklar. Bu, Microsoft Visual Studio 2005 veya 2008 Rapor Tasarımcısı'ndan Microsoft Excel formatlarına raporları tasarım zamanında dışa aktarmanızı sağlar. 

{{% /alert %}} 
- **Entegrasyon Süreci**
1. **Aspose.Cells.ReportingServices.dll**'yi Visual Studio dizinine kopyalayın. 
   1. Visual Studio 2005 Rapor Tasarımcısı ile entegre etmek için: **Aspose.Cells.ReportingServices.dll**'yi C:\Program Files\Microsoft Visual Studio 8\Common7\IDE\PrivateAssemblies dizinine kopyalayın.
   1. Visual Studio 2008 Rapor Tasarımcısı ile entegre etmek için: **Aspose.Cells.ReportingServices.dll**'yi C:\Program Files\Microsoft Visual Studio 9.0\Common7\IDE\PrivateAssemblies dizinine kopyalayın.
1. Aspose.Cells for Reporting Services'ü bir raporlama uzantısı olarak kaydedin: 
   1. Open **C:\Program Files\Microsoft Visual Studio <Version>\Common7\IDE\PrivateAssemblies\ RSReportDesigner.config** 
      (where <Version> is “8” for Visual Studio 2005 or “9.0” for Visual Studio 2008) and add the following lines into the <Render> element: 

**XML**

{{< highlight csharp >}}

 <Extension Name="ACXLS" Type="Aspose.Cells.ReportingServices.XlsRenderer,Aspose.Cells.ReportingServices" />

      <Extension Name="ACXLSX" Type="Aspose.Cells.ReportingServices.Excel2007XlsxRenderer,Aspose.Cells.ReportingServices" />

      <Extension Name="ACXLSB" Type="Aspose.Cells.ReportingServices.XlsbRenderer,Aspose.Cells.ReportingServices" />

      <Extension Name="ACXLSM" Type="Aspose.Cells.ReportingServices.Excel2007XlsmRenderer,Aspose.Cells.ReportingServices" />

      <Extension Name="ACXML" Type="Aspose.Cells.ReportingServices.SpreadsheetMLRenderer,Aspose.Cells.ReportingServices" />

      <Extension Name="ACHTML" Type="Aspose.Cells.ReportingServices.HtmlRenderer,Aspose.Cells.ReportingServices" />

      <Extension Name="ACCSV" Type="Aspose.Cells.ReportingServices.CSVRenderer,Aspose.Cells.ReportingServices" />

      <Extension Name="ACODS" Type="Aspose.Cells.ReportingServices.ODSRenderer,Aspose.Cells.ReportingServices" />

      <Extension Name="ACTXT" Type="Aspose.Cells.ReportingServices.TabDelimitedRenderer,Aspose.Cells.ReportingServices" />



{{< /highlight >}}

1. Aspose.Cells for Reporting Services'ün çalışmasına izin verin: 
   1. Open C:\Program Files\Microsoft Visual Studio <Version>\Common7\IDE\PrivateAssemblies\RSPreviewPolicy.config
      (where <Version> is “8” for Visual Studio 2005 or “9.0” for Visual Studio 2008) and add the following as the last item in the second to outer <CodeGroup> element (which should be <CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">): 

**XML**

{{< highlight csharp >}}

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

1. Aspose.Cells for Reporting Services'ün başarılı bir şekilde yüklendiğini doğrulayın: 
   1. Microsoft Visual Studio 2005 veya 2008 Rapor Tasarımcısı'nı çalıştırın veya yeniden başlatın.
      Dışa aktarma formatları listesinde yeni formatların farkına varmalısınız. 

**Bileşen kaydedildiğinde, Rapor Tasarımcısı'nda yeni dışa aktarma biçimleri görünür** 

![todo:image_alt_text](integrating-manually-with-visual-studio-2005-or-2008-report-designer_1.png)
