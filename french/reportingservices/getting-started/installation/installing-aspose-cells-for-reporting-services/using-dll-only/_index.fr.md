---
title: Utilisation de DLL seulement
type: docs
weight: 20
url: /fr/reportingservices/using-dll-only/
---

## Comment installer Aspose.Cells for Reporting Services en utilisant uniquement le DLL :

- Visitez la page de téléchargement Aspose.Cells for Reporting Services (https://downloads.aspose.com/cells/reportingservices) et téléchargez l'archive **Aspose.Cells for Reporting Services (zip)** contenant la dernière version du composant et la documentation installée.
   - Il existe 7 types de versions Aspose.Cells.ReprotingSerivces.dll dans Aspose.Cells.ReportingServices.DLLs_xx.xx.zip. Ils prennent en charge différents produits de serveur de rapports Microsoft.
       - Aspose.Cells.ReportingServices.dll dans le dossier SSRS2005 prend en charge Microsoft SQL Server 2005 Reporting Services.
       - Aspose.Cells.ReportingServices.dll dans le dossier SSRS2008 prend en charge Microsoft SQL Server 2008 Reporting Services.
       - Aspose.Cells.ReportingServices.dll dans le dossier SSRS2008R2 prend en charge Microsoft SQL Server 2008R2/2012/2014 Reporting Services.
       - Aspose.Cells.ReportingServices.dll dans le dossier SSRS2016 prend en charge Microsoft SQL Server 2016/2017/2019 Reporting Services.

- Décompressez l'archive dans un répertoire sur votre disque dur.

- Installez Aspose.Cells for Reporting Services Report Designer :
   - Enregistrez **Aspose.Cells.ReportingServices.Client.dll** à l'aide de l'utilitaire Regasm.exe.
   - Ajoutez Aspose.Cells for Reporting Services module complémentaire dans Excel.

- Installez Aspose.Cells for Reporting Services pour le composant services Microsoft SQL Server Reporting Services :
   - Placez le **Aspose.Cells.ReportingServices.dll** dans le dossier d'installation ${Microsoft SQL Server Reporting Services}\ReportServer\bin. 
   - Ajoutez Aspose.Cells for Reporting Services extensions de rendu :  
      - Ouvrez **${dossier d'installation de Microsoft SQL Server Reporting Services}\ReportServer\rsreportserver.config**
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
   - Ajoutez les autorisations Aspose.Cells for Reporting Services pour exécuter :
      - Ouvrez **${dossier d'installation de Microsoft SQL Server Reporting Services}\ReportServer\rssrvpolicy.config** et a
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

## Vérifiez que Aspose.Cells for Reporting Services est installé avec succès :
   1. Open the Report Manager and check the list of available export types for a report. (Launch Report Manager by opening a browser and type the Report Manager URL into the address bar. (By default, the URL is http://<ComputerName>/Reports).
   1. Sélectionnez l'un des rapports sur le serveur et ouvrez la liste **Sélectionner le format**.
      Vous devriez voir la liste des formats d'exportation fournis par Aspose.Cells for Reporting Services.
   1. Sélectionnez **XLS - Classeur Excel via Aspose.Cells**.
   1. Cliquez sur **Exportation**.
      Le rapport est généré dans le format sélectionné.
   1. Envoyez-le au client et ouvrez-le dans une application appropriée. Dans ce cas, le rapport s'ouvre dans Microsoft Excel.

Félicitations, vous avez installé avec succès Aspose.Cells for Reporting Services et généré un rapport sous forme de fichier Microsoft Excel!


Il existe 7 types de versions Aspose.Cells.ReprotingSerivces.dll dans Aspose.Cells.ReportingServices.DLLs_xx.xx.zip. Ils prennent en charge différents produits de serveur de rapports Microsoft. 
