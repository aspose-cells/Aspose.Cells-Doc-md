---
title: 限制和API差异
type: docs
weight: 10
url: /zh/nodejs-java/limitations-and-api-differences/
keywords: "nodejs, excel, limitation, api, differences"
description: "Aspose.Cells for Node.js via Java 的限制和 API 差异。"
---

## **公共API差异**
以下列表（带有示例代码段）显示了 Aspose.Cells for Java 与 Aspose.Cells for Node.js via Java API 之间的一些差异。
### **导入库（软件包对比）**

**Aspose.Cells for Java**

{{< highlight java >}}

 import com.aspose.cells.*;

{{< /highlight >}}


**Aspose.Cells for Node.js via Java**

{{< highlight java >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

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
### **文件流式传输**

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
## **与 Aspose.Cells for Java API 相比，Aspose.Cells for Node.js via Java API 的其他限制**
1. 不支持从Array、ArrayList、ResultSet等导入/导出数据。
1. 不支持打印。

