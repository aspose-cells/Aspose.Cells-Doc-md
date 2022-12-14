---
title: Manuelle Integration mit Visual Studio 2005 oder 2008 Report Designer
type: docs
weight: 30
url: /de/reportingservices/integrating-manually-with-visual-studio-2005-or-2008-report-designer/
---
{{% alert color="primary" %}} 

 Bitte führen Sie die folgenden Schritte der Reihe nach aus, wenn Sie Aspose.Cells für Reporting Services manuell für Microsoft Visual Studio Report Designer ohne das MSI-Installationsprogramm installieren möchten. Wir empfehlen Ihnen, das MSI-Installationsprogramm zu verwenden, da es alle erforderlichen Installationen und Konfigurationen automatisch durchführt. Wenn die Installation mit dem MSI-Installationsprogramm jedoch fehlschlägt, befolgen Sie bitte die folgenden Richtlinien.
In diesem Abschnitt wird beschrieben, wie Sie Aspose.Cells für Reporting Services auf einem Computer mit Business Intelligence Development Studio installieren. Dadurch können Sie Berichte zur Entwurfszeit aus dem Microsoft Visual Studio 2005 oder 2008 Report Designer in Microsoft Excel-Formate exportieren.

{{% /alert %}} 
- **Integrationsprozess**
1.  Kopieren**Aspose.Cells.ReportingServices.dll** in das Visual Studio-Verzeichnis.
 1. Zur Integration mit Visual Studio 2005 Report Designer: kopieren**Aspose.Cells.ReportingServices.dll** in das Verzeichnis C:\Programme\Microsoft Visual Studio 8\Common7\IDE\PrivateAssemblies.
 1. Zur Integration mit Visual Studio 2008 Report Designer: kopieren**Aspose.Cells.ReportingServices.dll** in das Verzeichnis C:\Programme\Microsoft Visual Studio 9.0\Common7\IDE\PrivateAssemblies.
1.  Registrieren Sie Aspose.Cells für Reporting Services als Rendering-Erweiterung:
 1. Öffnen**C:\Programme\Microsoft Visual Studio <Version>\Common7\IDE\PrivateAssemblies\ RSReportDesigner.config** 
 (wo<Version>ist „8“ für Visual Studio 2005 oder „9.0“ für Visual Studio 2008) und fügen Sie die folgenden Zeilen in die hinzu<Render> Element:

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

1.  Geben Sie Aspose.Cells für Reporting Services-Berechtigungen zur Ausführung:
 1. Öffnen Sie C:\Programme\Microsoft Visual Studio<Version>\Common7\IDE\PrivateAssemblies\RSPreviewPolicy.config
 (wo<Version> ist „8“ für Visual Studio 2005 oder „9.0“ für Visual Studio 2008) und fügen Sie Folgendes als letztes Element in der zweiten nach außen hinzu<CodeGroup> Element (das sein sollte<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">): 

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

1.  Überprüfen Sie, ob Aspose.Cells für Reporting Services erfolgreich installiert wurde:
 1. Führen Sie Microsoft Visual Studio 2005 oder 2008 Report Designer aus oder starten Sie ihn neu.
 In der Liste der Exportformate sollten Sie neue verfügbare Formate bemerken.

**Wenn die Komponente registriert wurde, erscheinen neue Exportformate im Report Designer** 

![todo: Bild_alt_Text](integrating-manually-with-visual-studio-2005-or-2008-report-designer_1.png)
