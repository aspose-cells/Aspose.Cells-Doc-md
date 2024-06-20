---
title: عروض الورقة العمل
type: docs
weight: 10
url: /ar/java/worksheet-views/
---

## **معاينة كسر الصفحة**
يمكن عرض جميع الصفحات العمل في وضعين:

- العرض العادي.
- معاينة كسر الصفحة.

العرض العادي هو العرض الافتراضي لورقة العمل. معاينة فواصل الصفحات هو عرض للتحرير يعرض ورقة العمل كما سيتم طباعتها. تعرض معاينة فواصل الصفحات البيانات التي ستذهب في كل صفحة حتى تتمكن من ضبط منطقة الطباعة وفواصل الصفحات. باستخدام Aspose.Cells يمكن للمطورين تمكين وضع العرض العادي أو معاينة فواصل الصفحات.
### **التحكم في أوضاع العرض**
توفر Aspose.Cells فئة [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) التي تمثل ملف Microsoft Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) على [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) التي تسمح بالوصول إلى كل ورق عمل في ملف Excel.

يتم تمثيل ورقة العمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). توفر فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة الأوراق العمل. لتمكين أوضاع العرض العادي أو عرض معاينة الفواصل، استخدم أسلوب [setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) في فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).
#### **تمكين العرض العادي**
قم بتعيين أي ورقة عمل إلى العرض العادي باستخدام أسلوب [setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) في فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) وتمرير **false** كمعلمة.
#### **تمكين معاينة كسر الصفحة**
قم بتعيين أي ورقة عمل إلى عرض معاينة الفواصل باستخدام أسلوب [setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) في فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) وتمرير **true** كمعلمة.

يوجد مثال كامل أدناه يوضح استخدام أسلوب [setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) في فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) لتمكين وضع معاينة الفواصل للورقة العمل الأولى في ملف Excel.

في لقطة الشاشة أدناه، يمكنك رؤية ملف Book1.xls في العرض العادي.

**Book1.xls: ورقة عمل قبل التعديل** 

![todo:image_alt_text](worksheet-views_1.png)

يتم فتح ملف Book1.xls باستخدام فئة [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) وتغيير الوضع إلى عرض معاينة الفواصل للورقة العمل الأولى. يتم حفظ الملف المعدل بوصف output.xls.

**Ouput.xls: ورقة عمل بعد التعديل** 

![todo:image_alt_text](worksheet-views_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageBreakPreview-PageBreakPreview.java" >}}
## **عامل التكبير**
يوفر Microsoft Excel ميزة تتيح للمستخدمين تعيين عامل تكبير أو تدرج الورقة العمل. تساعد هذه الميزة المستخدمين في رؤية محتويات ورقة العمل في عروض أصغر أو أكبر. يمكن للمستخدمين تعيين عامل التكبير إلى أي قيمة.

**ضبط عامل التكبير باستخدام Microsoft Excel** 

![todo:image_alt_text](worksheet-views_3.png)

تسمح Aspose.Cells أيضًا للمطورين بضبط عامل تكبير ورقة العمل.
### **التحكم في عامل التكبير**
توفر Aspose.Cells فئة [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) التي تمثل ملف Microsoft Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) على [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) التي تسمح بالوصول إلى كل ورق عمل في ملف Excel.

يتم تمثيل ورقة العمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). توفر فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة الأوراق العمل. لضبط عامل تكبير ورقة العمل، استخدم أسلوب [setZoom ](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom) في فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

يوجد مثال كامل أدناه يوضح كيفية استخدام أسلوب [setZoom ](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom) لضبط عامل التكبير لأول ورقة عمل في ملف Excel.

في اللقطة الشاشة أدناه، يمكنك رؤية ملف Book1.xls في العرض الافتراضي.

**Book1.xls: ورقة العمل قبل التعديل** 

![todo:image_alt_text](worksheet-views_4.png)

يتم فتح ملف Book1.xls باستخدام فئة [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) ويتم تعيين معامل التكبير للورقة العمل الأولى إلى 75. يتم حفظ الملف المعدل بصيغة output.xls.

**output.xls: ورقة العمل بعد التعديل** 

![todo:image_alt_text](worksheet-views_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ZoomFactor-ZoomFactor.java" >}}
## **تجميد الألواح**
تجميد الألواح هو ميزة تقدمها مايكروسوفت إكسل. يتيح لك تجميد الألواح تحديد البيانات التي تظل مرئية عند التمرير في ورقة البيانات.

**استخدام تجميد الرسوم البيانية في Microsoft Excel** 

![todo:image_alt_text](worksheet-views_6.png)

تسمح Aspose.Cells أيضًا للمطورين بتطبيق تجميد الرسوم البيانية على الأوراق العمل في وقت التشغيل.

يوفر Aspose.Cells فئة [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) التي تمثل ملف Microsoft Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) على [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

تمثل ورقة العمل بواسطة الفئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). توفر الفئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة ورق العمل. لتكوين تجميد الرسوم البيانية ، اتصل بأسلوب [freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\))  في فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). يأخذ أسلوب [freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\)) البارمترات التالية:

- **الصف**، فهرس الصف للخلية التي سيبدأ منها التجميد.
- **العمود**، فهرس العمود للخلية التي سيبدأ منها التجميد.
- **الصفوف المجمدة**، عدد الصفوف المرئية في اللوحة العلوية.
- **الأعمدة المجمدة**، عدد الأعمدة المرئية في اللوحة اليسرى.

يلي أدناه مثال كامل يوضح كيفية استخدام أسلوب [freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\))  في فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) لتجميد الصفوف والأعمدة (ابتداءً من C4 ، الممثلة بالصف الرابع والعمود الثالث، حيث تبدأ الصفوف والأعمدة من مؤشرات 0) من الورقة العمل الأولى لملف Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FreezePanes-FreezePanes.java" >}}


في اللقطة أدناه ، يمكنك رؤية ملف Book1.xls بدون تجميد الرسوم البيانية.

**Book1.xls: عرض ورقة العمل قبل أي تعديل** 

![todo:image_alt_text](worksheet-views_7.png)

يتم فتح ملف Book1.xls باستخدام فئة [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) ومن ثم تجميد عدد قليل من الصفوف والأعمدة في ورقة العمل الأولى. يتم حفظ الملف المعدل بصيغة output.xls.

**Outlook.xls: عرض ورقة العمل بعد التعديل** 

![todo:image_alt_text](worksheet-views_8.png)
## **تقسيم الألواح**
إذا كنت بحاجة إلى تقسيم الشاشة للحصول على مناظر مختلفة في نفس ورقة البيانات، استخدم تقسيم الألواح. تقدم مايكروسوفت إكسل ميزة مفيدة تسمح لك بعرض أكثر من نسخة واحدة من ورقة البيانات الخاصة بك، وتمكنك من التمرير من خلال كل لوحة من ورقة البيانات بشكل مستقل: تقسيم الألواح.

الألواح تعمل بشكل متزامن. إذا قمت بإجراء تغيير في أحدها، فإن التغيير يظهر بشكل متزامن في الآخر. توفر Aspose.Cells ميزة تقسيم الألواح للمستخدمين.
### **تطبيق وإزالة تقسيم الألواح**
#### **تقسيم الألواح**
توفر Aspose.Cells [فئة الدفتر](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) التي تمثل ملف Microsoft Excel. توفر فئة الدفتر مجموعة واسعة من الخصائص والأساليب لإدارة ملفات Excel. لتنفيذ عرض الانقسام، استخدم أسلوب [split](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#split\(\)) لفئة [صفحة العمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). لإزالة تقسيم الأقسام، استخدم أسلوب [removeSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit\(\))

في المثال، نستخدم ملف قالب بسيط يتم تحميله، ثم يتم تطبيق ميزة تقسيم الألواح المحددة على خلية في الورقة البيانات الأولى. يتم حفظ الملف المحدث.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SplitPanes-SplitPanes.java" >}}



بعد تشغيل الشيفرة أعلاه، يحتوي الملف الناتج على عرض مقسم

**تقسيم الأقسام في الملف الناتج** 

![todo:image_alt_text](worksheet-views_9.png)
#### **إزالة النوافذ**
يمكن للمطورين إزالة تقسيم الأقسام باستخدام أسلوب [removeSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit\(\)) لفئة [صفحة العمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovePanes-RemovePanes.java" >}}


## **مواضيع متقدمة**
- [إخفاء عرض القيم الصفرية في صفحة العمل](/cells/ar/java/hiding-the-display-of-zero-values-in-the-worksheet/)
- [تعيين لون علامة تبويب الصفحة العمل](/cells/ar/java/set-worksheet-tab-color/)
- [عرض وإخفاء العناصر](/cells/ar/java/show-and-hide-elements/)
- [عرض الصيغ بدلاً من القيم في صفحة العمل](/cells/ar/java/show-formulas-instead-of-values-in-a-worksheet/)
- [استخدام خيارات فحص الأخطاء](/cells/ar/java/use-error-checking-options/)
