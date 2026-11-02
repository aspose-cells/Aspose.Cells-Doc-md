---
title: تحويل Excel إلى تنسيق OFD
linktitle: تحويل Excel إلى تنسيق OFD
description: تُعد Aspose.Cells for JavaScript via C++ مكتبة JavaScript للعمل مع ملفات جداول البيانات، وتتيح تحويل مصنفات Excel إلى تنسيق OFD (مستند مفتوح ذو تخطيط ثابت). يوضح هذا المقال كيفية إنشاء محتوى Excel وتصديره بتنسيق OFD، وكذلك كيفية تحويل ملفات Excel الموجودة إلى OFD باستخدام Aspose.Cells.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, مكتبة JavaScript, جدول بيانات, تحويل Excel إلى OFD, تحويل OFD, SaveFormat.Ofd, مستند ذو تخطيط ثابت, تصدير مصنف
type: docs
weight: 195
url: /ar/javascript-cpp/converting-excel-to-ofd-format/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
يدعم Aspose.Cells تحويل مصنفات Excel مباشرةً إلى تنسيق OFD (مستند مفتوح ذو تخطيط ثابت) باستخدام قيمة التعداد `SaveFormat.Ofd`. يحافظ مستند OFD الناتج على التخطيط المرئي للمصنف ومحتواه، وعلى الخلايا المدمجة وعروض الأعمدة وارتفاعات الصفوف والخطوط والألوان والحدود وتنسيقات الأرقام. وهذا يجعل Aspose.Cells مناسبًا لسير عمل الأرشفة والطباعة والإيداعات التنظيمية والإيداعات الحكومية التي تتطلب ناتجًا ذا تخطيط ثابت.
{{% /alert %}}

## **مقدمة**
OFD (مستند مفتوح ذو تخطيط ثابت) هو معيار وطني صيني (GB/T 33190-2016) لتمثيل المستندات الرقمية ضمن تخطيط ثابت قائم على الصفحات. يؤدي دورًا مشابهًا لدور PDF في حالات الاستخدام التي يجب فيها الحفاظ على المظهر البصري للمستند المصدر تمامًا كما أُعدّ. ويُستخدم OFD على نطاق واسع في الإيداعات الحكومية والإيداعات التنظيمية والفواتير الإلكترونية والأرشفة طويلة الأجل في جمهورية الصين الشعبية.
يُعد تحويل مصنفات Excel إلى OFD متطلبًا شائعًا في السيناريوهات التي يجب فيها توزيع محتوى جدول البيانات كنتاج للقراءة فقط ذي تخطيط مقفل بدلاً من جدول بيانات قابل للتحرير. ومن الأمثلة إرسال فاتورة نهائية إلى عميل، أو أرشفة تقرير مالي ربع سنوي، أو تقديم جدول بيانات الميزانية إلى جهة تنظيمية. تتيح Aspose.Cells هذه القدرة من خلال قيمة التعداد `SaveFormat.Ofd`، التي تكتب المصنف مباشرةً بتنسيق OFD دون الحاجة إلى خطوة تحويل وسيطة. ويحافظ ناتج OFD على قيم الخلايا والنطاقات المدمجة والخطوط والألوان والحدود وتنسيقات الأرقام وخيارات إعداد الصفحة المضبوطة على المصنف.

{{% alert color="primary" %}}
يحافظ ناتج OFD الذي ينشئه Aspose.Cells على التخطيط المرئي للمصنف المصدر، بما في ذلك محتوى الخلايا والخلايا المدمجة وعروض الأعمدة وارتفاعات الصفوف. كما تُعرض تنسيقات الخلايا، مثل الخطوط والألوان والحدود والمحاذاة وتنسيقات الأرقام، في الناتج ذي التخطيط الثابت. وتؤثر خيارات إعداد الصفحة المضبوطة في ورقة العمل، مثل حجم الورق والاتجاه ومنطقة الطباعة، في تخطيط مستند OFD الناتج.
{{% /alert %}}

## **إنشاء مصنف Excel وحفظه بتنسيق OFD**
يتيح Aspose.Cells إنشاء مصنف برمجيًا، وتعبئته بالبيانات، ثم حفظه مباشرةً بتنسيق OFD باستخدام قيمة التعداد `SaveFormat.Ofd`. ينشئ المثال التالي فاتورة من الصفر، ويضيف إليها شعار الشركة ومعلومات الترويسة وقسم بيانات العميل وبنود الفاتورة والإجماليات المحسوبة، ثم يصدّر المصنف إلى مستند OFD.

### **إنشاء فاتورة مع شعار**
يبني المثال ورقة عمل الفاتورة عن طريق إدراج صورة الشعار في الجزء الأيسر العلوي، وتعبئة اسم الشركة وبيانات الاتصال، وإضافة عنوان "INVOICE" عبر خلايا مدمجة، وتسجيل رقم الفاتورة وتاريخها، وإدراج بيانات العميل الذي وُجّهت إليه الفاتورة، وبناء جدول بنود الفاتورة يتضمن أعمدة الوصف والكمية وسعر الوحدة والإجمالي، وحساب المجموع الفرعي والضريبة والإجمالي النهائي باستخدام صيغ الخلايا. وتُطبق تنسيقات مثل رؤوس الجدول الغامقة وتنسيق العملة للأسعار والحدود وعروض الأعمدة باستخدام كائنات `Style` و`Font`. وأخيرًا، يُحفظ المصنف بامتداد `.ofd` باستخدام `SaveFormat.Ofd`.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
        const { Workbook, Color } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            try {
                // إنشاء مصنف جديد
                const workbook = new Workbook();
                // الحصول على ورقة العمل الأولى
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                // تعيين عرض الأعمدة
                cells.setColumnWidth(0, 5);
                cells.setColumnWidth(1, 35);
                cells.setColumnWidth(2, 12);
                cells.setColumnWidth(3, 15);
                cells.setColumnWidth(4, 15);
                cells.setColumnWidth(5, 5);
                // إدراج شعار الشركة
                // إنشاء صورة PNG في الذاكرة لأن المتصفح لا يملك مسارًا لنظام الملفات.
                const logoCanvas = document.createElement("canvas");
                logoCanvas.width = 100;
                logoCanvas.height = 30;
                const logoContext = logoCanvas.getContext("2d");
                logoContext.fillStyle = "#000080";
                logoContext.fillRect(0, 0, logoCanvas.width, logoCanvas.height);
                logoContext.fillStyle = "#FFFFFF";
                logoContext.font = "bold 18px Arial";
                logoContext.fillText("ACME", 16, 21);
                const logoBlob = await new Promise(resolve => logoCanvas.toBlob(resolve, "image/png"));
                if (!logoBlob) {
                    throw new Error("Unable to create the company logo.");
                }
                const logoData = new Uint8Array(await logoBlob.arrayBuffer());
                worksheet.pictures.add(1, 1, logoData);
                // اسم الشركة وبيانات الاتصال
                cells.get("B3").value = "Acme Corporation";
                cells.get("B4").value = "123 Business Street";
                cells.get("B5").value = "City, State 12345";
                cells.get("B6").value = "Phone: (555) 123-4567";
                // عنوان الفاتورة - دمج الخلايا
                cells.merge(7, 1, 2, 4);
                const titleCell = cells.get("B8");
                titleCell.value = "INVOICE";
                const titleStyle = workbook.createStyle();
                titleStyle.font.isBold = true;
                titleStyle.font.size = 20;
                titleStyle.horizontalAlignment = AsposeCells.TextAlignmentType.Center;
                titleCell.style = titleStyle;
                // رقم الفاتورة والتاريخ
                cells.get("B11").value = "Invoice Number:";
                cells.get("C11").value = "INV-2024-001";
                cells.get("B12").value = "Date:";
                const now = new Date();
                const invoiceDate = [
                    now.getFullYear(),
                    String(now.getMonth() + 1).padStart(2, "0"),
                    String(now.getDate()).padStart(2, "0")
                ].join("-");
                cells.get("C12").value = invoiceDate;
                // قسم الفوترة
                cells.get("B14").value = "Bill To:";
                cells.get("B15").value = "Client Name";
                cells.get("B16").value = "Client Address";
                cells.get("B17").value = "Client City, State";
                // رأس بنود الفاتورة
                const headerDesc = cells.get("B19");
                const headerQty = cells.get("C19");
                const headerPrice = cells.get("D19");
                const headerTotal = cells.get("E19");
                headerDesc.value = "Description";
                headerQty.value = "Quantity";
                headerPrice.value = "Unit Price";
                headerTotal.value = "Total";
                const headerStyle = workbook.createStyle();
                headerStyle.font.isBold = true;
                headerStyle.font.color = Color.fromArgb(255, 255, 255);
                headerStyle.foregroundColor = Color.fromArgb(0, 0, 128);
                headerStyle.pattern = AsposeCells.BackgroundType.Solid;
                headerStyle.horizontalAlignment = AsposeCells.TextAlignmentType.Center;
                headerStyle.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                headerStyle.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                headerStyle.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                headerStyle.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                headerDesc.style = headerStyle;
                headerQty.style = headerStyle;
                headerPrice.style = headerStyle;
                headerTotal.style = headerStyle;
                // نمط العملة مع الحدود
                const currencyStyle = workbook.createStyle();
                currencyStyle.custom = '"$"#,##0.00';
                currencyStyle.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                currencyStyle.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                currencyStyle.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                currencyStyle.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                // نمط حدود بسيط لخلايا الوصف والكمية
                const borderStyle = workbook.createStyle();
                borderStyle.borders.get(AsposeCells.BorderType.TopBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                borderStyle.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                borderStyle.borders.get(AsposeCells.BorderType.LeftBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                borderStyle.borders.get(AsposeCells.BorderType.RightBorder).lineStyle = AsposeCells.CellBorderType.Thin;
                // صفوف بنود الفاتورة
                const lineItems = [
                    ["Product A - Widget", 2, 50.00],
                    ["Product B - Gadget", 3, 75.00],
                    ["Product C - Service", 1, 100.00]
                ];
                for (let i = 0; i < lineItems.length; i++) {
                    const row = 20 + i;
                    const descCell = cells.get(row, 1);
                    const qtyCell = cells.get(row, 2);
                    const priceCell = cells.get(row, 3);
                    const totalCell = cells.get(row, 4);
                    descCell.value = lineItems[i][0];
                    qtyCell.value = lineItems[i][1];
                    priceCell.value = lineItems[i][2];
                    totalCell.formula = "C" + (row + 1) + "*D" + (row + 1);
                    descCell.style = borderStyle;
                    qtyCell.style = borderStyle;
                    priceCell.style = currencyStyle;
                    totalCell.style = currencyStyle;
                }
                // المجموع الفرعي والضريبة والإجمالي الكلي
                cells.get("B24").value = "Subtotal:";
                const subtotalCell = cells.get("E24");
                subtotalCell.formula = "SUM(E21:E23)";
                cells.get("B25").value = "Tax (10%):";
                const taxCell = cells.get("E25");
                taxCell.formula = "E24*0.1";
                cells.get("B26").value = "Grand Total:";
                const grandTotalCell = cells.get("E26");
                grandTotalCell.formula = "E24+E25";
                // نمط عريض وعملة لقيم الإجماليات
                const totalStyle = workbook.createStyle();
                totalStyle.font.isBold = true;
                totalStyle.custom = '"$"#,##0.00';
                subtotalCell.style = totalStyle;
                taxCell.style = totalStyle;
                grandTotalCell.style = totalStyle;
                // نمط عريض لتسميات الإجماليات
                const boldStyle = workbook.createStyle();
                boldStyle.font.isBold = true;
                cells.get("B24").style = boldStyle;
                cells.get("B25").style = boldStyle;
                cells.get("B26").style = boldStyle;
                // حفظ المصنف كملف OFD
                const outputData = workbook.save(AsposeCells.SaveFormat.Ofd);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "Invoice.ofd";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                document.getElementById('result').innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
        </script>
    </body>
</html>
```

## **تحويل ملف Excel موجود إلى OFD**
يمكن لـ Aspose.Cells أيضًا تحميل مصنف Excel موجود من القرص وتصديره مباشرةً بتنسيق OFD. وهذا مفيد في مسارات التحويل الدفعي وسير عمل الأرشفة، وفي السيناريوهات التي أُنتج فيها المصنف المصدر بواسطة أداة أخرى ولا يلزم فيها سوى إعادة تصديره في صورة ناتج ذا تخطيط ثابت. يحمّل المثال التالي مصنف `.xlsx` موجودًا، ويقرأ البيانات من خلاياه، ويطبق تعديلات اختيارية على إعدادات الصفحة، ثم يحفظ النتيجة كمستند OFD.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, CellsHelper } = AsposeCells;
            const fileInput = document.getElementById("fileInput");
            const runButton = document.getElementById("runExample");
            const downloadLink = document.getElementById("downloadLink");
            const result = document.getElementById("result");
            const readyPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            function formatTimestamp(date) {
                const pad = value => String(value).padStart(2, "0");
                return date.getFullYear() + "-" +
                    pad(date.getMonth() + 1) + "-" +
                    pad(date.getDate()) + " " +
                    pad(date.getHours()) + ":" +
                    pad(date.getMinutes()) + ":" +
                    pad(date.getSeconds());
            }
            function escapeHtml(value) {
                const entities = {
                    "&": "&amp;",
                    "<": "&lt;",
                    ">": "&gt;",
                    '"': "&quot;",
                    "'": "&#39;"
                };
                return String(value).replace(/[&<>"']/g, character => entities[character]);
            }
            runButton.addEventListener("click", async () => {
                try {
                    const file = fileInput.files[0];
                    if (!file) {
                        result.innerHTML = '<p style="color: red;">Please select an Excel file first.</p>';
                        return;
                    }
                    runButton.disabled = true;
                    downloadLink.style.display = "none";
                    downloadLink.removeAttribute("href");
                    // فتح مصنف Excel موجود من القرص
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    // (1) قراءة وعرض قيم الخلايا المحددة للتأكد من تحميل الملف
                    const firstSheet = workbook.worksheets.get(0);
                    const cells = firstSheet.cells;
                    const output = [];
                    output.push("First sheet name: " + firstSheet.name);
                    output.push("Cell A1: " + cells.get("A1").stringValue);
                    output.push("Cell B1: " + cells.get("B1").stringValue);
                    output.push("Cell C1: " + cells.get("C1").stringValue);
                    // (2) التكرار على مجموعة Worksheets لتعداد أوراق العمل المتاحة
                    output.push("");
                    output.push("Available worksheets:");
                    for (let i = 0; i < workbook.worksheets.count; i++) {
                        const ws = workbook.worksheets.get(i);
                        output.push("  [" + i + "] " + ws.name);
                    }
                    // (3) تحديث اختياري لخلية الطابع الزمني ليعكس وقت التحويل
                    cells.get("A1").value = "Converted on: " + formatTimestamp(new Date());
                    // إضافة صف رأس ملخص في أعلى كتلة البيانات
                    cells.insertRow(0);
                    cells.get("A1").value = "Conversion Summary";
                    cells.get("A2").value = "Generated: " + formatTimestamp(new Date());
                    // (4) تكوين خصائص PageSetup على ورقة العمل
                    const pageSetup = firstSheet.pageSetup;
                    pageSetup.orientation = AsposeCells.PageOrientationType.Landscape;
                    pageSetup.paperSize = AsposeCells.PaperSizeType.PaperA4;
                    pageSetup.fitToPagesTall = 1;
                    pageSetup.fitToPagesWide = 1;
                    // (5) تعيين منطقة الطباعة اختياريًا لمخرجات OFD
                    const lastRow = cells.maxDataRow;
                    const lastCol = cells.maxDataColumn;
                    const lastColLetter = CellsHelper.columnIndexToName(lastCol);
                    const printArea = "A1:" + lastColLetter + (lastRow + 1);
                    pageSetup.printArea = printArea;
                    output.push("");
                    output.push("Print area set to: " + printArea);
                    // (6) حفظ المصنف كملف OFD
                    const outputData = workbook.save(AsposeCells.SaveFormat.Ofd);
                    const blob = new Blob([outputData]);
                    downloadLink.href = URL.createObjectURL(blob);
                    downloadLink.download = "SampleBook.ofd";
                    downloadLink.textContent = "Download SampleBook.ofd";
                    downloadLink.style.display = "block";
                    output.push("");
                    output.push("File successfully converted to OFD format: SampleBook.ofd");
                    result.innerHTML =
                        '<pre style="white-space: pre-wrap;">' +
                        escapeHtml(output.join("\n")) +
                        "</pre>" +
                        '<p style="color: green;">Done! Click the download link to get the result file.</p>';
                } catch (error) {
                    console.error(error);
                    const message = error && error.message ? error.message : String(error);
                    result.innerHTML = '<p style="color: red;">Error: ' + escapeHtml(message) + "</p>";
                } finally {
                    runButton.disabled = false;
                }
            });
        </script>
    </body>
</html>
```

## **مقالات ذات صلة**
- [إدراج صورة في خلية](/cells/ar/javascript-cpp/inserting-an-image-into-a-cell/)

{{< app/cells/assistant language="javascript-cpp" >}}