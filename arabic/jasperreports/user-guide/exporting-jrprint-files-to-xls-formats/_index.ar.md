---
title: تصدير ملفات .jrprint إلى تنسيقات XLS
type: docs
weight: 20
url: /ar/jasperreports/exporting-jrprint-files-to-xls-formats/
---
{{% alert color="primary" %}} 

 يوفر Aspose.Cells for JasperReports فئة تسمى ACXlsExporter لتصدير التقارير إلى ملفات XLS. يأخذ ملف jrprint أو كائن JasperPrint كمدخل له ، ويصدره إلى ملف XLS.

{{% /alert %}} 

يوضح مقتطف التعليمات البرمجية التالي كيفية تصدير كائن jasperPrint إلى مسار ملف ما ، على سبيل المثال ، destFile.

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
