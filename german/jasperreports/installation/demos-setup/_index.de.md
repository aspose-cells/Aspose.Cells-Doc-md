---
title: Demos Setup
type: docs
weight: 40
url: /de/jasperreports/demos-setup/
---

{{% alert color="primary" %}}

Aspose.Cells for JasperReports enthält eine Reihe von Demoprojekten, um Ihnen beim Exportieren von Berichten in Microsoft Excel-Dokumentformate aus Ihrer Anwendung zu helfen.

Die mit Aspose.Cells for JasperReports bereitgestellten Demos sind Standard JasperReports-Demos, die modifiziert wurden, um die Verwendung der neuen Exporter zu demonstrieren.

{{% /alert %}}

Um die Demos von Aspose.Cells for JasperReports auszuführen, führen Sie die folgenden Schritte aus:

1. Download JasperReports (e.g <https://sourceforge.net/projects/jasperreports/files/archive/>). Make sure to download the entire archived project with the source code and demos, not just a single JAR.
1. Entpacken Sie das archivierte Projekt an einen beliebigen Ort auf Ihrer Festplatte, zum Beispiel C:\.
1. Copy all demo folders from the \demo folder of **Aspose.Cells.JasperReports.zip** to **\<InstallDir>\demo\samples**, where "\<InstallDir>" is the location you have unpacked JasperReports to. This step is required because demo build scripts rely on the JasperReports’ folder structure, otherwise you will need to modify build scripts.
1. Copy **aspose.cells.jasperreports.jar** from the \lib folder of Aspose.Cells.JasperReports.zip to **\<InstallDir>\lib**.
1. Prepare Ant Build Tool and Ivy Dependency Manager, see **\<InstallDir>\readme.txt**.
1. Modify the **build.xml** at **\<InstallDir>\demo\samples**, add the aspose.cells.jasperreports.jar into the classpath:
   **\<path id="project-classpath"> ... \<pathelement location="../../lib/aspose.cells.jasperreports.jar"/> </path>**.
1. Change the current directory to **\<InstallDir>\demo\hsqldb** and run the following command line:
   **ant runServer**
1. Change the current directory to one of the Aspose.Cells for JasperReports demos, for example **\<InstallDir>\demo\samples\ac.charts** and run the following commands in the command line:
   **ant test** - zum Erstellen von Berichtsdateien mit dem Aspose XLS-Exporter.
1. Open one of the resulting documents to view, for example **\<InstallDir>\demo\samples\ac.charts\build\reports\AreaChartReport.xls** in Microsoft Excel or another application.
