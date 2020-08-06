---
title: Read and Manipulate Excel 2016 Charts
type: docs
weight: 20
url: /cpp/read-and-manipulate-excel-2016-charts/
---

## **Possible Usage Scenarios**
Aspose.Cells supports the reading and manipulation of Microsoft Excel 2016 charts which are not present in Microsoft Excel 2013 or earlier versions.
## **Read and Manipulate Excel 2016 Charts**
The following sample code loads the [sample Excel file](attachments/66257152/66519072.xlsx) which contains Excel 2016 charts in the first worksheet. It reads all charts one by one and changes its title as per its chart type. The following screenshot shows the sample Excel file before the execution of the code. As you can see, the chart title is the same for all charts.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_1.png)

The following screenshot shows the [output Excel file](attachments/66257152/66519073.xlsx) after the execution of code. As you can see, the chart title is changed as per its chart type.

![todo:image_alt_text](read-and-manipulate-excel-2016-charts_2.png)
## **Sample Code**
{{< gist "aspose-com-gists" "0edd1c91ebaa6cd099be1200b1ec7480" "Charts-ReadAndManipulateExcel2016Charts.cpp" >}}
## **Console Output**
Here is the console output of the above sample code when executed with the provided sample Excel file.

{{< highlight java >}}

 Waterfall

Treemap

Sunburst

Histogram

BoxWhisker

{{< /highlight >}}
