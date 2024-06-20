---
title: Exportation de fichiers .jrprint au format XLS
type: docs
weight: 20
url: /fr/jasperreports/exporting-jrprint-files-to-xls-formats/
---

{{% alert color="primary" %}} 

Aspose.Cells for JasperReports fournit une classe nommée ACXlsExporter pour exporter des rapports vers des fichiers XLS. Il prend comme entrée un fichier .jrprint ou un objet JasperPrint, et l'exporte vers un fichier XLS. 

{{% /alert %}} 

Le code suivant montre comment exporter l'objet jasperPrint vers un chemin de fichier, par exemple, destFile.

**Java**

{{< highlight csharp >}}

 import com.aspose.cells.jasperreports. ACXlsExporter;

.................

ACXlsExporter exporter = new ACXlsExporter ();

exporter.setParameter(JRExporterParameter.JASPER_PRINT, jasperPrint);

exporter.setParameter(JRExporterParameter.OUTPUT_FILE_NAME, destFile.toString());

exporter.setParameter(JRXlsExporterParameter.IS_ONE_PAGE_PER_SHEET, Boolean.TRUE);

exporter.setParameter(ACXlsExporterParameter.IS_USE_EXCEL_CHART, Boolean.FALSE);

exporter.exportReport();



{{< /highlight >}}
