---  
title: Node.js kullanarak C++ ile Excel Çalışma Sayfasına Satır Ekleme veya Silme  
linktitle: Bir Excel Çalışma Sayfasına Satır Ekle veya Sil  
type: docs  
weight: 20  
url: /tr/nodejs-cpp/insert-or-delete-rows-in-an-excel-worksheet/  
description: Bu makale, Node.js kodunu kullanarak C++ ile Excel çalışma sayfasına satır ekleme ve silme işlemlerini sağlar.  
keywords: node.js ile excel çalışma sayfasına satır ekle veya sil, node.js ile excel e satır ekle veya sil, node.js ile excel e satır ekle, node.js ile excel den satır sil, node.js ile excel çalışma sayfasına satır ekle veya sil, node.js ile excel de satır ekle veya sil, node.js ile excel e satır ekle, node.js ile excel den satır sil  
---  

{{% alert color="primary" %}}  

Yeni bir çalışma sayfası oluştururken veya mevcut bir çalışma sayfasıyla çalışırken, verileri sığdırmak için ek satırlar veya sütunlar eklemeniz gerekebilir. Ayrıca, bazen belirli pozisyonlardan satır veya sütun silmeniz gerekebilir.  

{{% /alert %}}  

Aspose.Cells for Node.js via C++, satır ekleme ve silme işlemleri için [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) ve [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-) olmak üzere iki yöntem sunar. Bu metodlar performans açısından optimize edilmiştir ve çok hızlı çalışır.  

Satır ekleme veya kaldırma işlemi sırasında, hazırladığımız veya hazırlayacağımız her durumda, her zaman [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) ve [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-) metodlarını kullanmanızı öneririz, çünkü [**Cells.insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-) veya [**Cells.deleteRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRow-number-) metodlarını döngü içinde kullanmak yerine.  

Aspose.Cells, Microsoft Excel'in çalışma şekliyle aynı şekilde çalışır. Satırlar veya sütunlar eklenirse, çalışma sayfası içeriği aşağıya ve sağa kaydırılır. Satırlar veya sütunlar kaldırıldığında, çalışma sayfası içeriği yukarı veya sola kaydırılır. Satırlar eklenip kaldırıldığında diğer çalışma sayfaları ve hücrelerdeki referanslar güncellenir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object.
// Load a template file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "book1.xlsx"));

// Get the first worksheet in the book.
const sheet = workbook.getWorksheets().get(0);

// Insert 10 rows at row index 2 (insertion starts at 3rd row)
sheet.getCells().insertRows(2, 10);

// Delete 5 rows now. (8th row - 12th row)
sheet.getCells().deleteRows(7, 5);

// Save the excel file.
workbook.save(path.join(dataDir, "out_book1.out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
