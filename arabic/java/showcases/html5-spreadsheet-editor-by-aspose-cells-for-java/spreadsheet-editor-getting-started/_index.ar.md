---
title: بدء محرر جداول البيانات
type: docs
weight: 10
url: /ar/java/spreadsheet-editor-getting-started/
---
**جدول المحتويات**

- [مقدمة](#SpreadsheetEditorGettingStarted-Introduction)
- [متطلبات النظام](#SpreadsheetEditorGettingStarted-SystemRequirements)
- [التنزيل والتثبيت](#SpreadsheetEditorGettingStarted-DownloadandInstallation)
- [الدعم](#SpreadsheetEditorGettingStarted-Support)
- [مساهمة](#SpreadsheetEditorGettingStarted-Contribute)
- [رخصة](#SpreadsheetEditorGettingStarted-License)
### **مقدمة**
Html5 Spreadsheet Editor هو تطبيق ويب يمكنه عرض مستندات جداول البيانات وتحريرها في مستعرض ويب. وهو يدعم Excel و SpreadsheetML و CVS و OpenDocument والعديد من التنسيقات الأخرى التي يدعمها Microsoft Excel. يتم دعم جميع الميزات الأساسية بما في ذلك تحرير الخلايا والتنسيق وتحرير الصيغة وإدارة الصفوف والأعمدة وما إلى ذلك.

![ما يجب القيام به: image_بديل_نص](aowcrc1.png)

 يستخدم محرر جداول بيانات HTML5 العديد من ميزات[Aspose.Cells for Java](https://products.aspose.com/cells/java/) ويوضح كيفية استخدامها لإنشاء جدول بيانات ومعالجته وعرضه في تطبيق Java الخاص بك.

**سمات**

- العمل مع الملفات
 - التنسيقات المدعومة
 - فتح الملفات المحلية
 - فتح من Dropbox
 - فتح من URL
 - إنشاء جدول بيانات جديد
 - تصدير إلى صيغ مختلفة
-  العمل مع جداول البيانات
 - إضافة وإزالة الأوراق
 - إعادة تسمية الأوراق
 - التبديل بين الأوراق
-  العمل مع الصفوف والأعمدة
 - أضف صف
 - أضف عمود
 - إزالة صف
 - إزالة عمود
 - عرض العمود وارتفاع الصف
-  العمل مع Cells
 - اختيار خلية
 - تحرير خلية
 - تحرير الصيغة
 - Cell محاذاة
 - مسح Cell
 - أضف خلية
 - إزالة خلية
-  العمل مع تنسيق النص
 - غامق ومائل وتسطير
 - نمط الخط وحجمه
 - تنسيق واضح
### **متطلبات النظام**
**متطلبات البرنامج**

- دعم CDI خادم تطبيق Java
- [Aspose.Cells for Java](https://products.aspose.com/cells/java/)
- [JavaServer Faces 2.0](https://javaee.github.io/javaserverfaces-spec/)
- [الأوجه 5.1](https://www.primefaces.org/)

**متطلبات الأجهزة**

تختلف متطلبات الأجهزة بناءً على خادم التطبيق Java الذي نختاره لنشر محرر جداول بيانات HTML5 وعدد جداول البيانات التي نفتحها في وقت واحد. فيما يلي تقدير ، سيساعد في البداية في إعداد البيئة.

- 2 جيجاهرتز وحدة المعالجة المركزية
- 2 جيجا رام
- 500 ميغا بايت
### **التنزيل والتثبيت**
 HTML5 Spreadsheet Editor هو تطبيق Java EE ويمكن نشره في أي ملف تعريف ويب لخادم تطبيق Java مع دعم CDI. تم اختباره مع[السمكة الزجاجية](https://javaee.github.io/glassfish/).

**مصدر الرمز**

 مصدر المشروع متاح في[جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/). نقوم أيضًا بصيانة مرايا Git في المواقع التالية:

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [Google كود](https://code.google.com/archive/p/html5-spreadsheet-editor/)
- [المصدر](https://sourceforge.net/p/html5-spreadsheet-editor/)

استخدم أحد الأوامر التالية لتنزيل التعليمات البرمجية المصدر عبر سطر الأوامر:

**جيثب**

{{< highlight "bash" >}}

 git clone https://github.com/aspose-cells/Aspose.Cells-for-Java.git

{{< /highlight >}}

**Bitbucket**

{{< highlight "bash" >}}

 git clone https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java.git

{{< /highlight >}}

**Google كود**

{{< highlight "bash" >}}

 git clone https://code.google.com/p/html5-spreadsheet-editor/

{{< /highlight >}}

**المصدر**

{{< highlight "bash" >}}

 git clone git://git.code.sf.net/p/html5-spreadsheet-editor/code html5-spreadsheet-editor-code

{{< /highlight >}}

**بناء باستخدام Maven**

تدار عملية بناء المشروع باستخدام Maven. لذا يمكنك تحضير ملف WAR من سطر الأوامر بدون أي IDE. استخدم الأمر التالي لإنشاء WAR للنشر. سيساعدك توثيق خادم التطبيق المقابل في كيفية نشر الحرب التي تم إنشاؤها وتوابعها.

{{< highlight "java" >}}

 mvn clean install

{{< /highlight >}}

**باستخدام NetBeans**

 من السهل جدًا إدارة المشروع باستخدام[NetBeans IDE](https://netbeans.apache.org/). NetBeans هو أحد IDEs المشهور بين مطوري Java وترعاه Oracle.

- قم بتنزيل الكود المصدري للمشروع.
- افتح المشروع في NetBeans IDE.
-  انقر***يركض*** زر على شريط الأدوات.
-  يختار***السمكة الزجاجية*** الخادم كخادم التطبيق.

**باستخدام الكسوف**

[كسوف IDE](http://www.eclipse.org/ide/) يوفر التكامل الرسمي لاستيراد Maven مشاريع تسمى[M2Eclipse](http://www.eclipse.org/m2e/):

1. قم بتثبيت M2Eclipse في Eclipse IDE الخاص بك. تم وصف إجراء التثبيت على موقع الويب الخاص بهم.
1. قم بتنزيل الكود المصدري للمشروع.
1. افتح ال***يستورد*** الحوار من القائمة ملف.
1.  يختار***Maven المشروع*** من مربع حوار الاستيراد.
1.  انقر***التالي***.
1.  انقر***تصفح*** لتحديد موقع شفرة المصدر.
1.  يختار***pom.xml*** من القائمة أدناه.
1.  انقر***ينهي***.

يجب أن يقوم Eclipse IDE باستيراد وتحميل المشروع.
### **الدعم**
**تقرير الشوائب**

 لإرسال تقرير خطأ ، أنشئ مشكلة جديدة في[صفحة مشروع جيثب](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) وتطبيق الملصق***خلل برمجي***.

**طلب المواصفات**

 نحن نقدر تقديرا عاليا ملاحظاتك والميزات التي تطلبها. لطلب ميزة جديدة أو تحسين في القائمة ، يرجى إنشاء عدد جديد في[صفحة مشروع جيثب](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) وتطبيق الملصق***التعزيز***.

**أسئلة ومساعدة**

 يمكنك طرح جميع أنواع الأسئلة المتعلقة باستخدام محرر جداول بيانات HTML5[قضية جيثب](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) . ما عليك سوى إنشاء عدد جديد وتطبيق***سؤال*** ضع الكلمة المناسبة.

**منتديات Aspose.Cells for Java**

 توفر منتديات المنتج Aspose الدعم الكامل للعملاء التجريبيين والعملاء المدفوعين. يجلس الخبراء على مدار الساعة طوال أيام الأسبوع لتقديم المساعدة والإجابة على الاستفسارات. يزور[منتديات المنتج هنا](https://forum.aspose.com/c/cells/9).

**Aspose مدونة**

 تواصل معنا وابق على اطلاع بأحدث الأخبار حول منتجاتنا وعروضنا. الاشتراك في[مدونتنا هنا](http://blog.aspose.com).
### **مساهمة**
[](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)

[! \ [يجب القيام به: image_alt_text \]](https://s3.amazonaws.com/github/ribbons/forkme_right_red_aa0000.png)(https://github.com/AsposeShowcase/Html5_جدول_محرر_بواسطة_Aspose.Cells_إلى عن على_Java)


HTML5 Spreadsheet Editor هو مشروع مفتوح المصدر يتيح الحد الأقصى من الخيارات للجميع للمساهمة في المشروع.

**مصدر الرمز**

 مصدر المشروع متاح في[جيثب](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java). نقوم أيضًا بصيانة مرايا Git في المواقع التالية:

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [المصدر](https://sourceforge.net/p/html5-spreadsheet-editor/)

**طلبات السحب**

 للمساهمة بكود المصدر في المشروع ، ما عليك سوى إرسال طلب سحب عبر Github. اقرأ المزيد من المعلومات في مقالة جيثب عن[قم بإنشاء طلب سحب](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).
### **رخصة**
**ترخيص MIT**

 نحن نستخدم أحد أكثر التراخيص مفتوحة المصدر ليبرالية للحد الأدنى من الالتزامات على المساهمين. تم إصدار محرر جداول بيانات HTML5 تحت[ترخيص MIT](https://opensource.org/licenses/mit-license.php).

**ترخيص Aspose**

 المنتج يعمل بدون ترخيص Aspose ،[مع قيود](/cells/ar/java/licensing/) . لإزالة القيود ، يمكنك الحصول على ملف[رخصة مؤقتة مجانية](https://purchase.aspose.com/temporary-license) أو[شراء الرخصة الكاملة](https://purchase.aspose.com/buy).

 بشكل افتراضي ، سيحاول المحرر التحميل**Aspose.Total.Java.lic** ملف من**src / main / resources / com / aspose / spreadsheeteditor** الدليل. فقط انسخ ملف الترخيص إلى هذا الدليل. يمكن تغيير السلوك الافتراضي عن طريق تحرير ملف**Aspose الترخيص** صف دراسي.
