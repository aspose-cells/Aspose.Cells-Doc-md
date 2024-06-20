---
title: تثبيت Aspose.Cells for JasperReports
type: docs
weight: 20
url: /ar/jasperreports/installing-aspose-cells-for-jasperreports/
---

لاستخدام **Aspose.Cells for JasperReports** من تطبيقك، قم بنسخ **aspose.cells.jasperreports.jar** من مجلد \lib في Aspose.Cells.JasperReports.zip إلى مجلد JasperReports\lib أو إلى مجلد المكتبة الخاص بتطبيقك. بعد ذلك، يمكنك الوصول إلى المصدرين بشكل برمجي.

يوضح المثال التالي الشفرة النموذجية اللازمة لتصدير تقرير إلى ملف XLS باستخدام Aspose.Cells for JasperReports. يمكن العثور على المزيد من الأمثلة في تقارير الديمو المضمنة في الأرشيف المنتج.

**Java**

{{< highlight csharp >}}

    import com.aspose.cells.jasperreports.*;


   ACXlsExporter exporter = new ACXlsExporter ();

   ACXlsReportConfiguration conf = new ACXlsReportConfiguration ();

   File sourceFile = new File(fileName);

   JasperPrint jasperPrint = (JasperPrint)JRLoader.loadObject(sourceFile);

   exporter.setConfiguration(conf);

   exporter.setExporterInput(new SimpleExporterInput(jasperPrint));


   File destFile = new File(sourceFile.getParent(), jasperPrint.getName() + ".xls");

   exporter.setExporterOutput(new SimpleOutputStreamExporterOutput(destFile.toString());

   exporter.exportReport();



{{< /highlight >}}
