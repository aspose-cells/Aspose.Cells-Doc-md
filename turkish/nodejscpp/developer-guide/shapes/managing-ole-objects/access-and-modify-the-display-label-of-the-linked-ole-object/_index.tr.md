---
title: Node.js ve C++ kullanarak Bağlantılı Ole Nesnesinin Görüntü Etiketini Erişin ve Değiştirin
linktitle: Bağlantılı Ole Nesnesinin Görüntü Etiketini Erişme ve Değiştirme
type: docs
weight: 100
url: /tr/nodejs-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/
description: Bağlantılı Ole nesnesinin görüntü etiketine nasıl erişileceğini ve değiştirileceğini Aspose.Cells for Node.js via C++ kullanarak öğrenin. 
---

## **Olası Kullanım Senaryoları**

Microsoft Excel, aşağıdaki ekran görüntüsünde gösterildiği gibi Ole nesnesinin görüntü etiketini değiştirmeye izin verir. Ayrıca, Aspose.Cells API'leriyle [**OleObject.getLabel()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getLabel--) özelliği kullanılarak Ole nesnesinin görüntü etiketine erişebilir veya değiştirebilirsiniz.

![todo:image_alt_text](access-and-modify-the-display-label-of-the-linked-ole-object_1.png)

## **Bağlı Ole Nesnesinin Görüntü Etiketini Erişme ve Değiştirme**

 Lütfen aşağıdaki örnek kodu inceleyin, bu kod [örnek Excel dosyasını](64716810.xlsx) yükler ve içerisinde Ole Nesnesi bulunur. Kod, Ole Nesnesine erişir ve etiketini 'Sample APIs' değerinden 'Aspose APIs' değerine değiştirir. Aşağıda, örnek kodun bu Excel dosyasına etkisini gösteren konsol çıktısını görebilirsiniz.

## **Örnek Kod**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleAccessAndModifyLabelOfOleObject.xlsx");

// Load the sample Excel file 
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access first Ole Object
let oleObject = ws.getOleObjects().get(0);

// Display the Label of the Ole Object
console.log("Ole Object Label - Before: " + oleObject.getLabel());

// Modify the Label of the Ole Object
oleObject.setLabel("Aspose APIs");

// Save workbook to memory stream
const ms = wb.save(AsposeCells.SaveFormat.Xlsx);

// Set the workbook reference to null
wb.dispose();

// Load workbook from memory stream
const wbFromStream = new AsposeCells.Workbook(ms);

// Access first worksheet
const wsFromStream = wbFromStream.getWorksheets().get(0);

// Access first Ole Object
oleObject = wsFromStream.getOleObjects().get(0);

// Display the Label of the Ole Object that has been modified earlier
console.log("Ole Object Label - After: " + oleObject.getLabel());
```

## **Konsol Çıktısı**

{{< highlight javascript >}}

Ole Object Label - Before: Sample APIs

Ole Object Label - After: Aspose APIs

{{< /highlight >}}
