---
title: Node.js kullanarak C++ ile Çoklu Kodlamalarla CSV Dosyasını Okuma
linktitle: Birden Fazla Kodlama ile CSV Dosyasını Okuma
type: docs
weight: 200
url: /tr/nodejs-cpp/reading-csv-file-with-multiple-encodings/
description: Aspose.Cells for Node.js via C++ kullanarak çoklu kodlamalarda CSV dosyalarını nasıl okuyacağınızı öğrenin.
---


{{% alert color="primary" %}}

Bazen, CSV dosyanız birden fazla Kodlama (Unicode, ANSI, UTF8, UTF7 vb) içerir. Aspose.Cells, bu tür CSV dosyalarını yüklemenize ve başka biçimlere dönüştürmenize olanak tanır, örneğin PDF veya XLSX.

{{% /alert %}}

Aspose.Cells, [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--) özelliği sağlar, bu özelliği doğru şekilde yüklemek için **true** olarak ayarlamanız gerekir.

Aşağıdaki ekran görüntüsü, iki satır içeren örnek bir CSV dosyasını gösterir. İlk satır **ANSI** kodlamasındadır ve ikinci satır **Unicode** kodlamasındadır

|**Giriş dosyası**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)|

Aşağıdaki ekran görüntüsü, yukarıdaki CSV dosyasından dönüştürülmüş XLSX dosyasını gösterir, [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--) özelliği **true** olarak ayarlanmamıştır. Görüldüğü gibi, Unicode metni düzgün çevrilmemiştir.

|**Çıktı dosyası 1: çoklu kodlamalar için herhangi bir düzenleme yapılmamıştır**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)|

Aşağıdaki ekran görüntüsü, [**TxtLoadOptions.isMultiEncoded()**](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#isMultiEncoded--) özelliği **true** olarak ayarlandıktan sonra yukarıdaki CSV dosyasından dönüştürülmüş XSLX dosyasını göstermektedir. Görüleceği üzere, Unicode metin artık düzgün şekilde dönüştürülmüştür.

|**Çıktı dosyası 2: IsMultiEncoded true olarak ayarlandı**|
| :- |
|![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)|

Aşağıdaki örnek kod, yukarıdaki CSV dosyasını XLSX formatına uygun bir şekilde dönüştürür.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "MultiEncoded.csv");

// Set Multi Encoded Property to True
const options = new AsposeCells.TxtLoadOptions();
options.setIsMultiEncoded(true);

// Load the CSV file into Workbook
const workbook = new AsposeCells.Workbook(filePath, options);

// Save it in XLSX format
workbook.save(path.join(dataDir, "MultiEncoded.csv.out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```

## İlgili Makaleler

- [CSV Dosyalarını Açma](/cells/tr/nodejs-cpp/opening-files-with-different-formats/#opening-csv-files)
