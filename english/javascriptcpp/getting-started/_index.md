---
title: Getting Started
type: docs
weight: 5
url: /javascript-cpp/getting-started/
keywords: "Excel,Browser,Serverless,XLS,XLSX,XLSB,CSV,PDF,JPG,PNG,HTML,ODS,XLSM,Spreadsheet,Markdown,XPS,DOCX,PPTX,MHTML,SVG,JSON,SQL,XML"
description: "Setup Aspose.Cells for JavaScript via C++ and installation guidelines."
---

## **Product Description**
Aspose.Cells for JavaScript via C++ is a high‑performance, feature‑rich library for manipulating and converting spreadsheet files, including Excel (XLS, XLSX, XLSB, XLSM), ODS, CSV, and HTML formats. It provides a comprehensive set of features for creating, editing, converting, and rendering spreadsheets in both browser and Node.js environments. With full support for all major Excel formats, Aspose.Cells for JavaScript via C++ ensures maximum compatibility and flexibility across diverse use cases.  
Built with WebAssembly to unlock near‑native performance directly in the browser, Aspose.Cells for JavaScript via C++ enables fast and efficient spreadsheet processing without the need for a server. Its lightweight runtime footprint makes it perfect for serverless web applications that require advanced Excel functionality. Whether you're building dashboards, data processing pipelines, or document generation tools, Aspose.Cells for JavaScript via C++ offers a complete, reliable, and high‑performance solution. Aspose.Cells for JavaScript via C++ supports browsers and Node.js, primarily browsers.

## **Key Features**
1. **File Creation and Editing:** Create new spreadsheets from scratch or edit existing ones with ease. This includes adding or modifying data, formatting cells, managing worksheets, and more.  
2. **Data Processing:** Perform complex data manipulations such as sorting, filtering, and validation. The library also supports advanced formulas and functions to facilitate data analysis and calculations.  
3. **File Conversion:** Convert Excel files to various formats such as PDF, HTML, ODS, and image formats like PNG and JPEG. This feature is useful for sharing and distributing spreadsheet data in different formats.  
4. **Chart and Graphics:** Create and customize a wide range of charts and graphics to visually represent data. The library supports bar charts, line charts, pie charts, and many more, along with customization options for design and layout.  
5. **Rendering and Printing:** Render Excel sheets to high‑fidelity images and PDFs, ensuring that the visual representation is accurate. The library also provides options for printing spreadsheets with precise control over page layout and formatting.  
6. **Advanced Protection and Security:** Protect spreadsheets with passwords, encrypt files, and manage access permissions to ensure data security and integrity.  
7. **Performance and Scalability:** Designed to handle large datasets and complex spreadsheets efficiently, Aspose.Cells for JavaScript via C++ ensures high performance and scalability for enterprise‑level applications.

## **Prerequisites**

Before getting started, make sure you have:
- Node.js installed on your system (download from https://nodejs.org/)
- A valid Aspose license file (e.g., Aspose.Total.lic, Aspose.Cells.lic, or aspose.cells.js.lic) for full‑featured use
- Basic knowledge of HTML and JavaScript

## **Step 1: Installation**

### Install Aspose.Cells for JavaScript

Create a new project directory and install the package:

{{< highlight bash >}}
# Create a new project directory
mkdir my-excel-project
cd my-excel-project

# Install Aspose.Cells for JavaScript
npm install aspose.cells.js
{{< /highlight >}}

### Install HTTP Server (Required for License Setup)

Install a simple HTTP server globally:

{{< highlight bash >}}
npm install -g http-server
{{< /highlight >}}

Or use Python's built‑in server (if Python is installed):

{{< highlight bash >}}
# Python 3
python -m http.server

# Python 2
python -m SimpleHTTPServer
{{< /highlight >}}

## **Step 2: License Setup (Required for Full Features)**

### Encrypt Your License File

1. **Start the HTTP server** in your project directory:

{{< highlight bash >}}
http-server -p 8080
{{< /highlight >}}

2. **Open the license encryption tool** in your browser:

```
http://localhost:8080/node_modules/aspose.cells.js/encrypt_lic.html
```

3. **Upload your license file**:
   - Click **Choose File** and select your license file (e.g., `Aspose.Total.lic`, `Aspose.Cells.lic`, or `aspose.cells.js.lic`)
   - The encryption process will complete automatically (very fast)

4. **Download the encrypted license**:
   - Click **Download Processed File** to download `aspose.cells.enc`
   - Save this file to your project directory

### Place the Encrypted License

Move the `aspose.cells.enc` file to your project root or a specific folder where your application can access it.

## **Step 3: Usage Examples**

### Browser Usage

Create an `index.html` file in your project directory:

{{< highlight html >}}
<!DOCTYPE html>
<html>
<head>
    <title>Aspose.Cells Browser Example</title>
</head>
<body>
    <h1>Excel Processing with Aspose.Cells</h1>
    <button id="createExcel">Create Excel File</button>
    <div id="output"></div>

    <script src="./node_modules/aspose.cells.js/aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, FileFormatType, SaveFormat } = AsposeCells;
        
        // Initialize with license (optional, remove for trial mode)
        AsposeCells.onReady({
            license: "aspose.cells.enc"  // Path to your encrypted license
        }).then(() => {
            console.log("Aspose.Cells is ready!");
            
            document.getElementById('createExcel').onclick = function() {
                // Create a new workbook
                var workbook = new Workbook(FileFormatType.Xlsx);
                
                // Get the first worksheet
                var worksheet = workbook.worksheets.get(0);
                
                // Add some data
                worksheet.cells.get("A1").putValue("Hello World");
                worksheet.cells.get("A2").putValue("Created with Aspose.Cells for JavaScript");
                worksheet.cells.get("B1").putValue(42);
                
                // Save as Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);
                
                // Create download link
                const blob = new Blob([outputData]);
                const downloadLink = document.createElement('a');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.textContent = 'Download Excel File';
                downloadLink.download = "my-excel-file.xlsx";
                downloadLink.style.display = 'block';
                
                const output = document.getElementById('output');
                output.innerHTML = '';
                output.appendChild(downloadLink);
            };
        }).catch(error => {
            console.error("Error initializing Aspose.Cells:", error);
        });
    </script>
</html>
{{< /highlight >}}

**To run the browser example:**

{{< highlight bash >}}
# Start HTTP server
http-server -p 8080

# Open browser and visit:
# http://localhost:8080
{{< /highlight >}}

### Node.js Usage

Create a `node-example.js` file:

{{< highlight javascript >}}
const { AsposeCells, Workbook, SaveFormat, FileFormatType } = require("aspose.cells.js");
const fs = require('fs');

// Initialize Aspose.Cells with license
AsposeCells.onReady({
    license: "aspose.cells.enc",  // Path to your encrypted license
    fontPath: "./fonts/"         // Optional: path to system fonts
}).then(() => {
    console.log("Aspose.Cells initialized successfully!");
    
    // Create a new workbook
    const workbook = new Workbook(FileFormatType.Xlsx);
    
    // Get the first worksheet
    const worksheet = workbook.worksheets.get(0);
    
    // Add data to cells
    worksheet.cells.get("A1").putValue("Product");
    worksheet.cells.get("B1").putValue("Price");
    worksheet.cells.get("A2").putValue("Apple");
    worksheet.cells.get("B2").putValue(1.99);
    worksheet.cells.get("A3").putValue("Orange");
    worksheet.cells.get("B3").putValue(2.49);
    
    // Save as Excel file
    const excelData = workbook.save(SaveFormat.Xlsx);
    fs.writeFileSync('output.xlsx', Buffer.from(excelData));
    console.log('Excel file saved as output.xlsx');
    
    // Save as PDF
    const pdfData = workbook.save(SaveFormat.Pdf);
    fs.writeFileSync('output.pdf', Buffer.from(pdfData));
    console.log('PDF file saved as output.pdf');
    
}).catch(error => {
    console.error("Error:", error);
});
{{< /highlight >}}

**To run the Node.js example:**

{{< highlight bash >}}
node node-example.js
{{< /highlight >}}

## **Common File Operations**

### Reading an Existing Excel File

{{< highlight javascript >}}
// Browser (using File input)
const fileInput = document.getElementById('fileInput');
fileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    const reader = new FileReader();
    reader.onload = (e) => {
        const arrayBuffer = e.target.result;
        const workbook = new Workbook(new Uint8Array(arrayBuffer));
        // Process the workbook...
    };
    reader.readAsArrayBuffer(file);
});

// Node.js
const fs = require('fs');
const fileBuffer = fs.readFileSync('input.xlsx');
const workbook = new Workbook(fileBuffer);
{{< /highlight >}}

### Converting Between Formats

{{< highlight javascript >}}
// Convert Excel to PDF
const pdfData = workbook.save(SaveFormat.Pdf);

// Convert Excel to HTML
const htmlData = workbook.save(SaveFormat.Html);

// Convert Excel to CSV
const csvData = workbook.save(SaveFormat.Csv);

// Convert Excel to JSON
const jsonData = workbook.save(SaveFormat.Json);
{{< /highlight >}}

## **Troubleshooting**

### Common Issues and Solutions

1. **"Module not found" error**
   - Make sure you're running the HTTP server from the correct directory
   - Verify the script src path points to the correct location

2. **License not working**
   - Ensure the `aspose.cells.enc` file is in the correct location
   - Check that the encrypted license file was generated properly
   - Verify the original license file is valid and not expired

3. **CORS issues in browser**
   - Always use an HTTP server; never open HTML files directly
   - Use `http-server` or similar tools for local development

### Getting Help

If you encounter issues:
- Check the [Aspose.Cells documentation](https://docs.aspose.com/cells/javascript-cpp/)
- Visit the [Aspose Forums](https://forum.aspose.com/c/cells/9) for community support
- Contact Aspose Support with your license information

## **Next Steps**

- Explore the [API Reference](https://reference.aspose.com/cells/javascript-cpp/) for detailed documentation
- Learn about advanced features like charts, formulas, and formatting
- Check out more examples and tutorials in the documentation
- Consider integrating with your existing web applications or build tools