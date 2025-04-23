---
title: تعليقات متداخلة باستخدام C++
linktitle: تعليقات متداخلة
type: docs
weight: 140
url: /ar/cpp/threaded-comments/
description: تعلم كيفية إضافة، قراءة، تحرير، وحذف التعليقات المتداخلة في ملفات Excel باستخدام Aspose.Cells مع C++.
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

توفر Aspose.Cells طريقة [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/addthreadedcomment/) لإضافة تعليقات مترابطة. طريقة [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/addthreadedcomment/) تقبل المعلمات الثلاثة التالية.

- اسم الخلية: اسم الخلية التي سيتم إدراج التعليق فيها.
- نص التعليق: نص التعليق.
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentauthor/): مؤلف التعليق

يوضح الكود النموذجي التالي استخدام الطريقة [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/addthreadedcomment/) لإضافة تعليق متداخل إلى الخلية A1. يرجى الاطلاع على الملف الإكسل الناتج (89849859.xlsx) المُنشأ بواسطة الكود للإشارة.

#### **الكود المثالي**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add Author
    int authorIndex = workbook.GetWorksheets().GetThreadedCommentAuthors().Add(u"Aspose Test", u"", u"");
    ThreadedCommentAuthor author = workbook.GetWorksheets().GetThreadedCommentAuthors().Get(authorIndex);

    // Add Threaded Comment
    workbook.GetWorksheets().Get(0).GetComments().AddThreadedComment(u"A1", u"Test Threaded Comment", author);

    // Save the workbook
    workbook.Save(outDir + u"AddThreadedComments_out.xlsx");

    std::cout << "Threaded comment added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **قراءة التعليقات المتداخلة**

### **قراءة التعليقات المتداخلة بإكسل**

لقراءة التعليقات المتداخلة في إكسل، ما عليك سوى تحريك الماوس فوق الخلية التي تحتوي على التعليقات لعرض التعليقات. ستبدو عرض التعليقات مثل العرض في الصورة التالية.

![todo:image_alt_text](threaded-comments_1.jpg)

### **قراءة التعليقات المتداخلة باستخدام Aspose.Cells**

يوفر Aspose.Cells [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) الأسلوب لاسترداد التعليقات الموجودة للعمود المحدد. [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) الأسلوب يقبل اسم العمود كمعلمة ويعيد [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/). يمكنك التكرار فوق [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/) لعرض التعليقات.

يوضح المثال التالي قراءة التعليقات من العمود A1 عن طريق تحميل [ملف Excel عينة](89849861.xlsx). يرجى الاطلاع على إخراج الكونسول الذي تم إنشاؤه بواسطة الكود للرجوع إليه.

#### **الكود المثالي**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook
    Workbook workbook(srcDir + u"ThreadedCommentsSample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get Threaded Comments
    ThreadedCommentCollection threadedComments = worksheet.GetComments().GetThreadedComments(u"A1");

    // Iterate through threaded comments
    for (int i = 0; i < threadedComments.GetCount(); i++)
    {
        ThreadedComment comment = threadedComments.Get(i);
        cout << "Comment: " << comment.GetNotes().ToUtf8() << endl;
        cout << "Author: " << comment.GetAuthor().GetName().ToUtf8() << endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

#### **مخرجات الوحدة**

{{< highlight cpp >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **قراءة الوقت الذي تم إنشاء التعليقات الموجهة**

يوفر Aspose.Cells [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) الأسلوب لاسترداد التعليقات الموجهة للعمود المحدد. [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) الأسلوب يقبل اسم العمود كمعلمة ويعيد [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/). يمكنك التكرار فوق [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/) واستخدام خاصية [**ThreadedComment.GetCreatedTime()**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcomment/getcreatedtime/).

يوضح المثال التالي قراءة الوقت الذي تم إنشاء التعليقات الموجهة من خلال تحميل [ملف Excel عينة](89849861.xlsx). يرجى الاطلاع على إخراج الكونسول الذي تم إنشاؤه بواسطة الكود للرجوع إليه.

#### **الكود المثالي**

```cpp
#include <iostream>
#include <iomanip>
#include <sstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    Workbook workbook(srcDir + u"ThreadedCommentsSample.xlsx");

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    ThreadedCommentCollection threadedComments = worksheet.GetComments().GetThreadedComments(u"A1");

    for (int i = 0; i < threadedComments.GetCount(); i++)
    {
        ThreadedComment comment = threadedComments.Get(i);
        cout << "Comment: " << comment.GetNotes().ToUtf8() << endl;
        cout << "Author: " << comment.GetAuthor().GetName().ToUtf8() << endl;
        Date createdTime = comment.GetCreatedTime();
        ostringstream oss;
        oss << setfill('0') 
            << setw(4) << createdTime.year << "-"
            << setw(2) << createdTime.month << "-"
            << setw(2) << createdTime.day << " "
            << setw(2) << createdTime.hour << ":"
            << setw(2) << createdTime.minute << ":"
            << setw(2) << createdTime.second;
        cout << "Created Time: " << oss.str() << endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

#### **مخرجات الوحدة**

{{< highlight cpp >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 5/15/2019 12:46:23 PM

{{< /highlight >}}

## **تحرير التعليقات الموجهة**

### **تحرير تعليق موجه بواسطة Excel**

لتحرير تعليق موجه في Excel، انقر على رابط **تحرير** على التعليق كما هو موضح في الصورة التالية.

![todo:image_alt_text](threaded-comments_7.jpg)

### **تحرير تعليق موجه باستخدام Aspose.Cells**

يوفر Aspose.Cells الأسلوب [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) لاسترداد التعليقات الموجهة للعمود المحدد. [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) الأسلوب يقبل اسم العمود كمعلمة ويعيد [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/). يمكنك تحديث التعليق المطلوب في [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/) وحفظ الدفتر.

يوضح المثال التالي تحرير أول تعليق موجه في العمود A1 عن طريق تحميل [ملف Excel عينة](89849861.xlsx). يرجى الاطلاع على [ملف Excel الناتج](89849862.xlsx) الذي تم إنشاؤه بواسطة الكود يظهر التعليق المحدث للرجوع إليه.

#### **الكود المثالي**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook workbook(srcDir + u"ThreadedCommentsSample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the threaded comment from cell A1
    ThreadedComment comment = worksheet.GetComments().GetThreadedComments(u"A1").Get(0);

    // Update the comment text
    comment.SetNotes(u"Updated Comment");

    // Save the workbook
    workbook.Save(outDir + u"EditThreadedComments.xlsx");

    std::cout << "Threaded comment updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **إزالة التعليقات المتداولة**

### **إزالة التعليقات المتداولة باستخدام Excel**

لإزالة التعليقات المتداولة في Excel، انقر بزر الماوس الأيمن على الخلية التي تحتوي على التعليقات وانقر على الخيار **حذف التعليق** كما هو موضح في الصورة التالية.

![todo:image_alt_text](threaded-comments_8.jpg)

### **إزالة التعليقات المتداولة باستخدام Aspose.Cells**

يوفر Aspose.Cells [**Comments.RemoveAt**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/removeat/) لإزالة التعليقات المتداولة للعمود المحدد. يقبل [**Comments.RemoveAt**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/removeat/) الاسم الخاص بالعمود كمعلمة ويزيل التعليقات في ذلك العمود.

يوضح المثال التالي إزالة التعليقات في العمود A1 من خلال تحميل [ملف Excel عينة](89849861.xlsx). يرجى الاطلاع على [ملف الإكسل الناتج](89849864.xlsx) الذي تم إنشاؤه بواسطة الكود للإشارة.

#### **الكود المثالي**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook workbook(srcDir + u"ThreadedCommentsSample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the comments collection
    CommentCollection comments = worksheet.GetComments();

    // Get the author of the first threaded comment in cell A1
    ThreadedCommentAuthor author = worksheet.GetComments().GetThreadedComments(u"A1").Get(0).GetAuthor();

    // Remove the comment at cell A1
    comments.RemoveAt(u"A1");

    // Get the threaded comment authors collection
    ThreadedCommentAuthorCollection authors = workbook.GetWorksheets().GetThreadedCommentAuthors();

    // Save the workbook
    workbook.Save(outDir + u"ThreadedCommentsSample_Out.xlsx");

    std::cout << "Threaded comments processed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

يرجى ملاحظة أنه عند إزالة التعليق باستخدام Aspose.Cells، فإن الكاتب لا يتم إزالته تلقائيًا. إذا كنت بحاجة إلى إزالة الكاتب أيضًا، يرجى استخدام طريقة ***RemoveAt*** للفئة [**ThreadedCommentAuthorCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentauthorcollection/) كما هو موضح في المثال أعلاه.

{{% /alert %}}
