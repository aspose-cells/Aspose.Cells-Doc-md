---
title: Set custom DataSource for WorkbookDesigner with Node.js via C++
linktitle: Set custom DataSource for WorkbookDesigner
type: docs
weight: 60
url: /nodejs-cpp/set-custom-datasource-for-workbookdesigner/
description: Learn how to set a custom DataSource for WorkbookDesigner using Aspose.Cells for Node.js via C++. 
---

Aspose.Cells provides the option to set a custom DataSource for WorkbookDesigner. The API provides an overloaded method [WorkbookDesigner.setDataSource](https://reference.aspose.com/cells/nodejs-cpp/workbookdesigner/#setDataSource-string-object-) which takes the name of the source as the first parameter and the instance of the class that implements [ICellsDataTable](https://reference.aspose.com/cells/nodejs-cpp/icellsdatatable/) as the second parameter.

The following code snippet demonstrates the use of [WorkbookDesigner.setDataSource](https://reference.aspose.com/cells/nodejs-cpp/workbookdesigner/#setDataSource-string-object-) method to set the custom DataSource.
## **Sample Code**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const sourceDir = RunExamples.Get_SourceDirectory();
const outputDir = RunExamples.Get_OutputDirectory();

const customers = [];
customers.push(new Customer("Thomas Hardy", "120 Hanover Sq., London"));
customers.push(new Customer("Paolo Accorti", "Via Monte Bianco 34, Torino"));

const filePath = path.join(sourceDir, "SmartMarker1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const designer = new AsposeCells.WorkbookDesigner(workbook);

designer.setDataSource("Customer", new CustomerDataSource(customers));

designer.process();

workbook.save(path.join(outputDir, "dest.xlsx"));
```

The implementation of *CustomerDataSource*, *Customer*, and *CustomerList* classes is given below

```javascript
class CustomerDataSource {
    constructor(customers) {
        this.m_DataSource = customers;
        this.m_Properties = Object.keys(customers[0]);
        this.m_Columns = this.m_Properties;
        this.m_PropHash = new Map(this.m_Properties.map(prop => [prop, prop]));
        this.m_IEnumerator = customers.values();
    }

    get Columns() {
        return this.m_Columns;
    }

    get Count() {
        return this.m_DataSource.length;
    }

    BeforeFirst() {
        this.m_IEnumerator = this.m_DataSource.values();
    }

    get(index) {
        const current = this.m_IEnumerator.next().value;
        return current[this.m_Properties[index]];
    }

    getByColumnName(columnName) {
        const current = this.m_IEnumerator.next().value;
        return current[this.m_PropHash.get(columnName)];
    }

    Next() {
        if (this.m_IEnumerator == null) return false;
        return this.m_IEnumerator.next().done === false;
    }
}

class Customer {
    constructor(aFullName, anAddress) {
        this.FullName = aFullName;
        this.Address = anAddress;
    }
}

class CustomerList extends Array {
    constructor(...args) {
        super(...args);
    }

    get(index) {
        return this[index];
    }

    set(index, value) {
        this[index] = value;
    }
}
```

The source and output excel files are attached for reference.

[Source File](95584319.xlsx)

[Output File](95584320.xlsx)
