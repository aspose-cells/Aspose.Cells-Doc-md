---
title: Sınırlamalar ve API Farklar
type: docs
weight: 10
url: /tr/nodejs-java/limitations-and-api-differences/
keywords: nodejs, excel, limitation, api, difference
description: Aspose.Cells for Node.js via Java kısıtlamalar ve api farklılıkları
---
## **Kamu API Farklar**
Aşağıdaki liste (örnek kod segmentleriyle birlikte), Aspose.Cells for Java ve Aspose.Cells for Node.js via Java API'ler arasındaki bazı farklılıkları göstermektedir.
### **Kitaplığı içe aktarma (Paket Karşılaştırmaları)**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 import com.aspose.cells.*;

{{< /highlight >}}


**Aspose.Cells for Node.js via Java**

{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

{{< /highlight >}}
### **Yeni bir Çalışma Kitabı örneği oluşturma**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 Workbook excelbook = new Workbook();

{{< /highlight >}}


**Aspose.Cells for Node.js via Java**

{{< highlight "java" >}}

 var excelbook = new aspose.cells.Workbook();

{{< /highlight >}}
### **Numaralandırmalar veya Sabitler**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 arc2.getLineFormat().setDashStyle(MsoLineDashStyle.SOLID);

{{< /highlight >}}



**Aspose.Cells for Node.js via Java**

{{< highlight "java" >}}

 arc2.getLineFormat().setDashStyle(aspose.cells.MsoLineDashStyle.SOLID);

{{< /highlight >}}
### **Akış Dosyaları**

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
## **Aspose.Cells for Node.js via Java API'in Aspose.Cells for Java API ile karşılaştırıldığında Diğer Sınırlamaları**
1. Array, ArrayList, ResultSet vb.'den veri içe/dışa aktarma desteklenmez.
1. Yazdırma desteklenmiyor.

