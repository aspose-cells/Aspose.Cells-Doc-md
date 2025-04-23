---  
title: تعليقات مترابطة مع Node.js عبر C++  
linktitle: تعليقات متداخلة  
type: docs  
weight: 140  
url: /ar/nodejs-cpp/threaded-comments/  
description: إدارة التعليقات المترابطة في مستندات Excel باستخدام Aspose.Cells for Node.js via C++. تعلم كيفية إضافة وقراءة وتحرير وحذف التعليقات المترابطة.  
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

توفر Aspose.Cells طريقة [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) لإضافة تعليقات مترابطة. طريقة [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) تقبل المعلمات الثلاثة التالية.  

- اسم الخلية: اسم الخلية التي سيتم إدراج التعليق فيها.  
- نص التعليق: نص التعليق.  
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentauthor): مؤلف التعليق  

يسلط الكود أدناه الضوء على استخدام طريقة [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) لإضافة تعليق مترابط إلى الخلية A1. يرجى مراجعة [ملف Excel الناتج](89849859.xlsx) الذي تم إنشاؤه بواسطة الكود للمرجعية.  

#### **الكود المثالي**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const outDir = path.join(__dirname, "output");

const workbook = new AsposeCells.Workbook();

// Add Author
const authorIndex = workbook.getWorksheets().getThreadedCommentAuthors().add("Aspose Test", "", "");
const author = workbook.getWorksheets().getThreadedCommentAuthors().get(authorIndex);

// Add Threaded Comment
workbook.getWorksheets().get(0).getComments().addThreadedComment("A1", "Test Threaded Comment", author);

workbook.save(outDir + "AddThreadedComments_out.xlsx");
```  

## **قراءة التعليقات المتداخلة**  

### **قراءة التعليقات المتداخلة بإكسل**  

لقراءة التعليقات المتداخلة في إكسل، ما عليك سوى تحريك الماوس فوق الخلية التي تحتوي على التعليقات لعرض التعليقات. ستبدو عرض التعليقات مثل العرض في الصورة التالية.  

![todo:image_alt_text](threaded-comments_1.jpg)  

### **قراءة التعليقات المتداخلة باستخدام Aspose.Cells**  

يوفر Aspose.Cells [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) الأسلوب لاسترداد التعليقات الموجودة للعمود المحدد. [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) الأسلوب يقبل اسم العمود كمعلمة ويعيد [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection). يمكنك التكرار فوق [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) لعرض التعليقات.  

يوضح المثال التالي قراءة التعليقات من العمود A1 عن طريق تحميل [ملف Excel عينة](89849861.xlsx). يرجى الاطلاع على إخراج الكونسول الذي تم إنشاؤه بواسطة الكود للرجوع إليه.  

#### **الكود المثالي**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data"); // Adjust as necessary

const filePath = path.join(sourceDir, "ThreadedCommentsSample.xlsx");

// Loads the workbook which contains threaded comments
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get Threaded Comments
const threadedComments = worksheet.getComments().getThreadedComments("A1");

const count = threadedComments.getCount();
for (let i = 0; i < count; i++) {
const comment = threadedComments.get(i);
console.log("Comment: " + comment.getNotes());
console.log("Author: " + comment.getAuthor().getName());
}
```  

#### **مخرجات الوحدة**  

{{< highlight javascript >}}  

Comment: Test Threaded Comment  

Author: Aspose Test  

{{< /highlight >}}  

### **قراءة الوقت الذي تم إنشاء التعليقات الموجهة**  

توفر Aspose.Cells طريقة [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) لاسترجاع التعليقات المترابطة للعمود المحدد. طريقة [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) تقبل اسم العمود كمعامل وتعيد [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection). يمكنك التكرار على [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) واستخدام الخاصية [**ThreadedComment.getCreatedTime()**](https://reference.aspose.com/cells/nodejs-cpp/threadedcomment/#getCreatedTime--).  

يوضح المثال التالي قراءة الوقت الذي تم إنشاء التعليقات الموجهة من خلال تحميل [ملف Excel عينة](89849861.xlsx). يرجى الاطلاع على إخراج الكونسول الذي تم إنشاؤه بواسطة الكود للرجوع إليه.  

#### **الكود المثالي**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const filePath = path.join(sourceDir, "ThreadedCommentsSample.xlsx");

// Loads the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get Threaded Comments
const threadedComments = worksheet.getComments().getThreadedComments("A1");

const count = threadedComments.getCount();

for (let i = 0; i < count; i++) {
const comment = threadedComments.get(i);
console.log("Comment: " + comment.getNotes());
console.log("Author: " + comment.getAuthor().getName());
console.log("Created Time: " + comment.getCreatedTime());
}
```  

#### **مخرجات الوحدة**  

{{< highlight javascript >}}  

Comment: Test Threaded Comment  

Author: Aspose Test  

Created Time: 5/15/2019 12:46:23 PM  

{{< /highlight >}}  

## **تحرير التعليقات الموجهة**  

### **تحرير تعليق موجه بواسطة Excel**  

لتحرير تعليق موجه في Excel، انقر على رابط **تحرير** على التعليق كما هو موضح في الصورة التالية.  

![todo:image_alt_text](threaded-comments_7.jpg)  

### **تحرير تعليق موجه باستخدام Aspose.Cells**  

توفر Aspose.Cells طريقة [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) لاسترجاع التعليقات المترابطة للعمود المحدد. طريقة [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) تقبل اسم العمود كمعامل وتعيد [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection). يمكنك تحديث التعليق المطلوب في [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) وحفظ المصنف.  

يوضح المثال التالي تحرير أول تعليق موجه في العمود A1 عن طريق تحميل [ملف Excel عينة](89849861.xlsx). يرجى الاطلاع على [ملف Excel الناتج](89849862.xlsx) الذي تم إنشاؤه بواسطة الكود يظهر التعليق المحدث للرجوع إليه.  

#### **الكود المثالي**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source and output directories
const sourceDir = path.join(__dirname, "data");
const outDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "ThreadedCommentsSample.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get Threaded Comment
const comment = worksheet.getComments().getThreadedComments("A1").get(0);
comment.setNotes("Updated Comment");

workbook.save(outDir + "EditThreadedComments.xlsx");
```  

## **إزالة التعليقات المتداولة**  

### **إزالة التعليقات المتداولة باستخدام Excel**  

لإزالة التعليقات المتداولة في Excel، انقر بزر الماوس الأيمن على الخلية التي تحتوي على التعليقات وانقر على الخيار **حذف التعليق** كما هو موضح في الصورة التالية.  

![todo:image_alt_text](threaded-comments_8.jpg)   


