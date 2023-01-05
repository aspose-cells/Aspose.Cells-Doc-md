---
title: تعليقات مترابطة
type: docs
weight: 140
url: /ar/net/threaded-comments/
---
## **تعليقات مترابطة**

يوفر MS Excel 365 ميزة لإضافة تعليقات مترابطة. تعمل هذه التعليقات كمحادثات ويمكن استخدامها للمناقشات. تأتي التعليقات الآن مع مربع الرد الذي يسمح بالمحادثات المترابطة. تسمى التعليقات القديمة ملاحظات في Excel 365. توضح لقطة الشاشة أدناه كيفية عرض التعليقات المترابطة عند فتحها في Excel.

![ما يجب القيام به: image_بديل_نص](threaded-comments_1.jpg)

تظهر التعليقات المترابطة بهذا الشكل في الإصدارات القديمة من Excel. تم التقاط الصور التالية عن طريق فتح ملف العينة في Excel 2016.

![ما يجب القيام به: image_بديل_نص](threaded-comments_2.jpg)

![ما يجب القيام به: image_بديل_نص](threaded-comments_3.jpg)

يوفر Aspose.Cells أيضًا الخاصية لإدارة التعليقات المترابطة.

## **إضافة تعليقات مترابطة**

### **إضافة تعليق مترابطة مع Excel**

لإضافة تعليقات مترابطة في Excel 365 ، اتبع الخطوات التالية.

- طريقة 1
 - انقر على**إعادة النظر** فاتورة غير مدفوعة
 - انقر على**تعليق جديد** زر
 - سيؤدي هذا إلى فتح حوار لإدخال التعليقات في الخلية النشطة.
  - ![ما يجب القيام به: image_بديل_نص](threaded-comments_4.jpg)
- الطريقة الثانية
 - انقر بزر الماوس الأيمن فوق الخلية حيث تريد إدراج التعليق.
 - انقر على**تعليق جديد** اختيار.
 - سيؤدي هذا إلى فتح حوار لإدخال التعليقات في الخلية النشطة.
  - ![ما يجب القيام به: image_بديل_نص](threaded-comments_5)

### **إضافة تعليق مترابط باستخدام Aspose.Cells**

يوفر Aspose.Cells[**التعليقات. AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) طريقة لإضافة تعليقات مترابطة[**التعليقات. AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1)تقبل الطريقة المعلمات الثلاثة التالية.

- Cell الاسم: اسم الخانة التي سيتم ادراج التعقيب بها.
- نص التعليق: نص التعليق.
- [**مؤلف**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthor): كاتب التعليق

يوضح نموذج التعليمات البرمجية التالي استخدام[**التعليقات. AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1)طريقة لإضافة تعليق مترابط إلى الخلية A1. الرجاء مراجعة[إخراج ملف Excel](89849859.xlsx) التي تم إنشاؤها بواسطة رمز كمرجع.

#### **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-AddThreadedComments-1.cs" >}}

## **قراءة التعليقات المترابطة**

### **قراءة التعليقات المترابطة باستخدام Excel**

لقراءة التعليقات المترابطة في Excel ، ما عليك سوى تحريك مؤشر الماوس فوق الخلية التي تحتوي على تعليقات لعرض التعليقات. سيبدو عرض التعليقات مثل العرض في الصورة التالية.

![ما يجب القيام به: image_بديل_نص](threaded-comments_1.jpg)

### **قراءة التعليقات المترابطة باستخدام Aspose.Cells**

يوفر Aspose.Cells[**التعليقات**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)طريقة لاسترداد التعليقات المترابطة للعمود المحدد.[**التعليقات**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)يقبل الأسلوب اسم العمود كمعامل ويعيد[**مجموعة التعليقات المترابطة**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). يمكنك التكرار على امتداد[**مجموعة التعليقات المترابطة**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection)لعرض التعليقات.

يوضح المثال التالي قراءة التعليقات من العمود A1 بتحميل ملف[نموذج لملف Excel](89849861.xlsx). يرجى الاطلاع على إخراج وحدة التحكم التي تم إنشاؤها بواسطة الرمز كمرجع.

#### **عينة من الرموز**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedComments-1.cs" >}}

#### **إخراج وحدة التحكم**

تعليق: اختبار تعليق مترابطة

المؤلف: Aspose اختبار

### **قراءة وقت الإنشاء للتعليقات المترابطة**

يوفر Aspose.Cells[**التعليقات**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)طريقة لاسترداد التعليقات المترابطة للعمود المحدد.[**التعليقات**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)يقبل الأسلوب اسم العمود كمعامل ويعيد[**مجموعة التعليقات المترابطة**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). يمكنك التكرار على امتداد[**مجموعة التعليقات المترابطة**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) واستخدم[**ThreadedComment.CreatedTime**](https://reference.aspose.com/cells/net/aspose.cells/threadedcomment/properties/createdtime) خاصية.

يوضح المثال التالي قراءة الوقت الذي تم إنشاؤه للتعليقات المترابطة عن طريق تحميل ملف[نموذج لملف Excel](89849861.xlsx). يرجى الاطلاع على إخراج وحدة التحكم التي تم إنشاؤها بواسطة الرمز كمرجع.

#### **عينة من الرموز**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedCommentCreatedTime-1.cs" >}}

#### **إخراج وحدة التحكم**

تعليق: اختبار تعليق مترابطة

المؤلف: Aspose اختبار

وقت الإنشاء: 5/15/2019 12:46:23 مساءً

## **تحرير التعليقات المترابطة**

### **تحرير تعليق مترابطة مع Excel**

 لتحرير تعليق مترابط في Excel ، انقر فوق**تعديل** رابط التعليق كما هو موضح في الصورة التالية.

![ما يجب القيام به: image_بديل_نص](threaded-comments_7.jpg)

### **تحرير التعليقات المترابطة باستخدام Aspose.Cells**

يوفر Aspose.Cells[**التعليقات**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) طريقة لاسترداد التعليقات المترابطة للعمود المحدد.[**التعليقات**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)يقبل الأسلوب اسم العمود كمعامل ويعيد[**مجموعة التعليقات المترابطة**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). يمكنك تحديث التعليق المطلوب في[**مجموعة التعليقات المترابطة**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection)وحفظ المصنف.

يوضح المثال التالي تحرير أول تعليق مترابط في العمود A1 عن طريق تحميل ملف[نموذج لملف Excel](89849861.xlsx). الرجاء مراجعة[إخراج ملف Excel](89849862.xlsx)التي تم إنشاؤها بواسطة الكود الذي يظهر التعليق المحدث للرجوع إليه.

#### **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-EditThreadedComments-1.cs" >}}

## **إزالة التعليقات المترابطة**

### **إزالة التعليقات المترابطة مع Excel**

 لإزالة التعليقات المترابطة في Excel ، انقر بزر الماوس الأيمن فوق الخلية التي تحتوي على التعليقات وانقر فوق**حذف تعليق** الخيار كما هو موضح في الصورة التالية.

![ما يجب القيام به: image_بديل_نص](threaded-comments_8.jpg)

### **إزالة التعليقات المترابطة باستخدام Aspose.Cells**

يوفر Aspose.Cells[**التعليقات**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/removeat/index)طريقة لإزالة التعليقات للعمود المحدد.[**التعليقات**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/removeat/index)يقبل الأسلوب اسم العمود كمعامل يزيل التعليقات الموجودة في هذا العمود.

يوضح المثال التالي إزالة التعليقات في العمود A1 بتحميل ملف[نموذج لملف Excel](89849861.xlsx). الرجاء مراجعة[إخراج ملف Excel](89849864.xlsx)تم إنشاؤها بواسطة رمز كمرجع.

#### **عينة من الرموز**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-RemoveThreadedComments-1.cs" >}}

{{% alert color="primary" %}}

 يرجى ملاحظة أنه بإزالة التعليق بالرقم Aspose.Cells ، لا تتم إزالة المؤلف تلقائيًا. إذا كنت بحاجة إلى إزالة المؤلف أيضًا ، فيرجى استخدام طريقة RemoveAt الخاصة بـ[**ThreadedCommentAuthorCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthorcollection) فئة كما هو موضح في المثال أعلاه.

{{% /alert %}}
