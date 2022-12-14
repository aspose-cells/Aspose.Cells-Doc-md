---
title: .jrprint Dosyalarını XLS Formatlarına Aktarma
type: docs
weight: 20
url: /tr/jasperreports/exporting-jrprint-files-to-xls-formats/
---
{{% alert color="primary" %}} 

JasperReports için Aspose.Cells, raporları XLS dosyalarına dışa aktarmak için ACXlsExporter adlı bir sınıf sağlar. Giriş olarak bir .jrprint dosyası veya bir JasperPrint nesnesi alır ve bunu bir XLS dosyasına verir.

{{% /alert %}} 

Aşağıdaki kod parçacığı, jasperPrint nesnesinin bir dosya yoluna, örneğin destFile'a nasıl aktarılacağını gösterir.

**Java**

{{< highlight "csharp" >}}

 import com.aspose.cells.jasperreports. ACXlsExporter;

.................

ACXlsExporter exporter = new ACXlsExporter ();

exporter.setParameter(JRExporterParameter.JASPER_PRINT, jasperPrint);

exporter.setParameter(JRExporterParameter.OUTPUT_FILE_NAME, destFile.toString());

exporter.setParameter(JRXlsExporterParameter.IS_ONE_PAGE_PER_SHEET, Boolean.TRUE);

exporter.setParameter(ACXlsExporterParameter.IS_USE_EXCEL_CHART, Boolean.FALSE);

exporter.exportReport();



{{< /highlight >}}
