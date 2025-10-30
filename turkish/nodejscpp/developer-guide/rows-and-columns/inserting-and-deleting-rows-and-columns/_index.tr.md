---
title: Excel dosyasının Satırları ve Sütunları Eklemek ve Silmek
linktitle: Satırları ve Sütunları Eklemek ve Silmek
type: docs
weight: 70
url: /tr/nodejs-cpp/inserting-and-deleting-rows-and-columns/
description: Bu makale, Aspose.Cells for Node.js via C++ API kullanarak satır ve sütunları nasıl ekleyip silineceğini gösterir.
keywords: Aspose.Cells Node.js ile C++ kullanarak satır ve sütunları yönetme, satır ve sütun ekleme ve silme
---

## **Giriş**

Sıfırdan yeni bir çalışma sayfası oluştururken veya mevcut bir çalışma sayfası üzerinde çalışırken, daha fazla veri eklemek için ekstra satırlar veya sütunlar eklememiz gerekebilir. Tersine, çalışma sayfasının belirli pozisyonlarından satırları veya sütunları silebiliriz. 
Bu gereksinimleri karşılamak için, Aspose.Cells for Node.js via C++ aşağıda tartışılan çok basit bir sınıf ve metod kümesi sağlar.

### **Satırları ve Sütunları Yönetmek**

Aspose.Cells for Node.js via C++, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) koleksiyonu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden bir [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) koleksiyonu sağlar.

[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) koleksiyonu, çalışma sayfasında satır ve sütunları yönetmek için birkaç metod sağlar. Bunlardan bazıları aşağıda tartışılmıştır.

{{% alert color="primary" %}}

Satır veya sütunlar eklendiğinde, çalışma sayfasındaki içerik aşağı veya sağa kayar; satır veya sütunlar kaldırıldığında ise içerik yukarı veya sola kayar.

{{% /alert %}}


## **Satırları ve Sütunları Eklemek**

### **Bir Satır Nasıl Eklenir**

Yeni bir satırı çalışma sayfasına herhangi bir konumda eklemek için [**insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-) koleksiyonunun [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) yöntemini çağırarak yapılır. Yeni satırın ekleneceği satırın indeksini alan [**insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-) yöntemi çağrılır.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Inserting a row into the worksheet at 3rd position
worksheet.getCells().insertRow(2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

### **Birkaç Satır Nasıl Eklenir**

Birden çok satırı çalışma sayfasına eklemek için [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) koleksiyonunun [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) yöntemini çağırın. [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) yöntemi iki parametre alır:

- Satır indeksi, yeni satırların ekleneceği satırın indeksi.
- Satır sayısı, eklenmesi gereken toplam satır sayısı.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

const fileData = fs.readFileSync(filePath);
const workbook = new AsposeCells.Workbook(fileData);

const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().insertRows(2, 10);

workbook.save(path.join(dataDir, "output.out.xls"));
```

### **Biçimlendirme Seçenekleriyle Bir Satır Nasıl Eklenir**

Biçimlendirme seçenekleriyle bir satır eklemek için, bir parametre olarak [**InsertOptions**](https://reference.aspose.com/cells/nodejs-cpp/insertoptions) kullanan [**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) aşırı yüklemesini kullanın. [**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/) sınıfının [**InsertOptions**](https://reference.aspose.com/cells/nodejs-cpp/insertoptions) özelliğini [**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/) Sıralama ile ayarlayın. [**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/) Sıralama'nın aşağıda listelenen üç üyesi bulunmaktadır.

- SameAsAbove: Satırı üstteki satır ile aynı şekilde biçimlendirir.
- SameAsBelow: Satırı alttaki satır ile aynı şekilde biçimlendirir.
- Temizle: Biçimlendirmeyi temizler.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Creating a file stream containing the Excel file to be opened
const filePath = path.join(dataDir, "book1.xls");
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting Formatting options
const insertOptions = new AsposeCells.InsertOptions();
insertOptions.setCopyFormatType(AsposeCells.CopyFormatType.SameAsAbove);

// Inserting a row into the worksheet at 3rd position
worksheet.getCells().insertRows(2, 1, insertOptions);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "InsertingARowWithFormatting.out.xls"));
```

### **Bir Sütun Nasıl Eklenir**

Geliştiriciler, herhangi bir konumda çalışma sayfasına bir sütun ekleyebilirler, bunun için [**insertColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertColumn-number-boolean-) koleksiyonunun [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) yöntemini çağırarak yapılır. [**insertColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertColumn-number-boolean-) yöntemi çağrılır.

```javascript
const fs = require('fs');
const path = require('path');
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fileStream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fileStream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Inserting a column into the worksheet at 2nd position
worksheet.getCells().insertColumn(1);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **Satırları ve Sütunları Silmek**

### **Birden Fazla Satır Nasıl Silinir**

Çalışma sayfasından birden fazla satır silmek için, [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) koleksiyonunun [**deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-) yöntemini çağırın. [**deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-) yöntemi iki parametre alır:

- Satır endeksi, satırların silineceği başlangıç satırının endeksi.
- satır sayısı, silinmesi gereken toplam satır sayısı

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Read file contents as Uint8Array
const fileContent = fs.readFileSync(filePath);
const fileBuffer = new Uint8Array(fileContent);

// Instantiating a Workbook object with file buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Deleting 10 rows from the worksheet starting from 3rd row
worksheet.getCells().deleteRows(2, 10);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```


### **Bir Sütunu Nasıl Silebilirsiniz**

Herhangi bir konumda faaliyet sayfasından bir sütun silmek için, [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) koleksiyonunun [**deleteColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteColumn-number-boolean-) yöntemini çağırın. [**deleteColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteColumn-number-boolean-) yöntemi silinecek sütunun endeksini alır.

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Creating a file stream containing the Excel file to be opened
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fs.readFileSync(filePath));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Deleting a column from the worksheet at 5th position
worksheet.getCells().deleteColumn(4);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));

// Closing resources is handled automatically by Node.js, no specific close needed.
```
{{< app/cells/assistant language="nodejs-cpp" >}}
