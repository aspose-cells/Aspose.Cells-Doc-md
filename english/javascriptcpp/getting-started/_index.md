---
title: Getting started
type: docs
weight: 5
url: /javascript-cpp/getting-started/
keywords: "Excel,Browser,Serverless,XLS,XLSX,XLSB,CSV,PDF,JPG,PNG,HTML,ODS,XLSM,Spreadsheet,Markdown,XPS,DOCX,PPTX,MHTML,SVG,JSON,SQL,XML"
description: "setup Aspose.Cells for javascript via C++ and installation guidelines."
---

## **Product Description**
Aspose.Cells for JavaScript via C++ is a high-performance, feature-rich library for manipulating and converting spreadsheet files, including Excel (XLS, XLSX, XLSB, XLSM), ODS, CSV, and HTML formats. It provides a comprehensive set of features for creating, editing, converting, and rendering spreadsheets in both browser and Node.js environments. With full support for all major Excel formats, Aspose.Cells for JavaScript via C++ ensures maximum compatibility and flexibility across diverse use cases.
Built with WebAssembly to unlock near-native performance directly in the browser, Aspose.Cells for JavaScript via C++ enables fast and efficient spreadsheet processing without the need for a server. Its lightweight runtime footprint makes it perfect for serverless web applications that require advanced Excel functionality. Whether you're building dashboards, data processing pipelines, or document generation tools, Aspose.Cells for JavaScript via C++ offers a complete, reliable, and high-performance solution.Aspose.Cells for JavaScript via C++ supports browsers and Node.js, mainly browsers.

## **Key features**
1. **File Creation and Editing:**  Create new spreadsheets from scratch or edit existing ones with ease. This includes adding or modifying data, formatting cells, managing worksheets, and more.
1. **Data Processing:** Perform complex data manipulations such as sorting, filtering, and validation. The library also supports advanced formulas and functions to facilitate data analysis and calculations.
1. **File Conversion:** Convert Excel files to various formats such as PDF, HTML, ODS, and image formats like PNG and JPEG. This feature is useful for sharing and distributing spreadsheet data in different formats.
1. **Chart and Graphics:** Create and customize a wide range of charts and graphics to visually represent data. The library supports bar charts, line charts, pie charts, and many more, along with customization options for design and layout.
1. **Rendering and Printing:** Render Excel sheets to high-fidelity images and PDFs, ensuring that the visual representation is accurate. The library also provides options for printing spreadsheets with precise control over page layout and formatting.
1. **Advanced Protection and Security:** Protect spreadsheets with passwords, encrypt files, and manage access permissions to ensure data security and integrity.
1. **Performance and Scalability:** Designed to handle large datasets and complex spreadsheets efficiently, Aspose.Cells for JavaScript via C++ ensures high performance and scalability for enterprise-level applications.


## **Install from NPM**
You can easily use Aspose.Cells for JavaScript via C++ from [NPM](https://www.npmjs.com/package/aspose.cells.js) with the following command.
{{< highlight java >}}

 $ npm install aspose.cells.js

{{< /highlight >}}

If you encounter any problems during the installation process, please refer to https://www.npmjs.com/package/package.


## **Hello World Example**



First, create a project directory and execute the npm command in the directory to download Aspose.Cells for JavaScript via C++

{{< highlight java >}}
$ npm install aspose.cells.js
{{< /highlight >}}

Then create an HelloWorldExample.html file in your project directory with the following content

{{< highlight cpp >}}

<!DOCTYPE html>
<html>
    <head>
    </head>
    <body>
    </body>

    <script src="./node_modules/aspose.cells.js/aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, FileFormatType, SaveFormat } = AsposeCells;
        AsposeCells.onReady().then(() => {
            var workbook = new Workbook(FileFormatType.Xlsx);
            workbook.worksheets.get(0).cells.get("A1").putValue("Hello World");
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.createElement('a');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.textContent = 'Download';
            downloadLink.download = "hello-world.xlsx";
            downloadLink.style.display = 'block';
            document.body.append(downloadLink);
        });
    </script>
</html>

{{< /highlight >}}

Run the http server in the project directory

{{< highlight cpp >}}

    python -m http.server 8080

{{< /highlight >}}

Visit http://localhost:8080/HelloWorldExample.html in your browser and click the Download button to download hello-world.xlsx.



## **License**

You need to use encrypt_lic.html in a http server to get the encrypted license file (aspose.cells.enc) in order to run in full-featured mode. To run the http server:

{{< highlight cpp >}}

    cd node_modules/aspose.cells.js
    python -m http.server 8080

{{< /highlight >}}