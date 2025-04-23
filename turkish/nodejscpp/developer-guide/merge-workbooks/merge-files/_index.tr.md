---
title: Node.js ve C++ kullanarak Dosyaları Birleştir
linktitle: Dosyaları Birleştirme
type: docs
weight: 20
url: /tr/nodejs-cpp/merge-files/
---

## **Giriş**

Aspose.Cells, dosya birleştirme için farklı yollar sunar. Veri, biçimlendirme ve formüller içeren basit dosyalar için [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#combine-workbook-) yöntemi birkaç çalışma kitabını birleştirmek; ve [**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#copy-worksheet-) yöntemi, çalışma sayfalarını yeni bir çalışma kitabına kopyalamak için kullanılabilir. Bu yöntemler kullanımı kolay ve etkilidir, ancak çok sayıda dosya birleştiriyorsanız, sistem kaynaklarınızın yoğun kullanıldığını fark edebilirsiniz. Bunu önlemek için, birkaç dosyayı birleştirmenin daha verimli yolu olan [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#mergeFiles-stringarray-string-string-) statik yöntemini kullanın.

## **Aspose.Cells for Node.js via C++ Kullanarak Dosyaları Birleştir**

Aşağıdaki örnek kod, büyük dosyaları [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#mergeFiles-stringarray-string-string-) yöntemi ile birleştirme yöntemini gösterir. İki basit ve büyük dosya olan Book1.xls ve Book2.xls kullanır. Dosyalar sadece biçimlendirilmiş veri ve formüller içerir.

{{% alert color="primary" %}}

Metod yalnızca veri, stiller, biçimlendirme ve formülleri birleştirmeyi destekler. Grafikler, resimler, yorumlar veya diğer nesneler gibi objeler, bu yöntemi kullanarak birleştirilmeyebilir. Ayrıca, işlem için geçici verileri saklamak için önbellek dosyası kullanılır.

{{% /alert %}}

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an Array (length=2)
const files = new Array(2);
// Specify files with their paths to be merged
files[0] = path.join(dataDir, "book1.xls");
files[1] = path.join(dataDir, "Book2.xlsx");

// Create a cachedFile for the process
const cacheFile = path.join(dataDir, "test.txt");

// Output File to be created
const dest = path.join(dataDir, "output.xlsx");

// Merge the files in the output file. Supports only .xls files
AsposeCells.CellsHelper.mergeFiles(files, cacheFile, dest);
console.log(cacheFile);
// Now if you need to rename your sheets, you may load the output file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "output.xlsx"));

let i = 1;

// Browse all the sheets to rename them accordingly
const worksheets = workbook.getWorksheets();
for (let j = 0; j < worksheets.getCount(); j++) {
worksheets.get(j).setName(`Sheet1${i}`);
i++;
}

// Re-save the file
workbook.save(path.join(dataDir, "output.xlsx"));
```
