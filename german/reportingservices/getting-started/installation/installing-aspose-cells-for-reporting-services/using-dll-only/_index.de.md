---
title: Nur DLL verwenden
type: docs
weight: 20
url: /de/reportingservices/using-dll-only/
---
## So installieren Sie Aspose.Cells für Reporting Services nur mit der DLL:

-  Besuchen Sie die Aspose.Cells für Reporting Services[Download-Seite](https://downloads.aspose.com/cells/reportingservices) und lade die herunter**Aspose.Cells für Reporting Services (zip)** Archiv, das die neueste Version der Komponente und die installierte Dokumentation enthält.
 - Es gibt 7 Arten von Versionen Aspose.Cells.ReprotingServices.dll in Aspose.Cells.ReportingServices.DLLs_xx.xx.zip. Sie unterstützen verschiedene Microsoft-Berichtsserverprodukte.
 - Aspose.Cells.ReportingServices.dll im SSRS2005-Ordner unterstützt Microsoft SQL Server 2005 Reporting Services.
 - Aspose.Cells.ReportingServices.dll im SSRS2008-Ordner unterstützt Microsoft SQL Server 2008 Reporting Services.
 - Aspose.Cells.ReportingServices.dll im SSRS2008R2-Ordner unterstützt Microsoft SQL Server 2008R2/2012/2014 Reporting Services.
 Aspose.Cells.ReportingServices.dll im SSRS2016-Ordner unterstützt Microsoft SQL Server 2016/2017/2019 Reporting Services.
   
- Entpacken Sie das Archiv in ein Verzeichnis auf Ihrer Festplatte.

- Installieren Sie Aspose.Cells für Reporting Services Report Designer:
 - Registrieren**Aspose.Cells.ReportingServices.Client.dll** mit dem Dienstprogramm Regasm.exe.
 - Fügen Sie Aspose.Cells für das Reporting Services-Add-In in Excel hinzu.
   
- Installieren Sie Aspose.Cells für Reporting Services für Microsoft SQL Server Reporting Services die Dienstkomponente:
 - Lege das**Aspose.Cells.ReportingServices.dll** in den Ordner ${Microsoft SQL Server Reporting Services-Installationsordner}\ReportServer\bin.
 - Fügen Sie Aspose.Cells für Reporting Services-Renderer-Erweiterungen hinzu:
 - Offen**${Microsoft SQL Server Reporting Services-Installationsordner}\ReportServer\rsreportserver.config**
 - Fügen Sie die folgenden Zeilen in die hinzu<Render>……</Render> Element:
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
 - Fügen Sie Aspose.Cells für auszuführende Reporting Services-Berechtigungen hinzu:
 - Offen**${Microsoft SQL Server Reporting Services-Installationsordner}\ReportServer\rssrvpolicy.config** und ein
 - Fügen Sie das Folgende als letztes Element im zweiten zum äußeren hinzu<CodeGroup> Element (das sein sollte<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. "> ): 

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

## Überprüfen Sie, ob Aspose.Cells für Reporting Services erfolgreich installiert wurde:
 1. Öffnen Sie den Berichtsmanager und suchen Sie in der Liste der verfügbaren Exporttypen nach einem Bericht. (Starten Sie Report Manager, indem Sie einen Browser öffnen und die URL des Report Managers in die Adressleiste eingeben. (Standardmäßig lautet die URL http://<ComputerName>/Berichte).
 1. Wählen Sie einen der Berichte auf dem Server aus und öffnen Sie die**Wählen Sie Format** aufführen.
 Sie sollten die Liste der Exportformate sehen, die von Aspose.Cells für Reporting Services bereitgestellt wird.
 1. Wählen**XLS – Excel-Arbeitsmappe über Aspose.Cells**.
 1. Klicken Sie auf**Export**.
 Der Bericht wird im ausgewählten Format erstellt.
 1. Senden Sie es an den Client und öffnen Sie es in einer geeigneten Anwendung. In diesem Fall wird der Bericht in Microsoft Excel geöffnet.

Herzlichen Glückwunsch, Sie haben Aspose.Cells erfolgreich für Reporting Services installiert und einen Bericht als Microsoft Excel-Datei erstellt!


 Es gibt 7 Arten von Versionen Aspose.Cells.ReprotingServices.dll in Aspose.Cells.ReportingServices.DLLs_xx.xx.zip. Sie unterstützen verschiedene Microsoft-Berichtsserverprodukte.