---
title: طرق عرض ورقة العمل
type: docs
weight: 10
url: /ar/java/worksheet-views/
---
## **معاينة فاصل الصفحة**
يمكن عرض جميع أوراق العمل في وضعين:

- العرض العادي.
- معاينة فاصل الصفحة.

العرض العادي هو طريقة العرض الافتراضية لورقة العمل. معاينة فاصل الصفحة هي طريقة عرض تحرير تعرض ورقة عمل كما ستتم طباعتها. تُظهر معاينة فاصل الصفحة البيانات التي سيتم نقلها على كل صفحة حتى تتمكن من ضبط منطقة الطباعة وفواصل الصفحات. باستخدام Aspose.Cells يمكن للمطورين تمكين العرض العادي أو أوضاع معاينة فاصل الصفحة.
### **التحكم في أوضاع العرض**
 يوفر Aspose.Cells أ[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) فئة تمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) فئة تحتوي على[ورقة العمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)يسمح بالوصول إلى كل ورقة عمل في ملف Excel.

 يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي. ال[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) توفر class مجموعة واسعة من الخصائص والأساليب لإدارة أوراق العمل. لتمكين أوضاع المعاينة العادية أو أوضاع معاينة فاصل الصفحة ، استخدم ملف[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي'[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)طريقة.
#### **تمكين العرض العادي**
عيّن أي ورقة عمل إلى العرض العادي باستخدام ملف[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) طريقة[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) الدرجة والمرور**خاطئة** كمعامل.
#### **تمكين معاينة فاصل الصفحة**
عيّن أي ورقة عمل لمعاينة فاصل الصفحات باستخدام ملف[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)طريقة[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) الدرجة والمرور**حقيقي**كمعامل.

 ويرد أدناه مثال كامل يوضح استخدام[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي'[setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)طريقة لتمكين وضع معاينة فاصل الصفحة لورقة العمل الأولى من ملف Excel.

في لقطة الشاشة أدناه ، يمكنك أن ترى أن ملف Book1.xls موجود في العرض العادي.

**Book1.xls: ورقة عمل قبل التعديل** 

![ما يجب القيام به: image_بديل_نص](worksheet-views_1.png)

 يتم فتح Book1.xls بامتداد[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)class ويتم تبديل الوضع إلى معاينة فاصل الصفحة لورقة العمل الأولى. يتم حفظ الملف المعدل كملف output.xls.

**Ouput.xls: ورقة عمل بعد التعديل** 

![ما يجب القيام به: image_بديل_نص](worksheet-views_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageBreakPreview-PageBreakPreview.java" >}}
## **عامل التكبير**
يوفر Microsoft Excel ميزة تتيح للمستخدمين تعيين تكبير / تصغير ورقة العمل أو عامل التحجيم. تساعد هذه الميزة المستخدمين على رؤية محتويات ورقة العمل في طرق عرض أصغر أو أكبر. يمكن للمستخدمين ضبط عامل التكبير / التصغير على أي قيمة.

**ضبط عامل التكبير باستخدام Microsoft Excel** 

![ما يجب القيام به: image_بديل_نص](worksheet-views_3.png)

يسمح Aspose.Cells أيضًا للمطورين بتعيين عامل تكبير ورقة العمل.
### **السيطرة على عامل الزوم**
يوفر Aspose.Cells أ[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) فئة تمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) فئة تحتوي على[ورقة العمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)يسمح بالوصول إلى كل ورقة عمل في ملف Excel.

 يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي. ال[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) توفر class مجموعة واسعة من الخصائص والأساليب لإدارة أوراق العمل. لتعيين عامل التكبير / التصغير الخاص بورقة العمل ، استخدم ملف[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي'[setZoom](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom)طريقة.

 ويرد أدناه مثال كامل يوضح كيفية استخدام[setZoom](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom)طريقة لتعيين عامل التكبير / التصغير لورقة العمل الأولى في ملف Excel.

في لقطة الشاشة أدناه ، يمكنك رؤية ملف Book1.xls في العرض الافتراضي.

**Book1.xls: ورقة عمل قبل التعديل** 

![ما يجب القيام به: image_بديل_نص](worksheet-views_4.png)

 يتم فتح الملف Book1.xls بامتداد[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)يتم تعيين فئة وعامل التكبير / التصغير لورقة العمل الأولى على 75. يتم حفظ الملف المعدل على هيئة output.xls.

**Output.xls: ورقة عمل بعد التعديل** 

![ما يجب القيام به: image_بديل_نص](worksheet-views_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ZoomFactor-ZoomFactor.java" >}}
## **أجزاء التجميد**
ألواح التجميد هي ميزة يوفرها Microsoft Excel. تسمح لك أجزاء التجميد بتحديد البيانات لتظل مرئية عند التمرير في ورقة العمل.

**استخدام ألواح التجميد في Microsoft Excel** 

![ما يجب القيام به: image_بديل_نص](worksheet-views_6.png)

يسمح Aspose.Cells أيضًا للمطورين بتطبيق ألواح التجميد على أوراق العمل في وقت التشغيل.

يوفر Aspose.Cells أ[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) فئة تمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) فئة تحتوي على[ورقة العمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)يسمح بالوصول إلى كل ورقة عمل في ملف Excel.

 يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي. ال[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) توفر class مجموعة واسعة من الخصائص والأساليب لإدارة أوراق العمل. لتكوين أجزاء التجميد ، اتصل بـ[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي'[أجزاء التجميد](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\) ) طريقة. ال[أجزاء التجميد](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\)) تأخذ الطريقة المعلمات التالية:

- **صف**، فهرس صف الخلية الذي سيبدأ التجميد منه.
- **عمودي**، فهرس العمود الخاص بالخلية التي سيبدأ التجميد منها.
- **صفوف مجمدة**، عدد الصفوف المرئية في الجزء العلوي.
- **أعمدة مجمدة**، عدد الأعمدة المرئية في الجزء الأيمن

 ويرد أدناه مثال كامل يوضح كيفية استخدام ملف[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي'[أجزاء التجميد](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\)) طريقة لتجميد الصفوف والأعمدة (بدءًا من C4 ، ممثلة بالصف الرابع والعمود الثالث ، حيث تبدأ الصفوف والأعمدة من 0 فهارس) من ورقة العمل الأولى من ملف Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FreezePanes-FreezePanes.java" >}}


في لقطة الشاشة أدناه ، يمكنك رؤية ملف Book1.xls بدون تجميد الأجزاء.

**Book1.xls: طريقة عرض ورقة العمل قبل أي تعديل** 

![ما يجب القيام به: image_بديل_نص](worksheet-views_7.png)

 يتم فتح الملف Book1.xls بامتداد[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)يتم تجميد فئة ثم بعض الصفوف والأعمدة في ورقة العمل الأولى. يتم حفظ الملف المعدل باسم output.xls.

**Outlook.xls: طريقة عرض ورقة العمل بعد التعديل** 

![ما يجب القيام به: image_بديل_نص](worksheet-views_8.png)
## **تقسيم الأجزاء**
إذا كنت بحاجة إلى تقسيم الشاشة للحصول على عرضين مختلفين في نفس ورقة العمل ، فقم بتقسيم الألواح. يوفر Microsoft Excel ميزة مفيدة للغاية تتيح لك عرض أكثر من نسخة واحدة من ورقة العمل الخاصة بك ، ولتتمكن من التمرير عبر كل جزء من ورقة العمل بشكل مستقل: تقسيم الأجزاء.

تعمل الأجزاء في وقت واحد. إذا قمت بإجراء تغيير في أحدهما ، فسيظهر التغيير في الآخر في نفس الوقت. يوفر Aspose.Cells ميزة الأجزاء المنقسمة للمستخدمين.
### **تطبيق وإزالة الأجزاء المنقسمة**
#### **تقسيم الأجزاء**
يوفر Aspose.Cells أ[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) فئة تمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)توفر class مجموعة واسعة من الخصائص والأساليب لإدارة ملفات Excel. لتنفيذ طرق العرض المقسمة ، استخدم ملف[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي'[ينقسم](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#split\(\) ) طريقة. لإزالة الأجزاء المنقسمة ، استخدم ملف[إزالة](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit\(\)) طريقة.

في المثال ، نستخدم ملف قالب بسيط يتم تحميله ، ثم يتم تطبيق ميزة تقسيم الأجزاء المحددة على خلية في ورقة العمل الأولى. يتم حفظ الملف المحدث.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SplitPanes-SplitPanes.java" >}}



بعد تشغيل الكود أعلاه ، يكون للملف الذي تم إنشاؤه طريقة عرض مقسمة.

**تقسيم الأجزاء في ملف الإخراج** 

![ما يجب القيام به: image_بديل_نص](worksheet-views_9.png)
#### **إزالة الأجزاء**
 يمكن للمطورين إزالة الأجزاء المنقسمة باستخدام ملحق[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي'[إزالة](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit\(\)) طريقة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovePanes-RemovePanes.java" >}}


## **موضوعات مسبقة**
- [إخفاء عرض القيم الصفرية في ورقة العمل](/cells/ar/java/hiding-the-display-of-zero-values-in-the-worksheet/)
- [تعيين لون علامة تبويب ورقة العمل](/cells/ar/java/set-worksheet-tab-color/)
- [إظهار وإخفاء العناصر](/cells/ar/java/show-and-hide-elements/)
- [إظهار الصيغ بدلاً من القيم في ورقة عمل](/cells/ar/java/show-formulas-instead-of-values-in-a-worksheet/)
- [استخدم خيارات تدقيق الأخطاء](/cells/ar/java/use-error-checking-options/)
