---
title: Modifica la direzione del testo del commento con Node.js tramite C++
linktitle: Cambia la Direzione del Testo del Commento
type: docs
weight: 10
url: /it/nodejs-cpp/change-text-direction-of-the-comment/
description: Scopri come cambiare la direzione del testo dei commenti utilizzando Aspose.Cells for Node.js via C++. Personalizza efficacemente le impostazioni di allineamento del commento.
---

{{% alert color="primary" %}}

Microsoft Excel permette agli utenti di aggiungere commenti alle celle per aggiungere informazioni aggiuntive e evidenziare i dati. Gli sviluppatori potrebbero dover personalizzare il commento per specificare le impostazioni di allineamento e la direzione del testo. Aspose.Cells for Node.js via C++ fornisce API per completare il task.

{{% /alert %}}

Aspose.Cells for Node.js via C++ fornisce una proprietà [**Shape.getTextDirection()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextDirection--) per impostare la direzione del testo di un commento. Il seguente esempio di codice dimostra l’uso della proprietà [**Shape.getTextDirection()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextDirection--) per impostare la direzione del testo di un commento.

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
{{< app/cells/assistant language="nodejs-cpp" >}}
