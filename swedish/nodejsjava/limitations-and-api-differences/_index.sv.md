---
title: Begränsningar och API-skillnader
type: docs
weight: 10
url: /sv/nodejs-java/limitations-and-api-differences/
keywords: nodejs, excel, limitation, api, difference
description: Aspose.Cells för Node.js via Java-begränsningar och API-skillnader
---
## **Offentliga API-skillnader**
Följande lista (med exempelkodsegment) visar några skillnader mellan Aspose.Cells för Java och Aspose.Cells för Node.js via Java API:er.
### **Importera bibliotek (paketjämförelser)**

**Aspose.Cells för Java**

{{< highlight "java" >}}

 import com.aspose.cells.*;

{{< /highlight >}}


**Aspose.Cells för Node.js via Java**

{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

{{< /highlight >}}
### **Instantierar en ny arbetsbok**

**Aspose.Cells för Java**

{{< highlight "java" >}}

 Workbook excelbook = new Workbook();

{{< /highlight >}}


**Aspose.Cells för Node.js via Java**

{{< highlight "java" >}}

 var excelbook = new aspose.cells.Workbook();

{{< /highlight >}}
### **Uppräkningar eller konstanter**

**Aspose.Cells för Java**

{{< highlight "java" >}}

 arc2.getLineFormat().setDashStyle(MsoLineDashStyle.SOLID);

{{< /highlight >}}



**Aspose.Cells för Node.js via Java**

{{< highlight "java" >}}

 arc2.getLineFormat().setDashStyle(aspose.cells.MsoLineDashStyle.SOLID);

{{< /highlight >}}
### **Strömmande filer**

**Aspose.Cells för Java**

{{< highlight "java" >}}

 InputStream inputstream = new FileInputStream(“Book1.xlsx”);

Workbook workbook = new Workbook(inputstream);

workbook.save(“result.xlsx”);

{{< /highlight >}}



**Aspose.Cells för Node.js via Java**

{{< highlight "java" >}}

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
## **Andra begränsningar av Aspose.Cells för Node.js via Java API jämfört med Aspose.Cells för Java API**
1. Import/export av data från en Array, ArrayList, ResultSet etc. stöds inte.
1. Utskrift stöds inte.

