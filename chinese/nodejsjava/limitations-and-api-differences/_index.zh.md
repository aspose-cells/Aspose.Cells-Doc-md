---
title: 限制和 API 差异
type: docs
weight: 10
url: /zh/nodejs-java/limitations-and-api-differences/
keywords: "nodejs, excel, limitation, api, differences"
description: "Aspose.Cells for Node.js via Java 的限制和 API 差异。"
---

## **公共 API 差异**
以下列表(含示例代码段)展示了Aspose.Cells for Java和Aspose.Cells for Node.js via Java API之间的一些差异。
### **导入库（包比较）**

**Aspose.Cells for Java**

{{< highlight java >}}

 import com.aspose.cells.*;

{{< /highlight >}}


**Aspose.Cells for Node.js via Java**

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells.java");

{{< /highlight >}}
### **实例化新工作簿**

**Aspose.Cells for Java**

{{< highlight java >}}

 Workbook excelbook = new Workbook();

{{< /highlight >}}


**Aspose.Cells for Node.js via Java**

{{< highlight java >}}

 var excelbook = new aspose.cells.Workbook();

{{< /highlight >}}
### **枚举或常量**

**Aspose.Cells for Java**

{{< highlight java >}}

 arc2.getLineFormat().setDashStyle(MsoLineDashStyle.SOLID);

{{< /highlight >}}



**Aspose.Cells for Node.js via Java**

{{< highlight java >}}

 arc2.getLineFormat().setDashStyle(aspose.cells.MsoLineDashStyle.SOLID);

{{< /highlight >}}
### **流式文件**

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
## **Aspose.Cells for Node.js via Java API相对于Aspose.Cells for Java API的其他限制**
1. 不支持从数组、ArrayList、ResultSet 等导入/导出数据。
1. 不支持打印。

