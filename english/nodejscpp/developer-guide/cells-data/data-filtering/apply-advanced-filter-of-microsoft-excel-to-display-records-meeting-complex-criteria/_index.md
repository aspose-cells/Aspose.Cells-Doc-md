---  
title: Apply Advanced Filter of Microsoft Excel to Display Records Meeting Complex Criteria with Node.js via C++  
type: docs  
weight: 280  
url: /nodejs-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/  
description: Learn how to apply advanced filter of Microsoft Excel to display records meeting complex criteria by using the Aspose.Cells for Node.js via C++ API.  
keywords: Apply Advanced Filter Node.js via C++, Set Advanced Filter Node.js via C++, Add Advanced Filter Node.js via C++, Create Advanced Filter Node.js via C++, How to add Advanced Filter to a range Node.js via C++  
---  

## **Possible Usage Scenarios**  

Microsoft Excel allows you to apply *Advanced Filter* on worksheet data to display records that meet complex criteria. You can apply Advanced Filter with Microsoft Excel via its *Data > Advanced* command as shown in this screenshot.  

![todo:image_alt_text](1.png)  

Aspose.Cells for Node.js via C++ also allows you to apply the Advanced Filter using the [**Worksheet.advancedFilter()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/methods/advancedfilter) method. Just like Microsoft Excel, it accepts the following parameters.  

**isFilter**  

Indicates whether filtering the list in place.  

**listRange**  

The list range.  

**criteriaRange**  

The criteria range.  

**copyTo**  

The range where copying data to.  

**uniqueRecordOnly**  

Only displaying or copying unique rows.  

## **Apply Advanced Filter of Microsoft Excel to Display Records Meeting Complex Criteria**  

The following sample code applies the advanced filter on the [Sample Excel File](48496692.xlsx) and generates the [Output Excel File](48496691.xlsx). The screenshot shows both files for comparison. As you can see inside the screenshot, data has been filtered inside the output Excel file according to complex criteria.  

![todo:image_alt_text](2.png)  

## **Sample Code**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Load your source workbook
const wb = new AsposeCells.Workbook(path.join(sourceDir, "sampleAdvancedFilter.xlsx"));

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Apply advanced filter on range A5:D19 and criteria range is A1:D2
// Besides, we want to filter in place
// And, we want all filtered records not just unique records
ws.advancedFilter(true, "A5:D19", "A1:D2", "", false);

// Save the workbook in xlsx format
wb.save(path.join(outputDir, "outputAdvancedFilter.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  
  