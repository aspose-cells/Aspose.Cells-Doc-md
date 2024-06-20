---
title: Solo Usando DLL
type: docs
weight: 20
url: /es/reportingservices/using-dll-only/
---

## Cómo instalar Aspose.Cells for Reporting Services solo usando el DLL:

- Visite la página de descarga Aspose.Cells for Reporting Services (https://downloads.aspose.com/cells/reportingservices) y descargue el archivo **Aspose.Cells for Reporting Services (zip)** que contiene la última versión del componente y la documentación instalada.
   - Hay 7 tipos de versiones Aspose.Cells.ReprotingSerivces.dll en Aspose.Cells.ReportingServices.DLLs_xx.xx.zip. Ellos admiten diferentes productos del servidor de informes de Microsoft.
       - Aspose.Cells.ReportingServices.dll en la carpeta SSRS2005 admite Microsoft SQL Server 2005 Reporting Services.
       - Aspose.Cells.ReportingServices.dll en la carpeta SSRS2008 admite Microsoft SQL Server 2008 Reporting Services.
       - Aspose.Cells.ReportingServices.dll en la carpeta SSRS2008R2 admite Microsoft SQL Server 2008R2/2012/2014 Reporting Services.
       - Aspose.Cells.ReportingServices.dll en la carpeta SSRS2016 admite Microsoft SQL Server 2016/2017/2019 Reporting Services.

- Descomprima el archivo en un directorio en su disco duro.

- Instale Aspose.Cells for Reporting Services Report Designer:
   - Registre **Aspose.Cells.ReportingServices.Client.dll** utilizando la utilidad Regasm.exe.
   - Agregue Aspose.Cells for Reporting Services complemento en Excel.

- Instale Aspose.Cells for Reporting Services para el componente de servicios de Microsoft SQL Server Reporting Services:
   - Coloque el **Aspose.Cells.ReportingServices.dll** en la carpeta de instalación de ${Microsoft SQL Server Reporting Services}\ReportServer\bin. 
   - Agregue extensiones de renderización Aspose.Cells for Reporting Services:  
      - Abra **${carpeta de instalación de Microsoft SQL Server Reporting Services}\ReportServer\rsreportserver.config**
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
   - Agregue permisos Aspose.Cells for Reporting Services para ejecutar:
      - Abra **${carpeta de instalación de Microsoft SQL Server Reporting Services}\ReportServer\rssrvpolicy.config** y a
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

## Verifique que Aspose.Cells for Reporting Services se instaló correctamente:
   1. Open the Report Manager and check the list of available export types for a report. (Launch Report Manager by opening a browser and type the Report Manager URL into the address bar. (By default, the URL is http://<ComputerName>/Reports).
   1. Seleccione uno de los informes en el servidor y abra la lista **Seleccionar formato**.
      Debería ver la lista de formatos de exportación proporcionados por Aspose.Cells for Reporting Services.
   1. Seleccione **XLS - Libro de Excel via Aspose.Cells**.
   1. Haga clic en **Exportar**.
      El informe se genera en el formato seleccionado.
   1. Envíelo al cliente y ábralo en una aplicación adecuada. En este caso, el informe se abre en Microsoft Excel.

¡Felicidades, ha instalado con éxito Aspose.Cells for Reporting Services y generado un informe como archivo de Microsoft Excel!


Hay 7 tipos de versiones de Aspose.Cells.ReprotingSerivces.dll en Aspose.Cells.ReportingServices.DLLs_xx.xx.zip. Admiten diferentes productos de servidor de informes de Microsoft. 
