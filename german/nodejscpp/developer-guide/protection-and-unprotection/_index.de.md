---
title: Schützen und Aufheben des Schutzes mit Node.js über C++
linktitle: Verschlüsselung und Schutz
description: Dieser Abschnitt beschreibt, wie Excel-Dateien ver- und entschlüsselt werden und Excel-Daten geschützt werden, einschließlich Dateiverschlüsselung, Schreibschutz, Schutz der Arbeitsmappenstruktur, Arbeitsblattschutz und digitaler Signaturen mit JavaScript-Code
keywords: Aspose.Cells, Node.js, C++, verschlüsseln, entschlüsseln, Passwort, schützen, Schutz aufheben, Arbeitsmappenschutz, Arbeitsblattschutz, schreibgeschützt, digitale Signatur, JavaScript
type: docs
weight: 68
url: /de/nodejs-cpp/protect-and-unprotect/
alias: [/nodejs-cpp/security-features/]
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel-Arbeitsmappen enthalten häufig vertrauliche finanzielle, geschäftliche oder persönliche Informationen, die vor unbefugtem Zugriff geschützt werden müssen. Aspose.Cells for Node.js via C++ bietet einen umfassenden Satz an Schutzfunktionen, die den Möglichkeiten von Microsoft Excel entsprechen und es Ihnen ermöglichen, Ihre Daten auf Datei-, Arbeitsmappen- und Arbeitsblattebene zu sichern.

{{% alert color="primary" %}}
Aspose.Cells for Node.js via C++ bietet eine breite Palette an Schutzfunktionen, von der Dateiebene bis zur Datenebene, ähnlich wie MS Excel. Diese Funktionen umfassen das Verschlüsseln von Dateien mit einem Passwort, das Erzwingen eines schreibgeschützten Zugriffs durch ein Passwort zur Änderung, den Schutz der Arbeitsmappenstruktur, den Schutz von Arbeitsblättern und das digitale Signieren von Arbeitsmappen.
{{% /alert %}}

## Excel-Dateien ver- und entschlüsseln
Ein für eine Excel-Datei festgelegtes Passwort verhindert, dass unbefugte Benutzer den Inhalt der Arbeitsmappe öffnen oder anzeigen können. Um eine Arbeitsmappe zu verschlüsseln, weisen Sie `workbook.getSettings().setPassword()` eine Passwortzeichenfolge zu und speichern Sie die Arbeitsmappe anschließend. Aspose.Cells schreibt die Datei in verschlüsselter Form. Um eine verschlüsselte Arbeitsmappe zur Entschlüsselung zu öffnen, instanziieren Sie ein `LoadOptions`-Objekt, setzen Sie `loadOptions.setPassword()` auf das gleiche Passwort, das bei der Verschlüsselung verwendet wurde, und übergeben Sie es an den `Workbook`-Konstruktor. Aspose.Cells wendet das angegebene Passwort transparent an, sodass der restliche Code mit dem entschlüsselten Inhalt interagieren kann, als wäre die Datei eine reguläre Arbeitsmappe.

```javascript
const AsposeCells = require("aspose.cells.node");
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

## Schreibschutz (Passwort zur Änderung)
Excel unterstützt zwei unterschiedliche Passwortebenen. Die erste ist ein Passwort zum Öffnen, das die Datei selbst verschlüsselt und im vorherigen Abschnitt behandelt wird. Die zweite ist ein Passwort zur Änderung, das Benutzer nicht am Öffnen der Arbeitsmappe hindert; stattdessen empfiehlt Excel, die Datei im schreibgeschützten Modus zu öffnen, sofern nicht das Änderungspasswort angegeben wird. Konfigurieren Sie dieses Verhalten in Aspose.Cells über `workbook.getSettings().getWriteProtection()`. Setzen Sie dessen Eigenschaft `password` auf das Änderungspasswort und dessen Eigenschaft `author`, um anzugeben, wer den Schutz angewendet hat. Verwenden Sie die Methode `writeProtection.validatePassword(string)`, um zu überprüfen, ob ein angegebenes Änderungspasswort korrekt ist. Die Methode gibt `true` bei Übereinstimmung und `false` andernfalls zurück.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
// Schreiben Sie einen Beispielwert in Zelle A1 des ersten Arbeitsblatts
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data");
// Konfigurieren Sie den Schreibschutz: Legen Sie das Passwort zum Ändern und den Autor fest
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd");
workbook.getSettings().getWriteProtection().setAuthor("AuthorName");
// Speichern Sie die Arbeitsmappe, damit der Schreibschutz beibehalten wird
workbook.save("WriteProtectedWorkbook.xlsx");
// Überprüfen Sie das Passwort zum Ändern mit dem richtigen Passwort
let isCorrectValid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd");
console.log("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
// Überprüfen Sie das Passwort zum Ändern mit einem falschen Passwort, um den anderen Zweig zu demonstrieren
let isWrongValid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd");
console.log("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## Arbeitsmappenstruktur schützen und Schutz aufheben
Der Schutz der Arbeitsmappenstruktur verhindert, dass andere Benutzer ausgeblendete Arbeitsblätter anzeigen, neue Arbeitsblätter hinzufügen, Arbeitsblätter verschieben, löschen, ausblenden oder umbenennen. Der geschützte Zustand gilt für die Blattstruktur, nicht für die Zelleninhalte innerhalb eines Blattes. Um den Strukturschutz anzuwenden, rufen Sie `workbook.protect(ProtectionType.Structure, "password")` auf. Um den Schutz aufzuheben, rufen Sie `workbook.unprotect("password")` auf und geben Sie das korrekte Passwort an. Der Enum-Wert `ProtectionType.Structure` wird hier verwendet und unterscheidet sich von anderen Schutztypen wie `ProtectionType.Windows`.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
// Fügen Sie ein zweites Arbeitsblatt hinzu
workbook.getWorksheets().add();
// Schreiben Sie einen Beispielwert in die Zelle A1 des ersten Arbeitsblatts
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data");
// Schützen Sie die Arbeitsmappenstruktur
workbook.protect(AsposeCells.ProtectionType.Structure, "StructPwd");
// Speichern Sie die Arbeitsmappe als structure_protected.xlsx
let filePath = "structure_protected.xlsx";
workbook.save(filePath);
// Laden Sie die Datei in eine neue Workbook-Instanz
let loadedWorkbook = new AsposeCells.Workbook(filePath);
// Entfernen Sie den Strukturschutz
loadedWorkbook.unprotect("StructPwd");
// Bestätigungsmeldung ausgeben
console.log("Structure protection has been successfully removed from the workbook.");
```

## Arbeitsblätter schützen und Schutz aufheben
Der Arbeitsblattschutz sperrt die Zellen eines Arbeitsblatts gegen versehentliche oder absichtliche Änderungen. Benutzer können gesperrte Zellen nicht bearbeiten, ohne das Passwort anzugeben. Dies ist der typische Schutz, der verwendet wird, um Formeln, Kopfzeilen oder bestimmte Dateneingabebereiche in freigegebenen Tabellen zu schützen. Um ein Arbeitsblatt zu schützen, rufen Sie `worksheet.protect(ProtectionType.All, "password")` auf. Die Verwendung von `ProtectionType.All` aktiviert jede verfügbare Schutzoption, wie z. B. das Auswählen gesperrter Zellen, das Formatieren von Zellen, das Einfügen von Zeilen und Spalten sowie das Löschen von Zeilen und Spalten. Um den Schutz aufzuheben, rufen Sie `worksheet.unprotect("password")` mit dem korrekten Passwort auf. Eine feinere Steuerung ist verfügbar, indem andere Schutztypen wie `Contents`, `Objects` und `Scenarios` mit bitweisem ODER kombiniert werden.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
sheet.getCells().get("A1").putValue("Sample Data");
sheet.protect(AsposeCells.ProtectionType.All, "SheetPwd");
workbook.save("sheet_protected.xlsx");
let workbookReloaded = new AsposeCells.Workbook("sheet_protected.xlsx");
let sheetReloaded = workbookReloaded.getWorksheets().get(0);
sheetReloaded.unprotect("SheetPwd");
console.log("Worksheet protection removed successfully.");
```

## Digitale Signaturen hinzufügen und validieren
Eine digitale Signatur gewährleistet den Empfängern, dass der Inhalt der Arbeitsmappe authentisch ist und seit der Signierung nicht verändert wurde. Aspose.Cells bietet Unterstützung für digitale Signaturen über den Namespace `Aspose.Cells.DigitalSignatures`. Der typische Workflow lädt eine `.pfx`-Zertifikatsdatei mithilfe der Kryptografie-Dienstprogramme von Node.js, packt sie in eine `Aspose.Cells.DigitalSignatures.DigitalSignature`, fügt die Signatur zu einer `DigitalSignatureCollection` hinzu und wendet die Sammlung über `workbook.addDigitalSignature(digitalSignatureCollection)` auf die Arbeitsmappe an. Die Eigenschaft `digitalSignature.comments` kann den Signierungskontext wie Signierungszeitpunkt und -zweck aufzeichnen. Jede Änderung an der Arbeitsmappe nach der Signierung macht die Signatur ungültig, sodass ein Validierungsschritt auf der Empfängerseite Manipulationen erkennen kann.

```javascript
const AsposeCells = require("aspose.cells.node");
let signature = new AsposeCells.DigitalSignature("signature.pfx", "pfx-password", "Signed by Aspose.Cells", new Date());
let signatures = new AsposeCells.DigitalSignatureCollection();
signatures.add(signature);
let workbook = new AsposeCells.Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value");
workbook.addDigitalSignature(signatures);
workbook.save("signed_workbook.xlsx");
console.log("The workbook has been digitally signed.");
```

## Verwandte Artikel
- [Excel-Dateien ver- und entschlüsseln](/cells/de/nodejs-cpp/encrypt-and-decrypt-excel-files/)
- [Arbeitsmappenstruktur schützen und Schutz aufheben](/cells/de/nodejs-cpp/protect-and-unprotect-workbook-structure/)
- [Arbeitsblatt schützen und Schutz aufheben](/cells/de/nodejs-cpp/protect-and-unprotect-worksheets/)
- [Freigegebene Arbeitsmappe mit Passwort schützen oder Schutz aufheben](/cells/de/nodejs-cpp/password-protect-or-unprotect-the-shared-workbook/)
- [Digitale Signaturen zuweisen und validieren](/cells/de/nodejs-cpp/assign-and-validate-digital-signatures/)
- [Passwort zur Änderung mit Aspose.Cells überprüfen](/cells/de/nodejs-cpp/check-password-to-modify-using-aspose-cells/)
- [Dateiformat verschlüsselter Office Open XML - OOXML-Dateien erkennen](/cells/de/nodejs-cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Excel-Dateien verschlüsseln](/cells/de/nodejs-cpp/encrypting-excel-files/)
- [Wie man ein Dateiformat erkennt und überprüft, ob die Datei verschlüsselt ist](/cells/de/nodejs-cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="nodejs-cpp" >}}