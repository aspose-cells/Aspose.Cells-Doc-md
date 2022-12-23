---
title: Configuración de demostraciones
type: docs
weight: 40
url: /es/jasperreports/demos-setup/
---
{{% alert color="primary" %}}

Aspose.Cells for JasperReports incluye una serie de proyectos de demostración para ayudarlo a comenzar a exportar informes a Microsoft formatos de documentos de Excel desde su aplicación.

Las demostraciones proporcionadas con Aspose.Cells for JasperReports son demostraciones estándar de JasperReports modificadas para demostrar el uso de los nuevos exportadores.

{{% /alert %}}

Para ejecutar demostraciones Aspose.Cells for JasperReports, realice los siguientes pasos:

1.  Descargar JasperReports (p. ej.<https://sourceforge.net/projects/jasperreports/files/archive/>). Asegúrese de descargar todo el proyecto archivado con el código fuente y las demostraciones, no solo un JAR.
1. Descomprima el proyecto archivado en alguna ubicación de su disco duro, por ejemplo, C:\.
1.  Copie todas las carpetas de demostración de la carpeta \demo de**Aspose.Cells.JasperReports.zip** a**\<dirección de instalación>\demo\samples**, dónde "\<InstallDir>" es la ubicación en la que ha desempaquetado JasperReports. Este paso es obligatorio porque los scripts de compilación de demostración se basan en la estructura de carpetas de JasperReports; de lo contrario, deberá modificar los scripts de compilación.
1.  Copiar**aspose.cells.jasperreports.jar** de la carpeta \lib de Aspose.Cells.JasperReports.zip a**\<dirección de instalación>\lib**.
1.  Prepare Ant Build Tool y Ivy Dependency Manager, consulte**\<dirección de instalación>\readme.txt**.
1.  Modificar el**construir.xml** en**\<dirección de instalación>\demo\samples**, agregue aspose.cells.jasperreports.jar en el classpath:
   **\<path id="project-classpath"> ... \<pathelement location="../../lib/aspose.cells.jasperreports.jar"/> </path>**.
1.  Cambiar el directorio actual a**\<dirección de instalación>\demo\hsqldb** y ejecute la siguiente línea de comando:
   **servidor de ejecución de hormigas**
1.  Cambie el directorio actual a una de las demostraciones Aspose.Cells for JasperReports, por ejemplo**\<dirección de instalación>\demo\samples\ac.charts** y ejecute los siguientes comandos en la línea de comando:
   **prueba de hormigas** - para producir archivos de informe usando el exportador Aspose XLS.
1.  Abra uno de los documentos resultantes para verlo, por ejemplo**\<dirección de instalación>\demo\samples\ac.charts\build\reports\AreaChartReport.xls** en Microsoft Excel u otra aplicación.
