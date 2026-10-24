---
title: Excel Dateien verschlüsseln, entschlüsseln, schützen und freigeben
linktitle: Verschlüsselung und Schutz
description: Dieser Abschnitt erläutert, wie Excel-Dateien verschlüsselt und entschlüsselt sowie Excel-Daten geschützt werden, einschließlich Dateiverschlüsselung, Schreibschutz, Schutz der Arbeitsmappenstruktur, Arbeitsblattschutz und digitaler Signaturen mit Java-Code
keywords: Aspose.Cells, Java, verschlüsseln, entschlüsseln, Passwort, schützen, Schutz aufheben, Arbeitsmappenschutz, Arbeitsblattschutz, schreibgeschützt, digitale Signatur
type: docs
weight: 68
url: /de/java/protect-and-unprotect/
alias: [/java/security-features/]
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel-Arbeitsmappen enthalten häufig vertrauliche Finanz-, Geschäfts- oder persönliche Daten, die vor unbefugtem Zugriff geschützt werden müssen. Aspose.Cells for Java bietet einen umfassenden Satz von Schutzfunktionen, die den Möglichkeiten von Microsoft Excel entsprechen und es Ihnen ermöglichen, Ihre Daten auf Datei-, Arbeitsmappen- und Arbeitsblattebene zu sichern.

{{% alert color="primary" %}}
Aspose.Cells for Java bietet eine breite Palette von Schutzfunktionen, von der Dateiebene bis zur Datenebene, ähnlich wie MS Excel. Zu diesen Funktionen gehören das Verschlüsseln von Dateien mit einem Passwort, das Erzwingen des Schreibschutzes durch ein Passwort zum Ändern, das Schützen der Arbeitsmappenstruktur, das Schützen von Arbeitsblättern und das digitale Signieren von Arbeitsmappen.
{{% /alert %}}

## Excel-Dateien verschlüsseln und entschlüsseln
Ein für eine Excel-Datei festgelegtes Passwort verhindert, dass unbefugte Benutzer den Inhalt der Arbeitsmappe öffnen oder einsehen können. Um eine Arbeitsmappe zu verschlüsseln, weisen Sie `Workbook.Settings.Password` (zugegriffen über `workbook.getSettings().setPassword(...)`) eine Passwortzeichenfolge zu und speichern die Arbeitsmappe anschließend. Aspose.Cells schreibt die Datei in verschlüsselter Form. Um eine verschlüsselte Arbeitsmappe zur Entschlüsselung zu öffnen, instanziieren Sie ein `LoadOptions`-Objekt, setzen `LoadOptions.Password` (über `loadOptions.setPassword(...)`) auf dasselbe Passwort, das bei der Verschlüsselung verwendet wurde, und übergeben es an den `Workbook`-Konstruktor. Aspose.Cells wendet das angegebene Passwort transparent an, sodass der restliche Code mit dem entschlüsselten Inhalt arbeiten kann, als wäre die Datei eine gewöhnliche Arbeitsmappe.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cell cell = sheet.getCells().get("A1");
cell.putValue("Confidential Data");
workbook.getSettings().setPassword("OpenPassword123");
workbook.save("encrypted.xlsx");
LoadOptions loadOptions = new LoadOptions();
loadOptions.setPassword("OpenPassword123");
Workbook decryptedWorkbook = new Workbook("encrypted.xlsx", loadOptions);
System.out.println("Decrypted cell A1 value: " + decryptedWorkbook.getWorksheets().get(0).getCells().get("A1").getStringValue());
```

## Schreibschutz (Passwort zum Ändern)
Excel unterstützt zwei unterschiedliche Passwortebenen. Die erste ist ein Passwort zum Öffnen, das die Datei selbst verschlüsselt und im vorherigen Abschnitt behandelt wird. Die zweite ist ein Passwort zum Ändern, das Benutzer nicht daran hindert, die Arbeitsmappe zu öffnen. Stattdessen empfiehlt Excel, die Datei im schreibgeschützten Modus zu öffnen, sofern nicht das Passwort zum Ändern angegeben wird. Konfigurieren Sie dieses Verhalten in Aspose.Cells über `Workbook.Settings.WriteProtection` (zugegriffen über `workbook.getSettings().getWriteProtection()`). Setzen Sie dessen `Password`-Eigenschaft (über `writeProtection.setPassword(...)`) auf das Passwort zum Ändern und dessen `Author`-Eigenschaft (über `writeProtection.setAuthor(...)`), um anzugeben, wer den Schutz angewendet hat. Verwenden Sie die Methode `WriteProtection.validatePassword(String)`, um zu prüfen, ob ein angegebenes Passwort zum Ändern korrekt ist. Die Methode gibt `true` bei Übereinstimmung und andernfalls `false` zurück.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data");
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd");
workbook.getSettings().getWriteProtection().setAuthor("AuthorName");
workbook.save("WriteProtectedWorkbook.xlsx");
boolean isCorrectValid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd");
System.out.println("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
boolean isWrongValid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd");
System.out.println("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## Arbeitsmappenstruktur schützen und Schutz aufheben
Der Schutz der Arbeitsmappenstruktur verhindert, dass andere Benutzer ausgeblendete Arbeitsblätter anzeigen, neue Arbeitsblätter hinzufügen, Arbeitsblätter verschieben, löschen, ausblenden oder umbenennen. Der geschützte Zustand gilt für die Blattstruktur und nicht für die Zellinhalte innerhalb eines Blattes. Um den Strukturschutz anzuwenden, rufen Sie `workbook.protect(ProtectionType.STRUCTURE, "password")` auf. Um den Schutz aufzuheben, rufen Sie `workbook.unprotect("password")` auf und geben das korrekte Passwort an. Der Enum-Wert `ProtectionType.STRUCTURE` wird hier verwendet und ist von anderen Schutztypen wie `ProtectionType.WINDOWS` zu unterscheiden.

```java
import com.aspose.cells.*;
// Erstellen einer neuen Arbeitsmappe
Workbook workbook = new Workbook();
// Ein zweites Arbeitsblatt hinzufügen
workbook.getWorksheets().add();
// Einen Beispielwert in Zelle A1 des ersten Arbeitsblatts schreiben
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data");
// Die Struktur der Arbeitsmappe schützen
workbook.protect(ProtectionType.STRUCTURE, "StructPwd");
// Die Arbeitsmappe als structure_protected.xlsx speichern
String filePath = "structure_protected.xlsx";
workbook.save(filePath);
// Die Datei in eine neue Workbook-Instanz neu laden
Workbook loadedWorkbook = new Workbook(filePath);
// Den Strukturschutz entfernen
loadedWorkbook.unprotect("StructPwd");
// Bestätigungsnachricht drucken
System.out.println("Structure protection has been successfully removed from the workbook.");
```

## Arbeitsblätter schützen und Schutz aufheben
Der Arbeitsblattschutz sperrt die Zellen eines Arbeitsblatts gegen versehentliche oder absichtliche Änderungen. Benutzer können gesperrte Zellen nicht ohne Angabe des Passworts bearbeiten. Dies ist der typische Schutz zur Absicherung von Formeln, Kopfzeilen oder bestimmten Dateneingabebereichen in freigegebenen Tabellenblättern. Um ein Arbeitsblatt zu schützen, rufen Sie `worksheet.protect(ProtectionType.ALL, "password")` auf. Die Verwendung von `ProtectionType.ALL` aktiviert alle verfügbaren Schutzoptionen, wie das Auswählen gesperrter Zellen, das Formatieren von Zellen, das Einfügen und Löschen von Zeilen und Spalten. Um den Schutz aufzuheben, rufen Sie `worksheet.unprotect("password")` mit dem korrekten Passwort auf. Eine feiner abgestimmte Steuerung ist durch die Kombination anderer Schutztypen wie `CONTENTS`, `OBJECTS` und `SCENARIOS` mittels bitweisem ODER möglich.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
sheet.getCells().get("A1").putValue("Sample Data");
sheet.protect(ProtectionType.ALL, "SheetPwd", "SheetPwd");
workbook.save("sheet_protected.xlsx");
Workbook workbookReloaded = new Workbook("sheet_protected.xlsx");
Worksheet sheetReloaded = workbookReloaded.getWorksheets().get(0);
sheetReloaded.unprotect("SheetPwd");
System.out.println("Worksheet protection removed successfully.");
```

## Digitale Signaturen hinzufügen und validieren
Eine digitale Signatur bestätigt den Empfängern, dass der Inhalt der Arbeitsmappe authentisch ist und seit der Signierung nicht verändert wurde. Aspose.Cells unterstützt digitale Signaturen über das Paket `com.aspose.cells.DigitalSignatures`. Der typische Arbeitsablauf lädt eine `.pfx`-Zertifikatsdatei über die Java-Sicherheits-APIs (wie `java.security.KeyStore` und `java.security.cert.X509Certificate`), kapselt sie in eine `com.aspose.cells.DigitalSignatures.DigitalSignature`, fügt die Signatur zu einer `DigitalSignatureCollection` hinzu und wendet die Sammlung über `workbook.addDigitalSignature(DigitalSignatureCollection)` auf die Arbeitsmappe an. Die Eigenschaft `DigitalSignature.getComments()` kann Signaturkontextinformationen wie Signierzeitpunkt und -zweck erfassen. Jede Änderung an der Arbeitsmappe nach der Signierung macht die Signatur ungültig, sodass ein Validierungsschritt auf Empfängerseite Manipulationen erkennen kann.

```java
import com.aspose.cells.*;
import java.io.FileInputStream;
import java.security.KeyStore;
KeyStore pfxKeyStore = KeyStore.getInstance("PKCS12");
pfxKeyStore.load(new FileInputStream("signature.pfx"), "pfx-password".toCharArray());
DigitalSignature signature = new DigitalSignature(pfxKeyStore, "pfx-password", "Signed by Aspose.Cells", new DateTime());
DigitalSignatureCollection signatures = new DigitalSignatureCollection();
signatures.add(signature);
Workbook workbook = new Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value");
workbook.addDigitalSignature(signatures);
workbook.save("signed_workbook.xlsx");
System.out.println("The workbook has been digitally signed.");
```

## Verwandte Artikel
- [Excel-Dateien verschlüsseln und entschlüsseln](/cells/de/java/encrypt-and-decrypt-excel-files/)
- [Arbeitsmappenstruktur schützen und Schutz aufheben](/cells/de/java/protect-and-unprotect-workbook-structure/)
- [Arbeitsblatt schützen und Schutz aufheben](/cells/de/java/protect-and-unprotect-worksheet/)
- [Freigegebene Arbeitsmappe mit Passwort schützen oder Schutz aufheben](/cells/de/java/password-protect-or-unprotect-the-shared-workbook/)
- [Digitale Signaturen zuweisen und validieren](/cells/de/java/assign-and-validate-digital-signatures/)
- [Dateiformat verschlüsselter Office Open XML – OOXML-Dateien erkennen](/cells/de/java/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Wie man ein Dateiformat erkennt und prüft, ob die Datei verschlüsselt ist](/cells/de/java/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="java" >}}