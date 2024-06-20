---
title: デモの設定
type: docs
weight: 40
url: /ja/jasperreports/demos-setup/
---

{{% alert color="primary" %}}

Aspose.Cells for JasperReportsは、アプリケーションからMicrosoft Excelドキュメント形式にレポートをエクスポートする際に始めるのに役立つデモプロジェクトを数多く含んでいます。

Aspose.Cells for JasperReportsに付属のデモは、新しいエクスポータの使用例を示すように変更された標準のJasperReportsデモです。

{{% /alert %}}

Aspose.Cells for JasperReportsのデモを実行するには、以下の手順を実行してください:

1. Download JasperReports (e.g <https://sourceforge.net/projects/jasperreports/files/archive/>). Make sure to download the entire archived project with the source code and demos, not just a single JAR.
1. ハードディスク上の任意の場所（たとえばC:\）にアーカイブされたプロジェクトを展開します。
1. Copy all demo folders from the \demo folder of **Aspose.Cells.JasperReports.zip** to **\<InstallDir>\demo\samples**, where "\<InstallDir>" is the location you have unpacked JasperReports to. This step is required because demo build scripts rely on the JasperReports’ folder structure, otherwise you will need to modify build scripts.
1. Copy **aspose.cells.jasperreports.jar** from the \lib folder of Aspose.Cells.JasperReports.zip to **\<InstallDir>\lib**.
1. Prepare Ant Build Tool and Ivy Dependency Manager, see **\<InstallDir>\readme.txt**.
1. Modify the **build.xml** at **\<InstallDir>\demo\samples**, add the aspose.cells.jasperreports.jar into the classpath:
   **\<path id="project-classpath"> ... \<pathelement location="../../lib/aspose.cells.jasperreports.jar"/> </path>**.
1. Change the current directory to **\<InstallDir>\demo\hsqldb** and run the following command line:
   **ant runServer**
1. Change the current directory to one of the Aspose.Cells for JasperReports demos, for example **\<InstallDir>\demo\samples\ac.charts** and run the following commands in the command line:
   **ant test** - Aspose XLSエクスポータを使用してレポートファイルを生成する。
1. Open one of the resulting documents to view, for example **\<InstallDir>\demo\samples\ac.charts\build\reports\AreaChartReport.xls** in Microsoft Excel or another application.
