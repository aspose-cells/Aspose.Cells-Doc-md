---
title: تعيين رؤوس وتذييلات مع JavaScript عبر C++
linktitle: ضبط رؤوس وأسافل
type: docs
weight: 30
url: /ar/javascript-cpp/setting-headers-and-footers/
description: يوضح هذا المقال كيفية إدراج صورة برمجيًا في رأس وتذييل أوراق عمل Excel باستخدام Aspose.Cells for JavaScript عبر C++. 
keywords: إدراج صورة في رأس وتذييل Excel JavaScript عبر C++, تعيين أوامر نصوص الرأس والتذييل في Excel JavaScript عبر C++
---

{{% alert color="primary" %}}

رؤوس وأسافل هي سطور النص المعروضة أسفل هامش الأعلى أو أعلى الهامش على التوالي. يمكن إضافة رؤوس وأسافل إلى الأوراق العمل أيضًا. يمكن استخدام رؤوس وأسافل لعرض معلومات مفيدة مثل رقم الصفحة أو اسم المؤلف أو اسم الموضوع أو التاريخ والوقت. يتم إدارة الرؤوس والأسافل باستخدام إعدادات تخطيط الصفحة.

{{% /alert %}}

## **ضبط رؤساء الصفحات وتذايلها**

يمكن لـ Aspose.Cells for JavaScript عبر C++ إضافة رؤوس وتذييلات لأوراق العمل في وقت التشغيل لكن نوصي بضبط الرؤوس والتذييلات يدويًا في ملف مصمم مسبقًا للطباعة. يمكنك استخدام Microsoft Excel كأداة رسومية لضبط الرؤوس والتذييلات لتوفير الجهد ووقت التطوير. يمكن لـ Aspose.Cells استيراد الملف وحفظ الإعدادات.

لإضافة رؤوس وتذييلات بناءً على النموذج، يوفر Aspose.Cells استدعاءات API خاصة وأوامر سكريبت لتنسيق الرؤوس والتذييلات.

### **أوامر السكريبت**

أوامر السكريبت هي أوامر خاصة تسمح لك بتعيين تنسيقات الرأس والتذييل.

| **أوامر السكريبت** | **الوصف** |
| :- | :- |
|&P| - رقم الصفحة الحالية
|&G| - صورة
|&N| - مجموع عدد الصفحات
|&D| - التاريخ الحالي
|&T| - الوقت الحالي
|&A| - اسم ورقة العمل
|&F| - اسم الملف بدون مساره
|&&Text|يعرض &Text. على سبيل المثال: &&WO سيتم عرضه كـ &WO|
|&"\<FontName>"| - يمثل اسم الخط. على سبيل المثال: &"Arial"
|&"\<FontName>, \<FontStyle>"| - يمثل اسم الخط بالنمط. مثال: &"Arial,Bold"
|&\<FontSize>| - يمثل حجم الخط. على سبيل المثال: “&14abc”. ولكن، إذا تبعت هذه الأمر برقم عادي يتم طباعته في الرأس، يجب أن يتم فصله بحرف مسافة عن حجم الخط. على سبيل المثال: “&14 123”.

### **تعيين رؤوس وتذييلات**

 توفر فئة [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) طريقتين، [**header(number, string)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#header-number-string-) و [**footer(number, string)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footer-number-string-)، لإضافة رأس وتذييل إلى ورقة عمل. تأخذ هذه الطرق وسيطين فقط:

- **القسم** – القسم الذي يجب وضع الرأس أو التذيل فيه. هناك ثلاثة أقسام: اليسار، الوسط، واليمين، يُمثلون بالترتيب 0، 1، و2.
- **السكريبت** – السكريبت الذي يجب استخدامه للرأس أو التذيل. يتضمن هذا السكريبت أوامر سكريبت لتنسيق الرؤوس أو التذيلات.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Set Headers and Footers Example</h1>
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
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Obtaining the reference of the PageSetup of the first worksheet
            const worksheet = workbook.worksheets.get(0);
            const pageSetup = worksheet.pageSetup;

            // Setting worksheet name at the left section of the header
            pageSetup.header = pageSetup.header || [];
            pageSetup.header[0] = "&A";

            // Setting current date and current time at the central section of the header
            // and changing the font of the header
            pageSetup.header[1] = "&\"Times New Roman,Bold\"&D-&T";

            // Setting current file name at the right section of the header and changing the
            // font of the header
            pageSetup.header[2] = "&\"Times New Roman,Bold\"&12&F";

            // Setting a string at the left section of the footer and changing the font
            // of a part of this string ("123")
            pageSetup.footer = pageSetup.footer || [];
            pageSetup.footer[0] = "Hello World! &\"Courier New\"&14 123";

            // Setting the current page number at the central section of the footer
            pageSetup.footer[1] = "&P";

            // Setting page count at the right section of footer
            pageSetup.footer[2] = "&N";

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetHeadersAndFooters_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Headers and footers set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **إدراج صورة في رأس أو تذيل**

 تحتوي فئة [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) على طريقتين إضافيتين، [**headerPicture(number, number[])**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#headerPicture-number-numberarray-) و [**footerPicture(number, number[])**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footerPicture-number-numberarray-)، لإضافة الصور إلى الرأس والتذييل. تأخذ هذه الطرق المعلمات:

- **القسم** – القسم الخطوط العليا أو السفلية حيث سيتم وضع الصورة. هناك ثلاثة أقسام، اليمين، الوسط واليسار، يُمثلها القيم 0، 1 و 2 على التوالي.
- **مصفوفة بايت** – البيانات الرسومية (يجب كتابة البيانات الثنائية في مخزن مصفوفة بايت).

بعد تنفيذ الكود أدناه وفتح الملف، تحقق من رأس الصفحة في ورقة العمل عن طريق:

1. في قائمة **ملف**, حدد **إعداد الصفحة**. سيتم عرض مربع حواري.
1. حدد علامة التبويب **رأس / تذييل**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Insert Image in Header/Footer Example</title>
    </head>
    <body>
        <h1>Insert Image in Header/Footer Example</h1>
        <p>Select an existing Excel file to modify (optional). If none is selected, a new workbook will be used.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <p>Select an image to insert into the header:</p>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Insert Image into Header</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file to insert into the header.</p>';
                return;
            }

            // Read image bytes
            const imageFile = imageInput.files[0];
            const imageBuffer = await imageFile.arrayBuffer();
            const binaryData = new Uint8Array(imageBuffer);

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const excelFile = fileInput.files[0];
                const excelBuffer = await excelFile.arrayBuffer();
                workbook = new Workbook(new Uint8Array(excelBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet's page setup
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Set the header picture and header scripts (converted from setters to properties)
            pageSetup.headerPicture = binaryData;
            pageSetup.header = "&G";
            pageSetup.header = "&A";

            // Save the workbook as Excel97-2003 (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'InsertImageInHeaderFooter_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Image inserted into header successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
