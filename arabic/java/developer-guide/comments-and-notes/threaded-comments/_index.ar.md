---
title: تعليقات متداخلة
type: docs
weight: 140
url: /ar/java/threaded-comments/
---

# **تعليقات متداخلة**
يوفر MS Excel 365 ميزة إضافة تعليقات متداخلة. تعمل هذه التعليقات كمحادثات ويمكن استخدامها للنقاشات. يأتي التعليق الآن مع مربع رد يسمح بالمحادثات المتداخلة. تسمى التعليقات القديمة الآن ملاحظات في Excel 365. تُظهر الصورة المصغرة أدناه كيف يتم عرض التعليقات المتداخلة عند فتحها في Excel.

![todo:image_alt_text](threaded-comments_1.jpg)

تُعرض التعليقات المتداخلة مثل هذا في الإصدارات السابقة من Excel. تم أخذ الصور التالية عن طريق فتح الملف العيني في Excel 2016.

![todo:image_alt_text](threaded-comments_2.jpg)



![todo:image_alt_text](threaded-comments_3.jpg)



توفر Aspose.Cells أيضاً ميزة إدارة التعليقات المتداخلة. 
## **إضافة تعليقات متداخلة**
### **إضافة تعليق متداخل مع إكسل**
لاضافة تعليقات متداخلة في إكسل 365، اتبع الخطوات التالية.

- الطريقة الأولى
  - انقر على علامة التبويب **مراجعة**
  - انقر على زر **تعليق جديد**
  - سيفتح هذا حوارًا لإدخال التعليقات في الخلية النشطة.
  - ![todo:image_alt_text](threaded-comments_4.jpg)
- الطريقة الثانية
  - انقر بزر الفأرة الأيمن على الخلية التي ترغب في إدراج التعليق فيها.
  - انقر على الخيار **تعليق جديد**
  - سيفتح هذا حوارًا لإدخال التعليقات في الخلية النشطة.
  - ![todo:image_alt_text](threaded-comments_5)
### **إضافة تعليق متداخل عبر Aspose.Cells**
توفر Aspose.Cells طريقة [Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\)) لإضافة تعليقات متداخلة. تقبل طريقة [Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\)) الثلاثة معلمات التالية.

- اسم الخلية: اسم الخلية التي سيتم إدراج التعليق فيها.
- نص التعليق: نص التعليق.
- [ThreadedCommentAuthor](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentAuthor): مؤلف التعليق

يوضح العينة البرمجية التالية استخدام طريقة [Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\)) لإضافة تعليق متداخل إلى الخلية A1. يرجى الاطلاع على [ملف الإكسل الناتج](AddThreadedComments_out.xlsx) من الكود للرجوع إليه.
#### **الكود المثالي**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddThreadedComments-1.java" >}}
## **قراءة التعليقات المتداخلة**
### **قراءة التعليقات المتداخلة بإكسل**
لقراءة التعليقات المتداخلة في إكسل، ما عليك سوى تحريك الماوس فوق الخلية التي تحتوي على التعليقات لعرض التعليقات. ستبدو عرض التعليقات مثل العرض في الصورة التالية.

![todo:image_alt_text](threaded-comments_1.jpg)
### **قراءة التعليقات المتداخلة باستخدام Aspose.Cells**
توفر Aspose.Cells طريقة [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) لاسترداد التعليقات المتداخلة للعمود المحدد. طريقة [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) تقبل اسم العمود كمعلمة وتُرجع [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). يمكنك تكرار [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection) لعرض التعليقات.

المثال التالي يوضح قراءة التعليقات من العمود A1 عن طريق تحميل [ملف Excel عينة](ThreadedCommentsSample.xlsx). الرجاء الاطلاع على إخراج وحدة التحكم الذي تم إنشاؤه بواسطة الكود للإشارة.
#### **الكود المثالي**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedComments-1.java" >}}
#### **مخرجات الوحدة**

{{< highlight java >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **قراءة الوقت الذي تم إنشاء التعليقات الموجهة**
يوفر Aspose.Cells طريقة [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) لاسترداد التعليقات المتداخلة للعمود المحدد. تقبل طريقة [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) الاسم الخاص بالعمود كمعلمة وترجع [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). يمكنك تكرار [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection) واستخدام خاصية [ThreadedComment.CreatedTime](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcomment#CreatedTime).

المثال التالي يوضح قراءة الوقت الذي تم إنشاء التعليق المتداخل بتحميل [ملف Excel عينة](ThreadedCommentsSample.xlsx). الرجاء الاطلاع على إخراج وحدة التحكم الذي تم إنشاؤه بواسطة الكود للإشارة.
#### **الكود المثالي**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedCommentCreatedTime-1.java" >}}
#### **مخرجات الوحدة**

{{< highlight java >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 2019-05-15T12:46:23

{{< /highlight >}}

## **تحرير التعليقات الموجهة**
### **تحرير تعليق موجه بواسطة Excel**
لتحرير تعليق متداخل في Excel، انقر فوق الرابط **تحرير** في التعليق كما هو موضح في الصورة التالية.

![todo:image_alt_text](threaded-comments_7.jpg)
### **تحرير تعليق موجه باستخدام Aspose.Cells**
يوفر Aspose.Cells طريقة [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) لاسترداد التعليقات المتداخلة للعمود المحدد. تقبل طريقة [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) الاسم الخاص بالعمود كمعلمة وترجع [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). يمكنك تحديث التعليق المطلوب في [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection) وحفظ الدفتر.

المثال التالي يوضح تحرير التعليق المتداخل الأول في العمود A1 من خلال تحميل [ملف Excel عينة](ThreadedCommentsSample.xlsx). يرجى الاطلاع على [ملف الإكسل الناتج](EditThreadedComments.xlsx) الذي تم إنشاؤه بواسطة الكود يظهر التعليق المحدث للرجوع إليه.
#### **الكود المثالي**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "EditThreadedComments-1.java" >}}
## **إزالة التعليقات المتداولة**
### **إزالة التعليقات المتداولة باستخدام Excel**
لإزالة التعليقات المتداخلة في Excel ، انقر بزر الماوس الأيمن على الخلية التي تحتوي على التعليقات وانقر على الخيار **حذف التعليق** كما هو موضح في الصورة التالية.

![todo:image_alt_text](threaded-comments_8.jpg)
### **إزالة التعليقات المتداولة باستخدام Aspose.Cells**
توفر Aspose.Cells طريقة [Comments.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt\(int\)) لإزالة التعليقات للعمود المحدد. تقبل الطريقة [Comments.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt\(int\)) اسم العمود كمعلمة تقوم بإزالة التعليقات في ذلك العمود. 

المثال التالي يوضح إزالة التعليقات في العمود A1 عن طريق تحميل ال [ملف Excel العيني](ThreadedCommentsSample.xlsx). يُرجى الاطلاع على [ملف Excel الناتج](ThreadedCommentsSample_Out.xlsx) الذي تم إنشاؤه بواسطة الكود للإشارة.
#### **الكود المثالي**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "RemoveThreadedComments-1.java" >}}

{{% alert color="primary" %}} 

يرجى ملاحظة أنه من خلال إزالة التعليق باستخدام Aspose.Cells ، لا يتم إزالة المؤلف تلقائيًا. إذا كنت بحاجة إلى إزالة المؤلف أيضًا ، يُرجى استخدام الطريقة [ThreadedCommentAuthorCollection.removeAt](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcommentauthorcollection#removeAt\(int\)) كما هو موضح في المثال أعلاه.

{{% /alert %}}
