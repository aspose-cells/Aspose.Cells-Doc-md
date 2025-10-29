---
title: تحويل ملف Excel إلى صيغة PDF متوافقة مع PDF/A 1a باستخدام JavaScript عبر C++
linktitle: تحويل ملف إكسل إلى تنسيق PDF متوافق مع PDF/A 1a
type: docs
weight: 130
url: /ar/javascript-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: تعلم كيفية تحويل ملفات Excel إلى ملفات PDF متوافقة مع PDF/A باستخدام Aspose.Cells for Java سكربت عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**  

PDF/A هو نوع فريد من PDF مصمم للحفاظ على المستندات على المدى الطويل. PDF/A هو نسخة معيارية من معيار ISO لملف المستندات المنقولة (PDF) والذي يتضمن جميع الخطوط المستخدمة في المستند داخل ملف PDF. يختلف PDF/A عن PDF بحظر بعض الميزات، مثل ربط الخطوط (على عكس تضمين الخطوط) والتشفير. يتيح لك سكربت Aspose.Cells for Java عبر C++ حفظ ملفات Excel كملفات PDF متوافقة مع PDF/A (يدعم PDF/A-1a، PDF/A-1b، PDF/A-2a، PDF/A-2b، PDF/A-2u، PDF/A-3a، PDF/A-2ab، و PDF/A-3u). يصف هذا الموضوع كيفية حفظ دفتر العمل Excel إلى ملف PDF متوافق مع PDF/A (PDF/A-1a).  

## **تحويل ملف Excel إلى تنسيق PDF متوافق مع PDF/A-1a**  

يمكن للمطورين استخدام فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) لضبط سمات مختلفة للتحويل. ضبط خصائص مختلفة من فئة [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) يمنحك السيطرة على إعدادات الطباعة، الخط، الأمان، والضغط لملف PDF الناتج. الخاصية الأهم هي [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#compliance--) التي تمكنك من حفظ ملفات Excel إلى ملفات PDF / A متوافقة.  

يشرح الكود النموذجي التالي كيفية تحويل ملف Excel إلى صيغة PDF متوافقة مع PDF/A-1a. يرجى الاطلاع على [ملف PDF الناتج](outputCompliancePdfA1a.pdf) والصورة الملتقطة للشاشة لمزيد من المعلومات.  

## **لقطة شاشة**  

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)  

## **الكود المثالي**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export to PDF (PDFA-1a) Example</h1>
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
            // Create workbook object
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access cell B5 and add some message inside it
            const cell = ws.cells.get("B5");
            cell.value = "This PDF format is compatible with PDFA-1a.";

            // Create pdf save options and set its compliance to PDFA-1a
            const opts = new AsposeCells.PdfSaveOptions();
            opts.compliance = AsposeCells.PdfCompliance.PdfA1a;

            // Save the output pdf
            const outputData = wb.save(SaveFormat.Pdf, opts);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCompliancePdfA1a.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
