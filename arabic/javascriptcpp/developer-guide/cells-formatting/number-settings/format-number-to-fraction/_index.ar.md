---
title: كيفية تنسيق الرقم إلى كسر
type: docs
weight: 10
url: /ar/javascript-cpp/how-to-format-number-to-fraction/
description: سيقدم هذا المقال كيفية تنسيق الرقم إلى كسر باستخدام API Script عبر C++.
keywords: تحويل رقم إلى تمثيل كسر، تحويل رقم إلى معادلته الكسرية، تغيير رقم إلى شكله الكسر المقابل، تنسيق قيمة رقمية إلى كسر، التعبير عن رقم على أنه كسر، تنسيق الرقم إلى كسر
---

## **سيناريوهات الاستخدام المحتملة**
تنسيق الأرقام إلى الكسور في إكسل مفيد لعدة أسباب، خاصة عندما تعمل مع بيانات تُعبر بشكل طبيعي عن طريق الكسور أو عندما تحتاج إلى إجراء عمليات تتضمن الكسور. إليك بعض الأسباب الرئيسية التي قد تجعلك ترغب في تنسيق الأرقام ككسور في إكسل:

1. **الوضوح والدقة**: يمكن أن تعبر الكسور أحيانًا عن المعلومات بشكل أكثر وضوحًا ودقة من الأعداد العشرية. على سبيل المثال، في الوصفات أو القياسات، فإن 1/2 كوب أو 3/4 إنش يكون أكثر فهمًا من 0.5 كوب أو 0.75 إنش. يمكن أن يجعل تنسيق الأرقام ككسور البيانات أسهل للقراءة والفهم للجمهور المستهدف.

2. **الدقة**: عند التعامل مع قيم دقيقة، يمكن للكسور أن تمثل الكميات بدقة أكبر من الأعداد العشرية التي قد تتطلب تقريبًا. على سبيل المثال، لا يمكن التعبير بدقة عن 1/3 كعدد عشري لكنه يمكن التعبير عنه بشكل دقيق ككسر.

3. **العمليات الرياضية**: في بعض الحالات، قد تحتاج إلى إجراء عمليات حسابية باستخدام الكسور، والحفاظ على الأرقام في شكل كسر يمكن أن يجعل هذه العمليات أكثر سهولة. على سبيل المثال، الجمع بين 1/2 و 1/4 أسهل وأكثر وضوحًا من جمع 0.5 و 0.25، خاصة إذا كنت تقوم بالحساب بدون آلة حاسبة.

4. **الأغراض التعليمية**: عند تعليم أو دراسة الكسور، من المفيد العمل مع الكسور الفعلية بدلاً من النظيرات العشرية لها. يمكن أن يكون قدرة إكسل على تنسيق الأرقام ككسور أداة قيمة في البيئات التعليمية.

5. **المعايير الصناعية**: قد تفضل بعض الصناعات أو المهن استخدام الكسور بدلاً من الأعداد العشرية. على سبيل المثال، البناء، والنجارة، وفنون الطهي غالبًا تستخدم القياسات الكسرية. يمكن أن يساعد استخدام الكسور في إكسل على الحفاظ على التناسق مع المعايير الصناعية.

6. **الجاذبية البصرية**: في بعض الوثائق أو العروض التقديمية، قد تكون الكسور أكثر جاذبية بصريًا أو مناسبة من الأعداد العشرية. هذا صحيح بشكل خاص في الوثائق الرسمية، والتقارير، أو عند محاولة مطابقة نمط تنسيق معين.

يجعل إكسل من السهل تنسيق الأرقام ككسور، ويوفر عدة نماذج للكسور للاختيار من بينها، بما في ذلك كسور ذات رقم واحد، وكسور حتى رقمين، وحتى كسور مكتوبة. تتيح هذه المرونة للمستخدمين تقديم بياناتهم بأكثر الطرق ملاءمة وفهمًا لاحتياجاتهم الخاصة.

## **كيفية تنسيق الرقم إلى كسر في إكسل**
تعد عملية تنسيق الأرقام ككسور في إكسل سهلة وبدون تعقيد، حيث تمكنك من عرض بياناتك بطريقة أكثر معنى، خاصة عند التعامل مع كميات غير أرقام كاملة. إليك كيفية تنسيق الأرقام ككسور في إكسل:

### باستخدام مربع حوار تنسيق الخلايا

1. **اختيار الخلايا**: أولاً، حدد الخلايا التي تريد تنسيقها ككسور. يمكنك النقر وسحب لتحديد العديد من الخلايا، أو النقر على خلية واحدة إذا كنت تنسيق خلية واحدة فقط.

2. **فتح مربع حوار تنسيق الخلايا**: مع تحديد الخلايا، انقر بزر الماوس الأيمن على واحدة من الخلايا المحددة واختر `تنسيق الخلايا` من القائمة السياقية. بدلاً من ذلك، يمكنك الضغط على `Ctrl + 1` على لوحة المفاتيح لفتح مربع حوار تنسيق الخلايا.

3. **اختيار نمط الكسر**: في مربع حوار تنسيق الخلايا، انتقل إلى علامة التبويب `الأرقام`. على الجانب الأيسر، سترى قائمة الفئات. اختر `كسر`.

4. **اختيار نوع الكسر**: على الجانب الأيمن، تحت قسم `النوع`، ستجد مجموعة من تنسيقات الكسر. يوفر إكسل العديد من نماذج الكسر المعرفة مسبقًا، بما في ذلك:
   - حتى رقم واحد (1/4)
   - حتى رقمين (21/25)
   - حتى ثلاثة أرقام (312/943)
   - كنصف (1/2)
   - كرباعيات (2/4)
   - كعشريات (4/8)
   - كسور ست عشرية (8/16)
   - كبعشريات (3/10)
   - مئات (30/100)

   اختر الأنسب لبياناتك. إذا لم تكن متأكدًا، فإن "حتى رقم واحد (1/4)" هو خيار عام جيد للعديد من التطبيقات.

5. **تطبيق التنسيق**: بعد اختيار نمط الكسر المطلوب، انقر على `موافقة` لتطبيق التنسيق على الخلايا المحددة.

### باستخدام الشريط

بدلاً من ذلك، يمكنك استخدام الشريط لتطبيق بعض تنسيقات الكسور بسرعة:

1. **اختيار الخلايا**: حدد الخلايا التي تريد تنسيقها.

2. **التوجه إلى علامة التبويب الصفحة الرئيسية**: على الشريط، انتقل إلى علامة التبويب `الصفحة الرئيسية`.

3. **فتح قائمة تنسيق الرقم**: في مجموعة `الرقم`، ستجد قائمة منسدلة لتنسيقات الأرقام. انقر عليها.

4. **اختيار الكسر**: سترى بعض التنسيقات الشائعة مباشرة في القائمة المنسدلة، بما في ذلك بعض خيارات الكسور. إذا رأيت تنسيق الكسر الذي تريده، يمكنك اختياره مباشرة هنا. إذا لم تجده، اختر `مزيد من تنسيقات الأرقام...` في أسفل القائمة واتبع الخطوات المذكورة في قسم مربع حوار تنسيق الخلايا أعلاه.

### نصائح

- **الكسور المخصصة**: إذا لم تلبي الصيغ المعروفة مسبقًا احتياجاتك، يمكنك إنشاء صيغة كسر مخصصة عن طريق اختيار `مخصص` في مربع حوار تنسيق الخلايا وإدخال رمز الصيغة المخصص الخاص بك.
- **الدقة**: عند تنسيق رقم ككسر، يُحوّل إكسل الرقم إلى أقرب كسر استنادًا إلى التنسيق الذي اخترته. وقد لا يكون هذا دائمًا دقيقًا تمامًا للأكاسير المعقدة أو الأرقام العشرية التي تحتوي على العديد من الأرقام.

باتباع هذه الخطوات، يمكنك تنسيق الأرقام بشكل فعال ككسور في إكسل، مما يسهل قراءة البيانات وتفسيرها.

## **كيفية تنسيق الرقم إلى كسر في Script عبر C++**
تكوين الأرقام إلى كسر في Script عبر C++ هو عملية مباشرة. أسموغ.Cells هي مكتبة قوية تتيح لك العمل مع ملفات إكسل في تطبيقات جافا سكريبت دون الحاجة إلى تثبيت Microsoft Excel. توفر مجموعة واسعة من الميزات، بما في ذلك تنسيق الأرقام ككسر.

إليك دليل خطوة بخطوة حول كيفية تنسيق الأرقام إلى كسر في Script عبر C++:

### الخطوة 1: تثبيت Aspose.Cells for JavaScript عبر C++

أولاً، تأكد من أن لديك مرجعاً لـ Aspose.Cells for JavaScript عبر C++ في مشروعك. يمكنك الحصول عليه من موقع Aspose.

### الخطوة 2: إنشاء مصنف جديد أو فتح مصنف موجود

يمكنك إما إنشاء مصنف جديد أو فتح واحد موجود.

### الخطوة 3: الوصول إلى ورقة العمل

تحتاج إلى الوصول إلى ورقة العمل التي تريد تنسيق الأرقام فيها. إذا كنت تعمل مع دفتر عمل جديد، فمن المحتمل أن تكون مع الورقة الأولى.

### الخطوة 4: تطبيق تنسيق الرقم الكسري

لتنسيق خلية ككسر، تحتاج إلى استخدام خاصية `number` من كائن Style لتعيين رمز تنسيق رقم معين. يدعم Aspose.Cells تنسيقات الكسر المختلفة، مثل "1/2"، "1/4"، "2/4"، وغيرها.

### الخطوة 5: حفظ المصنف

بعد تطبيق تنسيق الكسر، احفظ دفتر العمل إلى ملف:

### مثال على الكود

إليك مقتطف من كود يوضح هذه الخطوات:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells: Format Cell as Fraction Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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
            if (!fileInput.files.length) {
                // No file selected - create a new workbook as in the original JavaScript code
                const workbook = new Workbook();

                // Access the first worksheet
                const worksheet = workbook.worksheets.get(0);

                // Access the cell you want to format
                const cell = worksheet.cells.get("A1");

                // Set the cell value
                cell.value = 0.5;

                // Get the style of the cell
                const style = cell.style;

                // Set the number format to fraction (e.g., "# ?/?")
                style.custom = "# ?/?";

                // Apply the style to the cell
                cell.style = style;

                // Save the workbook and provide download
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'output.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and formatted successfully! Click the download link to get the file.</p>';
                return;
            }

            // If a file is selected, open and modify it
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the cell you want to format
            const cell = worksheet.cells.get("A1");

            // Set the cell value
            cell.value = 0.5;

            // Get the style of the cell
            const style = cell.style;

            // Set the number format to fraction (e.g., "# ?/?")
            style.custom = "# ?/?";

            // Apply the style to the cell
            cell.style = style;

            // Save the workbook and provide download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File processed and formatted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### ملاحظات إضافية

- تتيح لك خاصية `custom` من كائن النمط تحديد تنسيق الكسر بدقة. على سبيل المثال، يمكن أن يعرض "# ??/???" كسوراً مع ما يصل إلى ثلاثة أرقام في المقام.
- يدعم Aspose.Cells مجموعة واسعة من تنسيقات الأرقام، بما في ذلك العشرية، والنسبة المئوية، والعملات، وأكثر. يمكنك تخصيص التنسيق لتلبية متطلباتك الخاصة.

باتباع هذه الخطوات، يمكنك بسهولة تنسيق الأرقام ككسور في Aspose.Cells for JavaScript عبر C++. هذا قد يكون مفيدًا بشكل خاص للتطبيقات المالية أو الإحصائية أو التعليمية حيث تكون القيم الكسريّة الدقيقة ضرورية.
