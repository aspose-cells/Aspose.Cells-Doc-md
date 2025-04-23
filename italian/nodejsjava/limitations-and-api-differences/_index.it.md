---
title: Limitazioni e differenze dell API
type: docs
weight: 10
url: /it/nodejs-java/limitations-and-api-differences/
keywords: "nodejs, excel, limitation, api, differences"
description: "Aspose.Cells per Node.js via Java limitazioni e differenze dell API."
---

## **Differenze dell'API pubblica**
L'elenco seguente (con segmenti di codice di esempio) mostra alcune differenze tra Aspose.Cells for Java e le API Aspose.Cells per Node.js via Java.
### **Importazione della libreria (confronto dei pacchetti)**

**Aspose.Cells for Java**

{{< highlight java >}}

 import com.aspose.cells.*;

{{< /highlight >}}


**Aspose.Cells for Node.js via Java**

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells.java");

{{< /highlight >}}
### **Istanziare un nuovo foglio di lavoro**

**Aspose.Cells for Java**

{{< highlight java >}}

 Workbook excelbook = new Workbook();

{{< /highlight >}}


**Aspose.Cells for Node.js via Java**

{{< highlight java >}}

 var excelbook = new aspose.cells.Workbook();

{{< /highlight >}}
### **Enumerazioni o costanti**

**Aspose.Cells for Java**

{{< highlight java >}}

 arc2.getLineFormat().setDashStyle(MsoLineDashStyle.SOLID);

{{< /highlight >}}



**Aspose.Cells for Node.js via Java**

{{< highlight java >}}

 arc2.getLineFormat().setDashStyle(aspose.cells.MsoLineDashStyle.SOLID);

{{< /highlight >}}
### **File in streaming**

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
## **Altre limitazioni dell'API Aspose.Cells per Node.js via Java rispetto all'API Aspose.Cells for Java**
1. L'importazione/esportazione di dati da un Array, ArrayList, ResultSet, ecc. non è supportata.
1. La stampa non è supportata.

