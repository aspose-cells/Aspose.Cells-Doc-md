---
title: .jrprint Dosyalarını XLS Biçimlerine Dışa Aktarma
type: docs
weight: 20
url: /tr/jasperreports/exporting-jrprint-files-to-xls-formats/
---

{{% alert color="primary" %}} 

Aspose.Cells for JasperReports, raporları XLS dosyalarına dışa aktarmak için ACXlsExporter adında bir sınıf sağlar. .jrprint dosyası veya bir JasperPrint nesnesi alır ve bunu bir XLS dosyasına dışa aktarır. 

{{% /alert %}} 

Aşağıdaki kod örneği, jasperPrint nesnesini örneğin destFile'a nasıl dışa aktaracağını gösterir.

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
