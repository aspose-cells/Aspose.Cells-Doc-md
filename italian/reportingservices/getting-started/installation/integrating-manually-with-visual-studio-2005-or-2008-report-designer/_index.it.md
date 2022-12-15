---
title: Integrazione manuale con Visual Studio 2005 o 2008 Report Designer
type: docs
weight: 30
url: /it/reportingservices/integrating-manually-with-visual-studio-2005-or-2008-report-designer/
---
{{% alert color="primary" %}} 

Eseguire i seguenti passaggi nell'ordine se si desidera installare Aspose.Cells for Reporting Services manualmente per Microsoft Visual Studio Report Designer, senza il programma di installazione MSI. Si consiglia di utilizzare il programma di installazione MSI perché esegue automaticamente tutte le operazioni di installazione e configurazione necessarie. Tuttavia, se non riesci a eseguire l'installazione con il programma di installazione MSI, segui le seguenti linee guida.
 Questa sezione descrive come installare Aspose.Cells for Reporting Services su un computer con Business Intelligence Development Studio. Ciò consentirà di esportare report nei formati Microsoft Excel in fase di progettazione da Microsoft Visual Studio 2005 o 2008 Report Designer.

{{% /alert %}} 
- **Processo di integrazione**
1.  copia**Aspose.Cells.ReportingServices.dll** nella directory di Visual Studio.
 1. Per l'integrazione con Visual Studio 2005 Report Designer: copia**Aspose.Cells.ReportingServices.dll** nella directory C:\Program Files\Microsoft Visual Studio 8\Common7\IDE\PrivateAssemblies.
 1. Per l'integrazione con Visual Studio 2008 Report Designer: copia**Aspose.Cells.ReportingServices.dll**nella directory C:\Program Files\Microsoft Visual Studio 9.0\Common7\IDE\PrivateAssemblies.
1.  Registrati Aspose.Cells for Reporting Services come estensione rendering:
 1. Apri**C:\Programmi\Microsoft Visual Studio <Versione>\Common7\IDE\PrivateAssemblies\ RSReportDesigner.config** 
 (dove<Version> è "8" per Visual Studio 2005 o "9.0" per Visual Studio 2008) e aggiungere le seguenti righe nel<Render> elemento:

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

1.  Concedi a Aspose.Cells for Reporting Services le autorizzazioni per eseguire:
 1. Aprire C:\Programmi\Microsoft Visual Studio<Version>\Common7\IDE\PrivateAssemblies\RSPreviewPolicy.config
 (dove<Version> è "8" per Visual Studio 2005 o "9.0" per Visual Studio 2008) e aggiungere quanto segue come ultimo elemento nel secondo all'esterno<CodeGroup> elemento (che dovrebbe essere<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">): 

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

1.  Verificare che Aspose.Cells for Reporting Services sia stato installato correttamente:
 1. Eseguire o riavviare Microsoft Visual Studio 2005 o 2008 Report Designer.
 Dovresti notare i nuovi formati disponibili nell'elenco dei formati di esportazione.

**Quando il componente è stato registrato, in Report Designer vengono visualizzati nuovi formati di esportazione** 

![cose da fare:immagine_alt_testo](integrating-manually-with-visual-studio-2005-or-2008-report-designer_1.png)
