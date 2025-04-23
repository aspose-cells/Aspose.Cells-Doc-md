---
title: Blatt mit Node.js über C++ entsperren
linktitle: Arbeitsblatt entsperren
type: docs
weight: 20
url: /de/nodejs-cpp/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

Wenn ein Entwickler den Schutz von einem geschützten Arbeitsblatt zur Laufzeit entfernen muss, damit einige Änderungen an der Datei vorgenommen werden können? Dies kann mit Aspose.Cells einfach gemacht werden.

{{% /alert %}}

## **Arbeitsblatt entsperren**

### **Verwendung von Microsoft Excel**

Um den Schutz von einem Arbeitsblatt zu entfernen:

Wählen Sie im **Tools**-Menü **Protection** und dann **Unprotect Sheet**. Der Schutz wird entfernt, es sei denn, das Arbeitsblatt ist passwortgeschützt. In diesem Fall erscheint ein Dialog, der nach dem Passwort fragt. Geben Sie das Passwort ein, und das Arbeitsblatt wird ungeschützt.

### **Entsperren eines einfach geschützten Arbeitsblatts mit Aspose.Cells**

Ein Arbeitsblatt kann durch Aufrufen der [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse und ihrer [**unprotect()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unprotect--)-Methode entsperrt werden. Ein einfach geschütztes Arbeitsblatt ist eines, das nicht mit einem Passwort geschützt ist. Solche Arbeitsblätter können durch Aufrufen der [**unprotect()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unprotect--)-Methode ohne Parameter entsperrt werden.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unprotecting the worksheet without a password
worksheet.unprotect();

// Saving the Workbook
workbook.save(path.join(dataDir, "output.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **Entsperren eines passwortgeschützten Arbeitsblatts mit Aspose.Cells**

Ein passwortgeschütztes Arbeitsblatt ist eines, das mit einem Passwort geschützt ist. Solche Arbeitsblätter können entsperrt werden, indem eine überladene Version der [**unprotect()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unprotect--)-Methode aufgerufen wird, die das Passwort als Parameter annimmt.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unprotecting the worksheet with a password
worksheet.unprotect("");

// Save Workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```
