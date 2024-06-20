---
title: القيود والفروقات في واجهة برمجة التطبيقات
type: docs
weight: 10
url: /ar/nodejs-java/limitations-and-api-differences/
keywords: "nodejs, excel, limitation, api, differences"
description: "قيود Aspose.Cells for Node.js via Java وفروقات واجهة برمجة التطبيقات"
---

## **الفروقات العامة في واجهة برمجة التطبيقات**
يظهر القائمة التالية (مع شرائح رمز عينية) بعض الاختلافات بين Aspose.Cells for Java و Aspose.Cells for Node.js via Java APIs.
### **استيراد المكتبة (مقارنة الحزم)**

**Aspose.Cells for Java**

{{< highlight java >}}

 import com.aspose.cells.*;

{{< /highlight >}}


**Aspose.Cells for Node.js via Java**

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

{{< /highlight >}}
### **إنشاء ورقة عمل جديدة**

**Aspose.Cells for Java**

{{< highlight java >}}

 Workbook excelbook = new Workbook();

{{< /highlight >}}


**Aspose.Cells for Node.js via Java**

{{< highlight java >}}

 var excelbook = new aspose.cells.Workbook();

{{< /highlight >}}
### **ثوابت أو مستمرات**

**Aspose.Cells for Java**

{{< highlight java >}}

 arc2.getLineFormat().setDashStyle(MsoLineDashStyle.SOLID);

{{< /highlight >}}



**Aspose.Cells for Node.js via Java**

{{< highlight java >}}

 arc2.getLineFormat().setDashStyle(aspose.cells.MsoLineDashStyle.SOLID);

{{< /highlight >}}
### **تدفق الملفات**

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
## **قيود أخرى لواجهة برمجة التطبيقات Aspose.Cells for Node.js via Java مقارنة بواجهة برمجة التطبيقات Aspose.Cells for Java**
1. عدم دعم استيراد / تصدير البيانات من مصفوفة ، ArrayList ، ResultSet إلخ.
1. لا يتم دعم الطباعة.

