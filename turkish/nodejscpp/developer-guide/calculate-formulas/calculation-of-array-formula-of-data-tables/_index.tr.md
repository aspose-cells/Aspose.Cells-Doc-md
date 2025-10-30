---
title: C++ aracılığıyla Node.js kullanarak Veri Tablolarının Array Formüllerinin Hesaplanması
linktitle: Veri Tablolarının Dizilerini Hesaplama
description: Microsoft Excel de bir veri tablosu için dizi formüllerini hesaplamak amacıyla Aspose.Cells kütüphanesini kullanma. Bir Excel dosyasını yükleyin veya oluşturun, dizi formülünü hesaplayın ve düzenlenmiş dosyayı kaydedin.
keywords: Aspose.Cells, Excel, veri tabloları, dizi formülleri, hesaplamalar Node.js aracılığıyla C++
type: docs
weight: 70
url: /tr/nodejs-cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

Microsoft Excel'de Veri > Varsayılan Analiz > Veri Tablosu.... kullanarak bir Veri Tablosu oluşturabilirsiniz. Aspose.Cells artık veri tablosunun dizi formüllerini hesaplamanıza izin veriyor. Herhangi bir formülü hesaplamak için normalde [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) kullanın.

{{% /alert %}}

Aşağıdaki örnek kodda, [kaynak excel dosyası](5115535.xlsx)'ı kullandık. Eğer B1 hücresinin değerini 100 olarak değiştirirseniz, Sarı renkle doldurulan Veri Tablosu değerleri 120 olarak değişir ve [çıktı PDF'sini](5115538.pdf) oluşturur. Daha fazla bilgi için yorumları okuyunuz.

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

[çıktı PDF'sini](5115538.pdf) oluşturmak için [kaynak excel dosyası](5115535.xlsx)'ı kullanılan örnek kod aşağıdaki gibidir. Daha fazla bilgi için yorumları okuyunuz.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook from source excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "DataTable.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
worksheet.getCells().get("B1").putValue(100);

// Calculate formula, now it also calculates Data Table array formula
workbook.calculateFormula();

// Save the workbook in pdf format
workbook.save(path.join(dataDir, "output_out.pdf"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
