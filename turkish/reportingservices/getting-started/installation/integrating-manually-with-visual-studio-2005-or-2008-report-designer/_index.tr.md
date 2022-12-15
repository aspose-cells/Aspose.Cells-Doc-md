---
title: Visual Studio 2005 veya 2008 Rapor Tasarımcısı ile Manuel Olarak Tümleştirme
type: docs
weight: 30
url: /tr/reportingservices/integrating-manually-with-visual-studio-2005-or-2008-report-designer/
---
{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services'i Microsoft Visual Studio Report Designer için MSI yükleyicisi olmadan manuel olarak yüklemek istiyorsanız lütfen aşağıdaki adımları uygulayın. Gerekli tüm kurulum ve yapılandırmayı otomatik olarak gerçekleştirdiği için MSI yükleyicisini kullanmanızı öneririz. Ancak, MSI yükleyicisini yüklemeyi başaramazsanız, lütfen aşağıdaki yönergeleri izleyin.
 Bu bölüm, Business Intelligence Development Studio ile bir bilgisayara Aspose.Cells for Reporting Services'in nasıl kurulacağını açıklamaktadır. Bu, raporları tasarım zamanında Microsoft Visual Studio 2005 veya 2008 Rapor Tasarımcısı'ndan Microsoft Excel biçimlerine aktarmanıza olanak tanır.

{{% /alert %}} 
- **Entegrasyon Süreci**
1.  kopyala**Aspose.Cells.ReportingServices.dll** Visual Studio dizinine.
 1. Visual Studio 2005 Rapor Tasarımcısı ile entegre etmek için: kopyala**Aspose.Cells.ReportingServices.dll** C:\Program Files\Microsoft Visual Studio 8\Common7\IDE\PrivateAssemblies dizinine.
 1. Visual Studio 2008 Rapor Tasarımcısı ile entegre etmek için: kopyala**Aspose.Cells.ReportingServices.dll**C:\Program Files\Microsoft Visual Studio 9.0\Common7\IDE\PrivateAssemblies dizinine.
1.  Aspose.Cells for Reporting Services'i işleme uzantısı olarak kaydedin:
 1. Aç**C:\Program Files\Microsoft Visual Studio <Sürüm>\Common7\IDE\PrivateAssemblies\ RSReportDesigner.config** 
 (nerede<Version> Visual Studio 2005 için “8” veya Visual Studio 2008 için “9.0” dır) ve aşağıdaki satırları<Render> eleman:

**xml**

{{< highlight "csharp" >}}

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

1.  Aspose.Cells for Reporting Services'e aşağıdakileri yürütme izni verin:
 1. C:\Program Files\Microsoft Visual Studio'yu açın<Version>\Common7\IDE\PrivateAssemblies\RSPreviewPolicy.config
 (nerede<Version> Visual Studio 2005 için “8” veya Visual Studio 2008 için “9.0” dır) ve ikinciden dıştaki son öğe olarak aşağıdakini ekleyin<CodeGroup> eleman (olması gereken<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">): 

**xml**

{{< highlight "csharp" >}}

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

1.  Aspose.Cells for Reporting Services'in başarıyla yüklendiğini doğrulayın:
 1. Microsoft Visual Studio 2005 veya 2008 Rapor Tasarımcısını çalıştırın veya yeniden başlatın.
 Dışa aktarma biçimleri listesinde yeni biçimlerin bulunduğunu fark edeceksiniz.

**Bileşen kaydedildiğinde, Rapor Tasarımcısı'nda yeni dışa aktarma biçimleri görünür** 

![yapılacaklar:resim_alternatif_Metin](integrating-manually-with-visual-studio-2005-or-2008-report-designer_1.png)
