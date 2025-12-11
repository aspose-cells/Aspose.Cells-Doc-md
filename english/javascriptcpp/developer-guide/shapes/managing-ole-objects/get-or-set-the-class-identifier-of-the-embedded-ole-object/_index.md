---  
title: Get or Set the Class Identifier of the Embedded OLE Object with JavaScript via C++  
linktitle: Get or Set the Class Identifier of the Embedded OLE Object  
type: docs  
weight: 200  
url: /javascript-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/  
description: Learn how to get or set the class identifier of embedded OLE objects in JavaScript using Aspose.Cells via C++.  
---  

## **Possible Usage Scenarios**  
Aspose.Cells provides the [OleObject.classIdentifier](https://reference.aspose.com/cells/javascript-cpp/oleobject/#classIdentifier--) property which you can use to get or set the class identifier of an embedded OLE object. OLE object class identifiers are actually GUIDs, i.e., Globally Unique Identifiers. **A** GUID is always 16 bytes long; therefore, class identifiers are also 16 bytes long. They are often found inside the Windows Registry and provide information to the host application about how to open embedded OLE objects containing various embedded resources inside the client application.  

## **Get or Set the Class Identifier of the Embedded OLE Object**  
The following screenshot shows the OLE object class identifier, i.e., GUID, which has been read from the [sample Excel file](5115190.xls) containing the embedded PowerPoint OLE object.  

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)  

### **Sample Code**  
Please see the following sample code executed with the [sample Excel file](5115190.xls) and its console output, which prints the class identifier of the OLE object, i.e., GUID. The printed GUID is exactly the same as shown inside the screenshot.  

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

            // Convert 16‑byte array into GUID
            const bytes = new Uint8Array(oleObject.classIdentifier);
            const guid = bytes.reduce((acc, byte) => acc + String.fromCharCode(byte), '');

            // Print the GUID
            console.log(guid.toUpperCase());
            resultDiv.innerHTML = `<p style="color: green;">GUID: ${guid.toUpperCase()}</p>`;
        });
    </script>
</html>
```  

### **Console Output**  
This is the console output of the above sample code when executed with the [sample Excel file](5115190.xls).  

{{< highlight java >}}  
DC020317-E6E2-4A62-B9FA-B3EFE16626F4  
{{< /highlight >}}