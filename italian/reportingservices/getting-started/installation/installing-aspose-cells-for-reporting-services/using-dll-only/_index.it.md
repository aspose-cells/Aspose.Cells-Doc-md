---
title: Utilizzando solo DLL
type: docs
weight: 20
url: /it/reportingservices/using-dll-only/
---
## Come installare Aspose.Cells for Reporting Services utilizzando solo la DLL:

- Visita il Aspose.Cells for Reporting Services[pagina di download](https://downloads.aspose.com/cells/reportingservices) e scarica il**Aspose.Cells for Reporting Services (cap)** archivio che contiene l'ultima versione del componente e la documentazione installata.
 - Esistono 7 tipi di versioni Aspose.Cells.ReprotingSerivces.dll in Aspose.Cells.ReportingServices.DLLs_xx.xx.zip. Supportano diversi prodotti del server di report Microsoft.
 - Aspose.Cells.ReportingServices.dll nella cartella SSRS2005 supporta Microsoft SQL Server 2005 Reporting Services.
 - Aspose.Cells.ReportingServices.dll nella cartella SSRS2008 supporta Microsoft SQL Server 2008 Reporting Services.
 - Aspose.Cells.ReportingServices.dll nella cartella SSRS2008R2 supporta Microsoft SQL Server 2008R2/2012/2014 Reporting Services.
 - Aspose.Cells.ReportingServices.dll nella cartella SSRS2016 supporta Microsoft SQL Server 2016/2017/2019 Reporting Services.
   
- Decomprimere l'archivio in una directory sul disco rigido.

- Installa Aspose.Cells for Reporting Services Report Designer:
 - Registrati**Aspose.Cells.ReportingServices.Client.dll**utilizzando l'utilità Regasm.exe.
 - Aggiungere il componente aggiuntivo Aspose.Cells for Reporting Services in Excel.
   
- Installare Aspose.Cells for Reporting Services per Microsoft SQL Server Reporting Services il componente dei servizi:
 - Metti il**Aspose.Cells.ReportingServices.dll** nella cartella ${cartella di installazione di Microsoft SQL Server Reporting Services}\ReportServer\bin.
 - Aggiungi le estensioni del renderer Aspose.Cells for Reporting Services :
 - Aprire**${cartella di installazione di Microsoft SQL Server Reporting Services}\ReportServer\rsreportserver.config**
 - Aggiungere le seguenti righe nel file<Render>……</Render> elemento:
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
 - Aggiungi Aspose.Cells for Reporting Services autorizzazioni per eseguire:
 - Aprire**${cartella di installazione di Microsoft SQL Server Reporting Services}\ReportServer\rssrvpolicy.config** e un
 - Aggiungi quanto segue come ultimo elemento nel secondo verso l'esterno<CodeGroup> elemento (che dovrebbe essere<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. "> ): 

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

## Verificare che Aspose.Cells for Reporting Services sia installato correttamente:
1. Aprire Report Manager e controllare l'elenco dei tipi di esportazione disponibili per un report. (Avvia Report Manager aprendo un browser e digita l'URL di Report Manager nella barra degli indirizzi. (Per impostazione predefinita, l'URL è http://<ComputerName>/Rapporti).
 1. Selezionare uno dei report sul server e aprire il file**Seleziona Formato** elenco.
 Dovresti vedere l'elenco dei formati di esportazione fornito da Aspose.Cells for Reporting Services.
 1. Selezionare**XLS – Cartella di lavoro Excel tramite Aspose.Cells**.
 1. Fare clic**Esportare**.
 Il report viene generato nel formato selezionato.
 1. Inviarlo al client e aprirlo in un'applicazione appropriata. In questo caso, il report si apre in Microsoft Excel.

Congratulazioni, hai installato correttamente Aspose.Cells for Reporting Services e hai generato un report come file Microsoft Excel!


 Esistono 7 tipi di versioni Aspose.Cells.ReprotingSerivces.dll in Aspose.Cells.ReportingServices.DLLs_xx.xx.zip. Supportano diversi prodotti del server di report Microsoft.