---
title: Satır ve Sütunları Gizleme ve Gösterme ile Node.js kullanımı C++ ile
linktitle: Satır ve Sütunları Gizleme ve Gösterme
type: docs
weight: 60
url: /tr/nodejs-cpp/hiding-and-showing-rows-and-columns/
description: Aspose.Cells for Node.js via C++ kullanarak, bir sayfada satır ve sütunları nasıl gizleyip göstereceğinizi öğrenin.
---

{{% alert color="primary" %}}

Bazen bir çalışma sayfasında belirli satırları veya sütunları gizlemek ve daha sonra göstermek anlamlı olabilir. Microsoft Excel bu özelliği sağlar ve Aspose.Cells de aynısını sağlar.

{{% /alert %}}

## **Satır ve Sütunların Görünürlüğünü Kontrol Etme**

Aspose.Cells for Node.js via C++, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) adlı bir sınıf sağlar, bu sınıf Microsoft Excel dosyasını temsil eder. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, geliştiricilerin Excel dosyasındaki her sayfaya erişmesini sağlayan [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) metodunu içerir. Bir sayfa [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfıyla temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı, sayfadaki tüm hücreleri temsil eden [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonunu sağlar. [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonu, sayfadaki satır veya sütunları yönetmek için çeşitli metodlar sunar. Bunlardan bazıları aşağıda tartışılmıştır.

### **Satır ve Sütunları Gizleme**

Geliştiriciler, belirli bir satır veya sütunu gizlemek için sırasıyla [**hideRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRow-number-) ve [**hideColumn(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumn-number-) metodlarını çağırabilirler. Her iki yöntem de gizlenmek istenen satır ve sütun indekslerini parametre olarak alır.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fileBuffer = fs.readFileSync(filePath);

// Instantiating a Workbook object with Uint8Array
const workbook = new AsposeCells.Workbook(new Uint8Array(fileBuffer));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the 3rd row of the worksheet
worksheet.getCells().hideRow(2);

// Hiding the 2nd column of the worksheet
worksheet.getCells().hideColumn(1);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

{{% alert color="primary" %}}

Bir satır veya sütunu sıfır genişliğine ayarlayarak bir satır veya sütunu gizlemek de mümkündür.

{{% /alert %}}

### **Satır ve Sütunları Gösterme**

Geliştiriciler, [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) koleksiyonunun [**unhideRow(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRow-number-number-) ve [**unhideColumn(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumn-number-number-) metodlarını sırasıyla çağırarak herhangi bir gizli satır veya sütunu gösterebilirler. Her iki yöntem de iki parametre alır:

- **Satır veya sütun dizini** - belirli bir satır veya sütunun gösterilmesi için kullanılan dizin.
- **Satır yüksekliği veya sütun genişliği** - gizlendikten sonra atanan satır yüksekliği veya sütun genişliği.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Read the Excel file into a Buffer (Uint8Array)
const fileBuffer = fs.readFileSync(filePath);

// Instantiating a Workbook object with file buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unhiding the 3rd row and setting its height to 13.5
worksheet.getCells().unhideRow(2, 13.5);

// Unhiding the 2nd column and setting its width to 8.5
worksheet.getCells().unhideColumn(1, 8.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

{{% alert color="primary" %}}

Gizli bir sütunu görünür hale getirirken, önceden atanmış genişliğe veya orijinal genişliğe geri yüklemeniz gerekiyorsa, negatif genişlikle sütunu gizleme kaldırın. Örneğin: worksheet.cells.unhideColumn(5, -1)

{{% /alert %}}

### **Birden Fazla Satır ve Sütunu Gizleme**

Geliştiriciler, aynı anda birden fazla satır veya sütunu gizlemek için sırasıyla [**hideRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRows-number-number-) ve [**hideColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumns-number-number-) metodlarını çağırabilirler. Her iki yöntem de gizlenecek başlangıç satırı veya sütunu indeksi ve satır veya sütun sayısı parametreleri olarak alır.

```javascript
const fs = require("fs");
const path = require("path");
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

// Hiding 3, 4, and 5 rows in the worksheet
worksheet.getCells().hideRows(2, 3);

// Hiding 2 and 3 columns in the worksheet
worksheet.getCells().hideColumns(1, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "outputxls"));
```

{{% alert color="primary" %}}

Birden fazla satır ve sütunu görünür yapmak için [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) sınıfının [**unhideRows(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRows-number-number-number-) ve [**unhideColumns(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumns-number-number-number-) metodlarını kullanmak da mümkündür.

{{% /alert %}}
