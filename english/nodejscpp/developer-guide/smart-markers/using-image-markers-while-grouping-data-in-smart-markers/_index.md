---  
title: Using Image Markers while Grouping Data in Smart Markers with Node.js via C++  
linktitle: Using Image Markers while Grouping Data in Smart Markers  
type: docs  
weight: 30  
url: /nodejs-cpp/using-image-markers-while-grouping-data-in-smart-markers/  
description: Learn how to use image markers in smart markers while grouping data with Aspose.Cells for Node.js via C++.  
---  

## **Using Image Markers while Grouping Data in Smart Markers**  
The following sample creates a workbook and then adds the following smart marker tags in cells D2, E2 and F2 respectively.  

{{< highlight javascript >}}  
 &=Person.Name(group:normal,skip:1)  

&=Person.City  

&=Person.Photo(Picture:FitToCell)  
{{< /highlight >}}  

Then it fills the data source with data and calls the [WorkbookDesigner.process()](https://reference.aspose.com/cells/nodejs-cpp/workbookdesigner/#process) method to process smart marker tags. The code uses these images i.e [moon.png](5115492.png) and [moon2.png](5115491.png) but you can use any image.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

class Person {
constructor(name, city, photo) {
this._name = name;
this._city = city;
this._photo = photo;
}

get Name() {
return this._name;
}

set Name(value) {
this._name = value;
}

get City() {
return this._city;
}

set City(value) {
this._city = value;
}

get Photo() {
return this._photo;
}

set Photo(value) {
this._photo = value;
}
}

async function run() {
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Get the images
const photo1 = fs.readFileSync(path.join(dataDir, "moon.png"));
const photo2 = fs.readFileSync(path.join(dataDir, "moon2.png"));

// Create a new workbook and access its worksheet
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

// Set the standard row height to 35
worksheet.getCells().setStandardHeight(35);

// Set column widths of D, E and F
worksheet.getCells().setColumnWidth(3, 20);
worksheet.getCells().setColumnWidth(4, 20);
worksheet.getCells().setColumnWidth(5, 40);

// Add the headings in columns D, E and F
worksheet.getCells().get("D1").putValue("Name");
let st = worksheet.getCells().get("D1").getStyle();
st.getFont().setIsBold(true);
worksheet.getCells().get("D1").setStyle(st);

worksheet.getCells().get("E1").putValue("City");
worksheet.getCells().get("E1").setStyle(st);

worksheet.getCells().get("F1").putValue("Photo");
worksheet.getCells().get("F1").setStyle(st);

// Add smart marker tags in columns D, E, F
worksheet.getCells().get("D2").putValue("&=Person.Name(group:normal,skip:1)");
worksheet.getCells().get("E2").putValue("&=Person.City");
worksheet.getCells().get("F2").putValue("&=Person.Photo(Picture:FitToCell)");

// Create Persons objects with photos
const persons = [
new Person("George", "New York", photo1),
new Person("George", "New York", photo2),
new Person("George", "New York", photo1),
new Person("George", "New York", photo2),
new Person("Johnson", "London", photo2),
new Person("Johnson", "London", photo1),
new Person("Johnson", "London", photo2),
new Person("Simon", "Paris", photo1),
new Person("Simon", "Paris", photo2),
new Person("Simon", "Paris", photo1),
new Person("Henry", "Sydney", photo2),
new Person("Henry", "Sydney", photo1),
new Person("Henry", "Sydney", photo2)
];

// Create a workbook designer
const designer = new AsposeCells.WorkbookDesigner(workbook);

// Set the data source and process smart marker tags
designer.setDataSource("Person", persons);
designer.process();

// Save the workbook
await workbook.saveAsync(path.join(dataDir, "UsingImageMarkersWhileGroupingDataInSmartMarkers.xlsx"), AsposeCells.SaveFormat.Xlsx);
}
```  
  