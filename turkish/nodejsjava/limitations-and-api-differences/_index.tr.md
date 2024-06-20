---
title: Sınırlamalar ve API Farklılıkları
type: docs
weight: 10
url: /tr/nodejs-java/limitations-and-api-differences/
keywords: "nodejs, excel, limitation, api, differences"
description: Aspose.Cells for Node.js via Java" sınırlamaları ve API farkları.
---

## **Genel API Farklılıkları**
Aşağıdaki liste (örnek kod segmentleriyle birlikte) Aspose.Cells for Java ve Aspose.Cells for Node.js via Java API'leri arasındaki bazı farkları gösterir.
### **Kütüphane (Paket Karşılaştırmaları) içe aktarılıyor**

**Aspose.Cells for Java**

{{< highlight java >}}

 import com.aspose.cells.*;

{{< /highlight >}}


**Aspose.Cells for Node.js via Java**

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

{{< /highlight >}}
### **Yeni Bir Çalışma Kitabı Örneği Oluşturuluyor**

**Aspose.Cells for Java**

{{< highlight java >}}

 Workbook excelbook = new Workbook();

{{< /highlight >}}


**Aspose.Cells for Node.js via Java**

{{< highlight java >}}

 var excelbook = new aspose.cells.Workbook();

{{< /highlight >}}
### **Enumlar veya Sabitler**

**Aspose.Cells for Java**

{{< highlight java >}}

 arc2.getLineFormat().setDashStyle(MsoLineDashStyle.SOLID);

{{< /highlight >}}



**Aspose.Cells for Node.js via Java**

{{< highlight java >}}

 arc2.getLineFormat().setDashStyle(aspose.cells.MsoLineDashStyle.SOLID);

{{< /highlight >}}
### **Akış Dosyaları**

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
## **Aspose.Cells for Node.js via Java API, Aspose.Cells for Java API'ye göre diğer kısıtlamalar**
1. Bir Diziden, ArrayList'ten, ResultSet vb. içe/dışa aktarma verileri desteklenmez.
1. Yazdırma desteklenmiyor.

