---
title: القيود و API الاختلافات
type: docs
weight: 10
url: /ar/nodejs-java/limitations-and-api-differences/
keywords: nodejs, excel, limitation, api, difference
description: Aspose.Cells لـ Node.js عبر قيود Java واختلافات API
---
## **عام API الاختلافات**
توضح القائمة التالية (مع نماذج مقاطع الكود) بعض الاختلافات بين Aspose.Cells for Java و Aspose.Cells لـ Node.js عبر واجهات برمجة التطبيقات Java.
### **مكتبة الاستيراد (مقارنات الحزم)**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 import com.aspose.cells.*;

{{< /highlight >}}


**Aspose.Cells لـ Node.js عبر Java**

{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

{{< /highlight >}}
### **إنشاء مصنف جديد**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 Workbook excelbook = new Workbook();

{{< /highlight >}}


**Aspose.Cells لـ Node.js عبر Java**

{{< highlight "java" >}}

 var excelbook = new aspose.cells.Workbook();

{{< /highlight >}}
### **Enums أو الثوابت**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 arc2.getLineFormat().setDashStyle(MsoLineDashStyle.SOLID);

{{< /highlight >}}



**Aspose.Cells لـ Node.js عبر Java**

{{< highlight "java" >}}

 arc2.getLineFormat().setDashStyle(aspose.cells.MsoLineDashStyle.SOLID);

{{< /highlight >}}
### **تدفق الملفات**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 InputStream inputstream = new FileInputStream(“Book1.xlsx”);

Workbook workbook = new Workbook(inputstream);

workbook.save(“result.xlsx”);

{{< /highlight >}}



**Aspose.Cells لـ Node.js عبر Java**

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
## **قيود أخرى لـ Aspose.Cells لـ Node.js عبر Java API مقارنة بـ Aspose.Cells for Java API**
1. لا يتم دعم استيراد / تصدير البيانات من Array و ArrayList و ResultSet وما إلى ذلك.
1. الطباعة غير مدعومة.

