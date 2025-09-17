##Integrating Manually with Visual Studio 2005 or 2008 Report Designer
Please perform the following steps in order if you want install Aspose.Cells for Reporting Services manually for Microsoft Visual Studio Report Designer, without the MSI installer. We recommend you use the MSI installer because it performs all necessary installation and configuration automatically. However, if you fail to install with MSI installer then please follow the following guidelines.
This section describes how to install Aspose.Cells for Reporting Services on a computer with Business Intelligence Development Studio. This will enable you to export reports to Microsoft Excel formats at design time from the Microsoft Visual Studio 2005 or 2008 Report Designer.
- **Integration Process**
1. Copy **Aspose.Cells.ReportingServices.dll** to the Visual Studio directory.
1. To integrate with Visual Studio 2005 Report Designer: copy **Aspose.Cells.ReportingServices.dll** to the C:\Program Files\Microsoft Visual Studio 8\Common7\IDE\PrivateAssemblies directory.
1. To integrate with Visual Studio 2008 Report Designer: copy **Aspose.Cells.ReportingServices.dll** to the C:\Program Files\Microsoft Visual Studio 9.0\Common7\IDE\PrivateAssemblies directory.
1. Register Aspose.Cells for Reporting Services as a rendering extension:
1. Open **C:\Program Files\Microsoft Visual Studio <Version>\Common7\IDE\PrivateAssemblies\ RSReportDesigner.config**
(where <Version> is “8” for Visual Studio 2005 or “9.0” for Visual Studio 2008) and add the following lines into the <Render> element:
**XML**
1. Give Aspose.Cells for Reporting Services permissions to execute:
1. Open C:\Program Files\Microsoft Visual Studio <Version>\Common7\IDE\PrivateAssemblies\RSPreviewPolicy.config
(where <Version> is “8” for Visual Studio 2005 or “9.0” for Visual Studio 2008) and add the following as the last item in the second to outer <CodeGroup> element (which should be <CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">):
**XML**
...
...
1. Verify that Aspose.Cells for Reporting Services was installed successfully:
1. Run or restart Microsoft Visual Studio 2005 or 2008 Report Designer.
You should notice new formats available in the list of export formats.
**When the component has been registered, new export formats appear in Report Designer**
![todo:image_alt_text](integrating-manually-with-visual-studio-2005-or-2008-report-designer_1.png)
