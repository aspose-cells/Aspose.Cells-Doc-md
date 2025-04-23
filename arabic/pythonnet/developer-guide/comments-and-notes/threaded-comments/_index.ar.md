---
title: تعليقات متداخلة
type: docs
weight: 140
url: /ar/python-net/threaded-comments/
---

## **تعليقات متداخلة**

يوفر MS Excel 365 ميزة إضافة تعليقات متداخلة. تعمل هذه التعليقات كمحادثات ويمكن استخدامها للنقاشات. يأتي التعليق الآن مع مربع رد يسمح بالمحادثات المتداخلة. تسمى التعليقات القديمة الآن ملاحظات في Excel 365. تُظهر الصورة المصغرة أدناه كيف يتم عرض التعليقات المتداخلة عند فتحها في Excel.

![todo:image_alt_text](threaded-comments_1.jpg)

تُعرض التعليقات المتداخلة مثل هذا في الإصدارات السابقة من Excel. تم أخذ الصور التالية عن طريق فتح الملف العيني في Excel 2016.

![todo:image_alt_text](threaded-comments_2.jpg)

![todo:image_alt_text](threaded-comments_3.jpg)

توفر Aspose.Cells for Python via .NET أيضًا ميزة إدارة التعليقات المتداخلة.

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

### **إضافة تعليق متداخل باستخدام Aspose.Cells for Python via .NET**

توفر Aspose.Cells for Python via .NET طريقة [**Comments.add_threaded_comment**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add_threaded_comment/) لإضافة تعليقات متداخلة. تقبل طريقة [**Comments.add_threaded_comment**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add_threaded_comment) المعلمات الثلاثة التالية.

- اسم الخلية: اسم الخلية التي سيتم إدراج التعليق فيها.
- نص التعليق: نص التعليق.
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentauthor): مؤلف التعليق

يوضح الكود النموذجي التالي استخدام الطريقة [**Comments.add_threaded_comment**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add_threaded_comment) لإضافة تعليق متداخل إلى الخلية A1. يرجى الاطلاع على الملف الإكسل الناتج (89849859.xlsx) المُنشأ بواسطة الكود للإشارة.

#### **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-AddThreadedComments-1.py" >}}

## **قراءة التعليقات المتداخلة**

### **قراءة التعليقات المتداخلة بإكسل**

لقراءة التعليقات المتداخلة في إكسل، ما عليك سوى تحريك الماوس فوق الخلية التي تحتوي على التعليقات لعرض التعليقات. ستبدو عرض التعليقات مثل العرض في الصورة التالية.

![todo:image_alt_text](threaded-comments_1.jpg)

### **قراءة التعليقات المتداخلة باستخدام Aspose.Cells for Python via .NET**

توفر Aspose.Cells for Python via .NET طريقة [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) لاسترداد التعليقات المتداخلة للعمود المحدد. تقبل طريقة [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) اسم العمود كمعامل وترجع [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection). يمكنك تكرار [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection) لمشاهدة التعليقات.

يوضح المثال التالي قراءة التعليقات من العمود A1 عن طريق تحميل [ملف Excel عينة](89849861.xlsx). يرجى الاطلاع على إخراج الكونسول الذي تم إنشاؤه بواسطة الكود للرجوع إليه.

#### **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-ReadThreadedComments-1.py" >}}

#### **مخرجات الوحدة**

{{< highlight csharp >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **قراءة الوقت الذي تم إنشاء التعليقات الموجهة**

توفر Aspose.Cells for Python via .NET طريقة [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) لاسترداد التعليقات المتداخلة للعمود المحدد. تقبل طريقة [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) اسم العمود كمعامل وترجع [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection). يمكنك التكرار عبر [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection) واستخدام الخاصية [**ThreadedComment.created_time**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcomment/created_time).

يوضح المثال التالي قراءة الوقت الذي تم إنشاء التعليقات الموجهة من خلال تحميل [ملف Excel عينة](89849861.xlsx). يرجى الاطلاع على إخراج الكونسول الذي تم إنشاؤه بواسطة الكود للرجوع إليه.

#### **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-ReadThreadedCommentCreatedTime-1.py" >}}

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

### **تعديل التعليق المتداخل باستخدام Aspose.Cells for Python via .NET**

توفر Aspose.Cells for Python via .NET الطريقة [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) لاسترداد التعليقات المتداخلة للعمود المحدد. تقبل طريقة [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) اسم العمود كمعامل وترجع [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection). يمكنك تحديث التعليق المطلوب في [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection) وحفظ المصنف.

يوضح المثال التالي تحرير أول تعليق موجه في العمود A1 عن طريق تحميل [ملف Excel عينة](89849861.xlsx). يرجى الاطلاع على [ملف Excel الناتج](89849862.xlsx) الذي تم إنشاؤه بواسطة الكود يظهر التعليق المحدث للرجوع إليه.

#### **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-EditThreadedComments-1.py" >}}

