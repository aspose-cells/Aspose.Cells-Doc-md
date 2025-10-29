---
title: تعليقات متسلسلة باستخدام JavaScript عبر C++
linktitle: تعليقات متداخلة
type: docs
weight: 140
url: /ar/javascript-cpp/threaded-comments/
description: إدارة التعليقات المتسلسلة في مستندات إكسل باستخدام Aspose.Cells for Javaنص البرنامج النصي عبر C++. تعلم كيفية إضافة وقراءة وتحرير وحذف التعليقات المتسلسلة.
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

توفر Aspose.Cells طريقة [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) لإضافة تعليقات مترابطة. طريقة [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) تقبل المعلمات الثلاثة التالية.

- اسم الخلية: اسم الخلية التي سيتم إدراج التعليق فيها.
- نص التعليق: نص التعليق.
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentauthor): مؤلف التعليق

يسلط الكود أدناه الضوء على استخدام طريقة [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) لإضافة تعليق مترابط إلى الخلية A1. يرجى مراجعة [ملف Excel الناتج](89849859.xlsx) الذي تم إنشاؤه بواسطة الكود للمرجعية.

#### **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Threaded Comment</title>
    </head>
    <body>
        <h1>Add Threaded Comment Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            // Create a new workbook
            const workbook = new Workbook();

            // Add Author
            const authorIndex = workbook.worksheets.threadedCommentAuthors.add("Aspose Test", "", "");
            const author = workbook.worksheets.threadedCommentAuthors.get(authorIndex);

            // Add Threaded Comment to cell A1 in the first worksheet
            const worksheet = workbook.worksheets.get(0);
            worksheet.comments.addThreadedComment("A1", "Test Threaded Comment", author);

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddThreadedComments_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Threaded comment added successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **قراءة التعليقات المتداخلة**

### **قراءة التعليقات المتداخلة بإكسل**

لقراءة التعليقات المتداخلة في إكسل، ما عليك سوى تحريك الماوس فوق الخلية التي تحتوي على التعليقات لعرض التعليقات. ستبدو عرض التعليقات مثل العرض في الصورة التالية.

![todo:image_alt_text](threaded-comments_1.jpg)

### **قراءة التعليقات المتداخلة باستخدام Aspose.Cells**

يوفر Aspose.Cells [**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-) الأسلوب لاسترداد التعليقات الموجودة للعمود المحدد. [**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-) الأسلوب يقبل اسم العمود كمعلمة ويعيد [**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection). يمكنك التكرار فوق [**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection) لعرض التعليقات.

يوضح المثال التالي قراءة التعليقات من العمود A1 عن طريق تحميل [ملف Excel عينة](89849861.xlsx). يرجى الاطلاع على إخراج الكونسول الذي تم إنشاؤه بواسطة الكود للرجوع إليه.

#### **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Threaded Comments Example</title>
    </head>
    <body>
        <h1>Threaded Comments Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get Threaded Comments for cell A1
            const threadedComments = worksheet.comments.threadedComments("A1");

            const count = threadedComments.count;
            let html = '<h2>Threaded Comments</h2>';
            if (count === 0) {
                html += '<p>No threaded comments found for A1.</p>';
            } else {
                html += '<ul>';
                for (let i = 0; i < count; i++) {
                    const comment = threadedComments.get(i);
                    const notes = comment.notes;
                    const authorName = comment.author.name;
                    html += `<li><strong>Author:</strong> ${authorName} <br/><strong>Comment:</strong> ${notes}</li>`;
                }
                html += '</ul>';
            }

            resultDiv.innerHTML = html;
        });
    </script>
</html>
```

#### **مخرجات الوحدة**

{{< highlight javascript >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **قراءة الوقت الذي تم إنشاء التعليقات الموجهة**

توفر Aspose.Cells طريقة [**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-) لاسترجاع التعليقات المترابطة للعمود المحدد. طريقة [**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-) تقبل اسم العمود كمعامل وتعيد [**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection). يمكنك التكرار على [**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection) واستخدام الخاصية [**ThreadedComment.createdTime**](https://reference.aspose.com/cells/javascript-cpp/threadedcomment/#createdTime--).

يوضح المثال التالي قراءة الوقت الذي تم إنشاء التعليقات الموجهة من خلال تحميل [ملف Excel عينة](89849861.xlsx). يرجى الاطلاع على إخراج الكونسول الذي تم إنشاؤه بواسطة الكود للرجوع إليه.

#### **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Threaded Comments Example</title>
    </head>
    <body>
        <h1>Threaded Comments Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // No try-catch: allow errors to propagate for testing
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get Threaded Comments for cell A1
            const threadedComments = worksheet.comments.threadedComments("A1");

            const count = threadedComments.count;

            let html = '<h2>Threaded Comments (Cell A1)</h2>';
            if (count === 0) {
                html += '<p>No threaded comments found in cell A1.</p>';
            } else {
                html += '<ul>';
                for (let i = 0; i < count; i++) {
                    const comment = threadedComments.get(i);
                    const notes = comment.notes;
                    const authorName = comment.author.name;
                    const createdTime = comment.createdTime;

                    console.log("Comment: " + notes);
                    console.log("Author: " + authorName);
                    console.log("Created Time: " + createdTime);

                    html += `<li><strong>Author:</strong> ${authorName} <br/><strong>Created:</strong> ${createdTime} <br/><strong>Comment:</strong> ${notes}</li>`;
                }
                html += '</ul>';
            }

            resultDiv.innerHTML = html;

            // No file modifications or save in this example; hide download link
            downloadLink.style.display = 'none';
        });
    </script>
</html>
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

توفر Aspose.Cells طريقة [**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-) لاسترجاع التعليقات المترابطة للعمود المحدد. طريقة [**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-) تقبل اسم العمود كمعامل وتعيد [**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection). يمكنك تحديث التعليق المطلوب في [**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection) وحفظ المصنف.

 يُظهر المثال التالي تحرير أول تعليق متسلسل في العمود A1 بتحميل ملف إكسل النموذجي [ملف إكسل النموذجي](89849861.xlsx). يرجى الاطلاع على [ملف الإكسل الناتج](89849862.xlsx) الذي ينتجه الكود والذي يعرض التعليق المحدث للمرجعية.

#### **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Edit Threaded Comments Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get Threaded Comment from cell A1
            const comment = worksheet.comments.threadedComments("A1").get(0);

            // Update the threaded comment notes
            comment.notes = "Updated Comment";

            // Save the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'EditThreadedComments.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Edited Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Threaded comment updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **إزالة التعليقات المتداولة**

### **إزالة التعليقات المتداولة باستخدام Excel**

لإزالة التعليقات المتداولة في Excel، انقر بزر الماوس الأيمن على الخلية التي تحتوي على التعليقات وانقر على الخيار **حذف التعليق** كما هو موضح في الصورة التالية.

![todo:image_alt_text](threaded-comments_8.jpg)
