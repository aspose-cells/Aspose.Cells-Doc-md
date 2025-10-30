---
title: Gelişmiş Koruma Ayarları, Excel XP den Node.js ile C++ kullanımıyla
linktitle: Excel XP den beri Gelişmiş Koruma Ayarları
type: docs
weight: 30
url: /tr/nodejs-cpp/advanced-protection-settings-since-excel-xp/
---


{{% alert color="primary" %}}

2002 veya XP sürümüyle birlikte, Microsoft birçok gelişmiş koruma ayarı eklemiştir.

{{% /alert %}}


## **Giriş**

Bu koruma ayarları, kullanıcıların aşağıdakileri kısıtlamasına veya izin vermesini sağlar:

- Satırları veya sütunları sil.
- İçeriği, nesneleri veya senaryoları düzenle.
- Hücreleri, satırları veya sütunları biçimlendir.
- Satırları, sütunları veya köprüleri ekle.
- Kilitli veya kilitsiz hücreleri seç.
- Özet tabloları ve çok daha fazlasını kullanın.

Aspose.Cells for Node.js via C++, Excel XP veya sonraki sürümler tarafından sunulan tüm gelişmiş koruma ayarlarını destekler.

### **Excel XP'de bulunan koruma ayarlarını görüntülemek için:**

**Araçlar** menüsünden **Koruma** ardından **Sayfayı Koru**'yu seçin.

1. **Araçlar** menüsünden **Koruma** ve ardından **Çalışma Sayfası Koru** seçin. Bir iletişim kutusu görüntülenecektir.

Excel 2016'daki koruma ayarlarını görüntülemek için:

1. **Dosya** menüsünden **Çalışma Kitabını Koru** ve ardından **Mevcut Sayfayı Koru** seçin.
1. **İncele** menüsünde **Çalışma Sayfası Koru** seçin.

Yukarıdaki adımları takip etmek, çalışma sayfasında özellikleri izin verme veya kısıtlama ya da parola uygulama diyaloğunu gösterecektir.

### **Gelişmiş Koruma Ayarları Kullanımı Aspose.Cells for Node.js via C++ ile**

Aspose.Cells for Node.js via C++, tüm gelişmiş koruma ayarlarını destekler.

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, Excel dosyasındaki her bir çalışma sayfasına erişim izni veren bir [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı tarafından temsil edilir.

[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı, bu gelişmiş koruma ayarlarını uygulamak için kullanılan [**getProtection()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getProtection--) özelliğini sağlar. Aslında, [**getProtection()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getProtection--) özelliği, engelleme veya kısıtlamaları etkinleştirmek veya devre dışı bırakmak için birkaç Boolean özelliği kapsayan [**Protection**](https://reference.aspose.com/cells/nodejs-cpp/protection) sınıfından bir nesnedir.

Aşağıda küçük bir örnek uygulama bulunmaktadır. Bir Excel dosyası açar ve Excel XP ve sonraki sürümler tarafından desteklenen gelişmiş koruma ayarlarının çoğunu kullanır.

```javascript
try {
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.createReadStream(filePath);

// Reading the file stream into a buffer
const fileBuffer = [];
fstream.on('data', chunk => fileBuffer.push(chunk));
fstream.on('end', () => {
const workbook = new AsposeCells.Workbook(Buffer.concat(fileBuffer));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Restricting users to delete columns of the worksheet
worksheet.getProtection().setAllowDeletingColumn(false);

// Restricting users to delete row of the worksheet
worksheet.getProtection().setAllowDeletingRow(false);

// Restricting users to edit contents of the worksheet
worksheet.getProtection().setAllowEditingContent(false);

// Restricting users to edit objects of the worksheet
worksheet.getProtection().setAllowEditingObject(false);

// Restricting users to edit scenarios of the worksheet
worksheet.getProtection().setAllowEditingScenario(false);

// Restricting users to filter
worksheet.getProtection().setAllowFiltering(false);

// Allowing users to format cells of the worksheet
worksheet.getProtection().setAllowFormattingCell(true);

// Allowing users to format rows of the worksheet
worksheet.getProtection().setAllowFormattingRow(true);

// Allowing users to insert columns in the worksheet
worksheet.getProtection().setAllowFormattingColumn(true);

// Allowing users to insert hyperlinks in the worksheet
worksheet.getProtection().setAllowInsertingHyperlink(true);

// Allowing users to insert rows in the worksheet
worksheet.getProtection().setAllowInsertingRow(true);

// Allowing users to select locked cells of the worksheet
worksheet.getProtection().setAllowSelectingLockedCell(true);

// Allowing users to select unlocked cells of the worksheet
worksheet.getProtection().setAllowSelectingUnlockedCell(true);

// Allowing users to sort
worksheet.getProtection().setAllowSorting(true);

// Allowing users to use pivot tables in the worksheet
worksheet.getProtection().setAllowUsingPivotTable(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"), AsposeCells.SaveFormat.Excel97To2003);

// Closing the file stream to free all resources
fstream.close();
```

{{% alert color="primary" %}}

Lütfen [**getProtection()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getProtection--) özelliğini kullanırken [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfının [**protect(ProtectionType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#protect-protectiontype-) metodunu çağırmayın. Ayrıca, dosyayı Excel97'den 2003'e veya Xlsx formatında kaydedin çünkü gelişmiş koruma ayarları yalnızca Excel XP ve daha yeni sürümler tarafından desteklenir.

{{% /alert %}}

### **Hücre Kilitleme Sorunu**

Kullanıcıların hücreleri düzenlemesini engellemek istiyorsanız, hücreler herhangi bir koruma ayarı uygulanmadan önce kilitlenmiş olmalıdır. Aksi takdirde, çalışma sayfası korunsa bile hücreler düzenlenebilir. Microsoft Excel XP'de hücreler aşağıdaki iletişim kutusu aracılığıyla kilitlenebilir:

|**Excel XP'de Hücreleri Kilitlme İletişim Kutusu**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

Aspose.Cells API kullanarak da hücreler kilitlenebilir. Her hücre, [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) biçimlendirmeyi alan ve bir Boolean özellik [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) içeren [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) özelliğine sahip olabilir. Hücreyi kilitlemek veya kilidini açmak için [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) özelliğini **doğru** veya **yanlış** olarak ayarlayın.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").getStyle().setIsLocked(true);
// Finally, Protect the sheet now.
worksheet.protect(AsposeCells.ProtectionType.All);
workbook.save(path.join(dataDir, "output.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
