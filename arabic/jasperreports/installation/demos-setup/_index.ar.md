---
title: إعداد العروض التوضيحية
type: docs
weight: 40
url: /ar/jasperreports/demos-setup/
---
{{% alert color="primary" %}}

يتضمن Aspose.Cells for JasperReports عددًا من المشاريع التجريبية لمساعدتك على بدء تصدير التقارير إلى تنسيقات مستندات Excel Microsoft من التطبيق الخاص بك.

العروض التوضيحية المقدمة مع Aspose.Cells for JasperReports هي عروض توضيحية قياسية لـ JasperReports تم تعديلها لتوضيح استخدام المصدرين الجدد.

{{% /alert %}}

لتشغيل Aspose.Cells for JasperReports العروض التوضيحية ، قم بتنفيذ الخطوات التالية:

1.  تنزيل JasperReports (على سبيل المثال<https://sourceforge.net/projects/jasperreports/files/archive/>). تأكد من تنزيل المشروع المؤرشف بالكامل باستخدام كود المصدر والعروض التوضيحية ، وليس مجرد JAR واحد.
1. قم بفك ضغط المشروع المؤرشف إلى مكان ما على القرص الثابت لديك ، على سبيل المثال C: \.
1.  انسخ جميع مجلدات العرض التوضيحي من المجلد التجريبي الخاص بـ**Aspose.Cells.JasperReports.zip** إلى**\ <InstallDir> \ تجريبي \ عينات**، أين "\<InstallDir>"هو الموقع الذي قمت بفك حزم JasperReports إليه. هذه الخطوة مطلوبة لأن البرامج النصية للبناء التجريبي تعتمد على بنية مجلد JasperReports ، وإلا فستحتاج إلى تعديل البرامج النصية للبناء.
1.  ينسخ**aspose.cells.jasperreports.jar** من مجلد \ lib Aspose.Cells.JasperReports.zip إلى**\ <InstallDir> \ lib**.
1.  قم بإعداد أداة بناء النمل ومدير تبعية اللبلاب ، انظر**\ <InstallDir> \ readme.txt**.
1.  تعديل**build.xml** في**\ <InstallDir> \ تجريبي \ عينات**، أضف aspose.cells.jasperreports.jar إلى مسار الفصل الدراسي:
   **\ <path id = "project-classpath"> ... \ <pathelement location = "../../ lib / aspose.cells.jasperreports.jar" /> </path>**.
1.  قم بتغيير الدليل الحالي إلى**\ <InstallDir> \ demo \ hsqldb** وقم بتشغيل سطر الأوامر التالي:
   **نملة runServer**
1.  قم بتغيير الدليل الحالي إلى أحد العروض التوضيحية Aspose.Cells for JasperReports ، على سبيل المثال**\ <InstallDir> \ demo \ sample \ ac.charts** وقم بتشغيل الأوامر التالية في سطر الأوامر:
   **اختبار النمل** - لإنتاج ملفات التقارير باستخدام أداة تصدير Aspose XLS.
1.  افتح أحد المستندات الناتجة لعرضها ، على سبيل المثال**\ <InstallDir> \ demo \ sample \ ac.charts \ build \ Reports \ AreaChartReport.xls** في Microsoft Excel أو تطبيق آخر.
