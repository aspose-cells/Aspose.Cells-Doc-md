---
title: Limitations and API Differences
type: docs
weight: 10
url: /fr/nodejs-java/limitations-and-api-differences/
keywords: "nodejs, excel, limitation, api, differences"
description: "Aspose.Cells pour Node.js via Java limitations and api differences."
---

## **Différences d'API publiques**
La liste suivante (avec des segments de code d'exemple) montre quelques différences entre les API Aspose.Cells for Java et Aspose.Cells pour Node.js via Java.
### **Comparaisons de package de bibliothèque d'importation**

**Aspose.Cells for Java**

{{< highlight java >}}

 import com.aspose.cells.*;

{{< /highlight >}}


**Aspose.Cells for Node.js via Java**

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells.java");

{{< /highlight >}}
### **Instanciation d'un nouveau classeur**

**Aspose.Cells for Java**

{{< highlight java >}}

 Workbook excelbook = new Workbook();

{{< /highlight >}}


**Aspose.Cells for Node.js via Java**

{{< highlight java >}}

 var excelbook = new aspose.cells.Workbook();

{{< /highlight >}}
### **Énumérations ou constantes**

**Aspose.Cells for Java**

{{< highlight java >}}

 arc2.getLineFormat().setDashStyle(MsoLineDashStyle.SOLID);

{{< /highlight >}}



**Aspose.Cells for Node.js via Java**

{{< highlight java >}}

 arc2.getLineFormat().setDashStyle(aspose.cells.MsoLineDashStyle.SOLID);

{{< /highlight >}}
### **Fichiers en continu**

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
## **Autres limitations de l'API Aspose.Cells for Node.js via Java par rapport à l'API Aspose.Cells for Java**
1. L'importation/exportation de données à partir d'un tableau, d'un ArrayList, d'un ResultSet, etc. n'est pas prise en charge.
1. L'impression n'est pas prise en charge.

