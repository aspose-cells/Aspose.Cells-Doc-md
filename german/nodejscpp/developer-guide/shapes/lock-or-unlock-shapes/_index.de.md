---
title: Formen mit Node.js via C++ sperren oder entsperren
linktitle: Formen sperren oder freigeben
type: docs
weight: 200
url: /de/nodejs-cpp/lock-or-unlock-shapes/
description: Dieser Artikel zeigt Code, mit dem erklärt wird, wie Formen zum Schutz gesperrt oder entsperrt werden können, mithilfe der Aspose.Cells Bibliothek für Node.js via C++.
keywords: Formen in Node.js sperren, um sie zu schützen – wie man Formen mit Node.js via C++ sperrt oder entsperrt
---

## **Mögliche Verwendungsszenarien**

Manchmal müssen Sie alle Formen in bestimmten Tabellenblättern schützen, um zu verhindern, dass sie durch unerwünschte Situationen zerstört werden. In diesem Fall müssen Sie alle Formen im angegebenen Tabellenblatt sperren. 

Das Sperren von Formen in einer Tabelle oder einem Dokument kann aus mehreren Gründen vorteilhaft sein:
1. Vermeidung versehentlicher Änderungen: Das Sperren von Formen stellt sicher, dass sie nicht versehentlich verschoben, in der Größe verändert oder gelöscht werden. Besonders in komplexen Dokumenten, in denen Formen für Anmerkungen, Illustrationen oder als Teil des Designs verwendet werden.
1. Layout und Design beibehalten: Formen spielen oft eine entscheidende Rolle im Layout und der visuellen Gestaltung eines Dokuments. Das Sperren bewahrt das beabsichtigte Erscheinungsbild und sorgt dafür, dass das Dokument professionell und visuell ansprechend bleibt.
1. Datenintegrität: In Tabellen können Formen verwendet werden, um wichtige Datenpunkte hervorzuheben, Kommentare hinzuzufügen oder visuelle Erklärungen zu liefern. Das Sperren dieser Formen stellt sicher, dass die kontextbezogenen Informationen richtig und intakt bleiben.
1. Konsistenz bei gemeinsam genutzten Dokumenten: Bei der Zusammenarbeit an Dokumenten haben verschiedene Benutzer unterschiedliche Fachkenntnisse. Das Sperren von Formen hilft, die Konsistenz im gesamten Dokument zu wahren, indem unbeabsichtigte Änderungen verhindert werden.
1. Sicherheit: In sensiblen Dokumenten kann das Sperren von Formen ein Teil einer umfassenderen Strategie zum Schutz von Informationen sein. Beispielsweise in Finanzberichten oder rechtlichen Dokumenten, wo gesperrte Formen verwendet werden können, um bestimmte Anmerkungen oder Hervorhebungen zu sichern, die kritischen Kontext liefern.

Manchmal müssen Sie bestimmte Formen in bestimmten geschützten Arbeitsblättern ändern können. In diesem Fall müssen diese Formen entsperrt werden. Dieser Artikel erklärt im Detail, wie man bestimmte Formen sperrt und entsperrt.

## **Wie sperrt man Formen in Excel zum Schutz**

So sperren Sie Zellen in Microsoft Excel:

1. Öffnen Sie Ihre Excel-Datei: Öffnen Sie die Excel-Datei, die die Formen enthält, die Sie sperren möchten.

1. Wählen Sie die Form aus: Klicken Sie auf die Form, die Sie sperren möchten. Sie können auch mehrere Formen auswählen, indem Sie die Strg-Taste gedrückt halten und auf jede Form klicken.

1. Öffnen Sie das Formatieren-Formen-Paneel: Klicken Sie mit der rechten Maustaste auf die ausgewählte(n) Form(en) und wählen Sie „Größe und Eigenschaften“. Alternativ können Sie im Ribbon auf die Registerkarte „Format“ gehen und in der Gruppe „Größe“ den Dialogstarter (kleiner Pfeil) anklicken, um das „Form formatieren“-Fenster zu öffnen.
1. Sperren Sie die Form: Im „Form formatieren“-Paneel gehen Sie auf die Registerkarte „Größe & Eigenschaften“ (das Symbol sieht aus wie ein Quadrat mit Pfeilen). Unter dem Abschnitt „Eigenschaften“ setzen Sie das Häkchen bei „Gesperrt“.
<br>
<img src="1.png" width=60% />
1. Arbeitsblatt schützen: Gehen Sie auf die Registerkarte "Überprüfen" im Menüband. Klicken Sie auf "Blatt schützen". Legen Sie ein Passwort fest (optional) und wählen Sie die Berechtigungen, die Sie zulassen möchten (z. B. geschützte Zellen auswählen, Zellen formatieren usw.). Klicken Sie auf "OK."
<br>
<img src="2.png" width=60% />

## **So sperren Sie alle Formen in einem bestimmten Arbeitsblatt**

Um alle Formen in einem bestimmten Arbeitsblatt zu schützen, verwenden Sie die Methode `worksheet.protect(ProtectionType.Objects)`, wie im folgenden Beispielcode gezeigt.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const text = "This is a test";
const worksheet = workbook.getWorksheets().get(0);

let shape = worksheet.getShapes().addTextBox(1, 0, 1, 0, 30, 100);
shape.setText(text);

shape = worksheet.getShapes().addRectangle(5, 0, 1, 0, 30, 100);
shape.setText(text);

shape = worksheet.getShapes().addButton(9, 0, 1, 0, 30, 100);
shape.setText(text);

shape = worksheet.getShapes().addOval(13, 0, 1, 0, 50, 100);
shape.setText(text);

// Protect all shapes in a specified worksheet 
shape.getWorksheet().protect(AsposeCells.ProtectionType.Objects); // Protects the entire worksheet.
// or shape.getWorksheet().protect(AsposeCells.ProtectionType.All); // Protects all shapes in the specified worksheet.
// or worksheet.protect(AsposeCells.ProtectionType.Objects); // Protects the entire worksheet.
// or worksheet.protect(AsposeCells.ProtectionType.All); // Protects all shapes in the specified worksheet.

workbook.save("Locked.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **So entsperren Sie bestimmte Formen in einem geschützten Arbeitsblatt**

Um eine bestimmte Form in einem geschützten Arbeitsblatt zu entsperren, verwenden Sie `shape.isLocked`, wie im folgenden Beispielcode gezeigt.

Hinweis: `shape.isLocked` ist nur relevant, wenn das Arbeitsblatt geschützt ist.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Locked.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get protected worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get the specified shape to be unlocked
const shape = worksheet.getShapes().get("TextBox 1");

// Unlock the specified shape
if (!worksheet.getProtection().getAllowEditingObject() && shape.isLocked()) {
shape.setIsLocked(false);
}

workbook.save("UnLocked.xlsx", AsposeCells.SaveFormat.Xlsx);
```

{{< app/cells/assistant language="nodejs-cpp" >}}
