---
title: Belirli Unicode karakterlerin Yazarken Yazı Tipini Değiştirme
linktitle: PDF ye kaydederken belirli Unicode karakterlerinin yazı tipini değiştirin
type: docs
weight: 260
url: /tr/nodejs-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Aspose.Cells for Node.js via C++ kullanarak, PDF ye kaydederken belirli Unicode karakterlerin yazı tipini nasıl değiştireceğinizi öğrenin. 
---

{{% alert color="primary" %}} 

Bazı Unicode karakterleri, kullanıcı tarafından belirtilen font tarafından görüntülenemez. Bu tür bir Unicode karakter **Bilinmeyen Kesme** (U+2011)'dır ve Unicode numarası 8209'dur. Bu karakter **Times New Roman** ile görüntülenemez, ancak **Arial Unicode MS** gibi diğer fontlarla görüntülenebilir.

Bu tür bir karakter, Times New Roman gibi belirli bir yazı tipinde bir sözcük veya cümle içinde yer alıyorsa, Aspose.Cells tüm sözcüğün veya cümlenin yazı tipini bu karakteri gösterebilecek bir yazı tipine, örneğin Arial Unicode'dan MS'ye değiştirir.

Ancak, bu kullanıcılar için istenmeyen bir davranıştır ve yalnızca belirli karakterin yazı tipinin değiştirilmesini isterler; tüm kelimenin veya cümlenin yazı tipinin değiştirilmesi değil.

Bu sorunu çözmek için Aspose.Cells, sadece gösterilebilir olmayan belirli karakterlerin yazı tipini değiştiren ve diğer kısmın orijinal yazı tipinde kalmasını sağlayan `PdfSaveOptions.isFontSubstitutionCharGranularity` özelliğini sağlar. Bu özelliği true olarak ayarlamanız gerekir.

{{% /alert %}} 

## **Örnek**
Aşağıdaki ekran görüntüsü, aşağıdaki örnek kodu ile oluşturulan iki PDF'yi karşılaştırır.

İlk dosya, `PdfSaveOptions.isFontSubstitutionCharGranularity` özelliği ayarlanmadan oluşturulmuş, diğer ise bu özelliğin true olarak ayarlandığı dosyadır.

İlk PDF'de, Tüm cümlenin yazı tipi Non-Breaking Hyphen nedeniyle Times New Roman'dan Arial Unicode MS'ye değişti. İkinci PDF'de ise sadece Non-Breaking Hyphen'in yazı tipi değişti.

|**İlk Pdf Dosyası**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**İkinci Pdf Dosyası**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **Örnek Kod**


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cells
const cell1 = worksheet.getCells().get("A1");
const cell2 = worksheet.getCells().get("B1");

// Set the styles of both cells to Times New Roman
let style = cell1.getStyle();
style.getFont().setName("Times New Roman");
cell1.setStyle(style);
cell2.setStyle(style);

// Put the values inside the cell
cell1.putValue("Hello without Non-Breaking Hyphen");
cell2.putValue("Hello" + String.fromCharCode(8209) + " with Non-Breaking Hyphen");

// Autofit the columns
worksheet.autoFitColumns();

// Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
workbook.save(path.join(dataDir, "SampleOutput_out.pdf"));

// Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true
const opts = new AsposeCells.PdfSaveOptions();
opts.setIsFontSubstitutionCharGranularity(true);
workbook.save(path.join(dataDir, "SampleOutput2_out.pdf"), opts);
```



{{< app/cells/assistant language="nodejs-cpp" >}}
