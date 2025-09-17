##Using DLL Only
## How to install Aspose.Cells for Reporting Services using only the DLL:
- Visit the Aspose.Cells for Reporting Services [download page](https://downloads.aspose.com/cells/reportingservices) and download the **Aspose.Cells for Reporting Services (zip)** archive that contains the latest version of the component and the installed documentation.
- There are 7 kinds of versions Aspose.Cells.ReprotingSerivces.dll in Aspose.Cells.ReportingServices.DLLs_xx.xx.zip. They support different Microsoft report server products.
- Aspose.Cells.ReportingServices.dll in SSRS2005 folder support Microsoft SQL Server 2005 Reporting Services.
- Aspose.Cells.ReportingServices.dll in SSRS2008 folder support Microsoft SQL Server 2008 Reporting Services.
- Aspose.Cells.ReportingServices.dll in SSRS2008R2 folder support Microsoft SQL Server 2008R2/2012/2014 Reporting Services.
- Aspose.Cells.ReportingServices.dll in SSRS2016 folder support Microsoft SQL Server 2016/2017/2019 Reporting Services.
- Unpack the archive into a directory on your hard drive.
- Install Aspose.Cells for Reporting Services Report Designer:
- Register **Aspose.Cells.ReportingServices.Client.dll** using the Regasm.exe utility.
- Add Aspose.Cells for Reporting Services add-in in Excel.
- Install Aspose.Cells for Reporting Services for Microsoft SQL Server Reporting Services the services component:
- Put the **Aspose.Cells.ReportingServices.dll** into the ${Microsoft SQL Server Reporting Services installation folder}\ReportServer\bin folder.
- Add Aspose.Cells for Reporting Services renderer extensions :
- Open **${Microsoft SQL Server Reporting Services installation folder}\ReportServer\rsreportserver.config**
- Add the following lines into the <Render>……</Render> element:
...
- Add Aspose.Cells for Reporting Services permissions to execute:
- Open **${Microsoft SQL Server Reporting Services installation folder}\ReportServer\rssrvpolicy.config** and a
- Add the following as the last item in the second to the outer <CodeGroup> element (which should be <CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. "> ):
...
...
## Verify that Aspose.Cells for Reporting Services is installed successfully:
1. Open the Report Manager and check the list of available export types for a report. (Launch Report Manager by opening a browser and type the Report Manager URL into the address bar. (By default, the URL is http://<ComputerName>/Reports).
1. Select one of the reports on the server and open the **Select Format** list.
You should see the list of export formats provided by Aspose.Cells for Reporting Services.
1. Select **XLS – Excel Workbook via Aspose.Cells**.
1. Click **Export**.
The report is generated in the selected format.
1. Send it to the client and open it in an appropriate application. In this case, the report opens in Microsoft Excel.
Congratulations, you’ve successfully installed Aspose.Cells for Reporting Services and generated a report as a Microsoft Excel file!
There are 7 kinds of versions Aspose.Cells.ReprotingSerivces.dll in Aspose.Cells.ReportingServices.DLLs_xx.xx.zip. They support different Microsoft report server products.
