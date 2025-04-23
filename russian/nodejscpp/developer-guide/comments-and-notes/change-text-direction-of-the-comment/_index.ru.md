---
title: Изменить направление текста комментария с помощью Node.js через C++
linktitle: Изменение направления текста комментария
type: docs
weight: 10
url: /ru/nodejs-cpp/change-text-direction-of-the-comment/
description: Узнайте, как изменить направление текста комментариев с помощью Aspose.Cells for Node.js via C++. Эффективно настраивайте параметры выравнивания комментария и направление текста.
---

{{% alert color="primary" %}}

Microsoft Excel позволяет пользователям добавлять комментарии к ячейкам для добавления дополнительной информации и выделения данных. Разработчики могут настроить комментарий, чтобы указать параметры выравнивания и направление текста. Aspose.Cells for Node.js via C++ предоставляет API для выполнения этой задачи.

{{% /alert %}}

Aspose.Cells for Node.js via C++ предоставляет свойство [**Shape.getTextDirection()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextDirection--) для установки направления текста в комментарии. Следующий пример кода демонстрирует использование свойства [**Shape.getTextDirection()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextDirection--) для установки направления текста комментария.

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
