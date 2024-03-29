﻿---
title: محرر جداول البيانات - المكونات
type: docs
weight: 50
url: /ar/java/spreadsheet-editor-components/
---
**جدول المحتويات**

- [Index.html](#SpreadsheetEditor-Components-Index.html)
- [WorksheetView](#SpreadsheetEditor-Components-WorksheetView)
- [WorkbookService](#SpreadsheetEditor-Components-WorkbookService)
- [خدمة لودر](#SpreadsheetEditor-Components-LoaderService)
- [CellsService](#SpreadsheetEditor-Components-CellsService)

تم إنشاء محرر جداول بيانات HTML5 من مكونات قليلة تتحد معًا لتكوين النظام الكامل. هنا نصف الغرض ودور كل منهما.
### **Index.html**
إنها صفحة JSF تصف واجهة مستخدم المحرر ونقطة النهاية الرئيسية لتطبيقنا. يتم تنفيذ جميع التفاعلات التي يتم إجراؤها بين متصفح الويب والخادم من خلال نقطة النهاية هذه.

إلى جانب تحديد واجهة المستخدم ، يتم إرفاق جميع خدمات الواجهة الخلفية هنا باستخدام تقنيات JSF. عندما يتفاعل المستخدم مع أحداث واجهة المستخدم والبيانات يتم تمريرها ذهاباً وإياباً بين الخدمات والمستخدم لإكمال مهامنا ، مثل تصدير جداول البيانات.

لديها مجالان رئيسيان للاهتمام.

**شريط**

تسمى منطقة شريط الأدوات المبوبة في الأعلى الشريط تقنيًا. يحتوي على أزرار ، وقوائم منسدلة ، وقوائم راديو ، ومربعات نصوص ، وبعض الحقول المخفية التي تُستخدم لأداء العديد من العمليات على جدول البيانات. ترسل هذه الأزرار عند النقر فوقها أوامر إلى الخادم وتحديث الورقة وفقًا لذلك.

**ملزمة**

الورقة هي الصفوف والأعمدة. عند النقر فوق الخلايا ، يتم تحديث الشريط وفقًا لذلك دون إرسال طلبات إلى الخادم حيث يتم إرفاق كافة البيانات التي يحتاجها الشريط بكل خلية. يتتبع الشريط أيضًا الخلية والصف والعمود المحدد عندما يتنقل المستخدم عبر الورقة.

تحتوي كل خلية على محرر مضمن خاص بها يصبح مرئيًا عندما تكون الخلية في وضع التحرير.
### **WorksheetView**
إنها وحدة برامج خلفية JSF ذات نطاق العرض مسؤولة عن إدارة المحتويات الديناميكية لواجهة المستخدم الموضحة في index.html. يحتوي على معالجات الأحداث لطلبات Ajax التي يتم تشغيلها عندما يتفاعل المستخدم مع واجهة المستخدم.
### **WorkbookService**
WorkbookService عبارة عن وحدة برامج خلفية JSF ذات نطاق العرض. إنه يعمل كمكون خدمة ويحصل على جدول البيانات يتم تحميله وتفريغه بمساعدة خدمات أخرى. يحتوي على نقاط النهاية التالية:

**فيه**

 ال**فيه** يكون**PostConstruct** الطريقة التي يتم تنفيذها مباشرة بعد اكتمال إنشاء الكائن بواسطة Java Application Server. تحقق من**عنوان url** المعلمة في تعيين معلمات الطلب وتحميل جدول البيانات المقابل من موقع معين ، إن أمكن.

**هدم**

إنها مسؤولة عن تنظيف جميع الموارد المكتسبة عندما لا تكون هناك حاجة إليها.
### **خدمة لودر**
يقوم بإنشاء نسخ من جداول البيانات والاحتفاظ بها في الذاكرة طالما كانت هناك حاجة إليها.
### **CellsService**
 ال**CellsService** يدير ذاكرة التخزين المؤقت للصفوف والأعمدة والخلايا والتنسيق وهيكل أوراق العمل.
