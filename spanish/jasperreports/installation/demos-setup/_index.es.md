---
title: Configuración de demos
type: docs
weight: 40
url: /es/jasperreports/demos-setup/
---

{{% alert color="primary" %}}

Aspose.Cells for JasperReports incluye varios proyectos de demostración para ayudarlo a comenzar a exportar informes a los formatos de documento de Microsoft Excel desde su aplicación.

Las demos proporcionadas con Aspose.Cells for JasperReports son demos estándar de JasperReports modificadas para demostrar el uso de los nuevos exportadores.

{{% /alert %}}

Para ejecutar las demos de Aspose.Cells for JasperReports, realice los siguientes pasos:

1. Download JasperReports (e.g <https://sourceforge.net/projects/jasperreports/files/archive/>). Make sure to download the entire archived project with the source code and demos, not just a single JAR.
1. Desempaquete el proyecto archivado en alguna ubicación en su disco duro, por ejemplo, C:\.
1. Copy all demo folders from the \demo folder of **Aspose.Cells.JasperReports.zip** to **\<InstallDir>\demo\samples**, where "\<InstallDir>" is the location you have unpacked JasperReports to. This step is required because demo build scripts rely on the JasperReports’ folder structure, otherwise you will need to modify build scripts.
1. Copy **aspose.cells.jasperreports.jar** from the \lib folder of Aspose.Cells.JasperReports.zip to **\<InstallDir>\lib**.
1. Prepare Ant Build Tool and Ivy Dependency Manager, see **\<InstallDir>\readme.txt**.
1. Modify the **build.xml** at **\<InstallDir>\demo\samples**, add the aspose.cells.jasperreports.jar into the classpath:
   **\<path id="project-classpath"> ... \<pathelement location="../../lib/aspose.cells.jasperreports.jar"/> </path>**.
1. Change the current directory to **\<InstallDir>\demo\hsqldb** and run the following command line:
   **ant runServer**
1. Change the current directory to one of the Aspose.Cells for JasperReports demos, for example **\<InstallDir>\demo\samples\ac.charts** and run the following commands in the command line:
   **ant test** - para producir archivos de informe utilizando el exportador de Aspose XLS.
1. Open one of the resulting documents to view, for example **\<InstallDir>\demo\samples\ac.charts\build\reports\AreaChartReport.xls** in Microsoft Excel or another application.
