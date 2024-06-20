---
title: إعداد العروض التوضيحية
type: docs
weight: 40
url: /ar/jasperreports/demos-setup/
---

{{% alert color="primary" %}}

يتضمن Aspose.Cells for JasperReports عددًا من مشاريع العرض التوضيحي لمساعدتك في بدء تصدير التقارير إلى تنسيقات مستند Microsoft Excel من تطبيقك.

يتم توفير العروض التوضيحية المقدمة مع Aspose.Cells for JasperReports من خلال عروض تجريبية قياسية لـ JasperReports تم تعديلها لتوضيح استخدام المصدرات الجديدة.

{{% /alert %}}

لتشغيل العروض التوضيحية لـ Aspose.Cells for JasperReports، قم بأداء الخطوات التالية:

1. Download JasperReports (e.g <https://sourceforge.net/projects/jasperreports/files/archive/>). Make sure to download the entire archived project with the source code and demos, not just a single JAR.
1. قم بفك تجميع المشروع المؤرشف إلى موقع ما على القرص الصلب الخاص بك، على سبيل المثال C:\.
1. Copy all demo folders from the \demo folder of **Aspose.Cells.JasperReports.zip** to **\<InstallDir>\demo\samples**, where "\<InstallDir>" is the location you have unpacked JasperReports to. This step is required because demo build scripts rely on the JasperReports’ folder structure, otherwise you will need to modify build scripts.
1. Copy **aspose.cells.jasperreports.jar** from the \lib folder of Aspose.Cells.JasperReports.zip to **\<InstallDir>\lib**.
1. Prepare Ant Build Tool and Ivy Dependency Manager, see **\<InstallDir>\readme.txt**.
1. Modify the **build.xml** at **\<InstallDir>\demo\samples**, add the aspose.cells.jasperreports.jar into the classpath:
   **\<path id="project-classpath"> ... \<pathelement location="../../lib/aspose.cells.jasperreports.jar"/> </path>**.
1. Change the current directory to **\<InstallDir>\demo\hsqldb** and run the following command line:
   **ant runServer**
1. Change the current directory to one of the Aspose.Cells for JasperReports demos, for example **\<InstallDir>\demo\samples\ac.charts** and run the following commands in the command line:
   **اختبار النملة** - لإنتاج ملفات تقارير باستخدام مصدر التصدير Aspose XLS.
1. Open one of the resulting documents to view, for example **\<InstallDir>\demo\samples\ac.charts\build\reports\AreaChartReport.xls** in Microsoft Excel or another application.
