---
title: تصدير .jrprint الملفات إلى تنسيقات XLS
type: docs
weight: 20
url: /ar/jasperreports/exporting-jrprint-files-to-xls-formats/
---

{{% alert color="primary" %}} 

Aspose.Cells for JasperReportsيوفر فئة بأسم ACXlsExporter لتصدير التقارير إلى ملفات XLS. يأخذ ملف .jrprint أو كائن JasperPrint كإدخال له ويصدره إلى ملف XLS. 

{{% /alert %}} 

يُظهر مقتطف الكود التالي كيفية تصدير كائن jasperPrint إلى مسار ملف معين، على سبيل المثال، destFile.

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
