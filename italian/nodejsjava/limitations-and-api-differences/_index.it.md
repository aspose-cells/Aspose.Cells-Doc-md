---
title: Limitazioni e API Differenze
type: docs
weight: 10
url: /it/nodejs-java/limitations-and-api-differences/
keywords: nodejs, excel, limitation, api, difference
description: Aspose.Cells per Node.js tramite limitazioni Java e differenze API
---
## **Pubblico API Differenze**
L'elenco seguente (con segmenti di codice di esempio) mostra alcune differenze tra Aspose.Cells for Java e Aspose.Cells per Node.js tramite le API Java.
### **Libreria di importazione (confronto tra pacchetti)**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 import com.aspose.cells.*;

{{< /highlight >}}


**Aspose.Cells per Node.js tramite Java**

{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

{{< /highlight >}}
### **Creazione di un'istanza di una nuova cartella di lavoro**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 Workbook excelbook = new Workbook();

{{< /highlight >}}


**Aspose.Cells per Node.js tramite Java**

{{< highlight "java" >}}

 var excelbook = new aspose.cells.Workbook();

{{< /highlight >}}
### **Enum o costanti**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 arc2.getLineFormat().setDashStyle(MsoLineDashStyle.SOLID);

{{< /highlight >}}



**Aspose.Cells per Node.js tramite Java**

{{< highlight "java" >}}

 arc2.getLineFormat().setDashStyle(aspose.cells.MsoLineDashStyle.SOLID);

{{< /highlight >}}
### **File in streaming**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 InputStream inputstream = new FileInputStream(“Book1.xlsx”);

Workbook workbook = new Workbook(inputstream);

workbook.save(“result.xlsx”);

{{< /highlight >}}



**Aspose.Cells per Node.js tramite Java**

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
## **Altre limitazioni di Aspose.Cells per Node.js tramite Java API rispetto a Aspose.Cells for Java API**
1. L'importazione/esportazione di dati da Array, ArrayList, ResultSet ecc. non è supportata.
1. La stampa non è supportata.

