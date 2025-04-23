---
title: Çalışma Sayfasını Node.js ile C++ kullanarak Koru Olmayan hale getirme
linktitle: Bir Çalışma Sayfasının Korumasını Kaldır
type: docs
weight: 20
url: /tr/nodejs-cpp/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

Bir geliştirici, çalışma sayfasındaki korumayı çalışma zamanında kaldırarak dosyaya bazı değişiklikler yapabilir mi? Bu, Aspose.Cells ile kolayca yapılabilir.

{{% /alert %}}

## **Bir Çalışma Sayfasını Korumayı Kaldırma**

### **Microsoft Excel Kullanımı**

Çalışma sayfasından korumayı kaldırmak için:

**Araçlar** menüsünden, **Koruma** ardından **Sayfayı Koru** seçin. Koruma kaldırılır, sayfa şifrelenmiş değilse. Bu durumda, bir iletişim kutusu şifre istemektedir. Şifreyi girin ve sayfa koruması kaldırılacaktır.

### **Aspose.Cells Kullanarak Basit Korumalı Bir Çalışma Sayfasının Korumasız Bırakılması**

Bir çalışma sayfasını, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfının [**unprotect()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unprotect--) metodunu çağırarak korumasını kaldırabilirsiniz. Şifre koruması olmayan, basitçe korunmamış bir çalışma sayfası, şifre ile korunmamış olanıdır. Bu tür çalışma sayfaları, parametre geçirmeden [**unprotect()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unprotect--) metodunu çağırarak korunma kaldırılabilir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unprotecting the worksheet without a password
worksheet.unprotect();

// Saving the Workbook
workbook.save(path.join(dataDir, "output.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **Aspose.Cells Kullanarak Şifre Korumalı Bir Çalışma Sayfasının Korumasız Bırakılması**

Şifre ile korunan çalışma sayfası, parolayla korunmuş bir çalışma sayfasıdır. Bu tür çalışma sayfaları, şifreyi parametre olarak alan [**unprotect()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unprotect--) metodunun aşırı yüklenmiş bir versiyonunu çağırarak korunabilir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unprotecting the worksheet with a password
worksheet.unprotect("");

// Save Workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```
