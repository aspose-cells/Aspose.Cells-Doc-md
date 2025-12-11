---
title: Demos Setup
type: docs
weight: 40
url: /jasperreports/demos-setup/
ai_search_scope: cells_jasperreports
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells for JasperReports includes a number of demo projects to help you get started exporting reports to Microsoft Excel document formats from your application.

The demos provided with Aspose.Cells for JasperReports are standard JasperReports demos modified to demonstrate the use of the new exporters.

{{% /alert %}}

To run Aspose.Cells for JasperReports demos, perform the following steps:

1. Download JasperReports (e.g., <https://sourceforge.net/projects/jasperreports/files/archive/>). Make sure to download the entire archived project with the source code and demos, not just a single JAR.  
2. Unpack the archived project to some location on your hard disk, for example C:\.  
3. Copy all demo folders from the \demo folder of **Aspose.Cells.JasperReports.zip** to **\<InstallDir>\demo\samples**, where "\<InstallDir>" is the location you have unpacked JasperReports to. This step is required because demo build scripts rely on the JasperReports’ folder structure; otherwise you will need to modify the build scripts.  
4. Copy **aspose.cells.jasperreports.jar** from the \lib folder of Aspose.Cells.JasperReports.zip to **\<InstallDir>\lib**.  
5. Prepare Ant Build Tool and Ivy Dependency Manager, see **\<InstallDir>\readme.txt**.  
6. Modify the **build.xml** at **\<InstallDir>\demo\samples**, add the aspose.cells.jasperreports.jar to the classpath:  
   **\<path id="project-classpath"> ... \<pathelement location="../../lib/aspose.cells.jasperreports.jar"/> </path>**.  
7. Change the current directory to **\<InstallDir>\demo\hsqldb** and run the following command line:  
   **ant runServer**  
8. Change the current directory to one of the Aspose.Cells for JasperReports demos, for example **\<InstallDir>\demo\samples\ac.charts**, and run the following command in the command line:  
   **ant test** – to produce report files using the Aspose XLS exporter.  
9. Open one of the resulting documents to view, for example **\<InstallDir>\demo\samples\ac.charts\build\reports\AreaChartReport.xls** in Microsoft Excel or another application.
