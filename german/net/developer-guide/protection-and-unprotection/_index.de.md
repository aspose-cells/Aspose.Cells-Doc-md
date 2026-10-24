---
title: Schutz einrichten und aufheben
linktitle: Schutz einrichten und aufheben
description: Dieser Abschnitt beschreibt, wie Excel-Dateien mithilfe von C#-Code verschlüsselt und entschlüsselt sowie Excel-Daten geschützt werden. Behandelt werden die Dateiverschlüsselung, der Schreibschutz, der Schutz der Arbeitsmappenstruktur, der Schutz von Arbeitsblättern und digitale Signaturen.
keywords: Aspose.Cells, .NET, verschlüsseln, entschlüsseln, Kennwort, schützen, Schutz aufheben, Arbeitsmappenschutz, Arbeitsblattschutz, schreibgeschützt, digitale Signatur, C#
type: docs
weight: 68
url: /de/net/protect-and-unprotect/
alias: [/net/security-features/]
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel-Arbeitsmappen speichern häufig sensible finanzielle, geschäftliche oder persönliche Informationen, die vor unbefugtem Zugriff geschützt werden müssen. Aspose.Cells for .Net bietet eine umfassende Palette an Schutzfunktionen, die den Funktionen von Microsoft Excel entsprechen, und ermöglicht die Sicherung Ihrer Daten auf Datei-, Arbeitsmappen- und Arbeitsblattebene.

{{% alert color="primary" %}}
Aspose.Cells for .Net bietet eine breite Palette von Schutzfunktionen auf Datei- bis Datenebene, die den Funktionen von MS Excel ähneln. Zu diesen Funktionen gehören die Verschlüsselung von Dateien mit einem Kennwort, die Durchsetzung eines schreibgeschützten Zugriffs mithilfe eines Kennworts zum Ändern, der Schutz der Arbeitsmappenstruktur, der Schutz von Arbeitsblättern und das digitale Signieren von Arbeitsmappen.
{{% /alert %}}

## Excel-Dateien verschlüsseln und entschlüsseln
Ein für eine Excel-Datei festgelegtes Kennwort verhindert, dass unbefugte Benutzer die Arbeitsmappe öffnen oder ihren Inhalt einsehen können. Um eine Arbeitsmappe zu verschlüsseln, weisen Sie `Workbook.Settings.Password` eine Kennwortzeichenfolge zu und speichern Sie die Arbeitsmappe anschließend. Aspose.Cells schreibt die Datei in verschlüsselter Form. Um eine verschlüsselte Arbeitsmappe zur Entschlüsselung zu öffnen, instanziieren Sie ein `LoadOptions`-Objekt, setzen Sie `LoadOptions.Password` auf dasselbe Kennwort, das während der Verschlüsselung verwendet wurde, und übergeben Sie das `LoadOptions`-Objekt an den `Workbook`-Konstruktor. Aspose.Cells wendet das bereitgestellte Kennwort automatisch an, sodass der übrige Code mit dem entschlüsselten Inhalt arbeiten kann, als wäre die Datei eine reguläre Arbeitsmappe.

```csharp
using System;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cell cell = sheet.Cells["A1"];
cell.PutValue("Confidential Data");
workbook.Settings.Password = "OpenPassword123";
workbook.Save("encrypted.xlsx");
LoadOptions loadOptions = new LoadOptions();
loadOptions.Password = "OpenPassword123";
Workbook decryptedWorkbook = new Workbook("encrypted.xlsx", loadOptions);
Console.WriteLine("Decrypted cell A1 value: " + decryptedWorkbook.Worksheets[0].Cells["A1"].StringValue);
```

## Schreibschutz (Kennwort zum Ändern)
Excel unterstützt zwei unterschiedliche Kennwortebenen. Die erste ist ein Kennwort zum Öffnen, das die Datei selbst verschlüsselt und im vorherigen Abschnitt behandelt wurde. Die zweite ist ein Kennwort zum Ändern, das Benutzern das Öffnen der Arbeitsmappe nicht verhindert. Stattdessen empfiehlt Excel, die Datei im schreibgeschützten Modus zu öffnen, wenn das Änderungskennwort nicht angegeben wird. Konfigurieren Sie dieses Verhalten in Aspose.Cells mithilfe von `Workbook.Settings.WriteProtection`. Setzen Sie die Eigenschaft `Password` auf das Änderungskennwort und geben Sie in der Eigenschaft `Author` an, wer den Schutz angewendet hat. Verwenden Sie die Methode `WriteProtection.ValidatePassword(string)`, um zu überprüfen, ob ein angegebenes Änderungskennwort korrekt ist. Die Methode gibt bei einer Übereinstimmung `true` und andernfalls `false` zurück.

```csharp
using System;
using Aspose.Cells;
// Erstelle eine neue Arbeitsmappe von Grund auf
Workbook workbook = new Workbook();
// Schreibe einen Beispielwert in die Zelle A1 des ersten Arbeitsblatts
workbook.Worksheets[0].Cells["A1"].PutValue("Sample Data");
// Konfiguriere den Schreibschutz: Lege das Änderungskennwort und den Autor fest
workbook.Settings.WriteProtection.Password = "ModifyPwd";
workbook.Settings.WriteProtection.Author = "AuthorName";
// Speichere die Arbeitsmappe, damit der Schreibschutz beibehalten wird
workbook.Save("WriteProtectedWorkbook.xlsx");
// Validiere das Änderungskennwort mit dem richtigen Kennwort
bool isCorrectValid = workbook.Settings.WriteProtection.ValidatePassword("ModifyPwd");
Console.WriteLine("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
// Validiere das Änderungskennwort mit einem falschen Kennwort, um den anderen Zweig zu veranschaulichen
bool isWrongValid = workbook.Settings.WriteProtection.ValidatePassword("WrongPwd");
Console.WriteLine("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## Arbeitsmappenstruktur schützen und Schutz aufheben
Der Schutz der Arbeitsmappenstruktur verhindert, dass andere Benutzer ausgeblendete Arbeitsblätter einsehen sowie neue Arbeitsblätter hinzufügen, Arbeitsblätter verschieben, löschen, ausblenden oder umbenennen. Der Schutzstatus bezieht sich auf die Blattstruktur und nicht auf die Zellinhalte in den einzelnen Blättern. Rufen Sie zum Anwenden des Strukturschutzes `workbook.Protect(ProtectionType.Structure, "password")` auf. Rufen Sie zum Aufheben des Schutzes `workbook.Unprotect("password")` auf und geben Sie das korrekte Kennwort an. Der Enum-Wert `ProtectionType.Structure` wird hier verwendet und ist von anderen Schutztypen wie `ProtectionType.Windows` zu unterscheiden.

```csharp
using System;
using Aspose.Cells;
// Erstellen Sie eine neue Arbeitsmappe
Workbook workbook = new Workbook();
// Fügen Sie ein zweites Arbeitsblatt hinzu
workbook.Worksheets.Add();
// Schreiben Sie einen Beispielwert in die Zelle A1 des ersten Arbeitsblatts
workbook.Worksheets[0].Cells[0, 0].PutValue("Sample Data");
// Schützen Sie die Struktur der Arbeitsmappe
workbook.Protect(ProtectionType.Structure, "StructPwd");
// Speichern Sie die Arbeitsmappe als structure_protected.xlsx
string filePath = "structure_protected.xlsx";
workbook.Save(filePath);
// Laden Sie die Datei in eine neue Workbook-Instanz
Workbook loadedWorkbook = new Workbook(filePath);
// Entfernen Sie den Strukturschutz
loadedWorkbook.Unprotect("StructPwd");
// Drucken Sie eine Bestätigungsnachricht
Console.WriteLine("Structure protection has been successfully removed from the workbook.");
```

## Arbeitsblätter schützen und Schutz aufheben
Der Arbeitsblattschutz sperrt die Zellen eines Arbeitsblatts gegen versehentliche oder absichtliche Änderungen. Benutzer können gesperrte Zellen nicht bearbeiten, ohne das Kennwort anzugeben. Dieser Schutz wird üblicherweise eingesetzt, um Formeln, Kopfzeilen oder festgelegte Datenerfassungsbereiche in gemeinsam genutzten Tabellenkalkulationen zu schützen. Rufen Sie zum Schützen eines Arbeitsblatts `worksheet.Protect(ProtectionType.All, "password")` auf. Die Verwendung von `ProtectionType.All` aktiviert alle verfügbaren Schutzoptionen, etwa das Auswählen gesperrter Zellen, das Formatieren von Zellen, das Einfügen von Zeilen und Spalten sowie das Löschen von Zeilen und Spalten. Rufen Sie zum Aufheben des Schutzes `worksheet.Unprotect("password")` mit dem korrekten Kennwort auf. Eine differenziertere Steuerung ist möglich, indem andere Schutztypen wie `Contents`, `Objects` und `Scenarios` mithilfe einer bitweisen ODER-Verknüpfung kombiniert werden.

```csharp
using System;
using Aspose.Cells;
var workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
sheet.Cells["A1"].PutValue("Sample Data");
sheet.Protect(ProtectionType.All, "SheetPwd");
workbook.Save("sheet_protected.xlsx");
var workbookReloaded = new Workbook("sheet_protected.xlsx");
Worksheet sheetReloaded = workbookReloaded.Worksheets[0];
sheetReloaded.Unprotect("SheetPwd");
Console.WriteLine("Worksheet protection removed successfully.");
```

## Digitale Signaturen hinzufügen und validieren
Eine digitale Signatur gewährleistet den Empfängern, dass der Inhalt der Arbeitsmappe authentisch ist und seit der Signierung nicht verändert wurde. Aspose.Cells bietet Unterstützung für digitale Signaturen mithilfe des Namespace `Aspose.Cells.DigitalSignatures`. Der typische Workflow lädt eine `.pfx`-Zertifikatsdatei mithilfe von `System.Security.Cryptography.X509Certificates.X509Certificate2`, kapselt sie in einer `Aspose.Cells.DigitalSignatures.DigitalSignature`, fügt die Signatur zu einer `DigitalSignatureCollection` hinzu und wendet die Sammlung über `Workbook.AddDigitalSignature(DigitalSignatureCollection)` auf die Arbeitsmappe an. Die Eigenschaft `DigitalSignature.Comments` kann den Signaturkontext erfassen, etwa den Zeitpunkt der Signierung und ihren Zweck. Jede nach der Signierung an der Arbeitsmappe vorgenommene Änderung macht die Signatur ungültig, sodass ein Validierungsschritt auf der Empfängerseite Manipulationen erkennen kann.

```csharp
using System;
using System.IO;
using System.Security.Cryptography.X509Certificates;
using Aspose.Cells;
using Aspose.Cells.DigitalSignatures;
X509Certificate2 certificate = new X509Certificate2("signature.pfx", "pfx-password");
DigitalSignature signature = new DigitalSignature(certificate, "Signed by Aspose.Cells", DateTime.Now);
DigitalSignatureCollection signatures = new DigitalSignatureCollection();
signatures.Add(signature);
Workbook workbook = new Workbook();
workbook.Worksheets[0].Cells["A1"].PutValue("Sample Value");
workbook.AddDigitalSignature(signatures);
workbook.Save("signed_workbook.xlsx");
Console.WriteLine("The workbook has been digitally signed.");
```

## Verwandte Artikel
- [Excel-Dateien verschlüsseln und entschlüsseln](/cells/de/net/encrypt-and-decrypt-excel-files/)
- [Arbeitsmappenstruktur schützen und Schutz aufheben](/cells/de/net/protect-and-unprotect-workbook-structure/)
- [Arbeitsblatt schützen und Schutz aufheben](/cells/de/net/protect-and-unprotect-worksheets/)
- [Gemeinsame Arbeitsmappe mit Kennwort schützen oder Schutz aufheben](/cells/de/net/password-protect-or-unprotect-the-shared-workbook/)
- [Digitale Signaturen zuweisen und validieren](/cells/de/net/assign-and-validate-digital-signatures/)
- [Änderungskennwort mit Aspose.Cells überprüfen](/cells/de/net/check-password-to-modify-using-aspose-cells/)
- [Dateiformat verschlüsselter Office Open XML-Dateien (OOXML) ermitteln](/cells/de/net/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Excel-Dateien verschlüsseln](/cells/de/net/encrypting-excel-files/)
- [Dateiformat ermitteln und prüfen, ob die Datei verschlüsselt ist](/cells/de/net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="csharp" >}}