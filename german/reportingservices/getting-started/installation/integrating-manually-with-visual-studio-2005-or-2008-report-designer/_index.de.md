---
title: Manuelles Integrieren mit Visual Studio 2005 oder 2008 Report Designer
type: docs
weight: 30
url: /de/reportingservices/integrating-manually-with-visual-studio-2005-or-2008-report-designer/
---

{{% alert color="primary" %}} 

Bitte führen Sie die folgenden Schritte in der richtigen Reihenfolge aus, wenn Sie Aspose.Cells for Reporting Services manuell für den Microsoft Visual Studio Report Designer installieren möchten, ohne das MSI-Installationsprogramm. Wir empfehlen die Verwendung des MSI-Installationsprogramms, da es alle notwendigen Installationen und Konfigurationen automatisch durchführt. Wenn die Installation mit dem MSI-Installationsprogramm jedoch fehlschlägt, befolgen Sie bitte die folgenden Anleitungen. 
In diesem Abschnitt wird beschrieben, wie Sie Aspose.Cells for Reporting Services auf einem Computer mit Business Intelligence Development Studio installieren. Dadurch können Sie Berichte im Designzeitbereich vom Microsoft Visual Studio 2005 oder 2008 Report Designer in Microsoft Excel-Formate exportieren. 

{{% /alert %}} 
- **Integrationsprozess**
1. Kopieren Sie **Aspose.Cells.ReportingServices.dll** in das Visual Studio-Verzeichnis. 
   1. Um mit dem Visual Studio 2005 Report Designer zu integrieren: Kopieren Sie **Aspose.Cells.ReportingServices.dll** in das Verzeichnis C:\Program Files\Microsoft Visual Studio 8\Common7\IDE\PrivateAssemblies.
   1. Um mit dem Visual Studio 2008 Report Designer zu integrieren: Kopieren Sie **Aspose.Cells.ReportingServices.dll** in das Verzeichnis C:\Program Files\Microsoft Visual Studio 9.0\Common7\IDE\PrivateAssemblies.
1. Aspose.Cells for Reporting Services als Rendering-Erweiterung registrieren: 
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

1. Geben Sie Aspose.Cells for Reporting Services die Berechtigung zur Ausführung: 
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

1. Überprüfen Sie, ob Aspose.Cells for Reporting Services erfolgreich installiert wurde: 
   1. Führen Sie Microsoft Visual Studio 2005 oder 2008 Report Designer aus oder starten Sie es neu.
      Sie sollten neue Formate in der Liste der Exportformate bemerken. 

**Wenn das Komponente registriert wurde, erscheinen neue Exportformate im Report Designer** 

![todo:image_alt_text](integrating-manually-with-visual-studio-2005-or-2008-report-designer_1.png)
