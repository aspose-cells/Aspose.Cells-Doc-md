---
title: Web Uzantıları  Office Eklentileri JavaScript ile C++
linktitle: Web Eklentileri  Ofis Eklentileri
type: docs
weight: 130
url: /tr/javascript-cpp/web-extensions-office-add-ins/
---

Web Eklentileri, Ofis belgelerindeki içerikle etkileşimde bulunarak Ofis uygulamalarını genişletir. Web Eklentileri, kullanıcı deneyimini ve üretkenliği artırmak için Ofis istemcisine ek işlevsellik ekler.

Aspose.Cells, Web Eklentileri ile çalışma kabiliyeti de sunar.

## **Web Eklentisi Ekleme**

Excel'de Web Eklentileri (Office Eklentileri) ekleyebilirsiniz, bunun için **Ekle** sekmesine tıklayın ve sonra **Mağaza**/**Ekle Eklentileri Al** bağlantısını tıklayın. Eklentiler kutusunda, istediğiniz eklentiyi arayın ve ekleyin.

Aspose.Cells, ayrıca [**WebExtension**](https://reference.aspose.com/cells/javascript-cpp/webextension) ve [**WebExtensionTaskPane**](https://reference.aspose.com/cells/javascript-cpp/webextensiontaskpane) sınıflarını kullanarak Web Eklentileri ekleme özelliği sağlar. Aşağıdaki kod örneği, [**WebExtension**](https://reference.aspose.com/cells/javascript-cpp/webextension) ve [**WebExtensionTaskPane**](https://reference.aspose.com/cells/javascript-cpp/webextensiontaskpane) sınıflarını kullanarak bir Excel dosyasına web eklentisi eklemeyi gösterir. Lütfen referans olarak kod tarafından oluşturulan [çıktı Excel dosyasına](89849869.xlsx) bakın.

### **Örnek Kod**

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

## **Web Eklentisi Bilgilerine Erişme**

Aspose.Cells, Excel dosyasındaki Web Eklentileri bilgisine erişim sağlar. Aşağıdaki kod örneği, [örnek Excel dosyasını](89849870.xlsx) yükleyerek web eklentisi bilgisine nasıl ulaşılacağını gösterir. Kod tarafından üretilen konsol çıktısına bakın.

### **Örnek Kod**

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

### **Konsol Çıktısı**

{{< highlight javascript >}}

Width: 350

IsVisible: True

IsLocked: False

DockState: right

StoreName: en-US

StoreType: OMEX

WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF

{{< /highlight >}}
