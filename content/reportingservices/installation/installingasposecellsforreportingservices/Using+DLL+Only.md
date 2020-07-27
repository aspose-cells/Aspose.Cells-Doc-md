+++
title = "Using DLL Only" 
description = "" 
weight = 12021 
+++

Aspose.Cells for Reporting Services : Using DLL Only  

# Aspose.Cells for Reporting Services : Using DLL Only


To install Aspose.Cells using only the DLL:

1.  Visit the Aspose.Cells for Reporting Services [download page](https://downloads.aspose.com/cells/reportingservices) and download the **Aspose.Cells.ReportingServices.zip** archive that contains the latest version of the component and the installed documentation.
2.  Unpack the archive into a directory on your hard drive.
3.  Register the client component:
    1.  Register **Aspose.Cells.ReportingServices.Client.dll** using the Regasm.exe utility.
    2.  Add Aspose.Cells for Reporting Services add-in in Excel.
4.  Register the services component:
    1.  Put the **Aspose.Cells.ReportingServices.dll** into the …\\Microsoft SQL Server\\<SQL Server Instance>\\Reporting Services\\bin folder, where SQL Server version is 9.
5.  Register Aspose.Cells for Reporting Services as a rendering extension:
6.  Open **C:\\Program Files\\Microsoft SQL Server\\MSSQL.x\\Reporting Services\\ReportServer\\rsreportserver.config** and add the following lines into the <Render>……</Render> element:
    
    **XML**
    
{{< code lang="xml" >}}
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


<!--End here.-->

</Render>
{{< /code >}}
    
7.  Give Aspose.Cells for Reporting Services permissions to execute:
    1.  Open **C:\\Program Files\\Microsoft SQL Server\\MSSQL.x\\Reporting Services\\ReportServer\\rssrvpolicy.config** and add the following as the last item in the second to the outer <CodeGroup> element (which should be <CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. "> ):
        
        **XML**
        
{{< code lang="xml" >}}
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
 
{{< /code >}}
        
8.  Verify that Aspose.Cells for Reporting Services is installed successfully:
    1.  Open the Report Manager and check the list of available export types for a report. (Launch Report Manager by opening a browser and type the Report Manager URL into the address bar. (By default, the URL is http://<ComputerName>/Reports).
    2.  Select one of the reports on the server and open the **Select Format** list.  
        You should see the list of export formats provided by Aspose.Cells for Reporting Services.
    3.  Select **XLS – Excel Workbook via Aspose.Cells**.
    4.  Click **Export**.  
        The report is generated in the selected format.
    5.  Send it to the client and open it in an appropriate application. In this case, the report opens in Microsoft Excel.

Congratulations, you’ve successfully installed Aspose.Cells for Reporting Services and generated a report as a Microsoft Excel file!

