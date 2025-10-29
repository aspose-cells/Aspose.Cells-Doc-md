---
title: تعيين خصائص ScaleCrop وLinksUpToDate للخصائص المدمجة للمستند باستخدام JavaScript عبر C++
linktitle: ضبط خصائص ScaleCrop و LinksUpToDate لخصائص المستند المضمنة
type: docs
weight: 320
url: /ar/javascript-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: تعلم كيفية تعيين خصائص ScaleCrop وLinksUpToDate للخصائص المدمجة للمستند باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**
([BuiltInDocumentPropertyCollection.scaleCrop](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#scaleCrop--) و [BuiltInDocumentPropertyCollection.linksUpToDate](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#linksUpToDate--) هما خاصيتان موسعتان مدمجتان في المستند تم تعريفها داخل تنسيق OpenXml. والهدف من هذه الخصائص هو التالي.

## **1) ScaleCrop**
يشير هذا العنصر إلى وضع عرض الصورة المصغرة للمستند. قم بتعيين هذا العنصر إلى **TRUE** لتمكين تحجيم الصورة المصغرة للعرض. قم بتعيين هذا العنصر إلى **FALSE** لتمكين قص الصورة المصغرة لإظهار أقسام فقط تناسب العرض.

القيم الممكنة لهذا العنصر محددة بواسطة نوع البيانات البولياني لمخطط XML W3C.

## **2) LinksUpToDate**
يشير هذا العنصر إلى ما إذا كانت الروابط الفائقة في مستند محدثة. قم بتعيين هذا العنصر إلى **TRUE** للإشارة إلى أن الروابط الفائقة تم تحديثها. قم بتعيين هذا العنصر إلى **FALSE** للدلالة على أن الروابط الفائقة قديمة.

القيم الممكنة لهذا العنصر محددة بواسطة نوع البيانات البولياني لمخطط XML W3C.

## **لقطة شاشة تظهر هاتين الخاصيتين داخل ملف app.xml**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **ضبط خصائص ScaleCrop و LinksUpToDate لخصائص المستند المضمنة**
يحدد الكود النموذجي التالي خاصيتي المستند الموسعتين [BuiltInDocumentPropertyCollection.scaleCrop](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#scaleCrop--) و [BuiltInDocumentPropertyCollection.linksUpToDate](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#linksUpToDate--) للكتاب. يرجى التحقق من ملف إكسل الناتج [ملف الإخراج](5115500.xlsx) الذي تم إنشاؤه بهذا الكود، وتغيير امتداده إلى .zip واستخراج محتوياته وعرض app.xml كما هو موضح في لقطة الشاشة أعلاه.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Set BuiltIn Document Properties</h1>
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

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Accessing BuiltIn Document Properties and setting properties
            const builtInDocumentProperties = workbook.builtInDocumentProperties;
            // Setting ScaleCrop and LinksUpToDate BuiltIn Document Properties.
            builtInDocumentProperties.scaleCrop = true;
            builtInDocumentProperties.linksUpToDate = true;

            // Saving the Excel file.
            const outputData = workbook.save(SaveFormat.Auto);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
