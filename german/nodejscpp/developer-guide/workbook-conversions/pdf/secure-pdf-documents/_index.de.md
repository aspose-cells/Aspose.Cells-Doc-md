---
title: Sichere PDF Dokumente mit Node.js via C++
linktitle: Sichere PDF Dokumente
type: docs
weight: 120
url: /de/nodejs-cpp/secure-pdf-documents/
description: Lernen Sie, wie Sie PDF Dokumente mithilfe von Besitzer und Benutzerschlüsseln sichern und Berechtigungen für PDF Dateien mit Aspose.Cells for Node.js via C++ festlegen.
---

{{% alert color="primary" %}}

Manchmal müssen Entwickler mit verschlüsselten PDF-Dateien arbeiten. Zum Beispiel:

- Sichern Sie die Dokumente mit Besitzer- und Benutzerpasswörtern, so dass nicht jeder es öffnen kann.
- Legen Sie nach dem Öffnen des Dokuments Einschränkungen oder Berechtigungen für das Dokument fest. z.B. Beschränkung, ob der Dokumentinhalt gedruckt oder extrahiert werden kann.

In diesem Artikel wird erklärt, wie Sie PDF-Sicherheitsoptionen beim Speichern von Tabellen in PDF übergeben können.

{{% /alert %}}

Aspose.Cells bietet [**PdfSecurityOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsecurityoptions/) für die Arbeit mit Sicherheit. Sie können Besitzer- und Benutzerkennwörter beim Speichern in PDF festlegen. Das Besitzer- oder Benutzerkennwort ist erforderlich, um das verschlüsselte PDF-Dokument zu öffnen.

- Das Benutzerschlüssel kann null oder eine leere Zeichenkette sein; in diesem Fall wird kein Passwort vom Benutzer beim Öffnen des PDF-Dokuments verlangt.
- Das Öffnen des PDF-Dokuments mit dem richtigen Besitzerkennwort gewährt vollen Zugriff (ohne Zugriffsrestriktionen) auf das Dokument.
- Das Öffnen des PDF-Dokuments mit dem korrekten Benutzerpasswort (oder das Öffnen eines Dokuments, das kein Benutzerpasswort hat) ermöglicht eingeschränkten Zugriff entsprechend den festgelegten Berechtigungen.

Der unten stehende Beispielcode beschreibt, wie PDFs mit Aspose.Cells gesichert werden können.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const saveOption = new AsposeCells.PdfSaveOptions();
saveOption.setSecurityOptions(new AsposeCells.PdfSecurityOptions());

saveOption.getSecurityOptions().setUserPassword("user");
saveOption.getSecurityOptions().setOwnerPassword("owner");
saveOption.getSecurityOptions().setExtractContentPermission(false);
saveOption.getSecurityOptions().setPrintPermission(false);

workbook.save(path.join(dataDir, "securepdf_test.out.pdf"), saveOption);
```

{{% alert color="primary" %}}

Wenn die Tabelle Formeln enthält, ist es am besten, [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) kurz vor dem Rendern in PDF aufzurufen. Dadurch werden formelabhängige Werte neu berechnet und die richtigen Werte im PDF dargestellt.

{{% /alert %}}
