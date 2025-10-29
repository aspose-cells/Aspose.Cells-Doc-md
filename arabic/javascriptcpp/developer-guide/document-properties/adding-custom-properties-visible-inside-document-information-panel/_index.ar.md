---
title: إضافة خصائص مخصصة مرئية داخل لوحة معلومات معلومات المستند باستخدام JavaScript عبر C++
linktitle: إضافة خصائص مخصصة مرئية داخل لوحة معلومات المستند
type: docs
weight: 300
url: /ar/javascript-cpp/adding-custom-properties-visible-inside-document-information-panel/
description: تعلم كيفية إضافة خصائص مخصصة إلى كائن دفتر العمل باستخدام Aspose.Cells for JavaScript عبر C++. يمكن عرض هذه الخصائص في لوحة معلومات معلومات المستند.
---

## **إضافة خصائص مخصصة مرئية داخل لوحة معلومات الوثيقة**

 يمكن استخدام Aspose.Cells for JavaScript عبر C++ لإضافة خصائص مخصصة داخل كائن دفتر العمل والتي تكون مرئية داخل لوحة معلومات معلومات المستند. يمكنك فتح لوحة المعلومات في Microsoft Excel باستخدام أوامر قائمة ملف > معلومات > خصائص > عرض لوحة المستند.

 يرجى استخدام طريقة [**ContentTypePropertyCollection.add(string, string)**](https://reference.aspose.com/cells/javascript-cpp/contenttypepropertycollection/#add-string-string-) لإضافة خاصية مخصصة ستكون مرئية في لوحة معلومات المستند.

 يضيف رمز النموذج التالي خاصيتين مخصصتين. الخاصية الأولى بدون نوع معين والخاصية الثانية من نوع تاريخ ووقت. بمجرد فتح ملف إكسل الناتج الذي تم إنشاؤه بواسطة هذا الرمز، سترى هاتين الخاصيتين داخل لوحة معلومات المستند.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Adding Custom Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Workbook with Custom Properties</button>
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
            // Create workbook object
            const workbook = new Workbook();

            // Add simple property without any type
            workbook.contentTypeProperties.add("MK31", "Simple Data");

            // Add date time property with type
            workbook.contentTypeProperties.add("MK32", "04-Mar-2015", "DateTime");

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddingCustomPropertiesVisible_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **مقال ذو صلة**

{{% alert color="primary" %}}

- [استخدام أجزاء XML المخصصة في Aspose.Cells](/cells/ar/net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
