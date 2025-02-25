---  
title: Adding Anonymous or Custom Object into SmartMarkers with Node.js via C++  
linktitle: Adding Anonymous or Custom Object into SmartMarkers  
type: docs  
weight: 10  
url: /nodejs-cpp/adding-anonymous-or-custom-object-into-smartmarkers/  
description: Learn how to import anonymous or custom objects into SmartMarkers using Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

This explains how to import anonymous or custom objects into SmartMarkers.  

Sometimes, you need to include custom objects as a data source to the SmartMarkers. Aspose.Cells for Node.js via C++ makes it possible to use custom objects as the data source.  

{{% /alert %}}  

Please see the following sample code which shows how to add custom objects as a data source for SmartMarkers.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
}

async function run() {
    // The path to the documents directory.
    const dataDir = path.join(__dirname, "data");

    // Create directory if it is not already present.
    const fs = require("fs");
    if (!fs.existsSync(dataDir)) {
        fs.mkdirSync(dataDir);
    }

    // Open a designer workbook
    const designer = new AsposeCells.WorkbookDesigner();

    // Get worksheet Cells collection
    const cells = designer.getWorkbook().getWorksheets().get(0).getCells();

    // Set Cell Values
    cells.get("A1").putValue("Name");
    cells.get("B1").putValue("Age");

    // Set markers
    cells.get("A2").putValue("&=Person.Name");
    cells.get("B2").putValue("&=Person.Age");

    // Create Array list
    const list = [];

    // Add custom objects to the list
    list.push(new Person("Simon", 30));
    list.push(new Person("Johnson", 33));

    // Add designer's datasource
    designer.setDataSource("Person", list);

    // Process designer
    await designer.process(false);
    let outputFilePath = path.join(dataDir, "result.out.xls");
    // Save the resultant file
    await designer.getWorkbook().saveAsync(outputFilePath);

    console.log("\nProcess completed successfully.\nFile saved at " + outputFilePath);
}

run().catch(console.error);
```  
  
