---
title: Arbeitsblätter mit Node.js via C++ schützen
linktitle: Arbeitsblätter schützen
type: docs
weight: 10
url: /de/nodejs-cpp/protecting-worksheets/
description: Lernen Sie, wie Sie Arbeitsblätter in Excel mit Aspose.Cells for Node.js via C++ schützen, einschließlich Schutz für Zeilen, Spalten und bestimmte Zellen.
---


{{% alert color="primary" %}}

Wenn ein Arbeitsblatt geschützt ist, sind die Aktionen, die ein Benutzer durchführen kann, eingeschränkt. Zum Beispiel können sie keine Daten eingeben, Zeilen oder Spalten einfügen oder löschen usw.

{{% /alert %}}

## **Arbeitsblätter schützen**

### **Einführung**

Die allgemeinen Schutzeinstellungen in Microsoft Excel sind:

- Inhalt
- Objekte
- Szenarien

Geschützte Arbeitsblätter verbergen oder schützen keine sensiblen Daten, daher unterscheidet es sich von der Datei-Verschlüsselung. Allgemein ist der Arbeitsblattschutz für Präsentationszwecke geeignet. Er verhindert, dass der Endbenutzer Daten, Inhalt und Formatierung im Arbeitsblatt ändert.

### **Ein Arbeitsblatt schützen**

Aspose.Cells stellt eine Klasse [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) bereit, die eine Microsoft Excel-Datei repräsentiert. Die [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)-Klasse enthält eine [**getWorksheets()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)-Sammlung, die Zugriff auf jedes Arbeitsblatt in einer Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) dargestellt.

Die [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-Klasse bietet die [**protect(ProtectionType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#protect-protectiontype-)-Methode, die zum Anwenden des Schutzes auf das Arbeitsblatt verwendet wird. Die [**protect(ProtectionType)**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#protect-protectiontype-)-Methode akzeptiert die folgenden Parameter:

- Schutzttyp, der Typ des Schutzes, der auf das Arbeitsblatt angewendet werden soll. Der Schutzttyp wird mithilfe der Enumeration [**ProtectionType**](https://reference.aspose.com/cells/nodejs-cpp/protectiontype) angewendet.
- Neues Passwort, das neue Passwort, das zum Schutz des Arbeitsblatts verwendet wird.
- Altes Kennwort, das alte Kennwort, wenn das Arbeitsblatt bereits passwortgeschützt ist. Wenn das Arbeitsblatt noch nicht geschützt ist, dann einfach null übergeben.

Das [**ProtectionType**](https://reference.aspose.com/cells/nodejs-cpp/protectiontype)-Enum enthält die folgenden vordefinierten Schutzarten:

|**Schutztypen**|**Beschreibung**|
| :- | :- |
|All|Der Benutzer kann nichts auf diesem Arbeitsblatt ändern|
|Contents|Der Benutzer kann keine Daten in dieses Arbeitsblatt eingeben|
|Objects|Der Benutzer kann Zeichenobjekte nicht ändern|
|Scenarios|Der Benutzer kann gespeicherte Szenarien nicht ändern|
|Structure|Der Benutzer kann die Struktur nicht ändern|
|Windows|Der Schutz wird auf Fenster angewendet|
|None|Es ist kein Schutz angewendet|

Das folgende Beispiel zeigt, wie ein Arbeitsblatt mit einem Passwort geschützt wird.

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object with file buffer
const excel = new AsposeCells.Workbook(fs.readFileSync(filePath));

// Accessing the first worksheet in the Excel file
const worksheet = excel.getWorksheets().get(0);

// Protecting the worksheet with a password
worksheet.protect(AsposeCells.ProtectionType.All, "aspose", null);

// Saving the modified Excel file in default format
excel.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

Nachdem der obige Code zum Schutz des Arbeitsblatts verwendet wurde, können Sie den Schutz auf dem Arbeitsblatt überprüfen, indem Sie es öffnen. Sobald Sie die Datei öffnen und versuchen, einige Daten in das Arbeitsblatt einzufügen, sehen Sie den folgenden Dialog:

|**Ein Dialog, der darauf hinweist, dass ein Benutzer das Arbeitsblatt nicht ändern kann**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

Um am Arbeitsblatt zu arbeiten, heben Sie den Schutz des Arbeitsblatts auf, indem Sie im **Werkzeuge**-Menüpunkt **Schutz** und dann **Arbeitsblatt entsperren** auswählen.

Nachdem Sie den Menüpunkt Arbeitsblatt entsperren ausgewählt haben, öffnet sich ein Dialog, der Sie auffordert, das Passwort einzugeben, damit Sie am Arbeitsblatt arbeiten können, wie unten gezeigt:

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **Einige Zellen im Arbeitsblatt mit Microsoft Excel schützen**

Es kann bestimmte Szenarien geben, bei denen Sie nur einige Zellen im Arbeitsblatt sperren müssen. Wenn Sie bestimmte Zellen im Arbeitsblatt sperren möchten, müssen Sie alle anderen Zellen im Arbeitsblatt entsperren. Alle Zellen in einem Arbeitsblatt sind bereits für das Sperren initialisiert; Sie können dies überprüfen, indem Sie eine beliebige Excel-Datei in MS Excel öffnen und auf **Format | Zellen...** klicken, um das **Zellen formatieren**-Dialogfeld zu öffnen, dann die Registerkarte **Schutz** anklicken und sehen, dass das Kontrollkästchen "Gesperrt" standardmäßig aktiviert ist.

Die folgenden Punkte beschreiben, wie man einige Zellen mit MS Excel sperrt. Diese Methode gilt für Microsoft Office Excel 97, 2000, 2002, 2003 und spätere Versionen.

1. Wählen Sie das gesamte Arbeitsblatt aus, indem Sie auf die Schaltfläche **Alles auswählen** klicken (das graue Rechteck direkt über der Zeilennummer von Zeile 1 und links von Spaltenbuchstabe A).
2. Klicken Sie im **Format**-Menü auf **Zellen**, klicken Sie auf die Registerkarte **Schutz** und deaktivieren Sie das Kontrollkästchen **Gesperrt**.
   Dies entsperrt alle Zellen im Arbeitsblatt.
   Wenn der Befehl **Zellen** nicht verfügbar ist, können Teile des Arbeitsblatts bereits gesperrt sein. Klicken Sie im **Menü Extras** auf **Schutz**, und klicken Sie dann auf **Arbeitsblatt schützen**.
3. Wählen Sie nur die Zellen aus, die Sie sperren möchten, und wiederholen Sie Schritt 2, aber dieses Mal aktivieren Sie das Kontrollkästchen **Gesperrt**.
4. Beim **Tools**-Menü auf **Schutz** zeigen, klicken Sie auf **Blatt schützen** und dann auf **OK**.
5. Im Dialogfeld **Blatt schützen** haben Sie die Möglichkeit, ein Passwort festzulegen und die Elemente auszuwählen, die Benutzer ändern dürfen.

### **Einige Zellen im Arbeitsblatt mit Aspose.Cells schützen**

In dieser Methode verwenden wir nur die Aspose.Cells API, um die Aufgabe auszuführen.

Beispiel: Das folgende Beispiel zeigt, wie man wenige Zellen im Arbeitsblatt schützt. Es entsperrt zuerst alle Zellen im Arbeitsblatt und sperrt dann 3 Zellen (A1, B1, C1). Schließlich schützt es das Arbeitsblatt. Das Objekt [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) enthält eine boolesche Eigenschaft, [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--). Sie können die Eigenschaft [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) auf true oder false setzen und die Methode *Column/Row.applyStyle()* anwenden, um die Zeile/Spalte mit den gewünschten Attributen zu sperren oder zu entsperren.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new workbook.
const wb = new AsposeCells.Workbook();

// Create a worksheet object and obtain the first sheet.
const sheet = wb.getWorksheets().get(0);

// Define the style object.
let style;

// Define the styleflag object
const styleflag = new AsposeCells.StyleFlag();

// Loop through all the columns in the worksheet and unlock them.
for (let i = 0; i <= 255; i++) {
style = sheet.getCells().getColumns().get((i)).getStyle();
style.setIsLocked(false);
styleflag.setLocked(true);
sheet.getCells().getColumns().get((i)).applyStyle(style, styleflag);
}

// Lock the three cells...i.e. A1, B1, C1.
style = sheet.getCells().get("A1").getStyle();
style.setIsLocked(true);
sheet.getCells().get("A1").setStyle(style);
style = sheet.getCells().get("B1").getStyle();
style.setIsLocked(true);
sheet.getCells().get("B1").setStyle(style);
style = sheet.getCells().get("C1").getStyle();
style.setIsLocked(true);
sheet.getCells().get("C1").setStyle(style);

// Finally, Protect the sheet now.
sheet.protect(AsposeCells.ProtectionType.All);

// Save the excel file.
wb.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **Schützen Sie eine Zeile im Arbeitsblatt**

Aspose.Cells ermöglicht es Ihnen, jede Zeile im Arbeitsblatt bequem zu sperren. Hier können wir die [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/row/#applyStyle-style-styleflag-)-Methode der [**Aspose.Cells.Row**](https://reference.aspose.com/cells/nodejs-cpp/row)-Klasse verwenden, um [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) auf eine bestimmte Zeile im Arbeitsblatt anzuwenden. Diese Methode nimmt zwei Argumente: ein [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-Objekt und ein [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag)-Objekt, das alle Mitglieder im Zusammenhang mit angewendeter Formatierung enthält.

Das folgende Beispiel zeigt, wie man eine Zeile im Arbeitsblatt schützt. Es entsperrt zuerst alle Zellen im Arbeitsblatt und sperrt dann die erste Zeile. Schließlich schützt es das Arbeitsblatt. Das [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-Objekt enthält eine boolesche Eigenschaft, [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--). Sie können die Eigenschaft [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) auf true oder false setzen, um die Zeile/Spalte mit dem [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag)-Objekt zu sperren oder zu entsperren.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new workbook.
const wb = new AsposeCells.Workbook();

// Create a worksheet object and obtain the first sheet.
const sheet = wb.getWorksheets().get(0);

// Define the style object.
let style;

// Define the styleflag object.
const flag = new AsposeCells.StyleFlag();

// Loop through all the columns in the worksheet and unlock them.
for (let i = 0; i <= 255; i++) {
style = sheet.getCells().getColumns().get(i).getStyle();
style.setIsLocked(false);
flag.setLocked(true);
sheet.getCells().getColumns().get(i).applyStyle(style, flag);
}

// Get the first row style.
style = sheet.getCells().getRows().get(0).getStyle();

// Lock it.
style.setIsLocked(true);

// Set the lock setting.
flag.setLocked(true);

// Apply the style to the first row.
sheet.getCells().applyRowStyle(0, style, flag);

// Protect the sheet.
sheet.protect(AsposeCells.ProtectionType.All);

// Save the excel file.
wb.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **Schützen Sie eine Spalte im Arbeitsblatt**

Aspose.Cells ermöglicht es Ihnen, jede Spalte im Arbeitsblatt bequem zu sperren. Hier können wir die [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/nodejs-cpp/column/#applyStyle-style-styleflag-)-Methode der [**Aspose.Cells.Column**](https://reference.aspose.com/cells/nodejs-cpp/column)-Klasse verwenden, um [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) auf eine bestimmte Spalte im Arbeitsblatt anzuwenden. Diese Methode nimmt zwei Argumente: ein [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-Objekt und ein [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag)-Objekt, das alle Mitglieder im Zusammenhang mit angewendeter Formatierung enthält.

Das folgende Beispiel zeigt, wie man eine Spalte im Arbeitsblatt schützt. Es entsperrt zuerst alle Zellen im Arbeitsblatt und sperrt dann die erste Spalte. Schließlich schützt es das Arbeitsblatt. Das [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)-Objekt enthält eine boolesche Eigenschaft, [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--). Sie können die Eigenschaft [**isLocked()**](https://reference.aspose.com/cells/nodejs-cpp/style/#isLocked--) auf true oder false setzen, um die Zeile/Spalte mit dem [**StyleFlag**](https://reference.aspose.com/cells/nodejs-cpp/styleflag)-Objekt zu sperren oder zu entsperren.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a new workbook.
const wb = new AsposeCells.Workbook();

// Create a worksheet object and obtain the first sheet.
const sheet = wb.getWorksheets().get(0);

// Define the style object.
let style;

// Define the styleflag object.
const flag = new AsposeCells.StyleFlag();

// Loop through all the columns in the worksheet and unlock them.
for (let i = 0; i <= 255; i++) {
style = sheet.getCells().getColumns().get(i).getStyle();
style.setIsLocked(false);
flag.setLocked(true);
sheet.getCells().getColumns().get(i).applyStyle(style, flag);
}

// Get the first column style.
style = sheet.getCells().getColumns().get(0).getStyle();

// Lock it.
style.setIsLocked(true);

// Apply the style to the first column.
sheet.getCells().getColumns().get(0).applyStyle(style, flag);

// Protect the sheet.
sheet.protect(AsposeCells.ProtectionType.All);

// Save the excel file.
wb.save(path.join(dataDir, "output.out.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **Benutzern das Bearbeiten von Bereichen ermöglichen**

Das folgende Beispiel zeigt, wie man Benutzern das Bearbeiten eines Bereichs in einem geschützten Arbeitsblatt erlaubt.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const book = new AsposeCells.Workbook();

// Get the first (default) worksheet
const sheet = book.getWorksheets().get(0);

// Get the Allow Edit Ranges
const allowRanges = sheet.getAllowEditRanges();

// Define ProtectedRange
let protected_range;

// Create the range
const idx = allowRanges.add("r2", 1, 1, 3, 3);
protected_range = allowRanges.get(idx);

// Specify the password
protected_range.setPassword("123");

// Protect the sheet
sheet.protect(AsposeCells.ProtectionType.All);

// Save the Excel file
book.save(path.join(dataDir, "protectedrange.out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
