```markdown
---
title: إضافة أجزاء XML مخصصة واختيارها بمعرف باستخدام جافا سكريبت عبر C++
linktitle: إضافة أجزاء XML مخصصة وتحديدها حسب الهوية
type: docs
weight: 70
url: /ar/javascript-cpp/add-custom-xml-parts-and-select-them-by-id/
description: تعلم كيفية إضافة أجزاء XML مخصصة إلى مستندات إكسل واختيارها بواسطة المعرف باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**  

أجزاء XML المخصصة هي بيانات XML المخزنة داخل مستندات Microsoft Excel وتستخدمها التطبيقات التي تتعامل معها. لا توجد طريقة مباشرة لإضافتها باستخدام واجهة مستخدم Microsoft Excel حاليًا. ومع ذلك، يمكنك إضافتها برمجياً بطرق متعددة، مثل استخدام VSTO، أو Aspose.Cells، وغيرها. يرجى استخدام مجموعة [**Workbook.customXmlParts**](https://reference.aspose.com/cells/javascript-cpp/workbook/#customXmlParts--) إذا كنت تريد إضافة جزء XML مخصص باستخدام API Aspose.Cells. يمكنك أيضًا تعيين معرفها باستخدام خاصية [**CustomXmlPart.iD**](https://reference.aspose.com/cells/javascript-cpp/customxmlpart/#iD--). بالمثل، إذا كنت تريد اختيار جزء XML مخصص بواسطة المعرف، يمكنك استخدام مجموعة [**Workbook.customXmlParts**](https://reference.aspose.com/cells/javascript-cpp/workbook/#customXmlParts--).  

## **إضافة أجزاء XML مخصصة وتحديدها حسب الهوية**  

يعرض رمز العينة التالي أولاً إضافة أربعة أجزاء XML مخصصة باستخدام مجموعة [**Workbook.customXmlParts**](https://reference.aspose.com/cells/javascript-cpp/workbook/#customXmlParts--). ثم يعين معرفاتها باستخدام خاصية [**CustomXmlPart.iD**](https://reference.aspose.com/cells/javascript-cpp/customxmlpart/#iD--). أخيرًا، يبحث أو يختار أحد أجزاء XML المخصصة المضافة باستخدام مجموعة [**Workbook.customXmlParts**](https://reference.aspose.com/cells/javascript-cpp/workbook/#customXmlParts--). يرجى أيضًا مراجعة شعار الإخراج الخاص بالرمز أدناه للمرجعية.  

## **الكود المثالي**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Add and Select Custom XML Parts Example</title>
    </head>
    <body>
        <h1>Add and Select Custom XML Parts Example</h1>
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains hidden external links
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Some data in the form of byte array.
            // Please use correct XML and Schema instead.
            const btsData = new Uint8Array([1, 2, 3]);
            const btsSchema = new Uint8Array([1, 2, 3]);

            // Create four custom xml parts.
            wb.customXmlParts.add(btsData, btsSchema);
            wb.customXmlParts.add(btsData, btsSchema);
            wb.customXmlParts.add(btsData, btsSchema);
            wb.customXmlParts.add(btsData, btsSchema);

            // Assign ids to custom xml parts.
            wb.customXmlParts.get(0).id = "Fruit";
            wb.customXmlParts.get(1).id = "Color";
            wb.customXmlParts.get(2).id = "Sport";
            wb.customXmlParts.get(3).id = "Shape";

            // Specify search custom xml part id.
            let srchID = "Fruit";
            srchID = "Color";
            srchID = "Sport";

            // Search custom xml part by the search id.
            const cxp = wb.customXmlParts.selectByID(srchID);

            // Print the found or not found message on console and UI.
            if (cxp.isNull()) {
                console.log(`Not Found: CustomXmlPart ID ${srchID}`);
                document.getElementById('result').innerHTML = `<p style="color: red;">Not Found: CustomXmlPart ID ${srchID}</p>`;
            } else {
                console.log(`Found: CustomXmlPart ID ${srchID}`);
                document.getElementById('result').innerHTML = `<p style="color: green;">Found: CustomXmlPart ID ${srchID}</p>`;
            }

            // Save the modified workbook and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            console.log("AddCustomXMLPartsAndSelectThemByID executed successfully.");
        });
    </script>
</html>
```  

## **مخرجات الوحدة**  

{{< highlight java >}}  
 Found: CustomXmlPart ID Sport  
{{< /highlight >}}  
 ```
