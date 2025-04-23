---
title: Node.js ile C++ kullanarak İş Sayfasının Diyalog Sayfası olup olmadığını bulun
linktitle: Çalışma Sayfasının Diyaloğu Sayfa Olup Olmadığını Bulma
type: docs
weight: 90
url: /tr/nodejs-cpp/find-if-the-worksheet-is-dialog-sheet/
description: Bu makale, Aspose.Cells for Node.js via C++ kullanarak Excel iş sayfasının programlı olarak Diyalog Sayfası olup olmadığını belirleme talimatları ve örnek kodlar sağlar.
keywords: Excel iş sayfası diyalog tipi Node.js ile C++ kullanarak bulun, iş sayfası diyaloğu Node.js ve C++ ile
---

## **Olası Kullanım Senaryoları**

Diyalog Sayfası, bir diyalog kutusu içeren eski format bir sayfadır. Bu tür sayfa, eski Microsoft Excel sürümleri (örneğin 2003) tarafından eklenebilir ve ekran görüntüsüyle gösterilir. Ayrıca, yeni sürümlerde VBA kullanılarak da eklenebilir (örneğin Microsoft Excel 2016).

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Sayfanın diyalog sayfası veya başka bir tür olup olmadığını, Aspose.Cells for Node.js via C++ tarafından sağlanan [**Worksheet.getType()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getType--) özelliğiyle belirleyebilirsiniz. Eğer bu, [**SheetType.Dialog**](https://reference.aspose.com/cells/nodejs-cpp/sheettype) enumerate değeri ise, diyalog sayfasıyla ilgilendiğiniz anlamına gelir.

## **Çalışma Sayfasının Diyaloğu Sayfa Olup Olmadığını Bulma**

Aşağıdaki örnek kod, diyalog sayfası içeren [örnek Excel dosyasını](64716820.xlsx) yükler. [**Worksheet.getType()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getType--) özelliğini kontrol eder, [**SheetType.Dialog**](https://reference.aspose.com/cells/nodejs-cpp/sheettype) ile karşılaştırır ve mesajı yazdırır. Daha fazla yardım için aşağıdaki örnek kodun konsol çıktılarına bakabilirsiniz.

## **Örnek Kod**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFindIfWorksheetIsDialogSheet.xlsx");

// Load Excel file containing Dialog Sheet
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = workbook.getWorksheets().get(0);

// Find if the sheet type is dialog and print the message
if (ws.getType() === AsposeCells.SheetType.Dialog) {
console.log("Worksheet is a Dialog Sheet.");
}
```

## **Konsol Çıktısı**

{{< highlight js >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
