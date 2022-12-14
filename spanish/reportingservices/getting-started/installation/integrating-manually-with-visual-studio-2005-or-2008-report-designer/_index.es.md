---
title: Integración manual con Visual Studio 2005 o 2008 Report Designer
type: docs
weight: 30
url: /es/reportingservices/integrating-manually-with-visual-studio-2005-or-2008-report-designer/
---
{{% alert color="primary" %}} 

 Realice los siguientes pasos en orden si desea instalar Aspose.Cells para Reporting Services manualmente para Microsoft Visual Studio Report Designer, sin el instalador MSI. Le recomendamos que utilice el instalador MSI porque realiza toda la instalación y configuración necesarias automáticamente. Sin embargo, si no puede instalar con el instalador MSI, siga las siguientes pautas.
Esta sección describe cómo instalar Aspose.Cells para Reporting Services en una computadora con Business Intelligence Development Studio. Esto le permitirá exportar informes a formatos de Excel Microsoft en tiempo de diseño desde Visual Studio 2005 o 2008 Report Designer Microsoft.

{{% /alert %}} 
- **Proceso de Integración**
1.  Copiar**Aspose.Cells.ReportingServices.dll** al directorio de Visual Studio.
 1. Para integrarse con Visual Studio 2005 Report Designer: copiar**Aspose.Cells.ReportingServices.dll** al directorio C:\Program Files\Microsoft Visual Studio 8\Common7\IDE\PrivateAssemblies.
 1. Para integrarse con Visual Studio 2008 Report Designer: copiar**Aspose.Cells.ReportingServices.dll** al directorio C:\Program Files\Microsoft Visual Studio 9.0\Common7\IDE\PrivateAssemblies.
1.  Registre Aspose.Cells para Reporting Services como una extensión de representación:
 1. Abierto**C:\Archivos de programa\Microsoft Visual Studio <Versión>\Common7\IDE\PrivateAssemblies\ RSReportDesigner.config** 
 (dónde<Version>es "8" para Visual Studio 2005 o "9.0" para Visual Studio 2008) y agregue las siguientes líneas en el<Render> elemento:

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

1.  Otorgue Aspose.Cells para los permisos de Reporting Services para ejecutar:
 1. Abra C:\Archivos de programa\Microsoft Visual Studio<Version>\Common7\IDE\PrivateAssemblies\RSPreviewPolicy.config
 (dónde<Version> es "8" para Visual Studio 2005 o "9.0" para Visual Studio 2008) y agregue lo siguiente como el último elemento en el segundo al exterior<CodeGroup> elemento (que debe ser<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">): 

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

1.  Verifique que Aspose.Cells para Reporting Services se haya instalado correctamente:
 1. Ejecute o reinicie Microsoft Visual Studio 2005 o 2008 Report Designer.
 Debería notar nuevos formatos disponibles en la lista de formatos de exportación.

**Cuando se ha registrado el componente, aparecen nuevos formatos de exportación en el Diseñador de informes** 

![todo:imagen_alternativa_texto](integrating-manually-with-visual-studio-2005-or-2008-report-designer_1.png)
