---
title: Manage settings of Excel spreadsheet files with Node.js via C++
linktitle: Workbook Settings
type: docs
weight: 185
url: /nodejs-cpp/workbook-settings/
description: Manage settings of Excel files using Aspose.Cells for Node.js via C++.
---


## **Workbook Settings Overview**
Working with Excel files involves various settings that can be manipulated programmatically using Aspose.Cells for Node.js via C++. This document outlines how to manage these settings effectively.

## **Possible Usage Scenarios**
The following scenarios illustrate when you might need to manage workbook settings:
- Adjusting display options
- Setting calculation mode
- Configuring page setup parameters

## **Managing Workbook Settings using Aspose.Cells for Node.js via C++**
This example demonstrates how to manage workbook settings such as calculation options and display settings.

1. Create a new workbook or load an existing one.
2. Modify workbook settings as per your requirements.
3. Save the workbook to persist the changes.

### **Example Code**

```javascript
const { Workbook, SaveFormat } = require('aspose.cells');

// Create a new workbook
let workbook = new Workbook();

// Access the settings of the workbook
let settings = workbook.getSettings();
settings.setCalculationMode(1); // Manual calculation

// Display options
settings.setShowGridLines(false); // Disable gridlines

// Save the workbook
workbook.save('WorkbookSettingsExample.xlsx', SaveFormat.XLSX);
```

## **Key Workbook Settings Properties and Methods**
Aspose.Cells for Node.js provides a number of properties and methods to adjust workbook settings:
- **Workbook.getSettings()**: Accesses the workbook's settings.
- **Settings.setCalculationMode(mode)**: Sets the calculation mode for the workbook.
- **Settings.setShowGridLines(value)**: Enables or disables grid lines on the display.

## **Conclusion**
Managing workbook settings in Aspose.Cells for Node.js via C++ is straightforward and provides numerous options to customize Excel file behaviors. By utilizing the settings available, you can tailor the workbook to fit your specific requirements.

{{< app/cells/assistant language="nodejs-cpp" >}}