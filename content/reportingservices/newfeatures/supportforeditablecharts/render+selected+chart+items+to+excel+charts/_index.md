---
title : "Render Selected Chart Items to Excel Charts" 
description : "" 
weight : 12033 
toc : false
type: docs
url: /reportingservices/newfeatures/supportforeditablecharts/render+selected+chart+items+to+excel+charts/
---

# Aspose.Cells for Reporting Services : Render Selected Chart Items to Excel Charts


To render only some charts in a report to Excel charts:

1.  Open the **Aspose.Cells.ReportingServices.xml** file.
2.  Modify the configuration parameters of the **Aspose.Cells.ReportingServices.xml** file.
3.  Add the desired report configuration information.
4.  Add the information for the chart items you don’t want to export as editable charts. These items are exported as static images.

For example:

{{< code lang="cs" >}}
<Chart >
<Report name= "Employee Sales Summary 2008">
<ChartItem name="Chart1" type="image"/>
</Report >
</Chart> 
{{< /code >}}

**A chart exported as an image**  
![image](https://docs2.aspose.com/cells/reportingservices/attachments/6094931/6193413.png)

**A chart exported as an editable Excel chart**  
![image](https://docs2.aspose.com/cells/reportingservices/attachments/6094931/6193412.png)

