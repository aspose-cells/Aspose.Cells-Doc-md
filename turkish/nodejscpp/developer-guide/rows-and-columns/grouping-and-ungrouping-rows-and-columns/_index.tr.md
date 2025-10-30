---
title: C++ kullanarak Node.js ile Satır ve Sütunları Gruplama ve Gruplamayı Kaldırma
linktitle: Satır ve Sütunları Gruplandırma ve Grubu Çözme
type: docs
weight: 50
url: /tr/nodejs-cpp/grouping-and-ungrouping-rows-and-columns/
description: Excel de satır ve sütunları nasıl gruplayıp kaldıracağınızı Aspose.Cells for Node.js via C++ kullanarak keşfedin.
--- 

## **Giriş**

Bir Microsoft Excel dosyasında, veriler için bir biçim oluşturarak tek bir fare tıklamasıyla ayrıntı seviyelerini gösterip gizleyebilirsiniz.

Yalnızca özetler veya başlıkların bulunduğu satırları veya sütunları hızlı bir şekilde görüntülemek için **Özet Sembolleri**, 1,2,3, + ve - simgelerine tıklayabilirsiniz veya simgeleri kullanarak bir çalışma sayfasındaki bir bölümün altındaki ayrıntıları görebilirsiniz, aşağıdaki şekilde gösterildiği gibi:

|**Satır ve Sütun Gruplama.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Satır ve Sütun Grubu Yönetimi**

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, Excel dosyasındaki her sayfaya erişim sağlayan [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) metodunu içerir. Bir sayfa [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı, sayfadaki tüm hücreleri temsil eden [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonunu sağlar.

[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonu, bir sayfada satır veya sütunları yönetmek için çeşitli metodlar sağlar, bunlardan bazıları aşağıda daha detaylı anlatılmaktadır.

### **Satır ve Sütun Gruplama**

Satır veya sütunları gruplamak için [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonunun [**groupRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#groupRows-number-number-boolean-) ve [**groupColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#groupColumns-number-number-) metodları çağrılabilir. Her iki metod da aşağıdaki parametreleri alır:

- İlk satır/sütun indeksi, grup içindeki ilk satır veya sütun.
- Son satır/sütun indeksi, grup içindeki son satır veya sütun.
- Gizli mi, satırları/sütunları gruplandırmadan sonra gizlemek için bir Boolean parametre.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fs = require("fs");
const fileContent = fs.readFileSync(filePath);

// Opening the Excel file through the buffer
const workbook = new AsposeCells.Workbook(fileContent);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Grouping first six rows (from 0 to 5) and making them hidden by passing true
worksheet.getCells().groupRows(0, 5, true);

// Grouping first three columns (from 0 to 2) and making them hidden by passing true
worksheet.getCells().groupColumns(0, 2, true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

#### **Grup Ayarları**

Microsoft Excel, görüntüleme için grup ayarlarını yapılandırmanıza izin verir:

- Detayın altında özet satırlar.
- Ayrıntının sağında özet sütunlar.

Geliştiriciler, bu grup ayarlarını [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfının [**getOutline()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getOutline--) özelliğini kullanarak yapılandırabilirler.

### **Detaydan Aşağı Özet Satırlar**

Özet satırların detayların altında gösterilip gösterilmemesini [**getSummaryRowBelow()**](https://reference.aspose.com/cells/nodejs-cpp/outline/#getSummaryRowBelow--) özelliğini **true** veya **false** yaparak kontrol edebilirler.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);

// Grouping first six rows and first three columns
worksheet.getCells().groupRows(0, 5, true);
worksheet.getCells().groupColumns(0, 2, true);

// Setting SummaryRowBelow property to false
worksheet.getOutline().setSummaryRowBelow(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **Detayın Sağına Özet Sütunlar**

Geliştiriciler ayrıca, özet sütunların doğru da gösterilip gösterilmeyeceğini [**Outline**](https://reference.aspose.com/cells/nodejs-cpp/outline) sınıfının [**getSummaryColumnRight()**](https://reference.aspose.com/cells/nodejs-cpp/outline/#getSummaryColumnRight--) özelliğini **true** veya **false** yaparak kontrol edebilirler.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);

// Grouping first six rows and first three columns
worksheet.getCells().groupRows(0, 5, true);
worksheet.getCells().groupColumns(0, 2, true);

worksheet.getOutline().setSummaryColumnRight(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **Satır ve Sütunların Gruplandırılmasını Kaldırma**

Herhangi bir gruplanmış satır veya sütunu gruplamayı kaldırmak için, [**ungroupColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupColumns-number-number-) koleksiyonunun [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells), [**ungroupRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupRows-number-number-boolean-) ve [**ungroupColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupColumns-number-number-) metodlarını çağırın. Her iki metod da iki parametre alır:

- İlk satır veya sütun dizini, ayrılmak istenen ilk satır/sütun.
- Son satır veya sütun dizini, ayrılmak istenen son satır/sütun.

{1} aşırı yüklemeye sahiptir ve üçüncü Boolean parametre alır. Bunu **true** yaparsanız, tüm gruplanmış bilgiler kaldırılır. Aksi takdirde, yalnızca dış grup bilgisi kaldırılır.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading Excel file into buffer
const buffer = fs.readFileSync(filePath);

// Instantiating a Workbook object with file content
const workbook = new AsposeCells.Workbook(buffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Ungrouping first six rows (from 0 to 5)
worksheet.getCells().ungroupRows(0, 5);

// Ungrouping first three columns (from 0 to 2)
worksheet.getCells().ungroupColumns(0, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
