---
title: 制限事項と API の相違点
type: docs
weight: 10
url: /ja/nodejs-java/limitations-and-api-differences/
keywords: nodejs, excel, limitation, api, difference
description: Aspose.Cells for Node.js via Java 制限と API の違い
---
## **公開 API 違い**
次のリスト (サンプル コード セグメント付き) は、Aspose.Cells for Java と Aspose.Cells for Node.js via Java API の違いを示しています。
### **ライブラリのインポート (パッケージ比較)**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 import com.aspose.cells.*;

{{< /highlight >}}


**Aspose.Cells for Node.js via Java**

{{< highlight "java" >}}

 var aspose = aspose || {};

aspose.cells = require("aspose.cells");

{{< /highlight >}}
### **新しいワークブックのインスタンス化**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 Workbook excelbook = new Workbook();

{{< /highlight >}}


**Aspose.Cells for Node.js via Java**

{{< highlight "java" >}}

 var excelbook = new aspose.cells.Workbook();

{{< /highlight >}}
### **列挙型または定数**

**Aspose.Cells for Java**

{{< highlight "java" >}}

 arc2.getLineFormat().setDashStyle(MsoLineDashStyle.SOLID);

{{< /highlight >}}



**Aspose.Cells for Node.js via Java**

{{< highlight "java" >}}

 arc2.getLineFormat().setDashStyle(aspose.cells.MsoLineDashStyle.SOLID);

{{< /highlight >}}
### **ストリーミング ファイル**

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
## **Aspose.Cells for Node.js via Java API と Aspose.Cells for Java API のその他の制限事項**
1. Array、ArrayList、ResultSet などからのデータのインポート/エクスポートはサポートされていません。
1. 印刷は対応しておりません。

