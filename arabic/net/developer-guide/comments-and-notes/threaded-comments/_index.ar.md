---
title: تعليقات متداخلة
type: docs
weight: 140
url: /ar/net/threaded-comments/
---

## **تعليقات متداخلة**

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
  - انقر على علامة **مراجعة**
  - انقر على زر **تعليق جديد**
  - سيفتح هذا حوارًا لإدخال التعليقات في الخلية النشطة.
  - ![todo:image_alt_text](threaded-comments_4.jpg)
- الطريقة الثانية
  - انقر بزر الفأرة الأيمن على الخلية التي ترغب في إدراج التعليق فيها.
  - انقر على خيار **تعليق جديد**
  - سيفتح هذا حوارًا لإدخال التعليقات في الخلية النشطة.
  - ![todo:image_alt_text](threaded-comments_5)

### **إضافة تعليق متداخل عبر Aspose.Cells**

توفر Aspose.Cells الطريقة [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) لإضافة تعليقات متداخلة. تقبل الطريقة [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) الثلاثة معلمات التالية.

- اسم الخلية: اسم الخلية التي سيتم إدراج التعليق فيها.
- نص التعليق: نص التعليق.
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthor): مؤلف التعليق

يوضح الكود النموذجي التالي استخدام الطريقة [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) لإضافة تعليق متداخل إلى الخلية A1. يرجى الاطلاع على الملف الإكسل الناتج (89849859.xlsx) المُنشأ بواسطة الكود للإشارة.

#### **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-AddThreadedComments-1.cs" >}}

## **قراءة التعليقات المتداخلة**

### **قراءة التعليقات المتداخلة بإكسل**

لقراءة التعليقات المتداخلة في إكسل، ما عليك سوى تحريك الماوس فوق الخلية التي تحتوي على التعليقات لعرض التعليقات. ستبدو عرض التعليقات مثل العرض في الصورة التالية.

![todo:image_alt_text](threaded-comments_1.jpg)

### **قراءة التعليقات المتداخلة باستخدام Aspose.Cells**

يوفر Aspose.Cells [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) الأسلوب لاسترداد التعليقات الموجودة للعمود المحدد. [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) الأسلوب يقبل اسم العمود كمعلمة ويعيد [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). يمكنك التكرار فوق [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) لعرض التعليقات.

يوضح المثال التالي قراءة التعليقات من العمود A1 عن طريق تحميل [ملف Excel عينة](89849861.xlsx). يرجى الاطلاع على إخراج الكونسول الذي تم إنشاؤه بواسطة الكود للرجوع إليه.

#### **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedComments-1.cs" >}}

#### **مخرجات الوحدة**

{{< highlight csharp >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **قراءة الوقت الذي تم إنشاء التعليقات الموجهة**

يوفر Aspose.Cells [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) الأسلوب لاسترداد التعليقات الموجهة للعمود المحدد. [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) الأسلوب يقبل اسم العمود كمعلمة ويعيد [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). يمكنك التكرار فوق [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) واستخدام خاصية [**ThreadedComment.CreatedTime**](https://reference.aspose.com/cells/net/aspose.cells/threadedcomment/properties/createdtime).

يوضح المثال التالي قراءة الوقت الذي تم إنشاء التعليقات الموجهة من خلال تحميل [ملف Excel عينة](89849861.xlsx). يرجى الاطلاع على إخراج الكونسول الذي تم إنشاؤه بواسطة الكود للرجوع إليه.

#### **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedCommentCreatedTime-1.cs" >}}

#### **مخرجات الوحدة**

{{< highlight csharp >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 5/15/2019 12:46:23 PM

{{< /highlight >}}

## **تحرير التعليقات الموجهة**

### **تحرير تعليق موجه بواسطة Excel**

لتحرير تعليق موجه في Excel، انقر على رابط **تحرير** على التعليق كما هو موضح في الصورة التالية.

![todo:image_alt_text](threaded-comments_7.jpg)

### **تحرير تعليق موجه باستخدام Aspose.Cells**

يوفر Aspose.Cells الأسلوب [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) لاسترداد التعليقات الموجهة للعمود المحدد. [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) الأسلوب يقبل اسم العمود كمعلمة ويعيد [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). يمكنك تحديث التعليق المطلوب في [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) وحفظ الدفتر.

يوضح المثال التالي تحرير أول تعليق موجه في العمود A1 عن طريق تحميل [ملف Excel عينة](89849861.xlsx). يرجى الاطلاع على [ملف Excel الناتج](89849862.xlsx) الذي تم إنشاؤه بواسطة الكود يظهر التعليق المحدث للرجوع إليه.

#### **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-EditThreadedComments-1.cs" >}}

## **إزالة التعليقات المتداولة**

### **إزالة التعليقات المتداولة باستخدام Excel**

لإزالة التعليقات المتداولة في Excel، انقر بزر الماوس الأيمن على الخلية التي تحتوي على التعليقات وانقر على الخيار **حذف التعليق** كما هو موضح في الصورة التالية.

![todo:image_alt_text](threaded-comments_8.jpg)

### **إزالة التعليقات المتداولة باستخدام Aspose.Cells**

يوفر Aspose.Cells [**Comments.RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/removeat/index) لإزالة التعليقات المتداولة للعمود المحدد. يقبل [**Comments.RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/removeat/index) الاسم الخاص بالعمود كمعلمة ويزيل التعليقات في ذلك العمود.

يوضح المثال التالي إزالة التعليقات في العمود A1 من خلال تحميل [ملف Excel عينة](89849861.xlsx). يرجى الاطلاع على [ملف الإكسل الناتج](89849864.xlsx) الذي تم إنشاؤه بواسطة الكود للإشارة.

#### **الكود المثالي**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-RemoveThreadedComments-1.cs" >}}

{{% alert color="primary" %}}

يرجى ملاحظة أنه عند إزالة التعليق باستخدام Aspose.Cells، فإن الكاتب لا يتم إزالته تلقائيًا. إذا كنت بحاجة إلى إزالة الكاتب أيضًا، يرجى استخدام طريقة ***RemoveAt*** للفئة [**ThreadedCommentAuthorCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthorcollection) كما هو موضح في المثال أعلاه.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
