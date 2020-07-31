---
title : "Using Image Markers while Grouping Data in Smart Markers" 
description : "" 
weight : 12530 
toc : false
type: docs
url: /java/developerguide/technicalarticles/using+image+markers+while+grouping+data+in+smart+markers/
---

# Aspose.Cells for Java : Using Image Markers while Grouping Data in Smart Markers



This article presents an example that illustrates the usage of image markers while grouping data in smart markers.

#### Using Image Markers while Grouping Data in Smart Markers

The following sample code creates a workbook and then adds the following smart marker tags in cells D2, E2 and F2 respectively.

{{< code lang="cs" >}}
&=Person.Name(group:normal,skip:1)
&=Person.City
&=Person.Photo(Picture:FitToCell)
{{< /code >}}

Then it fills the data source with data and call the [WorkbookDesigner.Process()](https://apireference.aspose.com/java/cells/com.aspose.cells/workbookdesigner#process()) method to process smart marker tags. The code uses these images i.e [moon.png](https://docs2.aspose.com/cells/java/attachments/5276312/5472549.png) and [moon2.png](https://docs2.aspose.com/cells/java/attachments/5276312/5472548.png) but you can use any image. The following screenshot shows the output of this sample code. As you can see, the data in column E and F are grouped with respect to the data in column D.

![](https://docs2.aspose.com/cells/java/attachments/5276312/5472547.png)

