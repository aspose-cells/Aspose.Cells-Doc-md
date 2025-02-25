---  
title: Show and Hide Worksheets and Tabs with Node.js via C++  
linktitle: Show and Hide Worksheets and Tabs  
type: docs  
weight: 10  
url: /nodejs-cpp/show-and-hide-worksheets-and-tabs/  
description: This article provides sample code for using the Node.js API or Node.js Library to programmatically display and hide an Excel worksheet. Additionally, how to show and hide Excel workbook tabs.  
---  

{{% alert color="primary" %}}  
Aspose.Cells allows the user to show and hide elements of a workbook including worksheets and tabs.  
{{% /alert %}}  

## **Show and Hide a Worksheet**  

An Excel file can have one or more than one worksheets. Whenever we create an Excel file, we add worksheets to the Excel file in which we work. Each worksheet in an Excel file is independent from the other worksheet by having its own data and formatting settings etc. Sometimes, developers may require to make few worksheets hidden and others visible in the Excel file for their own interest. So, **Aspose.Cells** allows developers to control the visibility of the worksheets in their Excel files.  

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#worksheets) collection that allows access to each worksheet in the Excel file.  

A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides a wide range of properties and methods to manage worksheets. To control a worksheet's visibility, use the [**isVisible**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible) property of the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. [**isVisible**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible) is a Boolean property, which means that it can only store a **true** or **false** value.  

### **Making a Worksheet Visible**  

Make a worksheet visible by setting the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class' [**isVisible**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible) property to **true**.  

### **Hiding a Worksheet**  

Hide a worksheet by setting the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class' [**isVisible**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#isVisible) property to **false**.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fs = require("fs");
const fstream = fs.createReadStream(filePath);

// Instantiating a Workbook object with opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the first worksheet of the Excel file
worksheet.setIsVisible(false);

// Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
fstream.close();
```  

## **Show and Hide Tabs**  

If you closely look at the bottom of a Microsoft Excel file, you will see a number of controls. These include:  

- Sheet tabs.  
- Tab scrolling buttons.  

Sheet tabs represent the worksheets in the Excel file. Click any tab to switch to that worksheet. The more worksheets in the workbook, the more sheet tabs there are. If the Excel file has a good number of worksheets you need buttons to navigate through them. So, Microsoft Excel provides tab scrolling buttons for scrolling through the sheet tabs.  

Using Aspose.Cells, developers can control the visibility of sheet tabs and tabs scrolling buttons in Excel files.  

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook), that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class provides a wide range of properties and methods to manage an Excel file. To control the visibility of tabs in an Excel file, developers can use the [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class' [**workbookSettings.showTabs**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#showTabs) property. [**workbookSettings.showTabs**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#showTabs) is a Boolean property, which means that it can only store a **true** or **false** value.  

### **Making Tabs Visible**  

Make tabs visible with the [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class' [**workbookSettings.showTabs**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#showTabs) property to **true**.  

### **Hiding Tabs**  

Hide tabs in an Excel file by setting the [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class' [**workbookSettings.showTabs**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#showTabs) property to **false**.  

Below is a complete example that opens an Excel file (book1.xls), hides its tabs and saves the modified file as output.xls. After the code execution, you will see that the tabs of the workbook are hidden.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Opening the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Hiding the tabs of the Excel file
workbook.getSettings().setShowTabs(false);

// Shows the tabs of the Excel file
// workbook.getSettings().setShowTabs(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```  

### **Controlling the Tab Bar Width**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Loading the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Hiding the tabs of the Excel file
workbook.getSettings().setShowTabs(true);

// Adjusting the sheet tab bar width
workbook.getSettings().setSheetTabBarWidth(800);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls")); 
```  
  