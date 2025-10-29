---
title: ضبط الخط الافتراضي عند تحويل جدول البيانات إلى HTML باستخدام JavaScript عبر C++
linktitle: تعيين الخط الافتراضي أثناء تحويل جدول بيانات إكسل إلى HTML
type: docs
weight: 370
url: /ar/javascript-cpp/set-default-font-while-rendering-spreadsheet-to/
---

{{% alert color="primary" %}}
يتيح Aspose.Cells لك تعيين الخط الافتراضي أثناء تحويل جدول بيانات إكسل إلى HTML. يرجى استخدام [**HtmlSaveOptions.defaultFontName**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#defaultFontName--) لهذا الغرض. هذا الخاصية مفيدة عندما تكون هناك خلايا في جدول البيانات تحتوي على خطوط خطأ أو غير موجودة. ثم سيتم عرض تلك الخلايا بالخط المحدد بالخاصية [**HtmlSaveOptions.defaultFontName**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#defaultFontName--).
{{% /alert %}}

## تعيين الخط الافتراضي أثناء تحويل جدول بيانات إكسل إلى HTML

الكود العيني التالي يقوم بإنشاء دفتر عمل وإضافة نص معين في الخلية B4 من أول ورقة عمل ويقوم بتعيين خطه إلى خط غير معروف / غير موجود. ثم يقوم بحفظ الدفتر العمل بتنسيق HTML عن طريق تعيين أسماء خط مختلفة كـ Courier New, Arial, Times New Roman وما إلى ذلك.

تُظهر صورة لقطة الشاشة تأثير تعيين أسماء خطوط افتراضية مختلفة عبر خاصية [**HtmlSaveOptions.defaultFontName**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#defaultFontName--).

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-html_1.png)

يُولّد الكود ملف [HTML الناتج بخط Courier New](5115516), [HTML الناتج بخط Arial](5115518), و [HTML الناتج بخط Times New Roman](5115517).

## كود عينة

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink1" style="display: none;">Download Result 1</a><br/>
        <a id="downloadLink2" style="display: none;">Download Result 2</a><br/>
        <a id="downloadLink3" style="display: none;">Download Result 3</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Utils } = AsposeCells;

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
            // Creating a new workbook and accessing first worksheet.
            const wb = new Workbook();
            const ws = wb.worksheets.get(0);

            // Access cell B4 and add some text inside it.
            const cell = ws.cells.get("B4");
            cell.value = "This text has some unknown or invalid font which does not exist.";

            // Set the font of cell B4 which is unknown.
            const st = cell.style;
            st.font.name = "UnknownNotExist";
            st.font.size = 20;
            cell.style = st;

            // Prepare HtmlSaveOptions and save three variants with different default fonts.
            const opts = new HtmlSaveOptions();

            // 1) Default font Courier New
            opts.defaultFontName = "Courier New";
            const outputData1 = wb.save(SaveFormat.Html, opts);
            const blob1 = new Blob([outputData1], { type: "text/html" });
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'out_courier_new_out.htm';
            downloadLink1.style.display = 'block';
            downloadLink1.textContent = 'Download out_courier_new_out.htm';

            // 2) Default font Arial
            opts.defaultFontName = "Arial";
            const outputData2 = wb.save(SaveFormat.Html, opts);
            const blob2 = new Blob([outputData2], { type: "text/html" });
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'out_arial_out.htm';
            downloadLink2.style.display = 'block';
            downloadLink2.textContent = 'Download out_arial_out.htm';

            // 3) Default font Times New Roman
            opts.defaultFontName = "Times New Roman";
            const outputData3 = wb.save(SaveFormat.Html, opts);
            const blob3 = new Blob([outputData3], { type: "text/html" });
            const downloadLink3 = document.getElementById('downloadLink3');
            downloadLink3.href = URL.createObjectURL(blob3);
            downloadLink3.download = 'times_new_roman_out.htm';
            downloadLink3.style.display = 'block';
            downloadLink3.textContent = 'Download times_new_roman_out.htm';

            document.getElementById('result').innerHTML = '<p style="color: green;">Files generated successfully. Click the download links above to save the HTML files.</p>';
        });
    </script>
</html>
```
