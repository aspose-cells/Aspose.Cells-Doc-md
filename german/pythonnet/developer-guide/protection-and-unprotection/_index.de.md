---
title: Schützen und aufheben des Schutzes
linktitle: Verschlüsselung und Schutz
description: Dieser Abschnitt beschreibt, wie Excel-Dateien mit Python-Code verschlüsselt und entschlüsselt sowie Excel-Daten geschützt werden, einschließlich Dateiverschlüsselung, Schreibschutz, Arbeitsmappenstrukturschutz, Arbeitsblattschutz und digitaler Signaturen
keywords: Aspose.Cells, Python via .NET, verschlüsseln, entschlüsseln, Passwort, schützen, Schutz aufheben, Arbeitsmappenschutz, Arbeitsblattschutz, schreibgeschützt, digitale Signatur, Python
type: docs
weight: 68
url: /de/python-net/protect-and-unprotect/
alias: [/python-net/security-features/]
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel-Arbeitsmappen enthalten häufig sensible finanzielle, geschäftliche oder persönliche Informationen, die vor unbefugtem Zugriff geschützt werden müssen. Aspose.Cells for Python via .NET bietet einen umfassenden Satz an Schutzfunktionen, die den Möglichkeiten von Microsoft Excel entsprechen und es Ihnen ermöglichen, Ihre Daten auf Dateiebene, Arbeitsmappenebene und Arbeitsblattebene zu sichern.

{{% alert color="primary" %}}
Aspose.Cells for Python via .NET bietet eine breite Palette an Schutzfunktionen, von der Dateiebene bis zur Datenebene, ähnlich wie MS Excel. Zu diesen Funktionen gehören das Verschlüsseln von Dateien mit einem Passwort, das Erzwingen von Schreibschutz durch ein Passwort zur Änderung, das Schützen der Arbeitsmappenstruktur, das Schützen von Arbeitsblättern und das digitale Signieren von Arbeitsmappen.
{{% /alert %}}

## Excel-Dateien verschlüsseln und entschlüsseln
Ein auf eine Excel-Datei gesetztes Passwort verhindert, dass unbefugte Benutzer den Inhalt der Arbeitsmappe öffnen oder anzeigen können. Um eine Arbeitsmappe zu verschlüsseln, weisen Sie `workbook.settings.password` eine Passwortzeichenfolge zu und speichern Sie die Arbeitsmappe anschließend. Aspose.Cells schreibt die Datei in verschlüsselter Form. Um eine verschlüsselte Arbeitsmappe zur Entschlüsselung zu öffnen, instanziieren Sie ein `LoadOptions`-Objekt, setzen Sie `load_options.password` auf dasselbe Passwort, das bei der Verschlüsselung verwendet wurde, und übergeben Sie es an den `Workbook`-Konstruktor. Aspose.Cells wendet das angegebene Passwort transparent an, sodass der Rest Ihres Codes mit dem entschlüsselten Inhalt interagieren kann, als wäre die Datei eine normale Arbeitsmappe.

```python
import aspose.cells as ac
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cell = sheet.cells.get("A1")
cell.put_value("Confidential Data")
workbook.settings.password = "OpenPassword123"
workbook.save("encrypted.xlsx")
load_options = ac.LoadOptions()
load_options.password = "OpenPassword123"
decrypted_workbook = ac.Workbook("encrypted.xlsx", load_options)
print("Decrypted cell A1 value: " + decrypted_workbook.worksheets[0].cells.get("A1").string_value)
```

## Schreibschutz (Passwort zur Änderung)
Excel unterstützt zwei unterschiedliche Passwortebenen. Die erste ist ein Passwort zum Öffnen, das die Datei selbst verschlüsselt und im vorherigen Abschnitt behandelt wurde. Die zweite ist ein Passwort zur Änderung, das Benutzer nicht daran hindert, die Arbeitsmappe zu öffnen; stattdessen empfiehlt Excel, die Datei im schreibgeschützten Modus zu öffnen, sofern nicht das Passwort zur Änderung angegeben wird. Konfigurieren Sie dieses Verhalten in Aspose.Cells über `workbook.settings.write_protection`. Setzen Sie die Eigenschaft `password` auf das Passwort zur Änderung und die Eigenschaft `author`, um zu kennzeichnen, wer den Schutz angewendet hat. Verwenden Sie die Methode `write_protection.validate_password(string)`, um zu prüfen, ob ein angegebenes Passwort zur Änderung korrekt ist, wobei `true` bei Übereinstimmung und `false` andernfalls zurückgegeben wird.

```python
import aspose.cells as ac
# Erstellen Sie eine neue Arbeitsmappe von Grund auf
workbook = ac.Workbook()
# Schreiben Sie einen Beispieldatenwert in Zelle A1 des ersten Arbeitsblatts
workbook.worksheets[0].cells.get("A1").put_value("Sample Data")
# Konfigurieren Sie den Schreibschutz: Legen Sie das Passwort zum Ändern und den Autor fest
workbook.settings.write_protection.password = "ModifyPwd"
workbook.settings.write_protection.author = "AuthorName"
# Speichern Sie die Arbeitsmappe, damit der Schreibschutz erhalten bleibt
workbook.save("WriteProtectedWorkbook.xlsx")
# Überprüfen Sie das Passwort zum Ändern mit dem richtigen Passwort
is_correct_valid = workbook.settings.write_protection.validate_password("ModifyPwd")
print("ValidatePassword(\"ModifyPwd\") returned: " + str(is_correct_valid))
# Überprüfen Sie das Passwort zum Ändern mit einem falschen Passwort, um den anderen Zweig zu demonstrieren
is_wrong_valid = workbook.settings.write_protection.validate_password("WrongPwd")
print("ValidatePassword(\"WrongPwd\") returned: " + str(is_wrong_valid))
```

## Arbeitsmappenstruktur schützen und Schutz aufheben
Der Schutz der Arbeitsmappenstruktur verhindert, dass andere Benutzer ausgeblendete Arbeitsblätter anzeigen, neue Arbeitsblätter hinzufügen, Arbeitsblätter verschieben, löschen, ausblenden oder umbenennen können. Der geschützte Zustand gilt für die Blattstruktur und nicht für die Zellinhalte innerhalb eines Blattes. Um einen Strukturschutz anzuwenden, rufen Sie `workbook.protect(ProtectionType.STRUCTURE, "password")` auf. Um den Schutz aufzuheben, rufen Sie `workbook.unprotect("password")` auf und geben Sie das korrekte Passwort an. Der Enum-Wert `ProtectionType.STRUCTURE` wird hier verwendet und unterscheidet sich von anderen Schutztypen wie `ProtectionType.WINDOWS`.

```python
import aspose.cells as ac
# Erstellen Sie eine neue Arbeitsmappe
workbook = ac.Workbook()
# Fügen Sie ein zweites Arbeitsblatt hinzu
workbook.worksheets.add()
# Schreiben Sie einen Beispielwert in Zelle A1 des ersten Arbeitsblatts
workbook.worksheets[0].cells.get(0, 0).put_value("Sample Data")
# Schützen Sie die Struktur der Arbeitsmappe
workbook.protect(ac.ProtectionType.STRUCTURE, "StructPwd")
# Speichern Sie die Arbeitsmappe als structure_protected.xlsx
file_path = "structure_protected.xlsx"
workbook.save(file_path)
# Laden Sie die Datei in eine neue Workbook-Instanz
loaded_workbook = ac.Workbook(file_path)
# Entfernen Sie den Strukturschutz
loaded_workbook.unprotect("StructPwd")
# Bestätigungsmeldung ausgeben
print("Structure protection has been successfully removed from the workbook.")
```

## Arbeitsblätter schützen und Schutz aufheben
Der Arbeitsblattschutz sperrt die Zellen eines Arbeitsblatts gegen versehentliche oder absichtliche Änderungen. Benutzer können gesperrte Zellen nicht ohne Angabe des Passworts bearbeiten. Dies ist der typische Schutz, der verwendet wird, um Formeln, Kopfzeilen oder bestimmte Dateneingabebereiche in freigegebenen Tabellenkalkulationen zu schützen. Um ein Arbeitsblatt zu schützen, rufen Sie `worksheet.protect(ProtectionType.ALL, "password")` auf. Die Verwendung von `ProtectionType.ALL` aktiviert alle verfügbaren Schutzoptionen, wie z. B. das Auswählen gesperrter Zellen, das Formatieren von Zellen, das Einfügen und Löschen von Zeilen und Spalten. Um den Schutz aufzuheben, rufen Sie `worksheet.unprotect("password")` mit dem korrekten Passwort auf. Eine feinere Steuerung ist verfügbar, indem andere Schutztypen wie `Contents`, `Objects` und `Scenarios` mit bitweisem ODER kombiniert werden.

```python
import aspose.cells as ac
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
sheet.cells.get("A1").put_value("Sample Data")
sheet.protect(ac.ProtectionType.ALL, "SheetPwd")
workbook.save("sheet_protected.xlsx")
workbook_reloaded = ac.Workbook("sheet_protected.xlsx")
sheet_reloaded = workbook_reloaded.worksheets[0]
sheet_reloaded.unprotect("SheetPwd")
print("Worksheet protection removed successfully.")
```

## Digitale Signaturen hinzufügen und validieren
Eine digitale Signatur versichert den Empfängern, dass der Inhalt der Arbeitsmappe authentisch ist und seit der Signierung nicht verändert wurde. Aspose.Cells bietet Unterstützung für digitale Signaturen über den Namespace `aspose.cells.digital_signatures`. Der typische Workflow lädt eine `.pfx`-Zertifikatsdatei über `System.Security.Cryptography.X509Certificates.X509Certificate2`, packt sie in eine `aspose.cells.digital_signatures.DigitalSignature`, fügt die Signatur zu einer `DigitalSignatureCollection` hinzu und wendet die Sammlung über `workbook.add_digital_signature(DigitalSignatureCollection)` auf die Arbeitsmappe an. Die Eigenschaft `digital_signature.comments` kann Signaturkontext wie Signierzeit und -zweck aufzeichnen. Jede Änderung an der Arbeitsmappe nach der Signierung macht die Signatur ungültig, sodass ein Validierungsschritt auf Empfängerseite Manipulationen erkennen kann.

```python
from datetime import datetime
import aspose.cells as ac
from aspose.cells.digitalsignatures import DigitalSignature, DigitalSignatureCollection
with open("signature.pfx", "rb") as certificate_file:
    certificate = certificate_file.read()
signature = DigitalSignature(certificate, "Signed by Aspose.Cells", datetime.now())
signatures = DigitalSignatureCollection()
signatures.add(signature)
workbook = ac.Workbook()
workbook.worksheets[0].cells.get("A1").put_value("Sample Value")
workbook.add_digital_signature(signatures)
workbook.save("signed_workbook.xlsx")
print("The workbook has been digitally signed.")
```

## Verwandte Artikel
- [Excel-Dateien verschlüsseln und entschlüsseln](/cells/de/python-net/encrypt-and-decrypt-excel-files/)
- [Arbeitsmappenstruktur schützen und Schutz aufheben](/cells/de/python-net/protect-and-unprotect-workbook-structure/)
- [Arbeitsblatt schützen und Schutz aufheben](/cells/de/python-net/protect-and-unprotect-worksheets/)
- [Freigegebene Arbeitsmappe mit Passwort schützen oder Schutz aufheben](/cells/de/python-net/password-protect-or-unprotect-the-shared-workbook/)
- [Digitale Signaturen zuweisen und validieren](/cells/de/python-net/assign-and-validate-digital-signatures/)
- [Passwort zum Ändern mit Aspose.Cells überprüfen](/cells/de/python-net/check-password-to-modify-using-aspose-cells/)
- [Dateiformat verschlüsselter Office Open XML – OOXML-Dateien erkennen](/cells/de/python-net/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Excel-Dateien verschlüsseln](/cells/de/python-net/encrypting-excel-files/)
- [Wie man ein Dateiformat erkennt und prüft, ob die Datei verschlüsselt ist](/cells/de/python-net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="python-net" >}}