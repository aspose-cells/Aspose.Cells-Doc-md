---
title: Node.js ve C++ kullanarak Çalışma Sayfalarını Koruma
linktitle: Çalışma Sayfalarını Koruma
type: docs
weight: 10
url: /tr/nodejs-cpp/protecting-worksheets/
description: Aspose.Cells for Node.js via C++ kullanarak Excel de çalışma sayfalarını koruma yöntemlerini öğrenin, satırları, sütunları ve belirli hücreleri koruma dahil.
---


{{% alert color="primary" %}}

Bir çalışma sayfası korunduğunda, kullanıcıların yapabileceği işlemler kısıtlanır. Örneğin, veri girişi yapamazlar, satırları veya sütunları ekleyip silemezler vb.

{{% /alert %}}

## **Çalışma Sayfalarını Koruma**

### **Giriş**

Microsoft Excel'de genel koruma seçenekleri:

- İçerik
- Nesneler
- Senaryolar

Korunan çalışma sayfaları hassas verileri gizlemez veya korumaz, bu nedenle dosya şifrelemesinden farklıdır. Genellikle, çalışma sayfası koruması sunumsal amaçlar için uygundur. Kullanıcının çalışma sayfasındaki veri, içerik ve biçimlendirmeyi değiştirmesini önler.

### **Bir Çalışma Sayfasını Koruma**

Aspose.Cells, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) adlı bir sınıf sağlar, bu da bir Microsoft Excel dosyasını temsil eder. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) koleksiyonu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı ile temsil edilir.

[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı, çalışma sayfası üzerinde koruma uygulamak için kullanılan [**protect(ProtectionType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#protect-protectiontype-) yöntemini sağlar. [**protect(ProtectionType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#protect-protectiontype-) yöntemi aşağıdaki parametreleri kabul eder:

- Koruma Türü, çalışma sayfasına uygulanacak koruma türü. Koruma türü, [**ProtectionType**](https://reference.aspose.com/cells/nodejs-cpp/protectiontype) numaralandırması ile uygulanır.
- Yeni Parola, çalışma sayfasını korumak için kullanılan yeni parola.
- Eski Parola, çalışma sayfası zaten parola korumalıysa eski paroladır. Çalışma sayfası zaten korunmamışsa sadece null geçirin.

[**ProtectionType**](https://reference.aspose.com/cells/nodejs-cpp/protectiontype) enum'unda şu ön tanımlı koruma türleri bulunur:

|**Koruma Türleri**|**Açıklama**|
| :- | :- |
|All|Kullanıcı bu çalışma sayfasında herhangi bir şeyi değiştiremez|
|Contents|Kullanıcı bu çalışma sayfasında veri giremez|
|Objects|Kullanıcı çizim nesnelerini değiştiremez|
|Scenarios|Kullanıcı, kaydedilmiş senaryoları değiştiremez|
|Structure|Kullanıcı yapıyı değiştiremez|
|Windows|Koruma, pencerelere uygulanır|
|None|Koruma uygulanmaz|

Aşağıdaki örnek, bir çalışma sayfasını bir şifre ile korumanın nasıl yapıldığını göstermektedir.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object with file buffer
const excel = new AsposeCells.Workbook(fs.readFileSync(filePath));

// Accessing the first worksheet in the Excel file
const worksheet = excel.getWorksheets().get(0);

// Protecting the worksheet with a password
worksheet.protect(AsposeCells.ProtectionType.All, "aspose", null);

// Saving the modified Excel file in default format
excel.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

Yukarıdaki kod çalışma sayfasını korumak için kullanıldıktan sonra, çalışma sayfasının korumasını açarak kontrol edebilirsiniz. Dosyayı açtığınızda çalışma sayfasına bazı veriler eklemeye çalıştığınızda aşağıdaki iletişim kutusunu göreceksiniz:

|**Kullanıcının çalışma sayfasını değiştiremeyeceği konusunda uyarı veren iletişim kutusu**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

Çalışma sayfasında çalışmak için **Koruma**, ardından **Sayfayı Korumayı Kaldır** öğesini **Araçlar** menü öğesinden seçerek çalışma sayfasının korumasını kaldırın.

**Sayfayı Korumayı Kaldır** menü öğesini seçtikten sonra, bir iletişim kutusu açılacaktır ve size çalışma sayfasında çalışmanız için şifreyi girmenizi isteyecektir, aşağıda gösterildiği gibi:

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **Microsoft Excel Kullanarak Çalışma Sayfasındaki Birkaç Hücreyi Koruma**

Belli senaryolarda, sadece birkaç hücreyi kilitlemeniz gerekebilir. Belirli hücreleri kilitlemek istiyorsanız, diğer tüm hücreleri kilidini açmanız gerekir. Bir çalışma sayfasındaki tüm hücreler zaten kilitlenmek üzere ayarlanmıştır; bunu, herhangi bir Excel dosyasını MS Excel'de açıp **Biçim | Hücreler...** sekmesine tıklayarak ve **Koruma** sekmesine geçip "Kilitlemiş" onay kutusunun varsayılan olarak işaretli olduğunu görerek kontrol edebilirsiniz.

Microsoft Excel'de birkaç hücreyi kilitlemenin nasıl yapılacağını anlatan noktalar aşağıdadır. Bu yöntem, Microsoft Office Excel 97, 2000, 2002, 2003 ve sonraki sürümler için geçerlidir.

1. Satır numarası için doğrudan üzerindeki gri dikdörtgen (satır 1'in hemen üstündeki ve A sütun harfinin solundaki). **Tümünü Seç** düğmesine tıklayarak tüm çalışma sayfasını seçin.
2. **Biçim** menüsünde **Hücreler** seçeneğine tıklayın, **Koruma** sekmesine geçin ve ardından **Kilitlemiş** onay kutusunu temizleyin.
   Bu işlem, çalışma sayfasındaki tüm hücrelerin kilidini kaldırır.
   **Hücreler** komutu kullanılamıyorsa, çalışma sayfasının bazı bölümleri zaten kilitli olabilir. **Araçlar** menüsünde **Koruma**'ya gelin ve ardından **Sayfayı Korumayı Kaldır**'a tıklayın.
3. Sadece kilitlemek istediğiniz hücreleri seçin ve 2. adımı tekrarlayın, ancak bu sefer **Kilidi Açık** kutusunu seçin.
4. **Araçlar** menüsünden, **Koruma** üzerine gelin, **Sayfayı Koru** seçeneğine tıklayın ve ardından **Tamam** a tıklayın.
5. **Sayfayı Koru** iletişim kutusunda, bir şifre belirleme ve kullanıcıların değiştirmesini istediğiniz öğeleri seçme seçeneğiniz var.

### **Aspose.Cells Kullanarak Çalışma Sayfasında Birkaç Hücreyi Koru**

Bu yöntemde, yalnızca Aspose.Cells API'sini kullanarak bu işlemi gerçekleştiririz.

Örnek: Aşağıdaki örnek, çalışma sayfasında birkaç hücreyi nasıl koruyacağınızı gösterir. İlk olarak çalışma sayfasındaki tüm hücreleri açar ve ardından 3 hücreyi (A1, B1, C1) kilitler. Son olarak, çalışma sayfasını korur. [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesi, bir boolean özellik, [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) içerir. [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) özelliğini true veya false yapabilir ve *Column/Row.applyStyle()* metodunu kullanarak satır/sütun kilit veya kilit açabilirsiniz.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new workbook.
const wb = new AsposeCells.Workbook();

// Create a worksheet object and obtain the first sheet.
const sheet = wb.getWorksheets().get(0);

// Define the style object.
let style;

// Define the styleflag object
const styleflag = new AsposeCells.StyleFlag();

// Loop through all the columns in the worksheet and unlock them.
for (let i = 0; i <= 255; i++) {
style = sheet.getCells().getColumns().get((i)).getStyle();
style.setIsLocked(false);
styleflag.setLocked(true);
sheet.getCells().getColumns().get((i)).applyStyle(style, styleflag);
}

// Lock the three cells...i.e. A1, B1, C1.
style = sheet.getCells().get("A1").getStyle();
style.setIsLocked(true);
sheet.getCells().get("A1").setStyle(style);
style = sheet.getCells().get("B1").getStyle();
style.setIsLocked(true);
sheet.getCells().get("B1").setStyle(style);
style = sheet.getCells().get("C1").getStyle();
style.setIsLocked(true);
sheet.getCells().get("C1").setStyle(style);

// Finally, Protect the sheet now.
sheet.protect(AsposeCells.ProtectionType.All);

// Save the excel file.
wb.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **Çalışma Sayfasında Bir Satırı Koruma**

Aspose.Cells, çalışma sayfasındaki herhangi bir satırı kolayca kilitlemenize olanak tanır. Burada, [**Aspose.Cells.Row**](https://reference.aspose.com/cells/nodejs-cpp/row) sınıfının [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/row/#applyStyle-style-styleflag-) metodunu kullanarak belirli bir satıra [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) uygulayabiliriz. Bu metod iki argüman alır: bir [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesi ve tüm üyeleri ilgili biçimlendirmeyle olan [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag) nesnesi.

Aşağıdaki örnek, bir çalışma sayfasında satırı nasıl koruyacağınızı gösterir. İlk olarak çalışma sayfasındaki tüm hücreleri açar ve ardından ilk satırı kilitler. Son olarak, çalışma sayfasını korur. [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesi, bir boolean özellik, [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) içerir. [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) özelliğini true veya false yaparak satır/sütunu [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag) nesnesi kullanarak kilitleyebilir veya kilit açılsını açabilirsiniz.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new workbook.
const wb = new AsposeCells.Workbook();

// Create a worksheet object and obtain the first sheet.
const sheet = wb.getWorksheets().get(0);

// Define the style object.
let style;

// Define the styleflag object.
const flag = new AsposeCells.StyleFlag();

// Loop through all the columns in the worksheet and unlock them.
for (let i = 0; i <= 255; i++) {
style = sheet.getCells().getColumns().get(i).getStyle();
style.setIsLocked(false);
flag.setLocked(true);
sheet.getCells().getColumns().get(i).applyStyle(style, flag);
}

// Get the first row style.
style = sheet.getCells().getRows().get(0).getStyle();

// Lock it.
style.setIsLocked(true);

// Set the lock setting.
flag.setLocked(true);

// Apply the style to the first row.
sheet.getCells().applyRowStyle(0, style, flag);

// Protect the sheet.
sheet.protect(AsposeCells.ProtectionType.All);

// Save the excel file.
wb.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **Çalışma Sayfasında Bir Sütunu Koruma**

Aspose.Cells, herhangi bir sütunu kolayca kilitlemenize izin verir. Burada, [**Aspose.Cells.Column**](https://reference.aspose.com/cells/nodejs-cpp/column) sınıfının [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/column/#applyStyle-style-styleflag-) metodunu kullanarak belirli bir sütuna [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) uygulayabiliriz. Bu metod iki argüman alır: bir [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesi ve tüm üyeleri ilgili biçimlendirmeyle olan [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag) nesnesi.

Aşağıdaki örnek, bir çalışma sayfasında sütunu nasıl koruyacağınızı gösterir. İlk olarak çalışma sayfasındaki tüm hücreleri açar ve ardından ilk sütunu kilitler. Son olarak, çalışma sayfasını korur. [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesi, bir boolean özellik, [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) içerir. [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) özelliğini true veya false yaparak satır/sütunu [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag) nesnesi kullanarak kilitleyebilir veya kilit açabilirsiniz.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new workbook.
const wb = new AsposeCells.Workbook();

// Create a worksheet object and obtain the first sheet.
const sheet = wb.getWorksheets().get(0);

// Define the style object.
let style;

// Define the styleflag object.
const flag = new AsposeCells.StyleFlag();

// Loop through all the columns in the worksheet and unlock them.
for (let i = 0; i <= 255; i++) {
style = sheet.getCells().getColumns().get(i).getStyle();
style.setIsLocked(false);
flag.setLocked(true);
sheet.getCells().getColumns().get(i).applyStyle(style, flag);
}

// Get the first column style.
style = sheet.getCells().getColumns().get(0).getStyle();

// Lock it.
style.setIsLocked(true);

// Apply the style to the first column.
sheet.getCells().getColumns().get(0).applyStyle(style, flag);

// Protect the sheet.
sheet.protect(AsposeCells.ProtectionType.All);

// Save the excel file.
wb.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **Kullanıcılara Düzenleme Aralığı Izin Ver**

Aşağıdaki örnek, korunan bir çalışma sayfasında kullanıcılara bir aralığı düzenleme izni vermenin nasıl yapıldığını göstermektedir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const book = new AsposeCells.Workbook();

// Get the first (default) worksheet
const sheet = book.getWorksheets().get(0);

// Get the Allow Edit Ranges
const allowRanges = sheet.getAllowEditRanges();

// Define ProtectedRange
let protected_range;

// Create the range
const idx = allowRanges.add("r2", 1, 1, 3, 3);
protected_range = allowRanges.get(idx);

// Specify the password
protected_range.setPassword("123");

// Protect the sheet
sheet.protect(AsposeCells.ProtectionType.All);

// Save the Excel file
book.save(path.join(dataDir, "protectedrange.out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
