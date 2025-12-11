---  
title: Insert Timeline  
linktitle: Timelines  
type: docs  
weight: 170  
url: /nodejs-cpp/create-timeline/  
description: Learn how to create a timeline with Aspose.Cells for Node.js via C++.  
ai_search_scope: cells_nodejscpp  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"  
---  

## **Possible Usage Scenarios**  

Instead of adjusting filters to show dates, you can use a PivotTable Timeline—a dynamic filter option that lets you easily filter by date/time and zoom in on the period you want with a slider control. Microsoft Excel allows you to create a timeline by selecting a pivot table and then clicking *Insert > Timeline*. Aspose.Cells for Node.js via C++ also allows you to create a timeline using the [**Worksheet.getTimelines().add()**](https://reference.aspose.com/cells/nodejs-cpp/timelinecollection/#add-pivottable-number-number-string-) method.  

## **Create Timeline to a Pivot Table**  

Please see the following sample code. It loads the [sample Excel file](input.xlsx) that contains the pivot table. It then creates the timeline based on the first base pivot field. Finally, it saves the workbook in the [output XLSX](output.xlsx) format. The following screenshot shows the timeline created by Aspose.Cells for Node.js via C++ in the output Excel file.  

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)  

### **Sample Code**  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Timelines-CreateTimelineToPivotTable.js" >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
