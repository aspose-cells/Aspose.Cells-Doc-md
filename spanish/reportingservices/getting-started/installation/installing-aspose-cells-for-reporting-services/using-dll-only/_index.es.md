---
title: Usar solo DLL
type: docs
weight: 20
url: /es/reportingservices/using-dll-only/
---
## Cómo instalar Aspose.Cells for Reporting Services usando solo la DLL:

- Visita el Aspose.Cells for Reporting Services[página de descarga](https://downloads.aspose.com/cells/reportingservices) y descargar el**Aspose.Cells for Reporting Services (código postal)** archivo que contiene la última versión del componente y la documentación instalada.
 - Hay 7 tipos de versiones Aspose.Cells.ReprotingServivces.dll en Aspose.Cells.ReportingServices.DLLs_xx.xx.zip. Admiten diferentes productos de servidor de informes Microsoft.
 - Aspose.Cells.ReportingServices.dll en la carpeta SSRS2005 compatible con Microsoft SQL Server 2005 Reporting Services.
 - Aspose.Cells.ReportingServices.dll en la carpeta SSRS2008 compatible con Microsoft SQL Server 2008 Reporting Services.
 - Aspose.Cells.ReportingServices.dll en la carpeta SSRS2008R2 compatible con Microsoft SQL Server 2008R2/2012/2014 Reporting Services.
 - Aspose.Cells.ReportingServices.dll en la carpeta SSRS2016 compatible con Microsoft SQL Server 2016/2017/2019 Reporting Services.
   
- Descomprima el archivo en un directorio de su disco duro.

- Instalar Aspose.Cells for Reporting Services Diseñador de informes:
 - Registro**Aspose.Cells.ReportingServices.Client.dll**utilizando la utilidad Regasm.exe.
 - Agregue el complemento Aspose.Cells for Reporting Services en Excel.
   
- Instale Aspose.Cells for Reporting Services para Microsoft SQL Server Reporting Services el componente de servicios:
 - Pon el**Aspose.Cells.ReportingServices.dll** en la carpeta de instalación ${Microsoft SQL Server Reporting Services}\ReportServer\bin.
 - Agregue Aspose.Cells for Reporting Services extensiones de renderizador:
 - Abierto**${Microsoft Carpeta de instalación de SQL Server Reporting Services}\ReportServer\rsreportserver.config**
 - Agregue las siguientes líneas en el<Render>……</Render> elemento:
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
 - Agregar Aspose.Cells for Reporting Services permisos para ejecutar:
 - Abierto**${Microsoft Carpeta de instalación de SQL Server Reporting Services}\ReportServer\rssrvpolicy.config** y un
 - Agregue lo siguiente como el último elemento en el segundo al exterior<CodeGroup> elemento (que debe ser<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. "> ): 

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

## Verifique que Aspose.Cells for Reporting Services esté instalado correctamente:
1. Abra el Administrador de informes y consulte la lista de tipos de exportación disponibles para un informe. (Inicie el Administrador de informes abriendo un navegador y escriba la URL del Administrador de informes en la barra de direcciones. (De forma predeterminada, la URL es http://<ComputerName>/Informes).
 1. Seleccione uno de los informes en el servidor y abra el**Seleccionar formato** lista.
 Debería ver la lista de formatos de exportación proporcionada por Aspose.Cells for Reporting Services.
 1. Seleccione**XLS - Libro de trabajo de Excel a través de Aspose.Cells**.
 1. Haga clic en**Exportar**.
 El informe se genera en el formato seleccionado.
 1. Envíelo al cliente y ábralo en una aplicación apropiada. En este caso, el informe se abre en Microsoft Excel.

Felicitaciones, instaló correctamente Aspose.Cells for Reporting Services y generó un informe como un archivo de Excel Microsoft.


 Hay 7 tipos de versiones Aspose.Cells.ReprotingServivces.dll en Aspose.Cells.ReportingServices.DLLs_xx.xx.zip. Admiten diferentes productos de servidor de informes Microsoft.