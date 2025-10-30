---
title: Node.js ve C++ kullanarak Paylaşılan Çalışma Kitabını Parola ile Koruma veya Parolasını Kaldırma
linktitle: Paylaşılan Çalışma Kitabını Koruma Altına Alma veya Korumasız Yapma
type: docs
weight: 10
url: /tr/nodejs-cpp/password-protect-or-unprotect-the-shared-workbook/
---

## **Olası Kullanım Senaryoları**

Aşağıdaki ekran görüntüsünde gösterildiği gibi, Microsoft Excel kullanarak paylaşılan çalışma kitabını koruyabilir veya korumasını kaldırabilirsiniz. Aspose.Cells for Node.js via C++ aynı zamanda bu özelliği [**Workbook.protectSharedWorkbook(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#protectSharedWorkbook-string-) ve [**Workbook.unprotectSharedWorkbook(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#unprotectSharedWorkbook-string-) metodlarıyla destekler.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **Paylaşılan çalışma kitabını koruma altına alan ve paylaşımı etkinleştiren bir çalışma kitabı oluşturan aşağıdaki örnek kod ve bunu [çıktı Excel dosyası](55541777.xlsx) olarak kaydeden bir çalışma sayfasına şifre eklemesini göstermektedir. Ekran görüntüsü, korumasız yapmaya çalıştığınızda Microsoft Excel'in şifreyi girmenizi istediğini göstermektedir.**

Aşağıdaki örnek kod, bir çalışma kitabı oluşturur, onu korur ve paylaşımı etkinleştirir ve [çıktı Excel dosyası](55541777.xlsx) olarak kaydeder. Ekran görüntüsü, açmak için denediğinizde, Microsoft Excel'in onu korumak için şifreyi girmenizi istediğini gösterir.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **Örnek Kod**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Create empty Excel file
const workbook = new AsposeCells.Workbook();

// Protect the Shared Workbook with Password
workbook.protectSharedWorkbook("1234");

// Uncomment this line to Unprotect the Shared Workbook
// workbook.unprotectSharedWorkbook("1234");

// Save the output Excel file
workbook.save("outputProtectSharedWorkbook.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
