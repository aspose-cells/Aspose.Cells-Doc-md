---
title: Limitaciones y API Diferencias
type: docs
weight: 10
url: /es/nodejs-java/limitations-and-api-differences/
keywords: nodejs, excel, limitation, api, difference
description: Aspose.Cells for Node.js via Java limitaciones y diferencias api
---
## **Público API Diferencias**
La siguiente lista (con segmentos de código de muestra) muestra algunas diferencias entre las API Aspose.Cells for Java y Aspose.Cells for Node.js via Java.
### **Importación de biblioteca (comparaciones de paquetes)**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 import com.aspose.cells.*;

{{< /highlight >}}


**Aspose.Cells for Node.js via Java**

{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

{{< /highlight >}}
### **Crear una instancia de un nuevo libro de trabajo**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 Workbook excelbook = new Workbook();

{{< /highlight >}}


**Aspose.Cells for Node.js via Java**

{{< highlight "java" >}}

 var excelbook = new aspose.cells.Workbook();

{{< /highlight >}}
### **Enumeraciones o constantes**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 arc2.getLineFormat().setDashStyle(MsoLineDashStyle.SOLID);

{{< /highlight >}}



**Aspose.Cells for Node.js via Java**

{{< highlight "java" >}}

 arc2.getLineFormat().setDashStyle(aspose.cells.MsoLineDashStyle.SOLID);

{{< /highlight >}}
### **Transmisión de archivos**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 InputStream inputstream = new FileInputStream(“Book1.xlsx”);

Workbook workbook = new Workbook(inputstream);

workbook.save(“result.xlsx”);

{{< /highlight >}}



**Aspose.Cells for Node.js via Java**

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
## **Otras limitaciones de Aspose.Cells for Node.js via Java API en comparación con Aspose.Cells for Java API**
1. No se admite la importación/exportación de datos de un Array, ArrayList, ResultSet, etc.
1. No se admite la impresión.

