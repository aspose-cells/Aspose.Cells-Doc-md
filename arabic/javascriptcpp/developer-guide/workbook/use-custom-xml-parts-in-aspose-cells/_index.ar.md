---
title: استخدام أجزاء XML مخصصة في Aspose.Cells مع جافا سكريبت عبر ++C
linktitle: استخدام أجزاء XML المخصصة في Aspose.Cells
type: docs
weight: 390
url: /ar/javascript-cpp/use-custom-xml-parts-in-aspose-cells/
description: تعلم كيفية استخدام أجزاء XML المخصصة في Aspose.Cells for JavaScript عبر ++C. دمج بيانات XML الخارجية داخل ملفات Excel بسلاسة.
---

## استخدام أجزاء XML المخصصة في Aspose.Cells

أجزاء XML المخصصة هي البيانات XML التي يتم تخزينها بواسطة تطبيقات مختلفة مثل SharePoint وغيرها داخل ملف إكسل. يتم استهلاك هذه البيانات بواسطة تطبيقات مختلفة تحتاجها. لا يستخدم Microsoft Excel هذه البيانات لذلك لا يوجد واجهة رسومية لإضافتها. يمكنك عرض هذه البيانات بتغيير امتداد **.xlsx** إلى **.zip** ثم فتحه باستخدام **WinZip**. يمكنك أيضًا فتح ملف ZIP باستخدام أي أداة ضغط من طرف ثالث على Windows مثل WinRAR أو WinZip. البيانات موجودة داخل مجلد **customXml**.

يمكنك إضافة أجزاء XML مخصصة باستخدام Aspose.Cells for JavaScript عبر ++C من خلال طريقة [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/contenttypepropertycollection/)

يُظهر رمز المثال التالي استخدام طريقة [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/contenttypepropertycollection/) ويضيف **Book Catalog XML** واسمها **BookStore**. ويظهر الصورة التالية نتيجة هذا الرمز. كما ترى، تمت إضافة Book Catalog XML داخل عنصر BookStore الذي هو اسم الخاصية هذه.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## رمز جافا سكريبت لاستخدام أجزاء XML المخصصة

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Custom XML to Workbook Example</h1>
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

        const booksXML = `<catalog>
<book>
<title>Complete C#</title>
<price>44</price>
</book>
<book>
<title>Complete Java</title>
<price>76</price>
</book>
<book>
<title>Complete SharePoint</title>
<price>55</price>
</book>
<book>
<title>Complete PHP</title>
<price>63</price>
</book>
<book>
<title>Complete VB.NET</title>
<price>72</price>
</book>
</catalog>`;

        document.getElementById('runExample').addEventListener('click', async () => {
            // Create an instance of Workbook class
            const workbook = new Workbook();

            // Add Custom XML Part to ContentTypePropertyCollection
            workbook.contentTypeProperties.add("BookStore", booksXML);

            // Save the resultant spreadsheet
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Custom XML added and file prepared. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## مقال ذو صلة

- [إضافة خصائص مخصصة مرئية داخل لوحة معلومات الوثيقة](/cells/ar/javascript-cpp/adding-custom-properties-visible-inside-document-information-panel/)
