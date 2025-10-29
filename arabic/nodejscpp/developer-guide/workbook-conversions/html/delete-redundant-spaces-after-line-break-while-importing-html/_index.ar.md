---
title: حذف المسافات الزائدة بعد فاصل الأسطر أثناء استيراد HTML باستخدام Node.js عبر C++
linktitle: حذف المسافات الزائدة بعد فواصل الأسطر أثناء استيراد HTML
type: docs
weight: 20
url: /ar/nodejs-cpp/delete-redundant-spaces-after-line-break-while-importing/
description: تعلم كيفية حذف المسافات الزائدة بعد فواصل الأسطر أثناء استيراد HTML باستخدام Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

يرجى استخدام الخاصية [**HtmlLoadOptions.getDeleteRedundantSpaces()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getDeleteRedundantSpaces--) وتعيينها **true** لحذف جميع المسافات الزائدة التي تأتي بعد وسم فاصل الأسطر. بشكل افتراضي، تكون هذه الخاصية **false** ويتم الاحتفاظ بالمسافات الزائدة في ملفات Excel الناتجة.

{{% /alert %}}

# تأثير تعيين خاصية HTMLLoadOptions.deleteRedundantSpaces إلى false و true

تُظهر اللقطة الشاشة التالية تأثير تعيين هذه الخاصية إلى **false** و **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## حذف المسافات الزائدة بعد فواصل الأسطر أثناء استيراد HTML

### مثال برمجي

يعرض رمز النموذج التالي كيفية استخدام الخاصية [**HtmlLoadOptions.getDeleteRedundantSpaces()**](https://reference.aspose.com/cells/nodejs-cpp/htmlloadoptions/#getDeleteRedundantSpaces--). يرجى تعيينها إلى **true** أو **false** للحصول على الناتج كما هو موضح في لقطة الشاشة أعلاه.

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
