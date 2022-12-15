---
title: Интеграция вручную с Visual Studio 2005 или 2008 Report Designer
type: docs
weight: 30
url: /ru/reportingservices/integrating-manually-with-visual-studio-2005-or-2008-report-designer/
---
{{% alert color="primary" %}} 

Если вы хотите установить Aspose.Cells for Reporting Services вручную для конструктора отчетов Visual Studio Microsoft, выполните следующие шаги по порядку, без установщика MSI. Мы рекомендуем использовать установщик MSI, так как он автоматически выполняет всю необходимую установку и настройку. Однако, если вам не удалось выполнить установку с помощью установщика MSI, следуйте следующим рекомендациям.
 В этом разделе описывается, как установить Aspose.Cells for Reporting Services на компьютер с Business Intelligence Development Studio. Это позволит вам экспортировать отчеты в форматы Microsoft Excel во время разработки из конструктора отчетов Microsoft Visual Studio 2005 или 2008.

{{% /alert %}} 
- **Процесс интеграции**
1.  Копировать**Aspose.Cells.ReportingServices.dll** в каталог Visual Studio.
 1. Для интеграции с дизайнером отчетов Visual Studio 2005: скопируйте**Aspose.Cells.ReportingServices.dll** в каталог C:\Program Files\Microsoft Visual Studio 8\Common7\IDE\PrivateAssemblies.
 1. Для интеграции с конструктором отчетов Visual Studio 2008: скопируйте**Aspose.Cells.ReportingServices.dll**в каталог C:\Program Files\Microsoft Visual Studio 9.0\Common7\IDE\PrivateAssemblies.
1.  Зарегистрируйте Aspose.Cells for Reporting Services в качестве расширения рендеринга:
 1. Открыть**C:\Program Files\Microsoft Visual Studio <Версия>\Common7\IDE\PrivateAssemblies\ RSReportDesigner.config** 
 (куда<Version> равно «8» для Visual Studio 2005 или «9.0» для Visual Studio 2008) и добавьте следующие строки в<Render> элемент:

**XML**

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

1.  Дайте Aspose.Cells for Reporting Services разрешения на выполнение:
 1. Откройте C:\Program Files\Microsoft Visual Studio.<Version>\Common7\IDE\PrivateAssemblies\RSPreviewPolicy.config
 (куда<Version> равно «8» для Visual Studio 2005 или «9.0» для Visual Studio 2008) и добавьте следующий элемент в качестве последнего элемента во втором к внешнему<CodeGroup> элемент (который должен быть<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">): 

**XML**

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

1.  Убедитесь, что Aspose.Cells for Reporting Services успешно установлен:
 1. Запустите или перезапустите Microsoft Visual Studio 2005 или 2008 Report Designer.
 Вы должны заметить новые форматы, доступные в списке форматов экспорта.

**После регистрации компонента в дизайнере отчетов появляются новые форматы экспорта.** 

![дело:изображение_альтернативный_текст](integrating-manually-with-visual-studio-2005-or-2008-report-designer_1.png)
