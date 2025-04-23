---
title: Wie man den Druckbereich mit Node.js über C++ festlegt
linktitle: So legen Sie den Druckbereich fest
type: docs
weight: 200
url: /de/nodejs-cpp/how-to-set-print-area/
description: Dieser Artikel zeigt Ihnen Code, der erklärt, wie man den Druckbereich mit der Aspose.Cells Bibliothek für Node.js über C++ festlegt.
keywords: Druckbereich begrenzen, Druckbereich festlegen, Druckbereich löschen, Druckbereich setzen und löschen mit Node.js über C++, Druckbereich festlegen und löschen mit Node.js über C++, Wie man den Druckbereich in Node.js löscht, Druckbereich mit Node.js hinzufügen, Druckbereich mit Node.js entfernen, Druckbereich in Excel festlegen, Druckbereich in Excel löschen.
---

## **Mögliche Verwendungsszenarien**

Das Festlegen eines Druckbereichs in einem Dokument, wie z.B. einer Excel-Tabelle, hilft dabei, zu steuern, welche Inhalte beim Drucken enthalten sind. Hier sind einige Gründe, einen Druckbereich festzulegen:

1. Fokus auf bestimmte Daten: Sie können nur die relevantesten Abschnitte drucken und unnötigen Inhalt vermeiden.
1. Verbesserte Gestaltung: Es hilft, den Inhalt ordentlich auf den gedruckten Seiten anzuordnen und anzupassen, um Brüche oder unerwünschte Seitenumbrüche zu vermeiden.
1. Ressourcen sparen: Durch Begrenzung des Druckbereichs können Sie Papier- und Tintenverbrauch reduzieren.
1. Professionelle Darstellung: Es stellt sicher, dass nur die fertig ausgearbeitete Version der Daten gedruckt wird, was besonders bei Berichten oder Präsentationen wichtig ist.
1. Konsistenz: Beim mehrfachen Drucken desselben Dokuments sorgt ein festgelegter Druckbereich für einheitliches Ergebnis.

<br>
Das Festlegen eines Druckbereichs ist besonders in größeren Dokumenten nützlich, bei denen nur ein Teil in gedruckter Form geteilt oder überprüft werden soll.

## **So legen Sie den Druckbereich in Excel fest**

Um einen Druckbereich in Excel festzulegen, befolgen Sie diese Schritte:

1. Zellen auswählen: Klicken und ziehen Sie, um den Zellbereich auszuwählen, den Sie als Druckbereich festlegen möchten.
1. Gehen Sie auf die Registerkarte Seitenlayout: Wechseln Sie in die Registerkarte "Seitenlayout" im Menüband oben im Excel-Fenster.
1. Druckbereich festlegen: Klicken Sie im Bereich "Seite einrichten" auf "Druckbereich". Wählen Sie aus dem Dropdown-Menü "Druckbereich festlegen".
<br>
<img src="3.png" width=60% />

1. Zum Druckbereich hinzufügen: Wenn Sie zusätzliche Zellen zum bestehenden Druckbereich hinzufügen möchten, wählen Sie die zusätzlichen Zellen aus, gehen Sie im Menü "Seitenlayout" auf "Druckbereich" und wählen Sie "Druckbereich hinzufügen".

<br>
Diese Aktion legt die ausgewählten Zellen als Druckbereich fest. Wenn Sie das Arbeitsblatt drucken, wird nur dieser definierte Bereich gedruckt.

## **So entfernen Sie den Druckbereich in Excel**

Um den Druckbereich in Excel zu entfernen, folgen Sie diesen Schritten:

1. Öffnen Sie die Registerkarte Seitenlayout: Klicken Sie auf die Registerkarte "Seitenlayout" im Menüband oben im Excel-Fenster.
1. Druckbereich entfernen: Klicken Sie im Gruppenfeld "Seite einrichten" auf "Druckbereich". Wählen Sie im Dropdown-Menü "Druckbereich löschen".
<br>
<img src="4.png" width=60% />

<br>
Diese Aktion entfernt jeden zuvor festgelegten Druckbereich, sodass das gesamte Arbeitsblatt gedruckt werden kann.

## **Was passiert nach dem Entfernen des Druckbereichs**

Das Entfernen des Druckbereichs in einer Tabellenkalkulationsanwendung wie Excel mit Aspose.Cells führt dazu, dass beim Drucken das gesamte Arbeitsblatt eingeschlossen wird. Wenn ein Druckbereich festgelegt ist, wird nur der angegebene Zellbereich gedruckt. Durch das Entfernen des Druckbereichs wird sichergestellt, dass kein spezifischer Bereich mehr definiert ist und das Standarddruckverhalten, das das gesamte Blatt umfasst, wirksam wird.

1. Standard-Druckverhalten: Das gesamte Arbeitsblatt wird für den Druck berücksichtigt. Das bedeutet, alle Zellen mit Daten oder Formatierungen werden gedruckt.
1. Keine Druckbereichsbegrenzung: Vorher festgelegte Druckbereichsgrenzen werden entfernt. Wenn bestimmte Zeilen und Spalten für den Druck festgelegt waren, gelten diese Begrenzungen nicht mehr.
1. Vollständiger Inhalt: Alle Inhalte, einschließlich Kopf- und Fußzeilen sowie anderer Daten im Arbeitsblatt, werden im Druckauftrag eingeschlossen.

## **Wie man den Druckbereich mit Aspose.Cells for Node.js via C++ festlegt**

Um den Druckbereich in einem bestimmten Arbeitsblatt festzulegen: Laden Sie zunächst die [Beispieldatei](input.xlsx), und dann müssen Sie die [**PageSetup.getPrintArea()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintArea--)-Eigenschaft des [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/)-Objekts für das gewünschte Arbeitsblatt modifizieren. Das Festlegen dieser Eigenschaft auf eine Bereichszeichenfolge setzt den Druckbereich.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

// Load the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access the desired worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set the print area - specify the range you want to print
worksheet.getPageSetup().setPrintArea("A1:D10");

// Save the workbook
workbook.save("set_print_area.pdf");
```

Das Ausgabenergebnis:
<br>
<img src="1.png" width=60% />

## **Wie man den Druckbereich mit Aspose.Cells for Node.js via C++ löscht**

Um den Druckbereich in einem bestimmten Arbeitsblatt zu löschen: Laden Sie zuerst die [Beispieldatei](input.xlsx), und ändern Sie dann die Eigenschaft [**PageSetup.getPrintArea()**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/#getPrintArea--) des Objekts [**PageSetup**](https://reference.aspose.com/cells/nodejs-cpp/pagesetup/) für das gewünschte Arbeitsblatt. Das Setzen dieser Eigenschaft auf einen leeren String löscht den Druckbereich.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");

// Load the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access the desired worksheet
const worksheet = workbook.getWorksheets().get(0);

// Clear the print area
worksheet.getPageSetup().setPrintArea("");

// Save the workbook
workbook.save("clear_print_area.pdf");
```

Das Ausgabenergebnis:
<br>
<img src="2.png" width=60% />
