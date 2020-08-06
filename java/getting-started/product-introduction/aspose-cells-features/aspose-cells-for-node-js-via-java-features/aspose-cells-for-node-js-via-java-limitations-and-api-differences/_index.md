---
title: Aspose.Cells for Node.js via Java Limitations and API Differences
type: docs
weight: 10
url: /java/aspose-cells-for-node-js-via-java-limitations-and-api-differences/
---

## **Public API Differences**
The following list (with sample code segments) shows some differences between Aspose.Cells for Java and Aspose.Cells for Node.js via Java APIs.
### **Importing library (Package Comparisons)**
** 

**Aspose.Cells for Java**

{{< highlight java >}}

 import com.aspose.cells.*;

{{< /highlight >}}

** 

**Aspose.Cells for Node.js via Java**

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

{{< /highlight >}}
### **Instantiating a new Workbook**
** 

**Aspose.Cells for Java**

{{< highlight java >}}

 Workbook excelbook = new Workbook();

{{< /highlight >}}

** 

**Aspose.Cells for Node.js via Java**

{{< highlight java >}}

 var excelbook = new aspose.cells.Workbook();

{{< /highlight >}}
### **Enums or Constants**
** 

**Aspose.Cells for Java**

{{< highlight java >}}

 arc2.getLineFormat().setDashStyle(MsoLineDashStyle.SOLID);

{{< /highlight >}}



**Aspose.Cells for Node.js via Java**

{{< highlight java >}}

 arc2.getLineFormat().setDashStyle(aspose.cells.MsoLineDashStyle.SOLID);

{{< /highlight >}}
### **Streaming Files**
** 

**Aspose.Cells for Java**

{{< highlight java >}}

 InputStream inputstream = new FileInputStream(“Book1.xlsx”);

Workbook workbook = new Workbook(inputstream);

workbook.save(“result.xlsx”);

{{< /highlight >}}



**Aspose.Cells for Node.js via Java**

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

var fs = require("fs");

var readStream = fs.createReadStream("Book1.xlsx");

aspose.cells.Workbook.createWorkbookFromStream(readStream, function(workbook, err) {

    if (err) {

        console.log("open workbook error");

        return;

    }

   workbook.save('result.xlsx');

    console.log('saved to file');

});

{{< /highlight >}}
## **Other Limitations of Aspose.Cells for Node.js via Java API compared to Aspose.Cells for Java API**
1. Importing/exporting data from an Array, ArrayList, ResultSet etc. is not supported.
1. Printing is not supported.
