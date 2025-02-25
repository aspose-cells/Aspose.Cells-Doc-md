---  
title: Smartly importing and placing data with Smart markers via Node.js  
linktitle: Smart markers  
type: docs  
weight: 190  
url: /nodejs-cpp/using-smart-markers/  
description: Smartly importing and placing data according to the template Excel files with Aspose.Cells library for Node.js via C++.  
---  


## **Introduction**  
**Smart markers** are used to let Aspose.Cells know what information to place in a Microsoft Excel designer spreadsheet. Smart markers allow you to create templates that contain only specific information and formatting.  
## **Designer Spreadsheet & Smart Markers**  
Designer spreadsheets are standard Excel files that contain visual formatting, formulas, and smart markers. They can contain smart markers that reference one or more data source, such as information from a project and information for related contacts. Smart markers are written into the cells where you want the information.  

All smart markers start with &=. An example of a data marker is &=Party.FullName. If the data marker results in more than one item, for example, a complete row, then the following rows are moved down automatically to make room for the new information. Thus sub-totals and totals can be placed on the row immediately after the data marker to make calculations based on the inserted data. To make calculations on the inserted rows, use **dynamic formulas**.  

Smart markers consist of the **data source** and **field name** parts for most information. Special information may also be passed with variables and variable arrays. Variables always fill only one cell whereas variable arrays may fill several. Only use one data marker per cell. Unused smart markers are removed.  

Smart marker may also contain parameters. Parameters allow you to modify how the information is laid out. They are appended to the end of the smart marker in parentheses as a comma-separated list.  
### **Smart Marker Options**  
&=DataSource.FieldName  
&=[Data Source].[Field Name]  
&=$VariableName  
&=$VariableArray  
&==DynamicFormula  
&=&=RepeatDynamicFormula  
### **Parameters**  
The following parameters are allowed:  

- **noadd** - Do not add extra rows to fit data.  
- **skip:n** - Skip n number of rows for each row of data.  
- **ascending:n** or **descending:n** - Sort data in smart markers. If n is 1, then the column is the first key of the sorter. The data is sorted after processing the data source. For example: &=Table1.Field3(ascending:1).  
- **horizontal** - Write data left-to-right, instead of top-to-bottom.  
- **numeric** - Convert text to number if possible.  
- **shift** - Shift down or right, creating extra rows or columns to fit data. The shift parameter works the same way as in Microsoft Excel. For example in Microsoft Excel, when you select a range of cells, right-click and select **Insert** and specify **shift cells down**, **shift cells right** and other options. In short, the **shift** parameter fills the same function for vertical/normal (top to bottom) or horizontal (left to right) smart markers.  
- **copystyle** - Copy the base cell's style to all the cells in that column.  

The parameters noadd and skip can be combined to insert data on alternating rows. Because the template is processed from bottom to top, you should add noadd on the first row to avoid extra rows from being inserted before the alternate row.  

If you have multiple parameters, separate them with a commas, but no space: parameterA,parameterB,parameterC  

The following screenshots show how to insert data on every other row.  

|**Template File**|**Output File**|  
| :- | :- |  
|![todo:image_alt_text](using-smart-markers_1.jpg)|![todo:image_alt_text](using-smart-markers_2.jpg)|  
### **Dynamic Formulas**  
Dynamic formulas allow you to insert Excel formulas into cells even when the formula references rows that will be inserted during the export process. Dynamic formulas can repeat for each inserted row or use only the cell where the data marker is placed.  

Dynamic formulas allow the following additional options:  

- r - Current row number.  
- 2, -1 - Offset to current row number.  

For example:  

{{< highlight javascript >}}  
&=&=B{-1}/C{-1}~(skip:1)  
{{< /highlight >}}  

In the dynamic formula marker, "-1" denotes the offset to the current row in B and C columns respectively which will be set for division operation, the skip parameter is one row. Moreover, we should specify the following char:  

{{< highlight javascript >}}  
"~"  
{{< /highlight >}}  

as a separator character to apply further parameters in dynamic formulas.  

The following screenshots illustrate a repeating dynamic formula and the resulting Excel worksheet.  

|**Template File**|**OutPut File**|  
| :- | :- |  
|![todo:image_alt_text](using-smart-markers_3.jpg)|![todo:image_alt_text](using-smart-markers_4.jpg)|  
Cell "C1" contains the formula **= A1*B1**, cell "C2" contains **= A2*B2** and cell "C3" contains **= A3*B3**.  

It's very easy to process the smart markers. The following example code shows how to use dynamic formulas in Smart Markers. We load the [template file](templateDynamicFormulas.xlsx) and create test data, process the markers to fill data into the cells against the marker.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create directory if it is not already present.
const fs = require("fs");
if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir);
}

// Set the file path of designer spreadsheet containing smart markers
const designerFile = "templateDynamicFormulas.xlsx";

// Create your data set
const dataset = {
    Answer: []
};

// Define columns
const price = { name: "Price", type: "double" };
const amount = { name: "Amount", type: "int" };

// Add columns to dataset
dataset.Answer.push(price, amount);

// Add data rows
dataset.Answer.push({ Price: 100.00, Amount: 2 });
dataset.Answer.push({ Price: 75.25, Amount: 3 });
dataset.Answer.push({ Price: 25.00, Amount: 5 });

if (designerFile != null) {
    // Instantiating a WorkbookDesigner object
    const designer = new AsposeCells.WorkbookDesigner();

    // Open a designer spreadsheet containing smart markers
    designer.setWorkbook(new AsposeCells.Workbook(designerFile));

    // Set the data source for the designer spreadsheet
    designer.setDataSource(dataset);

    // Process the smart markers
    designer.process();
}
```  

## **Using Variable Arrays**  
The following example code shows how to use variable arrays in Smart Markers. We place a variable array marker into A1 cell of the first worksheet of the workbook dynamically which contains string values which we set for the marker, process the markers to fill data into the cells against the marker. Finally, we save the Excel file.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook designer.
const report = new AsposeCells.WorkbookDesigner();

// Get the first worksheet of the workbook.
const w = report.getWorkbook().getWorksheets().get(0);

// Set the Variable Array marker to a cell.
// You may also place this Smart Marker into a template file manually in Ms Excel and then open this file via Workbook.
w.getCells().get("A1").putValue("&=$VariableArray");

// Set the DataSource for the marker(s).
report.setDataSource("VariableArray", ["English", "Arabic", "Hindi", "Urdu", "French"]);

// Process the markers.
report.process(false);

// Save the Excel file.
report.getWorkbook().save(path.join(dataDir, "output.xlsx"));
```  
## **Grouping Data**  
In some Excel reports, you might need to break the data into groups to make it easier to read and analyze. One of the primary purposes for breaking data into groups is to run calculations (perform summary operations) on each group of records.  

Aspose.Cells smart markers allow you to group data by fields and place summary rows in between data sets or data groups. For example, if grouping data by Customers.CustomerID, you can add a summary record every time the group changes.  
### **Parameters**  
Following are some of the smart marker parameters used for grouping data.  
#### **group:normal/merge/repeat**  
We support three types of group that you can choose between.  

- **normal** - The group by field(s) value is not repeated for the corresponding records in the column; instead, they are printed once per data group.  
- **merge** - The same behavior as for the normal parameter, except that it merges the cells in the group by field(s) for each group set.  
- **repeat** - The group by field(s) value is repeated for the corresponding records.  

For example: &=Customers.CustomerID(group:merge)  
#### **skip**  
Skips a specified number of rows after each group.  

For example, &=Employees.EmployeeID(group:normal,skip:1)  
#### **subtotalN**  
Performs a summary operation for a specified field data related to a group by field. The N represents numbers between 1 and 11 which specify the function used when calculating subtotals within a list of data. (1=AVERAGE, 2=COUNT, 3=COUNTA, 4=MAX, 5=MIN,...9=SUM etc.) Refer to the Subtotal reference in Microsoft Excel's help for further details.  

The format actually states as:  
subtotalN:Ref where Ref refers to the group by column.  

For example,  

- &=Products.Units(subtotal9:Products.ProductID) specifies summary function upon **Units** field with respect to the **ProductID** field in the **Products** table.  
- &=Tabx.Col3(subtotal9:Tabx.Col1) specifies summary function upon the **Col3** field group by **Col1** in the table **Tabx**.  
- &=Table1.ColumnD(subtotal9:Table1.ColumnA&Table1.ColumnB) specifies summary function upon **ColumnD** field group by **ColumnA** and **ColumnB** in the table **Table1**.  

This example shows some of the grouping parameters in action. It uses the Northwind.mdb Microsoft Access database and extract data from the table named "Order Details". We create a designer file called SmartMarker_Designer.xls in Microsoft Excel and put smart markers into various cells in worksheets. The markers are processed to fill the worksheets. The data is placed and organized by a group field.  

The designer file has two worksheets. In the first, we put smart markers with grouping parameters as shown in the screenshot below. Three smart markers (with grouping parameters) are placed:  
&=[Order Details].OrderID(group:merge,skip:1),  
&=[Order Details].Quantity(subtotal9:Order Details.OrderID), and  
&=[Order Details].UnitPrice(subtotal9:Order Details.OrderID) go into A5, B5 and C5 respectively.  

|**The first worksheet in the SmartMarker_Designer.xls file, complete with smart markers**|  
| :- |  
|![todo:image_alt_text](using-smart-markers_5.png)|  
In the second worksheet of the designer file, we put some more smart markers as shown in the figure below. We place the following smart markers:  
&=[Order Details].OrderID(group:normal),  
&=[Order Details].Quantity,  
&=[Order Details].UnitPrice,  
&=&=B(r)*C(r), and  
&=subtotal9:Order Details.OrderID into A5, B5, C5, D5 and C6 respectively.  

|**The second worksheet of the SmartMarker_Designer.xls file, showing mixed smart markers.**|  
| :- |  
|![todo:image_alt_text](using-smart-markers_6.png)|  
Here is the source code used in the example.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");
const { WorkbookDesigner } = require("aspose.cells.node");

function smartMarkersGroupingData() {
    const dataDir = path.join(__dirname, "data");

    // Create a connection object, specify the provider info and set the data source.
    const con = new OleDbConnection(`provider=microsoft.jet.oledb.4.0;data source=${dataDir}/Northwind.mdb`);

    // Open the connection object.
    con.open();

    // Create a command object and specify the SQL query.
    const cmd = new OleDbCommand("Select * from [Order Details]", con);

    // Create a data adapter object.
    const da = new OleDbDataAdapter();

    // Specify the command.
    da.SelectCommand = cmd;

    // Create a dataset object.
    const ds = new DataSet();

    // Fill the dataset with the table records.
    da.Fill(ds, "Order Details");

    // Create a datatable with respect to dataset table.
    const dt = ds.getTables().get("Order Details");

    // Create WorkbookDesigner object.
    const wd = new WorkbookDesigner();

    // Open the template file (which contains smart markers).
    wd.Workbook = new AsposeCells.Workbook(path.join(dataDir, "Designer.xlsx"));

    // Set the datatable as the data source.
    wd.setDataSource(dt);

    // Process the smart markers to fill the data into the worksheets.
    wd.process(true);

    // Save the excel file.
    wd.Workbook.save(path.join(dataDir, "output.xlsx"));
}

class OleDbCommand {
    constructor(query, connection) {
        this.query = query;
        this.connection = connection;
    }
}

class OleDbConnection {
    constructor(connectionString) {
        this.connectionString = connectionString;
    }

    open() {
        // Implement connection opening logic if needed
    }
}

class OleDbDataAdapter {
    constructor() {
        this.SelectCommand = null;
    }

    fill(dataSet, tableName) {
        // Logic to fill dataset with records
    }
}
```  

{{% alert color="primary" %}}  
If you need to add your own custom labels to the Summary rows or you want to concatenate the field's name with a label, e.g "Subtotal of Orders", Aspose.Cells provides you Label and LabelPosition attributes, so you may place your custom labels in the Smart Markers while concatenating with the Subtotal rows in grouping data. See the document on how to Add Custom Labels to Concatenate with the Subtotal Rows in Smart Markers for your reference.  
{{% /alert %}}  
## **Using Anonymous Types or Custom Objects**  
Aspose.Cells also supports anonymous types or custom objects in smart markers. The example that follows shows how this works. For importing data from dynamic objects using Smart Markers, visit the following article:  

[Importing from dynamic object as data source](/cells/nodejs-cpp/import-data-into-worksheet/#importdataintoworksheet-importingfromdynamicobjectasdatasource)  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Smart Marker Customobjects.xls");

// Instantiate the workbookdesigner object.
const report = new AsposeCells.WorkbookDesigner();
// Get the first worksheet(default sheet) in the workbook.
const sheet = report.getWorkbook().getWorksheets().get(0);

// Input some markers to the cells.
sheet.getCells().get("A1").putValue("Name");
sheet.getCells().get("B1").putValue("Age");
sheet.getCells().get("A2").putValue("&=MyProduct.Name");
sheet.getCells().get("B2").putValue("&=MyProduct.Age");

// Instantiate the list collection based on the custom class.
const list = [];
// Provide values for the markers using the custom class object.
list.push(new Person("Simon", 30));
list.push(new Person("Johnson", 33));

// Set the data source.
report.setDataSource("MyProduct", list);

// Process the markers.
report.process(false);

// Save the excel file.
report.getWorkbook().save(filePath);

// Definition of Custom class.
class Person {
    constructor(name, age) {
        this.m_Name = name;
        this.m_Age = age;
    }
    
    get Name() {
        return this.m_Name;
    }

    set Name(value) {
        this.m_Name = value;
    }

    get Age() {
        return this.m_Age;
    }

    set Age(value) {
        this.m_Age = value;
    }
}
```  
## **Image Markers**  
Aspose.Cells smart markers support image markers too. This section shows you how to insert pictures using smart markers.  
### **Image Parameters**  
Smart marker parameters for managing images.  

- **Picture:FitToCell** - Auto-fit the image to the cell’s row height and column width.  
- **Picture:ScaleN** - Scale height and width to N percent.  
- **Picture:Width:Nin&Height:Nin** - Render the image N inches high and N inches wide. You can also specify Left and Top positions (in points).  

Here is the source code used in the example.  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Get the image data.
let imageData = fs.readFileSync(path.join(dataDir, "aspose-logo.jpg"));
// Create a datatable.
let t = new AsposeCells.DataTable("Table1");
// Add a column to save pictures.
let dc = t.getColumns().add("Picture");
// Set its data type.
dc.setDataType(Object);

// Add a new record to it.
let row = t.newRow();
row.set(0, imageData);
t.getRows().add(row);

// Add another record (having picture) to it.
imageData = fs.readFileSync(path.join(dataDir, "image2.jpg"));
row = t.newRow();
row.set(0, imageData);
t.getRows().add(row);

// Create WorkbookDesigner object.
let designer = new AsposeCells.WorkbookDesigner();
// Open the template Excel file.
designer.setWorkbook(new AsposeCells.Workbook(path.join(dataDir, "TestSmartMarkers.xlsx")));
// Set the datasource.
designer.setDataSource(t);
// Process the markers.
designer.process();
// Save the Excel file.
designer.getWorkbook().save(path.join(dataDir, "output.xls"));
```  
## **Using Nested Objects**  
Aspose.Cells supports nested objects in smart markers, the nested objects should be simple. We use a simple template file. See the designer spreadsheet that contains some nested smart markers.  

|**The first worksheet of the SM_NestedObjects.xlsx file showing nested smart markers.**|  
| :- |  
|![todo:image_alt_text](using-smart-markers_7.png)|  
The example that follows shows how this works.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SM_NestedObjects.xlsx");

// ****** Program ******
// Initialize WorkbookDesigner object
const designer = new AsposeCells.WorkbookDesigner();
// Load the template file
designer.setWorkbook(new AsposeCells.Workbook(filePath));

// Instantiate the list based on the class
const list = [];

// Create an object for the Individual class
const p1 = new Individual("Damian", 30);
// Create the relevant Wife class for the Individual
p1.Wife = new Wife("Dalya", 28);

// Create another object for the Individual class
const p2 = new Individual("Mack", 31);
// Create the relevant Wife class for the Individual
p2.Wife = new Wife("Maaria", 29);

// Add the objects to the list
list.push(p1);
list.push(p2);

// Specify the DataSource
designer.setDataSource("Individual", list);
// Process the markers
designer.process(false);
// Save the Excel file.
designer.getWorkbook().save(path.join(dataDir, "output.xlsx"));

class Individual {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    get Name() {
        return this.name;
    }

    set Name(value) {
        this.name = value;
    }

    get Age() {
        return this.age;
    }

    set Age(value) {
        this.age = value;
    }

    get Wife() {
        return this.wife;
    }

    set Wife(value) {
        this.wife = value;
    }
}

class Wife {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    get Name() {
        return this.name;
    }

    set Name(value) {
        this.name = value;
    }

    get Age() {
        return this.age;
    }

    set Age(value) {
        this.age = value;
    }
}
```  
## **Using JSON Data**  
Aspose.Cells supports JSON data in smart markers; JSON data can be nested hierarchically. Please check the [template file](smartmarker.xlsx), [JSON file](smartmarker.json) and the screenshot of the output Excel file generated with the following code.  

|**The first worksheet of the smartmarker.xlsx file showing smart markers.**|  
| :- |  
|![todo:image_alt_text](jsontemplate.png)|  

|**The screenshot of the output Excel file.**|  
| :- |  
|![todo:image_alt_text](jsonresult.png)|  

JSON data as follows:  
```json data  
{  
    "EntityCin" : "EntityCin Test",  
    "EntityName" : "EntityName Test",  
    "FirstName" : "FirstName Test",  
    "MiddleName" : "MiddleName Test",  
    "LastName" : "LastName Test",  
    "DOB" : "2025-02-08",  
    "SSN" : "11111111",  
    "Directors" : [  
        {  
            "id" : "director id 1",  
            "FirstName" : "director first 1",  
            "MiddleName" : "director middle 1",  
            "LastName" : "director last 1",  
            "Reportees" : [  
                {  
                    "id" : "aaa",  
                    "FirstName" : "first aaa",  
                    "MiddleName" : "middle aaa",  
                    "LastName" : "last aaa",  
                    "Department" : "aaa department",  
                    "City" : "aaa city",  
                    "GST" : "Yes",  
                    "ITR" : "No"  
                },  
                {  
                    "id" : "bbb",  
                    "FirstName" : "first bbb",  
                    "MiddleName" : "middle bbb",  
                    "LastName" : "last bbb",  
                    "Department" : "bbb department",  
                    "City" : "bbb city",  
                    "GST" : "Yes",  
                    "ITR" : "Yes"  
                },  
                {  
                    "id" : "ccc",  
                    "FirstName" : "first ccc",  
                    "MiddleName" : "middle ccc",  
                    "LastName" : "last ccc",  
                    "Department" : "ccc department",  
                    "City" : "ccc city",  
                    "GST" : "No",  
                    "ITR" : "No"  
                }  
            ]  
        },  
        {  
            "id" : "director id 2",  
            "FirstName" : "director first 2",  
            "MiddleName" : "director middle 2",  
            "LastName" : "director last 2",  
            "Reportees" : [  
                {  
                    "id" : "eee",  
                    "FirstName" : "first eee",  
                    "MiddleName" : "middle eee",  
                    "LastName" : "last eee",  
                    "Department" : "eee department",  
                    "City" : "eee city",  
                    "GST" : "Yes",  
                    "ITR" : "No"  
                },  
                {  
                    "id" : "fff",  
                    "FirstName" : "first fff",  
                    "MiddleName" : "middle fff",  
                    "LastName" : "last fff",  
                    "Department" : "fff department",  
                    "City" : "fff city",  
                    "GST" : "No",  
                    "ITR" : "No"  
                }  
            ]  
        }  
    ]  
}  
```  
The example that follows shows how this works.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "smartmarker.xlsx");

// Load the workbook
const wb = new AsposeCells.Workbook(filePath);
wb.getWorksheets().get(0).getCells().createRange("A2:H14").setName("_CellsSmartMarkers");

const designer = new AsposeCells.WorkbookDesigner();
designer.setLineByLine(false);
designer.setWorkbook(wb);
designer.setJsonDataSource("RootData", require("fs").readFileSync(path.join(dataDir, "smartmarker.json"), "utf8"));
designer.process(true);

wb.save(path.join(dataDir, "out.xlsx"));
```  
## **Using Generic List as Nested Object**  
Aspose.Cells now also supports using generic list as a nested object. Please check the screenshot of the output Excel file generated with the following code. As you can see in the screenshot, a Teacher object contains multiple nested Student objects.  

|![todo:image_alt_text](using-smart-markers_8.png)|  
| :- |  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Create a designer workbook
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Teacher Name");
worksheet.getCells().get("A2").putValue("&=Teacher.Name");

worksheet.getCells().get("B1").putValue("Teacher Age");
worksheet.getCells().get("B2").putValue("&=Teacher.Age");

worksheet.getCells().get("C1").putValue("Student Name");
worksheet.getCells().get("C2").putValue("&=Teacher.Students.Name");

worksheet.getCells().get("D1").putValue("Student Age");
worksheet.getCells().get("D2").putValue("&=Teacher.Students.Age");

// Apply Style to A1:D1
const range = worksheet.getCells().createRange("A1:D1");
const style = workbook.createStyle();
style.getFont().setIsBold(true);
style.setForegroundColor(AsposeCells.Color.Yellow);
style.setPattern(AsposeCells.BackgroundType.Solid);
const flag = new AsposeCells.StyleFlag();
flag.setAll(true);
range.applyStyle(style, flag);

// Initialize WorkbookDesigner object
const designer = new AsposeCells.WorkbookDesigner();

// Load the template file
designer.setWorkbook(workbook);

const list = [];

// Create an object for the Teacher class
let h1 = new Teacher("Mark John", 30);
// Create the relevant student objects for the Teacher object
h1.Students = [];
h1.Students.push(new Person("Chen Zhao", 14));
h1.Students.push(new Person("Jamima Winfrey", 18));
h1.Students.push(new Person("Reham Smith", 15));

// Create another object for the Teacher class
let h2 = new Teacher("Masood Shankar", 40);
// Create the relevant student objects for the Teacher object
h2.Students = [];
h2.Students.push(new Person("Karishma Jathool", 16));
h2.Students.push(new Person("Angela Rose", 13));
h2.Students.push(new Person("Hina Khanna", 15));

// Add the objects to the list
list.push(h1);
list.push(h2);

// Specify the DataSource
designer.setDataSource("Teacher", list);

// Process the markers
designer.process();

// Autofit columns
worksheet.autoFitColumns();

// Save the Excel file.
designer.getWorkbook().save(path.join(dataDir, "output.xlsx"));
```  
## **Using HTML property of Smart Markers**  
The following sample code explains the use of the HTML property of the Smart Markers. When it is processed, it will show "World" in "Hello World" as bold because of the HTML <b> tag.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "output.xls");

// Create a new workbook and designer
const workbook = new AsposeCells.Workbook();
const designer = new AsposeCells.WorkbookDesigner();
designer.setWorkbook(workbook);

// Set the value for A1 cell
workbook.getWorksheets().get(0).getCells().get("A1").putValue("&=$VariableArray(HTML)");
designer.setDataSource("VariableArray", ["Hello <b>World</b>", "Arabic", "Hindi", "Urdu", "French"]);

// Process the designer and save the workbook
designer.process();
workbook.save(filePath);
```  
## **Not line by line**  
The current default processing method is to process smart markers line by line. But sometimes the smart markers of the same data table need to be processed together, no matter if they are in the same row or not, then you have to specify a named range "_CellsSmartMarkers" and specify WorkbookDesigner.LineByLine as false before calling the processing.  

|![todo:image_alt_text](using-smart-markers_11.png)|  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const style = workbook.createStyle();
style.setPattern(AsposeCells.BackgroundType.Solid);
style.setForegroundColor(AsposeCells.Color.Black);
style.getFont().setColor(AsposeCells.Color.White);

const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Teacher Name");
worksheet.getCells().get("A1").setStyle(style);
worksheet.getCells().get("A2").putValue("&=Teacher.Name");

worksheet.getCells().get("B1").putValue("Teacher Age");
worksheet.getCells().get("B1").setStyle(style);
worksheet.getCells().get("B2").putValue("&=Teacher.Age");

worksheet.getCells().get("A3").putValue("Student Name");
worksheet.getCells().get("A3").setStyle(style);
worksheet.getCells().get("A4").putValue("&=Teacher.Students.Name");

worksheet.getCells().get("B3").putValue("Student Age");
worksheet.getCells().get("B3").setStyle(style);
worksheet.getCells().get("B4").putValue("&=Teacher.Students.Age");
worksheet.autoFitColumns();

worksheet.getCells().createRange("A1:B4").setName("_CellsSmartMarkers");

// Initialize WorkbookDesigner object
const designer = new AsposeCells.WorkbookDesigner();

// Load the template file
designer.setWorkbook(workbook);

const list = [];

// Create an object for the Teacher class
const h1 = new Teacher("Mark John", 30);

// Create the relevant student objects for the Teacher object
h1.Students = [];
h1.Students.push(new Person("Chen Zhao", 14));
h1.Students.push(new Person("Jamima Winfrey", 18));
h1.Students.push(new Person("Reham Smith", 15));

// Create another object for the Teacher class
const h2 = new Teacher("Masood Shankar", 40);

// Create the relevant student objects for the Teacher object
h2.Students = [];
h2.Students.push(new Person("Karishma Jathool", 16));
h2.Students.push(new Person("Angela Rose", 13));
h2.Students.push(new Person("Hina Khanna", 15));

// Add the objects to the list
list.push(h1);
list.push(h2);

// Specify the DataSource
designer.setDataSource("Teacher", list);
designer.setLineByLine(false);
// Process the markers
designer.process();

// Autofit columns
worksheet.autoFitColumns();

// Save the Excel file.
designer.getWorkbook().save(path.join(dataDir, "output.xlsx"));

class Person {
    constructor(name, age) {
        this.Name = name;
        this.Age = age;
    }
}

class Teacher {
    constructor(name, age) {
        this.Name = name;
        this.Age = age;
        this.Students = [];
    }
}
```  
## **Getting Notifications while Merging Data with Smart Markers**  
Sometimes, it may be required to get notifications about the cell reference or the particular Smart Marker being processed before completion. This can be achieved using the WorkbookDesigner.CallBack property and ISmartMarkerCallBack  

## **Advance topics**  
- [Adding Anonymous or Custom Object into SmartMarkers](/cells/nodejs-cpp/adding-anonymous-or-custom-object-into-smartmarkers/)  
- [Auto Populate Smart Marker Data to Other Worksheets if Data is too Large](/cells/nodejs-cpp/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)  
- [Formatting Smart Markers](/cells/nodejs-cpp/formatting-smart-markers/)  
- [Getting Notifications while Merging Data with Smart Markers](/cells/nodejs-cpp/getting-notifications-while-merging-data-with-smart-markers/)  
- [Set custom DataSource for WorkbookDesigner](/cells/nodejs-cpp/set-custom-datasource-for-workbookdesigner/)  
- [Show leading apostrophe in cells](/cells/nodejs-cpp/show-leading-apostrophe-in-cells/)  
- [Using Formula parameter in Smart Marker field](/cells/nodejs-cpp/using-formula-parameter-in-smart-marker-field/)  
- [Using Image Markers while Grouping Data in Smart Markers](/cells/nodejs-cpp/using-image-markers-while-grouping-data-in-smart-markers/)  

  