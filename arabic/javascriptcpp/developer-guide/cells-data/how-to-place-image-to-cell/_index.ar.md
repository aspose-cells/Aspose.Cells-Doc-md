---
title: كيفية إدراج صورة في الخلية
type: docs
weight: 130
url: /ar/javascript-cpp/how-to-insert-picture-in-cell/
description: تعلم كيفية إدراج صورة في خلية باستخدام Aspose.Cells for Javaسكريبت عبر C++.
keywords: كيفية إدراج صورة في الخلية، إدراج الصورة فوق الخلايا، وضع الصورة في الخلية، وضع الصورة فوق الخلايا، كيفية وضع الصورة في الخلية، كيفية وضع الصورة فوق الخلايا، التبديل بين الصورة في الخلية والصورة فوق الخلايا، التبديل بين الوضع في الخلية والوضع فوق الخلايا.
---

## **سيناريوهات الاستخدام المحتملة**
تضيف الصورة لمسة من السطوع إلى جدول البيانات الخاص بك وتوفر تمثيلًا بصريًا للمحتوى. كما تجعل من السهل عليك فهم البيانات واستخلاص الأفكار. على الرغم من أنك كنت قادرًا على استخدام الصور في Excel لسنوات عديدة، إلا أن Excel قام مؤخرًا فقط بتمكين ميزة تحويل الصور إلى قيم خلية فعلية. حتى إذا تم تعديل تخطيط الرسم، سيظل مرتبطًا بالبيانات. يمكنك استخدامه في الجداول والفرز والتصفية وتضمينه في الصيغ وما إلى ذلك!

## **كيفية إدراج الصورة في خلية باستخدام Excel**
حول كيفية إدراج صورة في خلية في Excel، اتبع هذه الخطوات:

1. انتقل إلى علامة التبويب الإدراج وانقر على خيار الصور.
2. حدد **وضع في الخلية**. حدد أحد المصادر التالية من القائمة المنسدلة إدراج صورة من(**هذا الجهاز**، **صور الأسهم** و **صور عبر الإنترنت**). هذا الجهاز لإدراج الصورة من جهازك. صور الأسهم لإدراج صورة من صور الأسهم. صور عبر الإنترنت لإدراج صورة من الويب.
<br>
<img src="1.png" width=60% />
3. حدد الصورة وأدرجها في خلية.
<br>
<img src="8.png" width=60% />

## **كيفية إدراج الصورة فوق الخلايا باستخدام Excel**
حول كيفية إدراج صورة فوق الخلايا في Excel، اتبع هذه الخطوات:

1. انتقل إلى علامة التبويب الإدراج وانقر على خيار الصور.
2. حدد **وضع فوق الخلايا**. حدد أحد المصادر التالية من القائمة المنسدلة إدراج صورة من(**هذا الجهاز**، **صور الأسهم** و **صور عبر الإنترنت**). هذا الجهاز لإدراج الصورة من جهازك. صور الأسهم لإدراج صورة من صور الأسهم. صور عبر الإنترنت لإدراج صورة من الويب.
<br>
<img src="2.png" width=60% />
3. حدد الصورة وأدرجها فوق الخلايا.
<br>
<img src="3.png" width=60% />

## **كيفية التبديل من الصورة في الخلية إلى الصورة فوق الخلايا باستخدام Excel**
يمكنك بسهولة التبديل من **الصورة في الخلية** إلى **الصورة فوق الخلايا**. يرجى اتباع هذه الخطوات:
1. انقر بزر الماوس الأيمن على الخلية وحدد **الصورة في الخلية** > **وضع فوق الخلايا**. 
<br>
<img src="4.png" width=60% />
2. النتيجة بعد التبديل كما يلي:
<br>
<img src="5.png" width=60% />

## **كيفية التبديل من الصورة فوق الخلايا إلى الصورة في الخلية باستخدام Excel**
يمكنك بسهولة التبديل من **الصورة فوق الخلايا** إلى **الصورة في الخلية**. يرجى اتباع هذه الخطوات:
1. انقر بزر الماوس الأيمن على الصورة وحدد **وضع في الخلية**. 
<br>
<img src="6.png" width=60% />
2. النتيجة بعد التبديل كما يلي:
<br>
<img src="7.png" width=60% />

## **كيفية إدراج صورة في خلية باستخدام Aspose.Cells for Javaسكريبت عبر C++**
إدراج صورة في الخلية باستخدام Aspose.Cells. يرجى الاطلاع على الكود المثالي التالي. بعد تنفيذ كود العينة، سيتم إدراج صورة في خلية.
1. قم بإنشاء كائن ورق العمل. 
2. احصل على الخلية التي ترغب في إدراج الصورة فيها.
3. ضبط خاصية الصورة المضمنة في الخلية. 
4. أخيرًا، يحفظ الدفتر بتنسيق [XLSX الناتج](out.xlsx). 

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Embed Image into New Workbook</h1>
        <p>Select an image file to embed into cell D8. A new workbook will be created with "Apple" in A2.</p>
        <input type="file" id="imageInput" accept="image/*" />
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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');

            // Create a new workbook
            const workbook = new Workbook();
            const cells = workbook.worksheets.get(0).cells;

            // Set A2 value to "Apple"
            const a2 = cells.get("A2");
            a2.value = "Apple";

            // Get D8 cell
            const d8 = cells.get("D8");

            // If an image file is selected, read it and embed into D8
            if (imageInput.files.length) {
                const file = imageInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                const imgBuf = new Uint8Array(arrayBuffer);
                d8.embeddedImage = imgBuf;
            }

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
