---
title: 演示设置
type: docs
weight: 40
url: /zh/jasperreports/demos-setup/
---

{{% alert color="primary" %}}

Aspose.Cells for JasperReports 包括许多演示项目，帮助您开始从应用程序导出报告为 Microsoft Excel 文档格式。

Aspose.Cells for JasperReports 提供的演示是标准的 JasperReports 演示，修改后演示了新导出器的使用。

{{% /alert %}}

运行 Aspose.Cells for JasperReports 演示，执行以下步骤：

1. Download JasperReports (e.g <https://sourceforge.net/projects/jasperreports/files/archive/>). Make sure to download the entire archived project with the source code and demos, not just a single JAR.
1. 将归档项目解压到硬盘上的某个位置，例如C:\。
1. Copy all demo folders from the \demo folder of **Aspose.Cells.JasperReports.zip** to **\<InstallDir>\demo\samples**, where "\<InstallDir>" is the location you have unpacked JasperReports to. This step is required because demo build scripts rely on the JasperReports’ folder structure, otherwise you will need to modify build scripts.
1. Copy **aspose.cells.jasperreports.jar** from the \lib folder of Aspose.Cells.JasperReports.zip to **\<InstallDir>\lib**.
1. Prepare Ant Build Tool and Ivy Dependency Manager, see **\<InstallDir>\readme.txt**.
1. Modify the **build.xml** at **\<InstallDir>\demo\samples**, add the aspose.cells.jasperreports.jar into the classpath:
   **\<path id="project-classpath"> ... \<pathelement location="../../lib/aspose.cells.jasperreports.jar"/> </path>**.
1. Change the current directory to **\<InstallDir>\demo\hsqldb** and run the following command line:
   **ant runServer**
1. Change the current directory to one of the Aspose.Cells for JasperReports demos, for example **\<InstallDir>\demo\samples\ac.charts** and run the following commands in the command line:
   **ant test** - 使用Aspose XLS导出器生成报表文件。
1. Open one of the resulting documents to view, for example **\<InstallDir>\demo\samples\ac.charts\build\reports\AreaChartReport.xls** in Microsoft Excel or another application.
