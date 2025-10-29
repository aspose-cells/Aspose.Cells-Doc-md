---
title: الحصول على أو تعيين معرف الفئة للكائن OLE المضمّن باستخدام JavaScript عبر C++
linktitle: الحصول على أو تعيين معرف الفئة لكائن Ole المضمن
type: docs
weight: 200
url: /ar/javascript-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/
description: تعلم كيفية الحصول على أو تعيين معرف فئة كائنات OLE المدمجة باستخدام JavaScript من خلال Aspose.Cells باستخدام C++،.
---

## **سيناريوهات الاستخدام المحتملة**  
 توفر Aspose.Cells الخاصية [OleObject.classIdentifier](https://reference.aspose.com/cells/javascript-cpp/oleobject/#classIdentifier--) والتي يمكنك استخدامها للحصول على أو تعيين معرف فئة الكائن OLE المضمّن. معرّفات فئة كائن OLE هي في الواقع GUIDs أي معرفات فريدة عالمياً. دائمًا ما يكون GUID بطول 16 بايت؛ لذلك، فإن معرفات الفئة تكون أيضًا بطول 16 بايت. وغالبًا ما توجد داخل سجل Windows وتوفر معلومات للتطبيق المضيف حول كيفية فتح الكائنات OLE المدمجة التي تحتوي على موارد مدمجة مختلفة داخل التطبيق العميل.

## **الحصول على معرف الفئة الخاص بكائن OLE المضمّن أو تعيينه**  
يُظهر لقطه الشاشة التالية معرف فئة كائن الـ OLE أي GUID الذي تم قراءته من [ملف إكسل النموذجي](5115190.xls) الذي يحتوي على كائن PowerPoint مدمج داخل OLE.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)  
### **الكود المثالي**  
يرجى الاطلاع على رمز النموذج التالي الذي تم تنفيذه باستخدام [ملف إكسل النموذجي](5115190.xls) وإخراجه عبر وحدة التحكم التي تطبع معرف فئة الكائن OLE أي GUID. GUID المطبوع هو بالضبط نفسه كما هو موضح داخل لقطة الشاشة.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract OLE Object Class Identifier (GUID)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access its first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first ole object inside the worksheet
            const oleObject = worksheet.oleObjects.get(0);

            // Convert 16-bytes array into GUID
            const bytes = new Uint8Array(oleObject.classIdentifier);
            const guid = bytes.reduce((acc, byte) => acc + String.fromCharCode(byte), '');

            // Print the GUID
            console.log(guid.toUpperCase());
            resultDiv.innerHTML = `<p style="color: green;">GUID: ${guid.toUpperCase()}</p>`;
        });
    </script>
</html>
```  
### **مخرجات الوحدة**  
هذه هي مخرجات وحدة التحكم للرمز النموذجي أعلاه عند تنفيذه باستخدام [ملف إكسل النموذجي](5115190.xls).

{{< highlight java >}}  
 DC020317-E6E2-4A62-B9FA-B3EFE16626F4  
{{< /highlight >}}
