---
title: Schützen und aufheben des Schutzes
linktitle: Verschlüsselung und Schutz
description: Dieser Abschnitt erläutert, wie Excel-Dateien verschlüsselt und entschlüsselt sowie Excel-Daten geschützt werden, einschließlich Dateiverschlüsselung, Schreibschutz, Schutz der Arbeitsmappenstruktur, Arbeitsblattschutz und digitalen Signaturen mit JavaScript-Code
keywords: Aspose.Cells, Node.js via Java, verschlüsseln, entschlüsseln, Passwort, schützen, Schutz aufheben, Arbeitsmappenschutz, Arbeitsblattschutz, schreibgeschützt, digitale Signatur, JavaScript
type: docs
weight: 68
url: /de/nodejs-java/protect-and-unprotect/
alias: [/nodejs-java/security-features/]
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel-Arbeitsmappen enthalten häufig sensible Finanz-, Geschäfts- oder persönliche Daten, die vor unbefugtem Zugriff geschützt werden müssen. Aspose.Cells for Node.js via Java stellt eine vollständige Reihe von Schutzfunktionen bereit, die den Möglichkeiten von Microsoft Excel entsprechen, und ermöglicht es Ihnen, Ihre Daten auf Dateiebene, Arbeitsmappenebene und Arbeitsblattebene zu sichern.

{{% alert color="primary" %}}
Aspose.Cells for Node.js via Java bietet eine breite Palette von Schutzfunktionen, von der Dateiebene bis zur Datenebene, ähnlich wie MS Excel. Diese Funktionen umfassen das Verschlüsseln von Dateien mit einem Passwort, das Erzwingen eines Schreibschutzes durch ein Passwort zum Ändern, das Schützen der Arbeitsmappenstruktur, das Schützen von Arbeitsblättern sowie das digitale Signieren von Arbeitsmappen.
{{% /alert %}}

## Excel-Dateien verschlüsseln und entschlüsseln
Ein für eine Excel-Datei festgelegtes Passwort verhindert, dass unbefugte Benutzer die Arbeitsmappe öffnen oder deren Inhalt anzeigen. Um eine Arbeitsmappe zu verschlüsseln, weisen Sie `workbook.getSettings().setPassword(...)` eine Passwortzeichenfolge zu und speichern Sie die Arbeitsmappe anschließend. Aspose.Cells schreibt die Datei in verschlüsselter Form. Um eine verschlüsselte Arbeitsmappe zur Entschlüsselung zu öffnen, erstellen Sie ein `LoadOptions`-Objekt, setzen Sie `loadOptions.setPassword(...)` auf das gleiche Passwort, das bei der Verschlüsselung verwendet wurde, und übergeben Sie es an den `Workbook`-Konstruktor. Aspose.Cells wendet das angegebene Passwort transparent an, sodass der restliche Code mit dem entschlüsselten Inhalt arbeiten kann, als wäre die Datei eine gewöhnliche Arbeitsmappe.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
let cell = sheet.getCells().get("A1");
cell.putValue("Confidential Data");
workbook.getSettings().setPassword("OpenPassword123");
workbook.save("encrypted.xlsx");
let loadOptions = new AsposeCells.LoadOptions();
loadOptions.setPassword("OpenPassword123");
let decryptedWorkbook = new AsposeCells.Workbook("encrypted.xlsx", loadOptions);
console.log("Decrypted cell A1 value: " + decryptedWorkbook.getWorksheets().get(0).getCells().get("A1").getStringValue());
```

## Schreibschutz (Passwort zum Ändern)
Excel unterstützt zwei unterschiedliche Passwortebenen. Die erste ist ein Passwort zum Öffnen, das die Datei selbst verschlüsselt und im vorherigen Abschnitt behandelt wurde. Die zweite ist ein Passwort zum Ändern, das Benutzer nicht am Öffnen der Arbeitsmappe hindert; stattdessen empfiehlt Excel, die Datei im schreibgeschützten Modus zu öffnen, sofern nicht das Passwort zum Ändern angegeben wird. Konfigurieren Sie dieses Verhalten in Aspose.Cells über `workbook.getSettings().getWriteProtection()`. Setzen Sie dessen `Password`-Eigenschaft auf das Passwort zum Ändern und dessen `Author`-Eigenschaft, um anzugeben, wer den Schutz angewendet hat. Verwenden Sie die Methode `writeProtection.validatePassword(string)`, um zu prüfen, ob ein angegebenes Passwort zum Ändern korrekt ist, wobei `true` bei Übereinstimmung und `false` andernfalls zurückgegeben wird.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
// Schreiben Sie einen Beispielwert in die Zelle A1 des ersten Arbeitsblatts
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data");
// Konfigurieren Sie den Schreibschutz: Setzen Sie das Passwort zum Ändern und den Autor
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd");
workbook.getSettings().getWriteProtection().setAuthor("AuthorName");
// Speichern Sie die Arbeitsmappe, damit der Schreibschutz übernommen wird
workbook.save("WriteProtectedWorkbook.xlsx");
// Überprüfen Sie das Passwort zum Ändern mit dem korrekten Passwort
let isCorrectValid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd");
console.log("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
// Überprüfen Sie das Passwort zum Ändern mit einem falschen Passwort, um den anderen Zweig zu demonstrieren
let isWrongValid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd");
console.log("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## Arbeitsmappenstruktur schützen und Schutz aufheben
Der Schutz der Arbeitsmappenstruktur verhindert, dass andere Benutzer versteckte Arbeitsblätter anzeigen, neue Arbeitsblätter hinzufügen, Arbeitsblätter verschieben, löschen, ausblenden oder umbenennen. Der geschützte Zustand gilt für die Blattstruktur und nicht für die Zellinhalte innerhalb eines Blattes. Um den Strukturschutz anzuwenden, rufen Sie `workbook.protect(ProtectionType.Structure, "password")` auf. Um den Schutz aufzuheben, rufen Sie `workbook.unprotect("password")` auf und übergeben Sie das korrekte Passwort. Der Enum-Wert `ProtectionType.Structure` wird hier verwendet und unterscheidet sich von anderen Schutztypen wie `ProtectionType.Windows`.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
// Fügen Sie ein zweites Arbeitsblatt hinzu
workbook.getWorksheets().add();
// Schreiben Sie einen Beispielwert in die Zelle A1 des ersten Arbeitsblatts
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data");
// Schützen Sie die Arbeitsmappenstruktur
workbook.protect(AsposeCells.ProtectionType.STRUCTURE, "StructPwd");
// Speichern Sie die Arbeitsmappe als structure_protected.xlsx
let filePath = "structure_protected.xlsx";
workbook.save(filePath);
// Laden Sie die Datei in eine neue Workbook-Instanz
let loadedWorkbook = new AsposeCells.Workbook(filePath);
// Entfernen Sie den Strukturschutz
loadedWorkbook.unprotect("StructPwd");
// Bestätigungsnachricht drucken
console.log("Structure protection has been successfully removed from the workbook.");
```

## Arbeitsblätter schützen und Schutz aufheben
Der Arbeitsblattschutz sperrt die Zellen eines Arbeitsblatts gegen versehentliche oder absichtliche Änderungen. Benutzer können gesperrte Zellen nicht ohne Angabe des Passworts bearbeiten. Dies ist der typische Schutz, der Formeln, Kopfzeilen oder festgelegte Dateneingabebereiche in gemeinsam genutzten Tabellen schützt. Um ein Arbeitsblatt zu schützen, rufen Sie `worksheet.protect(ProtectionType.All, "password")` auf. Die Verwendung von `ProtectionType.All` aktiviert alle verfügbaren Schutzoptionen wie das Auswählen gesperrter Zellen, das Formatieren von Zellen, das Einfügen von Zeilen und Spalten sowie das Löschen von Zeilen und Spalten. Um den Schutz aufzuheben, rufen Sie `worksheet.unprotect("password")` mit dem korrekten Passwort auf. Eine feiner abgestimmte Steuerung ist verfügbar, indem andere Schutztypen wie `Contents`, `Objects` und `Scenarios` mittels bitweisem ODER kombiniert werden.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
sheet.getCells().get("A1").putValue("Sample Data");
sheet.protect(AsposeCells.ProtectionType.ALL, "SheetPwd");
workbook.save("sheet_protected.xlsx");
let workbookReloaded = new AsposeCells.Workbook("sheet_protected.xlsx");
let sheetReloaded = workbookReloaded.getWorksheets().get(0);
sheetReloaded.unprotect("SheetPwd");
console.log("Worksheet protection removed successfully.");
```

## Digitale Signaturen hinzufügen und validieren
Eine digitale Signatur stellt für die Empfänger sicher, dass der Inhalt der Arbeitsmappe authentisch ist und seit der Signierung nicht verändert wurde. Aspose.Cells bietet Unterstützung für digitale Signaturen über Klassen wie `AsposeCells.DigitalSignature` und `AsposeCells.DigitalSignatureCollection`. Der typische Ablauf erstellt ein `AsposeCells.DigitalSignature` direkt aus einer PFX-Zertifikatsdatei zusammen mit ihrem Passwort und Signaturkommentaren, fügt die Signatur zu einer `DigitalSignatureCollection` hinzu und wendet die Sammlung über `workbook.addDigitalSignature(DigitalSignatureCollection)` auf die Arbeitsmappe an. Die Eigenschaft `DigitalSignature.Comments` kann Signaturkontextinformationen wie Signaturzeitpunkt und -zweck aufzeichnen. Jede nach der Signierung an der Arbeitsmappe vorgenommene Änderung macht die Signatur ungültig, sodass ein Validierungsschritt auf der Empfängerseite Manipulationen erkennen kann.

```javascript
const AsposeCells = require("aspose.cells");
let signature = new AsposeCells.DigitalSignature("signature.pfx", "pfx-password", "Signed by Aspose.Cells", new Date());
let signatures = new AsposeCells.DigitalSignatureCollection();
signatures.add(signature);
let workbook = new AsposeCells.Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value");
workbook.addDigitalSignature(signatures);
workbook.save("signed_workbook.xlsx");
console.log("The workbook has been digitally signed.");
```

{{< app/cells/assistant language="nodejs-java" >}}