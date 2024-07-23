---
title: Getting started
type: docs
weight: 5
url: /nodejs-cpp/getting-started/
keywords: "nodejs, excel, install"
description: "setup Aspose.Cells for Node.js via C++ and installation guidelines."
---

## **Product Description**
Aspose.Cells for Node.js via C++ is a powerful and robust library designed for high-performance spreadsheet manipulation and management within Node.js applications. It offers a comprehensive set of features that enable developers to create, edit, convert, and render Excel files programmatically. Supporting all major Excel formats, including XLS, XLSX, XLSM, and more, it ensures compatibility and flexibility. This makes Aspose.Cells for Node.js via C++ a versatile tool for a wide range of data processing and management tasks, providing developers with a complete and efficient solution for integrating comprehensive Excel functionality into their Node.js applications.

## **Key features**
1. **File Creation and Editing:** Create new spreadsheets from scratch or edit existing ones with ease. This includes adding or modifying data, formatting cells, managing worksheets, and more.
1. **Data Processing:** Perform complex data manipulations such as sorting, filtering, and validation. The library also supports advanced formulas and functions to facilitate data analysis and calculations.
1. **File Conversion:** Convert Excel files to various formats such as PDF, HTML, ODS, and image formats like PNG and JPEG. This feature is useful for sharing and distributing spreadsheet data in different formats.
1. **Chart and Graphics:** Create and customize a wide range of charts and graphics to visually represent data. The library supports bar charts, line charts, pie charts, and many more, along with customization options for design and layout.
1. **Rendering and Printing:** Render Excel sheets to high-fidelity images and PDFs, ensuring that the visual representation is accurate. The library also provides options for printing spreadsheets with precise control over page layout and formatting.
1. **Advanced Protection and Security:** Protect spreadsheets with passwords, encrypt files, and manage access permissions to ensure data security and integrity.
1. **Performance and Scalability:** Designed to handle large datasets and complex spreadsheets efficiently, Aspose.Cells for Node.js via C++ ensures high performance and scalability for enterprise-level applications.


## **Install from NPM**
You can easily use Aspose.Cells for Node.js via C++ from [NPM](https://www.npmjs.com/package/aspose.cells) with the following command.
{{< highlight java >}}

 $ npm install aspose.cells

{{< /highlight >}}

If you encounter any problems during the installation process, please refer to https://www.npmjs.com/package/package.


## **Hello World Example**

{{< highlight cpp >}}

const AsposeCells = require("aspose.cells");

var workbook = new AsposeCells.Workbook(AsposeCells.FileFormatType.Xlsx);
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Hello World");
workbook.save("hello-world.xlsx");

{{< /highlight >}}