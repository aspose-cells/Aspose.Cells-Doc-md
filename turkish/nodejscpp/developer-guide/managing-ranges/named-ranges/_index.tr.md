---
title: Node.js ve C++ kullanarak Çalışma Kitabı ve Çalışma Sayfası Kapsamlı Özel Ad Aralıkları Oluşturma
linktitle: Adlandırılmış Aralık
type: docs
weight: 40
url: /tr/nodejs-cpp/create-workbook-and-worksheet-scoped-named-ranges/
description: Aspose.Cells for Node.js via C++ kullanarak çalışma kitabı ve çalışma sayfası kapsamlı özel ad aralıklarını nasıl oluşturacağınızı öğrenin. 
---

{{% alert color="primary" %}} 

Microsoft Excel, kullanıcılara çalışma kitabı (aynı zamanda genel kapsam olarak da bilinir) ve çalışma sayfası olmak üzere iki farklı kapsamla adlandırılmış aralıkları tanımlama imkanı tanır.

- Bir çalışma kitabı kapsamına sahip adlandırılmış aralıklar, sadece isimlerini kullanarak o çalışma kitabındaki herhangi bir çalışma sayfasından erişilebilir.
- Çalışma sayfası kapsamlı adlandırılmış aralıklar, oluşturulduğu belirli çalışma sayfasına referansla erişilir.

Aspose.Cells for Node.js via C++, çalışma kitabı ve çalışma sayfası kapsamlı isimlendirilmiş aralıklar eklemek için Microsoft Excel ile aynı işlevselliği sağlar. Bir çalışma sayfası kapsamlı isimlendirilmiş aralık oluştururken, çalışma sayfası referansı, onu çalışma sayfası kapsamlı isimlendirilmiş aralık olarak belirtmek için isimlendirilmiş aralıkta kullanılmalıdır.

{{% /alert %}} 
## **Çalışma Kitabı Kapsamlı Adlandırılmış Aralık Ekleme**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook object
const workbook = new AsposeCells.Workbook();

// Get first worksheet of the workbook
const sheet = workbook.getWorksheets().get(0);

// Get worksheet's cells collection
const cells = sheet.getCells();

// Create a range of Cells from Cell A1 to C10
const workbookScope = cells.createRange("A1", "C10");

// Assign the name to workbook scope named range
workbookScope.setName("workbookScope");

// Save the workbook
workbook.save(path.join(dataDir, "WorkbookScope.out.xlsx"));
```
## **Çalışma Sayfası Kapsamlı Adlandırılmış Aralık Ekleme**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new Workbook object
const workbook = new AsposeCells.Workbook();

// Get first worksheet of the workbook
const sheet = workbook.getWorksheets().get(0);

// Get worksheet's cells collection
const cells = sheet.getCells();
// Create a range of Cells
const localRange = cells.createRange("A1", "C10");

// Assign name to range with sheet reference
localRange.setName("Sheet1!local");

// Save the workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **Gelişmiş Konular**
- [Erişim Oluştur ve Adlandırılmış Aralıkları Kopyala](/cells/tr/nodejs-cpp/create-access-and-copy-named-ranges/)
- [Biçimlendir ve Adlandırılmış Aralıkları Değiştir](/cells/tr/nodejs-cpp/format-and-modify-named-ranges/)
- [Harici Bağlantıları Olan Aralığı Al](/cells/tr/nodejs-cpp/get-range-with-external-links/)
- [Sıralı Olmayan Aralıkları Uygulama](/cells/tr/nodejs-cpp/implementing-non-sequential-ranges/)


{{< app/cells/assistant language="nodejs-cpp" >}}
