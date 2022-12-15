---
title: تركيب Aspose.Cells for JasperReports
type: docs
weight: 20
url: /ar/jasperreports/installing-aspose-cells-for-jasperreports/
---
 ليستخدم**Aspose.Cells for JasperReports** من التطبيق الخاص بك ، نسخ**aspose.cells.jasperreports.jar** من المجلد \ lib Aspose.Cells.JasperReports.zip إلى دليل JasperReports \ lib أو إلى مجلد مكتبة لتطبيقك. بعد ذلك ، يمكنك الوصول إلى المصدرين برمجيًا.

يوضح المثال التالي الكود النموذجي المطلوب لتصدير تقرير إلى ملف XLS باستخدام Aspose.Cells for JasperReports. يمكن العثور على مزيد من الأمثلة في تقارير العرض التوضيحي المضمنة في أرشيف المنتج.

**Java**

{{< highlight "csharp" >}}

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
