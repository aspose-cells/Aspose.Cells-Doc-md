---
title: Ручная интеграция с Visual Studio 2005 или 2008 Report Designer
type: docs
weight: 30
url: /ru/reportingservices/integrating-manually-with-visual-studio-2005-or-2008-report-designer/
---

{{% alert color="primary" %}} 

Пожалуйста, выполните следующие шаги в порядке, если вы хотите установить Aspose.Cells for Reporting Services вручную для Microsoft Visual Studio Report Designer, без использования установщика MSI. Мы рекомендуем использовать установщик MSI, потому что он выполняет все необходимые установку и настройку автоматически. Однако, если у вас не получается установить с помощью установщика MSI, пожалуйста, следуйте следующим рекомендациям. 
Этот раздел описывает, как установить Aspose.Cells for Reporting Services на компьютере с Business Intelligence Development Studio. Это позволит вам экспортировать отчеты в форматах Microsoft Excel на этапе проектирования из Microsoft Visual Studio 2005 или 2008 Report Designer. 

{{% /alert %}} 
- **Процесс интеграции**
1. Скопируйте **Aspose.Cells.ReportingServices.dll** в каталог Visual Studio. 
   1. Для интеграции с Visual Studio 2005 Report Designer: скопируйте **Aspose.Cells.ReportingServices.dll** в каталог C:\Program Files\Microsoft Visual Studio 8\Common7\IDE\PrivateAssemblies.
   1. Для интеграции с Visual Studio 2008 Report Designer: скопируйте **Aspose.Cells.ReportingServices.dll** в каталог C:\Program Files\Microsoft Visual Studio 9.0\Common7\IDE\PrivateAssemblies.
1. Зарегистрируйте Aspose.Cells for Reporting Services как расширение рендеринга: 
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

1. Предоставьте разрешения на выполнение Aspose.Cells for Reporting Services: 
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

1. Проверьте, что Aspose.Cells for Reporting Services был успешно установлен: 
   1. Запустите или перезапустите конструктор отчетов Microsoft Visual Studio 2005 или 2008.
      Вы должны заметить новые форматы, доступные в списке форматов экспорта. 

**После регистрации компонента в конструкторе отчетов появятся новые форматы экспорта** 

![todo:image_alt_text](integrating-manually-with-visual-studio-2005-or-2008-report-designer_1.png)
