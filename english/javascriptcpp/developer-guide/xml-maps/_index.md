---  
title: Import XML to Excel workbook with JavaScript via C++  
linktitle: XML Maps  
type: docs  
weight: 210  
url: /javascript-cpp/import-xml-map-inside-a-workbook-using-aspose-cells/  
description: Import data from XML files into Excel using Aspose.Cells for JavaScript via C++.  
---  

{{% alert color="primary" %}}  

Aspose.Cells allows you to import the XML map inside the workbook using the [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#importXml-string-string-number-number-) method. You can import an XML map using Microsoft Excel with the following steps:  

- Select **Developer** tab  
- Click **Import** in the XML section and follow the required steps.  

You will need to provide your XML data to complete the import. Here is a [sample XML data](5115037.txt) that you can use for testing.  

{{% /alert %}}  

## **Import XML Map using Microsoft Excel**  

The following screenshot shows how to import an XML map using Microsoft Excel.  

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|  
| :- |  

## **Import XML Map using Aspose.Cells for JavaScript via C++**  

The following sample code shows how to use the [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#importXml-string-string-number-number-). It generates the [output Excel file](5115036.xlsx) as shown in this screenshot.  

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_2.png)|  
| :- |  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Import XML</title>
    </head>
    <body>
        <h1>Import XML into Workbook Example</h1>
        <input type="file" id="xmlInput" accept=".xml,.txt" />
        <button id="runExample">Import XML and Save</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;
        
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
            const fileInput = document.getElementById('xmlInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an XML file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const xmlText = await file.text();

            // Create a workbook
            const workbook = new Workbook();

            // Import your XML map data starting from cell A1 on Sheet1
            workbook.importXml(xmlText, "Sheet1", 0, 0);

            // Save the workbook to XLSX and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">XML imported and workbook saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **Advanced topics**  
- [Add XML Map inside the Workbook using XmlMapCollection.add() method](/cells/javascript-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)  
- [Export XML Data linked to XML Map inside the Workbook](/cells/javascript-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)  
- [Find the Root Element Name of XML Map](/cells/javascript-cpp/find-the-root-element-name-of-xml-map/)  
- [Link Cells to XML Map Elements](/cells/javascript-cpp/link-cells-to-xml-map-elements/)  