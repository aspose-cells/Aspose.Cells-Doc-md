---
title: إضافات الويب  إضافات Office باستخدام جافا سكريبت عبر C++
linktitle: الإضافات الإلكترونية للويب  إضافات Office
type: docs
weight: 130
url: /ar/javascript-cpp/web-extensions-office-add-ins/
---

ملحقات الويب توسع تطبيقات Office وتتفاعل مع محتوى مستندات Office. تضيف ملحقات الويب وظائف إضافية إلى عميل Office لتحسين تجربة المستخدم وزيادة الإنتاجية.

توفر Aspose.Cells أيضًا القدرة على العمل مع ملحقات الويب.

## **إضافة ملحق ويب**

 يمكنك إضافة إضافات الويب (إضافات Office) في إكسل بالنقر على علامة التبويب **إدراج** ثم النقر على رابط **المتجر** / **الحصول على الإضافات**. في مربع الإضافات، تصفح الإضافة التي تريدها وأضفها.

توفر Aspose.Cells أيضًا ميزة إضافة إضافات الويب باستخدام فئتي [**WebExtension**](https://reference.aspose.com/cells/javascript-cpp/webextension) و [**WebExtensionTaskPane**](https://reference.aspose.com/cells/javascript-cpp/webextensiontaskpane). يوضح نموذج الكود التالي استخدام فئتي [**WebExtension**](https://reference.aspose.com/cells/javascript-cpp/webextension) و [**WebExtensionTaskPane**](https://reference.aspose.com/cells/javascript-cpp/webextensiontaskpane) لإضافة إضافة ويب إلى ملف إكسل. يرجى مراجعة ملف إكسل الناتج [ملف الإكسل الناتج](89849869.xlsx) باستخدام الكود للمراجعة.

### **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Add Web Extension Example</title>
    </head>
    <body>
        <h1>Add Web Extension Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, WebExtensionStoreType, Utils } = AsposeCells;

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

            // Create a new workbook or load from selected file
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access web extensions and task panes collections from worksheets
            const extensions = workbook.worksheets.webExtensions;
            const taskPanes = workbook.worksheets.webExtensionTaskPanes;

            // Add new web extension and task pane
            const extensionIndex = extensions.add();
            const taskPaneIndex = taskPanes.add();

            // Configure the extension reference
            const extension = extensions.get(extensionIndex);
            extension.reference.id = "wa104379955";
            extension.reference.storeName = "en-US";
            extension.reference.storeType = WebExtensionStoreType.OMEX;

            // Configure the task pane
            const taskPane = taskPanes.get(taskPaneIndex);
            taskPane.isVisible = true;
            taskPane.dockState = "right";
            taskPane.webExtension = extension;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddWebExtension_Out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Web extension and task pane added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **الوصول إلى معلومات ملحق الويب**

توفر Aspose.Cells القدرة على الوصول إلى معلومات إضافات الويب في ملف إكسل. يوضح مثال الكود التالي كيف يمكن الوصول إلى معلومات الإضافة عن طريق تحميل ملف إكسل العينة [ملف إكسل عينة](89849870.xlsx). يرجى الاطلاع على مخرجات وحدة التحكم التي تم إنشاؤها بواسطة الكود للمراجعة.

### **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Web Extensions Task Panes Example</title>
    </head>
    <body>
        <h1>Web Extensions Task Panes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing web extension task panes collection
            const taskPanes = workbook.worksheets.webExtensionTaskPanes;

            const lines = [];
            for (let i = 0; i < taskPanes.count; i++) {
                const taskPane = taskPanes.get(i);
                lines.push("Width: " + taskPane.width);
                lines.push("IsVisible: " + taskPane.isVisible);
                lines.push("IsLocked: " + taskPane.isLocked);
                lines.push("DockState: " + taskPane.dockState);

                const webExt = taskPane.webExtension;
                const reference = webExt.reference;
                lines.push("StoreName: " + reference.storeName);
                lines.push("StoreType: " + reference.storeType);
                lines.push("WebExtension.Id: " + webExt.id);
                lines.push("---------------------------------");
            }

            document.getElementById('result').innerHTML = '<pre>' + lines.join("\n") + '</pre>';
        });
    </script>
</html>
```

### **مخرجات الوحدة**

{{< highlight javascript >}}

Width: 350

IsVisible: True

IsLocked: False

DockState: right

StoreName: en-US

StoreType: OMEX

WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF

{{< /highlight >}}
