---
title: Begränsningar och API avvikelser
type: docs
weight: 10
url: /sv/nodejs-java/limitations-and-api-differences/
keywords: "nodejs, excel, limitation, api, differences"
description: "Aspose.Cells för Node.js via Java begränsningar och API avvikelser."
---

## **Offentliga API-avvikelser**
Följande lista (med exemplet kodsegment) visar några skillnader mellan Aspose.Cells for Java och Aspose.Cells för Node.js via Java API:er.
### **Importera bibliotek (Paketjämförelser)**

**Aspose.Cells for Java**

{{< highlight java >}}

 import com.aspose.cells.*;

{{< /highlight >}}


**Aspose.Cells for Node.js via Java**

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells.java");

{{< /highlight >}}
### **Skapa en ny arbetsbok**

**Aspose.Cells for Java**

{{< highlight java >}}

 Workbook excelbook = new Workbook();

{{< /highlight >}}


**Aspose.Cells for Node.js via Java**

{{< highlight java >}}

 var excelbook = new aspose.cells.Workbook();

{{< /highlight >}}
### **Enum eller Konstanter**

**Aspose.Cells for Java**

{{< highlight java >}}

 arc2.getLineFormat().setDashStyle(MsoLineDashStyle.SOLID);

{{< /highlight >}}



**Aspose.Cells for Node.js via Java**

{{< highlight java >}}

 arc2.getLineFormat().setDashStyle(aspose.cells.MsoLineDashStyle.SOLID);

{{< /highlight >}}
### **Strömma filer**

**Aspose.Cells for Java**

{{< highlight java >}}

 InputStream inputstream = new FileInputStream(“Book1.xlsx”);

Workbook workbook = new Workbook(inputstream);

workbook.save(“result.xlsx”);

{{< /highlight >}}



**Aspose.Cells for Node.js via Java**

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells.java");

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
## **Andra begränsningar för Aspose.Cells för Node.js via Java API jämfört med Aspose.Cells for Java API**
1. Importera/exportera data från en Array, ArrayList, ResultSet etc. stöds inte.
1. Utskrift stöds inte.

