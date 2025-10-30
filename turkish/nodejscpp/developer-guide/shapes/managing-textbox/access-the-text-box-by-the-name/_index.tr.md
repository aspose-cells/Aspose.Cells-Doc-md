---
title: Node.js ile C++ kullanarak isim ile Metin Kutusuna Erişim
linktitle: Ada Göre Metin Kutusuna Eriş
type: docs
weight: 230
url: /tr/nodejs-cpp/access-the-text-box-by-the-name/
description: Aspose.Cells for Node.js via C++ kullanarak koleksiyondan ad ile metin kutusuna nasıl erişileceğini öğrenin. 
---

## Ada Göre Metin Kutusuna Eriş

 Eskiden, metin kutularına [**Worksheet.getTextBoxes()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getTextBoxes--) koleksiyonundan indeks kullanılarak erişilirdi, ama şimdi koleksiyondan isimle de erişebilirsiniz. Bu, zaten adını bildiğiniz takdirde metin kutusuna hızlı ve kullanışlı bir erişim sağlar.

Aşağıdaki örnek kod öncelikle bir metin kutusu oluşturur ve ona bazı metin ve ad atar. Ardından aynı metin kutusuna adıyla erişir ve metnini yazdırır.

### Node.js kodu ile isim ile Metin Kutusuna erişme

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the TextBox to the worksheet
const idx = sheet.getTextBoxes().add(10, 10, 10, 10);

// Access newly created TextBox using its index & name it
const tb1 = sheet.getTextBoxes().get(idx);
tb1.setName("MyTextBox");

// Set text for the TextBox
tb1.setText("This is MyTextBox");

// Access the same TextBox via its name
const tb2 = sheet.getTextBoxes().get("MyTextBox");

// Display the text of the TextBox accessed via name
console.log(tb2.getText());

console.log("Press any key to continue...");
```

### Örnek kod tarafından oluşturulan konsol çıktısı

Yukarıdaki örnek kodun konsol çıktısı burada gösterilmektedir.

{{< highlight javascript >}}
This is MyTextBox
{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
