---
title: Node.js kullanarak C++ ile Microsoft Excel dosyalarında tabloları oluşturun ve yönetin
linktitle: Tablolar
type: docs
weight: 150
url: /tr/nodejs-cpp/create-and-format-table/
description: Aspose.Cells for Node.js via C++ kullanarak Excel dosyalarının tablolarını ekleyin, yeniden boyutlandırın, düzenleyin, silin ve biçimlendirin.
---

## **Tablo Oluştur**

Hesap tablolarının avantajlarından biri, telefon listeleri, görev listeleri, işlemler, varlıklar veya borçlar gibi farklı tiplerde listeler oluşturmanıza olanak tanımalarıdır. Çeşitli kullanıcılar birden fazla listeyi kullanmak, oluşturmak ve yönetmek için birlikte çalışabilir.

Aspose.Cells, listeler oluşturmayı ve yönetmeyi destekler.

### **Liste Nesnesi Avantajları**

Veri listesini gerçek bir Liste Nesnesine dönüştürdüğünüzde birkaç avantaj bulunmaktadır

- Yeni satır ve sütunlar otomatik olarak dahil edilir.
- Listenizin altından toplam satırı SUM, AVERAGE, COUNT vb. göstermek için kolayca ekleyebilirsiniz.
- Sağa eklenen sütunlar otomatik olarak List nesnesine dahil edilir.
- Satırlar ve sütunlara dayalı grafikler otomatik olarak genişletilecektir.
- Satırlara ve sütunlara atanan adlandırılmış aralıklar otomatik olarak genişletilir.
- Liste kazara satır ve sütun silme işlemlerine karşı korunur.

### **Microsoft Excel Kullanarak Bir Liste Nesnesi Oluşturma**

- Liste nesnesi oluşturmak için veri aralığını seçme
- Bu, Liste Oluştur iletişim kutusunu görüntüler.
- Veri için Liste nesnesini uygula ve toplam satırını belirtin (**Veri** > **Liste** > **Toplam Satır**) seçin.

### **Aspose.Cells API'si Kullanımı**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) koleksiyonunu içerir.

Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı, bir çalışma sayfasını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Bir çalışma sayfasında [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) oluşturmak için, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfının [**getListObjects()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getListObjects--) koleksiyon özelliğini kullanın. Her [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/), aslında [**ListObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/) sınıfının bir nesnesidir ve ek olarak [**add(number, number, number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/#add-number-number-number-number-boolean-) yöntemi ile Liste nesnesi ekleme ve hücre aralığını belirleme sağlar.

Belirtilen hücre aralığına göre, Aspose.Cells tarafından Liste nesnesi oluşturulur. Listeyi kontrol etmek için [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) sınıfının attribute'leri (örneğin, [**getShowTotals()**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#getShowTotals--), [**getListColumns()**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#getListColumns--) vb.) kullanın.

Aşağıdaki örnekte, yukarıdaki bölümde Microsoft Excel kullanarak oluşturduğumuzla aynı [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) nesnesini Aspose.Cells API kullanarak oluşturduk.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Create a Workbook object.
// Open a template excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Get the List objects collection in the first worksheet.
const listObjects = workbook.getWorksheets().get(0).getListObjects();

// Add a List based on the data source range with headers on.
listObjects.add(1, 1, 7, 5, true);

// Show the total row for the List.
listObjects.get(0).setShowTotals(true);

// Calculate the total of the last (5th) list column.
listObjects.get(0).getListColumns().get(4).setTotalsCalculation(AsposeCells.TotalsCalculation.Sum);

// Save the excel file.
workbook.save(path.join(dataDir, "output.xls"));
```

## **Tabloyu Biçimlendir**

İlgili veri grubunu yönetmek ve analiz etmek için, hücre aralığını bir liste nesnesine (aynı zamanda bir Excel tablosu olarak da bilinir) dönüştürmek mümkündür. Bir tablo, ilişkili verileri içeren bir dizi satır ve sütun, diğer satır ve sütunlardaki veriden bağımsız olarak yönetilir. Varsayılan olarak, tablodaki her sütunun başlık satırında filtreleme etkinleştirilir, böylece listeniz nesnesi verilerinizi hızlı bir şekilde filtreleyebilir veya sıralayabilir. Listeniz nesnesine (sayısal verilerle çalışmak için faydalı olan bir listede özel bir satır) toplam satır ekleyebilirsiniz. Bu toplam satırın her hücresi için bir toplama işlevlerinin açılır menüsünü sağlayan özel bir satır. Aspose.Cells, listelerin (veya tabloların) oluşturulması ve yönetilmesi için seçenekler sunar.

### **Liste Nesnesini Biçimlendirme**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) koleksiyonunu içerir.

Bir çalışma sayfası [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı, çalışma sayfalarını yönetmek için geniş özellik ve yöntemler sağlar. Bir çalışma sayfasında [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) oluşturmak için, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfının [**getListObjects()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getListObjects--) koleksiyon özelliğini kullanın. Her [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/), aslında [**ListObjectCollection**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/) sınıfının bir nesnesidir ve ek olarak [**add(number, number, number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/listobjectcollection/#add-number-number-number-number-boolean-) yöntemi ile bir Liste nesnesi ekleyip kapsaması gereken hücre aralığını belirler. Belirtilen hücre aralığına göre, Aspose.Cells çalışma sayfasında [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) oluşturur. Formata uygun hale getirmek için [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) sınıfının [**TableStyleType**](https://reference.aspose.com/cells/nodejs-cpp/tablestyletype/) attribute'lerini kullanın.

Aşağıdaki örnek, çalışma sayfasına örnek veri ekler, bir [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) ekler ve varsayılan stilleri uygular. [**ListObject**](https://reference.aspose.com/cells/nodejs-cpp/listobject/) stilleri, Microsoft Excel 2007/2010 tarafından desteklenir.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook.
const workbook = new AsposeCells.Workbook();

// Obtaining the reference of the default(first) worksheet
const sheet = workbook.getWorksheets().get(0);

// Obtaining Worksheet's cells collection
const cells = sheet.getCells();

// Setting the value to the cells
cells.get(1, 1).putValue("Employee");
cells.get(1, 2).putValue("Quarter");
cells.get(1, 3).putValue("Product");
cells.get(1, 4).putValue("Continent");
cells.get(1, 5).putValue("Country");
cells.get(1, 6).putValue("Sale");

cells.get(2, 1).putValue("David");
cells.get(3, 1).putValue("David");
cells.get(4, 1).putValue("David");
cells.get(5, 1).putValue("David");
cells.get(6, 1).putValue("James");
cells.get(7, 1).putValue("James");
cells.get(8, 1).putValue("James");
cells.get(9, 1).putValue("James");
cells.get(10, 1).putValue("James");
cells.get(11, 1).putValue("Miya");
cells.get(12, 1).putValue("Miya");
cells.get(13, 1).putValue("Miya");
cells.get(14, 1).putValue("Miya");
cells.get(15, 1).putValue("Miya");
cells.get(2, 2).putValue(1);
cells.get(3, 2).putValue(2);
cells.get(4, 2).putValue(3);
cells.get(5, 2).putValue(4);
cells.get(6, 2).putValue(1);
cells.get(7, 2).putValue(2);
cells.get(8, 2).putValue(3);
cells.get(9, 2).putValue(4);
cells.get(10, 2).putValue(4);
cells.get(11, 2).putValue(1);
cells.get(12, 2).putValue(1);
cells.get(13, 2).putValue(2);
cells.get(14, 2).putValue(2);
cells.get(15, 2).putValue(2);

cells.get(2, 3).putValue("Maxilaku");
cells.get(3, 3).putValue("Maxilaku");
cells.get(4, 3).putValue("Chai");
cells.get(5, 3).putValue("Maxilaku");
cells.get(6, 3).putValue("Chang");
cells.get(7, 3).putValue("Chang");
cells.get(8, 3).putValue("Chang");
cells.get(9, 3).putValue("Chang");
cells.get(10, 3).putValue("Chang");
cells.get(11, 3).putValue("Geitost");
cells.get(12, 3).putValue("Chai");
cells.get(13, 3).putValue("Geitost");
cells.get(14, 3).putValue("Geitost");
cells.get(15, 3).putValue("Geitost");

cells.get(2, 4).putValue("Asia");
cells.get(3, 4).putValue("Asia");
cells.get(4, 4).putValue("Asia");
cells.get(5, 4).putValue("Asia");
cells.get(6, 4).putValue("Europe");
cells.get(7, 4).putValue("Europe");
cells.get(8, 4).putValue("Europe");
cells.get(9, 4).putValue("Europe");
cells.get(10, 4).putValue("Europe");
cells.get(11, 4).putValue("America");
cells.get(12, 4).putValue("America");
cells.get(13, 4).putValue("America");
cells.get(14, 4).putValue("America");
cells.get(15, 4).putValue("America");

cells.get(2, 5).putValue("China");
cells.get(3, 5).putValue("India");
cells.get(4, 5).putValue("Korea");
cells.get(5, 5).putValue("India");
cells.get(6, 5).putValue("France");
cells.get(7, 5).putValue("France");
cells.get(8, 5).putValue("Germany");
cells.get(9, 5).putValue("Italy");
cells.get(10, 5).putValue("France");
cells.get(11, 5).putValue("U.S.");
cells.get(12, 5).putValue("U.S.");
cells.get(13, 5).putValue("Brazil");
cells.get(14, 5).putValue("U.S.");
cells.get(15, 5).putValue("U.S.");

cells.get(2, 6).putValue(2000);
cells.get(3, 6).putValue(500);
cells.get(4, 6).putValue(1200);
cells.get(5, 6).putValue(1500);
cells.get(6, 6).putValue(500);
cells.get(7, 6).putValue(1500);
cells.get(8, 6).putValue(800);
cells.get(9, 6).putValue(900);
cells.get(10, 6).putValue(500);
cells.get(11, 6).putValue(1600);
cells.get(12, 6).putValue(600);
cells.get(13, 6).putValue(2000);
cells.get(14, 6).putValue(500);
cells.get(15, 6).putValue(900);

// Adding a new List Object to the worksheet
const index = sheet.getListObjects().add("A1", "F15", true);

const listObject = sheet.getListObjects().get(index);

// Adding Default Style to the table
listObject.setTableStyleType(AsposeCells.TableStyleType.TableStyleMedium10);

// Show Total
listObject.setShowTotals(true);

// Set the Quarter field's calculation type
listObject.getListColumns().get(1).setTotalsCalculation(AsposeCells.TotalsCalculation.Count);

// Saving the Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```

## **Gelişmiş Konular**
- [Tabloyu ODS'ye Dönüştür](/cells/tr/nodejs-cpp/convert-table-to-ods/)
- [Dış Veri Bağlantılarıyla İlgili Sorgu Tablolarını ve List Obje Bulma](/cells/tr/nodejs-cpp/find-query-tables-and-list-objects-related-to-external-data-connections/)
- [Sorgu Tablosu Veri Kaynağı ile Tablo Okuma ve Yazma](/cells/tr/nodejs-cpp/read-and-write-table-with-query-table-data-source/)
- [Çalışma Sayfası içinde Masa veya Liste Nesnesi Yorumunu Ayarlayın](/cells/tr/nodejs-cpp/set-the-comment-of-table-or-list-object-inside-the-worksheet/)
- [Tablolar ve Aralıklar](/cells/tr/nodejs-cpp/tables-and-ranges/)

