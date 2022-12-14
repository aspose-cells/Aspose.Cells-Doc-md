---
title: Intégration manuelle avec Visual Studio 2005 ou 2008 Report Designer
type: docs
weight: 30
url: /fr/reportingservices/integrating-manually-with-visual-studio-2005-or-2008-report-designer/
---
{{% alert color="primary" %}} 

 Veuillez effectuer les étapes suivantes dans l'ordre si vous souhaitez installer Aspose.Cells pour Reporting Services manuellement pour Microsoft Visual Studio Report Designer, sans le programme d'installation MSI. Nous vous recommandons d'utiliser le programme d'installation MSI car il effectue automatiquement toute l'installation et la configuration nécessaires. Cependant, si vous ne parvenez pas à installer avec le programme d'installation MSI, veuillez suivre les instructions suivantes.
Cette section décrit comment installer Aspose.Cells pour Reporting Services sur un ordinateur avec Business Intelligence Development Studio. Cela vous permettra d'exporter des rapports aux formats Excel Microsoft au moment de la conception à partir de Microsoft Visual Studio 2005 ou 2008 Report Designer.

{{% /alert %}} 
- **Processus d'intégration**
1.  Copie**Aspose.Cells.ReportingServices.dll** dans le répertoire Visual Studio.
 1. Pour intégrer avec Visual Studio 2005 Report Designer : copiez**Aspose.Cells.ReportingServices.dll** dans le répertoire C:\Program Files\Microsoft Visual Studio 8\Common7\IDE\PrivateAssemblies.
 1. Pour intégrer avec Visual Studio 2008 Report Designer : copiez**Aspose.Cells.ReportingServices.dll** dans le répertoire C:\Program Files\Microsoft Visual Studio 9.0\Common7\IDE\PrivateAssemblies.
1.  Enregistrez Aspose.Cells pour Reporting Services en tant qu'extension de rendu :
 1. Ouvrir**C:\Program Files\Microsoft Visual Studio <Version>\Common7\IDE\PrivateAssemblies\ RSReportDesigner.config** 
 (où<Version>est "8" pour Visual Studio 2005 ou "9.0" pour Visual Studio 2008) et ajoutez les lignes suivantes dans le<Render> élément:

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

1.  Donnez Aspose.Cells pour les autorisations Reporting Services à exécuter :
 1. Ouvrez C:\Program Files\Microsoft Visual Studio<Version>\Common7\IDE\PrivateAssemblies\RSPreviewPolicy.config
 (où<Version> est "8" pour Visual Studio 2005 ou "9.0" pour Visual Studio 2008) et ajoutez ce qui suit comme dernier élément dans le deuxième à l'extérieur<CodeGroup> élément (qui devrait être<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">): 

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

1.  Vérifiez que Aspose.Cells pour Reporting Services a été installé avec succès :
 1. Exécutez ou redémarrez Microsoft Visual Studio 2005 ou 2008 Report Designer.
 Vous devriez remarquer de nouveaux formats disponibles dans la liste des formats d'exportation.

**Une fois le composant enregistré, de nouveaux formats d'exportation apparaissent dans Report Designer** 

![tâche : image_autre_texte](integrating-manually-with-visual-studio-2005-or-2008-report-designer_1.png)
