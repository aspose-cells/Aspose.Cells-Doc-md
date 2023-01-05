---
title: Ограничения и API Различия
type: docs
weight: 10
url: /ru/nodejs-java/limitations-and-api-differences/
keywords: nodejs, excel, limitation, api, difference
description: Aspose.Cells for Node.js via Java ограничения и различия API
---
## **Общественный API Различия**
В следующем списке (с примерами сегментов кода) показаны некоторые различия между API Aspose.Cells for Java и Aspose.Cells for Node.js via Java.
### **Импорт библиотеки (сравнение пакетов)**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 import com.aspose.cells.*;

{{< /highlight >}}


**Aspose.Cells for Node.js via Java**

{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

{{< /highlight >}}
### **Создание новой книги**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 Workbook excelbook = new Workbook();

{{< /highlight >}}


**Aspose.Cells for Node.js via Java**

{{< highlight "java" >}}

 var excelbook = new aspose.cells.Workbook();

{{< /highlight >}}
### **Перечисления или константы**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 arc2.getLineFormat().setDashStyle(MsoLineDashStyle.SOLID);

{{< /highlight >}}



**Aspose.Cells for Node.js via Java**

{{< highlight "java" >}}

 arc2.getLineFormat().setDashStyle(aspose.cells.MsoLineDashStyle.SOLID);

{{< /highlight >}}
### **Потоковые файлы**

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
## **Другие ограничения Aspose.Cells for Node.js via Java API по сравнению с Aspose.Cells for Java API**
1. Импорт/экспорт данных из Array, ArrayList, ResultSet и т. д. не поддерживается.
1. Печать не поддерживается.

