---
title: HTML içe aktarırken satır sonrasında fazla boşlukları silmek için Node.js ve C++ kullanırken gereksiz boşlukları silmek
linktitle: HTML içe aktarılırken satır sonrası gereksiz boşlukları silin
type: docs
weight: 20
url: /tr/nodejs-cpp/delete-redundant-spaces-after-line-break-while-importing/
description: Aspose.Cells for Node.js via C++ kullanarak HTML içe aktarırken satır sonrasında gereksiz boşlukların nasıl silineceğini öğrenin.
---

{{% alert color="primary" %}}

 Lütfen [**HtmlLoadOptions.getDeleteRedundantSpaces()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getDeleteRedundantSpaces--) özelliğini kullanın ve **true** olarak ayarlayın, böylece satır sonu etiketi sonrası gelen tüm gereksiz boşluklar silinir. Varsayılan olarak, bu özellik **false**'dur ve gereksiz boşluklar çıktı Excel dosyalarında korunur.

{{% /alert %}}

## HTMLLoadOptions.deleteRedundantSpaces özelliği false ve true olarak ayarlandığında etkisi

Bu özelliği **false** ve **true** olarak ayarlamanın etkisini gösteren aşağıdaki ekran görüntüsü.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

HTML içe aktarılırken satır sonrası gereksiz boşlukları silme

### Programlama Örneği

Aşağıdaki örnek kod, [**HtmlLoadOptions.getDeleteRedundantSpaces()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getDeleteRedundantSpaces--) özelliğinin kullanımını gösterir. Lütfen çıktı almak için yukarıdaki ekran görüntüsünde gösterildiği gibi **true** veya **false** olarak ayarlayın.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Sample Html containing redundant spaces after <br> tag
const html = "<html> <body> <table> <tr> <td> <br>    This is sample data <br>    This is sample data<br>    This is sample data</td> </tr> </table> </body> </html>";

// Convert Html to byte array
const byteArray = Buffer.from(html, 'utf-8');

// Set Html load options and keep precision true
const loadOptions = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);
loadOptions.setDeleteRedundantSpaces(true);

// Convert byte array into stream
const stream = Uint8Array.from(byteArray);

// Create workbook from stream with Html load options
const workbook = new AsposeCells.Workbook(stream, loadOptions);

// Access first worksheet
const sheet = workbook.getWorksheets().get(0);

// Auto fit the sheet columns
sheet.autoFitColumns();

// Save the workbook
const outputDir = path.join(__dirname, "output");
workbook.save(path.join(outputDir, "outputDeleteRedundantSpacesWhileImportingFromHtml.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
