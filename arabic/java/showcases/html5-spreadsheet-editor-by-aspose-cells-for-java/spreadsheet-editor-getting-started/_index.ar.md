---
title: بدء استخدام تحرير جداول البيانات
type: docs
weight: 10
url: /ar/java/spreadsheet-editor-getting-started/
---

جدول المحتويات

- [مقدمة](#SpreadsheetEditorGettingStarted-Introduction)
- [متطلبات النظام](#SpreadsheetEditorGettingStarted-SystemRequirements)
- [تنزيل وتثبيت](#SpreadsheetEditorGettingStarted-DownloadandInstallation)
- [الدعم](#SpreadsheetEditorGettingStarted-Support)
- [المساهمة](#SpreadsheetEditorGettingStarted-Contribute)
- [رخصة](#SpreadsheetEditorGettingStarted-License)
### **مقدمة**
Html5 محرّر جداول البيانات هو تطبيق ويب يمكنه عرض وتعديل مستندات جداول البيانات في متصفح الويب. يدعم Excel وSpreadsheetML وCVS وOpenDocument والعديد من التنسيقات المدعومة من قبل Microsoft Excel. كل الميزات الأساسية بما في ذلك تحرير الخلية وتنسيقها وتحرير الصيغ وإدارة الصفوف والأعمدة وما إلى ذلك مدعومة.

![todo:image_alt_text](aowcrc1.png)

يستخدم محرر جداول البيانات HTML5 العديد من ميزات [Aspose.Cells for Java](https://products.aspose.com/cells/java/) ويُظهر كيفية استخدامها لإنشاء وتلاعب وعرض جدول بيانات في تطبيق Java الخاص بك.

**الميزات**

- العمل مع الملفات 
  - التنسيقات المدعومة
  - فتح ملفات محلية
  - فتح من Dropbox
  - فتح من عنوان URL
  - إنشاء جدول بيانات جديد
  - التصدير إلى تنسيقات مختلفة
- العمل مع الأوراق 
  - إضافة وإزالة الأوراق
  - إعادة تسمية الأوراق
  - التبديل بين الأوراق
- العمل مع الصفوف والأعمدة 
  - إضافة صف
  - إضافة عمود
  - إزالة صف
  - إزالة عمود
  - عرض العمود وارتفاع الصف
- العمل مع الخلايا 
  - تحديد خلية
  - تحرير خلية
  - تحرير الصيغة
  - توجيه الخلية
  - مسح الخلية
  - إضافة خلية
  - إزالة خلية
- العمل مع تنسيق النص 
  - عريض، مائل، تحتية
  - نمط الخط والحجم
  - مسح التنسيق
### **متطلبات النظام**
**متطلبات البرنامج**

- خادم تطبيقات جافا المدعوم من CDI
- [Aspose.Cells for Java](https://products.aspose.com/cells/java/)
- [JavaServer Faces 2.0](https://javaee.github.io/javaserverfaces-spec/)
- [Primefaces 5.1](https://www.primefaces.org/)

**متطلبات الأجهزة**

تختلف متطلبات الأجهزة اعتمادًا على خادم تطبيقات جافا الذي نختاره لنشر محرر ورقة البيانات HTML5 وعدد جداول البيانات التي نفتحها في وقت واحد. وفيما يلي تقدير، الذي سيساعد في إعداد البيئة في بادئ الأمر.

- 2 GHz CPU
- 2 GB RAM
- 500 ميجابايت للقرص الصلب
### **تنزيل وتثبيت**
محرر ورقة البيانات HTML5 هو تطبيق Java EE ويمكن نشره على أي خادم تطبيقات جافا الويب مع دعم CDI. تم اختباره مع [Glassfish](https://javaee.github.io/glassfish/).

**شفرة المصدر**

مصدر المشروع متوفر في [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/). كما نقوم بإدارة الأنظمة الأخرى التي تضم مرايا Git على المواقع التالية:

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [Google Code](https://code.google.com/archive/p/html5-spreadsheet-editor/)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

استخدم أحد الأوامر التالية لتنزيل مصدر الكود عبر سطر الأوامر:

**Github**

{{< highlight bash >}}

 git clone https://github.com/aspose-cells/Aspose.Cells-for-Java.git

{{< /highlight >}}

**Bitbucket**

{{< highlight bash >}}

 git clone https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java.git

{{< /highlight >}}

**Google Code**

{{< highlight bash >}}

 git clone https://code.google.com/p/html5-spreadsheet-editor/

{{< /highlight >}}

**SourceForge**

{{< highlight bash >}}

 git clone git://git.code.sf.net/p/html5-spreadsheet-editor/code html5-spreadsheet-editor-code

{{< /highlight >}}

**انشئ باستخدام Maven**

عملية بناء المشروع تُدار باستخدام Maven. بحيث يمكنك تجهيز ملف WAR من سطر الأوامر بدون أي بيئة تطوير متكاملة. استخدم الأمر التالي لتوليد WAR للنشر. ستساعدك وثائق خادم التطبيق المقابل على كيفية نشر WAR المولَّد وتبعياته.

{{< highlight java >}}

 mvn clean install

{{< /highlight >}}

**استخدام NetBeans**

من السهل جدًا إدارة المشروع باستخدام [NetBeans IDE](https://netbeans.apache.org/). NetBeans هو أحد بيئات تطوير البرمجيات الشائعة بين مطوري Java ومُنتجة من قِبل Oracle.

- قم بتنزيل مصدر مشروع الكود.
- افتح المشروع في NetBeans IDE.
- انقر على زر ***تشغيل*** في شريط الأدوات.
- حدد ***خادم Glassfish*** كخادم تطبيقات.

**استخدام Eclipse**

[Eclipse IDE](http://www.eclipse.org/ide/) يوفر تكاملًا رسميًا لاستيراد مشاريع Maven يُسمى [M2Eclipse](http://www.eclipse.org/m2e/):

1. قم بتثبيت M2Eclipse في بيئة Eclipse IDE الخاصة بك. إجراء التثبيت موضح على موقعهم على الويب.
1. قم بتنزيل مصدر مشروع الكود.
1. افتح حوار الاستيراد من القائمة الملف.
1. حدد ***مشروع Maven*** من حوار الاستيراد.
1. انقر على ***التالي***.
1. انقر ***تصفح*** لتحديد موقع الشفرة المصدرية.
1. حدد ***pom.xml*** من القائمة أدناه.
1. انقر ***إنهاء***.

يجب على بيئة Eclipse IDE استيراد وتحميل المشروع.
### **الدعم**
**تقرير الخلل**

لإرسال تقرير عن خلل، أنشئ مشكلة جديدة على [صفحة المشروع على Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) وقم بتطبيق علامة ***bug***.

**طلب ميزة**

نحن نقدر تقديرا كبيرا لردود الفعل الخاصة بك والميزات التي تطلبها. لطلب ميزة جديدة أو تحسين في الميزات الحالية، يرجى إنشاء مشكلة جديدة على [صفحة المشروع على Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) وتطبيق علامة ***enhancement***.

**الأسئلة والمساعدة**

يمكنك طرح جميع أنواع الأسئلة المتعلقة بمحرر جدول البيانات HTML5 باستخدام [مشكلة Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues). ما عليك سوى إنشاء مشكلة جديدة وتطبيق علامة ***question***.

**منتديات Aspose Aspose.Cells for Java**

توفر منتديات منتج Aspose دعما كاملا لكل من العملاء التجريبيين والمدفوعين. الخبراء متواجدون على مدار الساعة لتقديم المساعدة والرد على الاستفسارات. قم بزيارة [منتديات المنتج هنا](https://forum.aspose.com/c/cells/9).

**مدونات Aspose**

تواصل معنا وابق على اطلاع على آخر الأخبار حول منتجاتنا وعروضنا. اشترك في [مدونتنا هنا](http://blog.aspose.com).
### **المساهمة**
[](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)

[!\[todo:image_alt_text\](https://s3.amazonaws.com/github/ribbons/forkme_right_red_aa0000.png)](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)


محرر جدول البيانات HTML5 مشروع مفتوح المصدر الذي يتيح خيارات كحد أقصى للجميع للمساهمة في المشروع.

**شفرة المصدر**

المصدر المشروع متاح على [Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java). نحن أيضا نحتفظ بمرايا Git على المواقع التالية:

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

**طلبات السحب**

للمساهمة بشفرة المصدر في المشروع، ما عليك سوى إرسال طلب سحب عبر Github. اقرأ مزيد من المعلومات في مقال Github عن [إنشاء طلب سحب](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).
### **رخصة**
**رخصة MIT**

نحن نستخدم إحدى الرخص الحرة الأكثر سخاءً بحيث لا تكون هناك مسؤوليات كبيرة على المساهمين. تم إصدار HTML5 Spreadsheet Editor تحت [رخصة MIT](https://opensource.org/licenses/mit-license.php).

**رخصة Aspose**

يعمل المنتج دون ترخيص Aspose، [مع قيود](/cells/ar/java/licensing/). لإزالة القيود، يمكنك الحصول على [ترخيص مؤقت مجاني](https://purchase.aspose.com/temporary-license) أو [شراء ترخيص كامل](https://purchase.aspose.com/buy).

بشكل افتراضي، سيحاول المحرر تحميل ملف **Aspose.Total.Java.lic** من الدليل **src/main/resources/com/aspose/spreadsheeteditor**. ما عليك سوى نسخ ملف الترخيص إلى هذا الدليل. يمكن تغيير السلوك الافتراضي عن طريق تحرير فئة **AsposeLicense**.
