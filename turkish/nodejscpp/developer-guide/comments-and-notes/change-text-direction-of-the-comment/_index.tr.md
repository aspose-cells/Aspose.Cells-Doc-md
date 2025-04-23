---
title: Yorumun Metin Yönünü Node.js kullanarak C++ ile Değiştirin
linktitle: Yorumun Metin Yönünü Değiştir
type: docs
weight: 10
url: /tr/nodejs-cpp/change-text-direction-of-the-comment/
description: Aspose.Cells for Node.js via C++ kullanarak yorumların metin yönünü nasıl değiştireceğinizi öğrenin. Yorum hizalama ayarlarını ve metin yönünü etkili şekilde özelleştirin.
---

{{% alert color="primary" %}}

Microsoft Excel, hücrelere ek bilgiler eklemek ve veriyi vurgulamak için yorumlar eklemeye izin verir. Geliştiriciler, hizalama ayarlarını ve metin yönünü belirlemek için yorumu özelleştirmeleri gerekebilir. Aspose.Cells for Node.js via C++, bu görevi yerine getirmek için API'ler sağlar.

{{% /alert %}}

Aspose.Cells for Node.js via C++, yorunun metin yönünü ayarlamak için [**Shape.getTextDirection()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextDirection--) özelliği sağlar. Aşağıdaki örnek kod, [**Shape.getTextDirection()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextDirection--) özelliğinin kullanımıyla yorunun metin yönünü ayarlamayı gösterir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const wb = new AsposeCells.Workbook();

// Get the first worksheet
const sheet = wb.getWorksheets().get(0);

// Add a comment to A1 cell
const commentIndex = sheet.getComments().add("A1");
const comment = sheet.getComments().get(commentIndex);

// Set its vertical alignment setting            
comment.getCommentShape().setTextVerticalAlignment(AsposeCells.TextAlignmentType.Center);

// Set its horizontal alignment setting
comment.getCommentShape().setTextHorizontalAlignment(AsposeCells.TextAlignmentType.Right);

// Set the Text Direction - Right-to-Left
comment.getCommentShape().setTextOrientationType(AsposeCells.TextDirectionType.RightToLeft);

// Set the Comment note
comment.setNote("This is my Comment Text. This is test");

const outputFilePath = path.join(dataDir, "OutCommentShape.out.xlsx");
// Save the Excel file
wb.save(outputFilePath);
```
