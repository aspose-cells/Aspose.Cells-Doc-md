---  
title: Export DataBar, ColorScale and IconSet Conditional Formatting while Excel to HTML Conversion with Node.js via C++  
linktitle: Export DataBar, ColorScale and IconSet Conditional Formatting while Excel to HTML Conversion  
type: docs  
weight: 30  
url: /nodejs-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}} 

You can export DataBar, ColorScale and IconSet Conditional Formatting while converting your Excel file into HTML. This feature is partially supported by Microsoft Excel but Aspose.Cells for Node.js via C++ supports it fully.

{{% /alert %}}  

## **Export DataBar, ColorScale and IconSet Conditional Formatting while Excel to HTML Conversion**  
The following screenshot shows the [sample excel file](5115558.xlsx) with DataBar, ColorScale and IconSet Conditional Formatting. You can download the [sample excel file](5115558.xlsx) from the given link.  

![todo:image_alt_text](conversion_1.png)  

The following screenshot shows the Aspose.Cells output HTML file showing DataBar, ColorScale and IconSet Conditional Formatting. As you can see, it looks exactly like [sample excel file](5115558.xlsx).  

![todo:image_alt_text](conversion_2.png)  

### **Sample Code**  
The following sample code converts the sample excel file into HTML which is just a normal [Excel to HTML conversion](/cells/nodejs-cpp/convert-workbook-to-different-formats/#convertworkbooktodifferentformats-convertingexcelworkbooktohtml).  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save it in HTML format
wb.save(path.join(dataDir, "ConvertingToHTMLFiles_out.html"), AsposeCells.SaveFormat.Html);
```  

  
{{< app/cells/assistant language="nodejs-cpp" >}}
