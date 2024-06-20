---
title: Utilizzando solo DLL
type: docs
weight: 20
url: /it/reportingservices/using-dll-only/
---

## Come installare Aspose.Cells for Reporting Services utilizzando solo il DLL:

- Visita la pagina di [download](https://downloads.aspose.com/cells/reportingservices) di Aspose.Cells for Reporting Services e scarica l'archivio **Aspose.Cells for Reporting Services (zip)** che contiene la versione più recente del componente e la documentazione installata.
   - Ci sono 7 tipi di versioni Aspose.Cells.ReprotingSerivces.dll in Aspose.Cells.ReportingServices.DLLs_xx.xx.zip. Supportano diversi prodotti del server di report Microsoft.
       - Aspose.Cells.ReportingServices.dll nella cartella SSRS2005 supporta Microsoft SQL Server 2005 Reporting Services.
       - Aspose.Cells.ReportingServices.dll nella cartella SSRS2008 supporta Microsoft SQL Server 2008 Reporting Services.
       - Aspose.Cells.ReportingServices.dll nella cartella SSRS2008R2 supporta Microsoft SQL Server 2008R2/2012/2014 Reporting Services.
       - Aspose.Cells.ReportingServices.dll nella cartella SSRS2016 supporta Microsoft SQL Server 2016/2017/2019 Reporting Services.

- Scompatta l'archivio in una directory sul tuo disco rigido.

- Installa Aspose.Cells for Reporting Services Report Designer:
   - Registra **Aspose.Cells.ReportingServices.Client.dll** utilizzando l'utility Regasm.exe.
   - Aggiungi il componente aggiuntivo Aspose.Cells for Reporting Services in Excel.

- Installa Aspose.Cells for Reporting Services per il componente dei servizi di Microsoft SQL Server Reporting Services:
   - Metti **Aspose.Cells.ReportingServices.dll** nella cartella di installazione di ${Microsoft SQL Server Reporting Services}\ReportServer\bin. 
   - Aggiungi le estensioni di rendering Aspose.Cells for Reporting Services:  
      - Apri **${Microsoft SQL Server Reporting Services installation folder}\ReportServer\rsreportserver.config**
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
   - Aggiungi i permessi di esecuzione Aspose.Cells for Reporting Services:
      - Apri **${Microsoft SQL Server Reporting Services installation folder}\ReportServer\rssrvpolicy.config** e
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

## Verifica che Aspose.Cells for Reporting Services sia stato installato correttamente:
   1. Open the Report Manager and check the list of available export types for a report. (Launch Report Manager by opening a browser and type the Report Manager URL into the address bar. (By default, the URL is http://<ComputerName>/Reports).
   1. Seleziona uno dei report sul server e apri l'elenco **Seleziona Formato**.
      Dovresti vedere l'elenco dei formati di esportazione forniti da Aspose.Cells for Reporting Services.
   1. Seleziona **XLS - Cartella di lavoro Excel tramite Aspose.Cells**.
   1. Clicca su **Esporta**.
      Il report è generato nel formato selezionato.
   1. Invialo al cliente e aprilo in un'applicazione appropriata. In questo caso, il report si apre in Microsoft Excel.

Congratulazioni, hai installato con successo Aspose.Cells for Reporting Services e generato un report come file Microsoft Excel!


Ci sono 7 tipi di versioni Aspose.Cells.ReprotingSerivces.dll in Aspose.Cells.ReportingServices.DLLs_xx.xx.zip. Supportano diversi prodotti server Microsoft report. 
