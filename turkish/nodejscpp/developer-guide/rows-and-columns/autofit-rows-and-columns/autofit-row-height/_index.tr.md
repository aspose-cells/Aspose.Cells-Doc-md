---
title: Node.js kullanarak dosya yüklenirken otomatik Satır yüksekliği ayarla (C++ ile)
linktitle: Dosya Yüklenirken Otomatik Satır Yüksekliğini Ayarla
type: docs
weight: 120
url: /tr/nodejs-cpp/autofit-row-height/
description: Aspose.Cells for Node.js via C++ kullanarak, yüklenen dosyada özelleştirilmemiş yükseklikteki satırların sığdırılmasını nasıl öğreneceğinizi öğrenin.
keywords: Yükleme sırasında Otomatik Satır Yüksekliği ayarlama, Node.js kullanarak, excel dosyasını açarken satır yüksekliğini otomatik ayarlayın 
---

## **Olası Kullanım Senaryoları**
Satır yüksekliği, içeriğin fontuna uygun şekilde otomatik olarak ayarlanır, ancak önbelleğe alınan satır yüksekliği dosyadaki içerikle eşleşmiyorsa, MS Excel yükleme sırasında satır yüksekliğini otomatik olarak ayarlar, Aspose.Cells for Node.js via C++ ise bunu otomatik olarak ayarlamaz ve performansı artırır. Dosya yüklerken satır yüksekliğinin otomatik uyumunu yapmak için, kodunuzdaki [setAutoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setAutoFitterOptions-autofitteroptions-) parametresiyle gerçekleştirebilirsiniz.

Lütfen aşağıdaki görsel veriye bakın. Satır 11’deki önbelleğe alınmış satır yüksekliği 15 olup, Excel yükleme sırasında otomatik olarak satır yüksekliğini ayarlamıştır.
<br>
<img src="1.png" width=70% />

## **Aspose.Cells for Node.js via C++ kullanarak Satır Yüksekliğini Ayarla**
Dosyayı doğrudan yükleyip PDF olarak kaydettiğinizde, PDF'de veriler tam olarak görüntülenmeyebilir çünkü önbelleğe alınmış satır yüksekliği sadece 15'tir.
<br>
<img src="2.png" width=70% />
<br>
Dosyayı yüklerken [setAutoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setAutoFitterOptions-autofitteroptions-) parametresini true yaparsanız, Aspose.Cells otomatik olarak satır yüksekliğini ayarlayacaktır. Bu ayarlanan satır yüksekliği, metin gösterim ihtiyaçlarınızı karşılayacak seviyededir.
<br>
<img src="3.png" width=70% />

## **Node.js Örnek Kodu**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
workbook.save(path.join(dataDir, "out.pdf"));

const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setAutoFitterOptions(new AsposeCells.AutoFitterOptions());
loadOptions.getAutoFitterOptions().setOnlyAuto(true);
const book = new AsposeCells.Workbook(filePath, loadOptions);
book.save(path.join(dataDir, "out2.pdf"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
