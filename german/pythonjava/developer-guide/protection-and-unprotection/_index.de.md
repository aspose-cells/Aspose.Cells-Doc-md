---
title: Schützen und aufheben des Schutzes
linktitle: Schutz
description: Dieser Abschnitt erläutert, wie Excel-Dateien verschlüsselt und entschlüsselt sowie Excel-Daten geschützt werden, einschließlich Dateiverschlüsselung, Schreibschutz, Schutz der Arbeitsmappenstruktur, Arbeitsblattschutz und digitaler Signaturen mit Python-Code
keywords: Aspose.Cells, Python via Java, verschlüsseln, entschlüsseln, Passwort, schützen, Schutz aufheben, Arbeitsmappenschutz, Arbeitsblattschutz, schreibgeschützt, digitale Signatur, Python
type: docs
weight: 68
url: /de/python-java/protect-and-unprotect/
alias: [/python-java/security-features/]
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel-Arbeitsmappen speichern häufig sensible finanzielle, geschäftliche oder persönliche Informationen, die vor unbefugtem Zugriff geschützt werden müssen. Aspose.Cells for Python via Java bietet einen umfassenden Satz an Schutzfunktionen, die den Möglichkeiten von Microsoft Excel entsprechen und es Ihnen ermöglichen, Ihre Daten auf Dateiebene, Arbeitsmappenebene und Arbeitsblattebene zu sichern.

{{% alert color="primary" %}}
Aspose.Cells for Python via Java bietet eine breite Palette an Schutzfunktionen, von der Dateiebene bis zur Datenebene, ähnlich wie MS Excel. Zu diesen Funktionen gehören das Verschlüsseln von Dateien mit einem Passwort, das Erzwingen eines schreibgeschützten Zugriffs durch ein Passwort zum Ändern, der Schutz der Arbeitsmappenstruktur, der Schutz von Arbeitsblättern sowie das digitale Signieren von Arbeitsmappen.
{{% /alert %}}

## Excel-Dateien verschlüsseln und entschlüsseln
Ein für eine Excel-Datei festgelegtes Passwort verhindert, dass unbefugte Benutzer die Arbeitsmappe öffnen oder deren Inhalt einsehen können. Um eine Arbeitsmappe zu verschlüsseln, weisen Sie `workbook.getSettings().setPassword(...)` eine Passwortzeichenfolge zu und speichern die Arbeitsmappe anschließend. Aspose.Cells schreibt die Datei in verschlüsselter Form. Um eine verschlüsselte Arbeitsmappe zur Entschlüsselung zu öffnen, instanziieren Sie ein `LoadOptions`-Objekt, legen das Passwort über `load_options.setPassword(...)` auf das gleiche Passwort fest, das bei der Verschlüsselung verwendet wurde, und übergeben es an den `Workbook`-Konstruktor. Aspose.Cells wendet das angegebene Passwort transparent an, sodass der restliche Code mit dem entschlüsselten Inhalt interagieren kann, als wäre die Datei eine normale Arbeitsmappe.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cell, LoadOptions
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cell = sheet.getCells().get("A1")
cell.putValue("Confidential Data")
workbook.getSettings().setPassword("OpenPassword123")
workbook.save("encrypted.xlsx")
load_options = LoadOptions()
load_options.setPassword("OpenPassword123")
decrypted_workbook = Workbook("encrypted.xlsx", load_options)
print("Decrypted cell A1 value: " + decrypted_workbook.getWorksheets().get(0).getCells().get("A1").getStringValue())
jpype.shutdownJVM()
```

## Schreibschutz (Passwort zum Ändern)
Excel unterstützt zwei unterschiedliche Passwortebenen. Die erste ist ein Passwort zum Öffnen, das die Datei selbst verschlüsselt und im vorherigen Abschnitt behandelt wurde. Die zweite ist ein Passwort zum Ändern, das Benutzer nicht am Öffnen der Arbeitsmappe hindert; stattdessen empfiehlt Excel, die Datei im schreibgeschützten Modus zu öffnen, sofern nicht das Passwort zum Ändern angegeben wird. Konfigurieren Sie dieses Verhalten in Aspose.Cells über `workbook.getSettings().getWriteProtection()`. Legen Sie das Passwort über `setPassword(...)` als Passwort zum Ändern und den Autor über `setAuthor(...)` fest, um denjenigen zu kennzeichnen, der den Schutz angewendet hat. Verwenden Sie die Methode `writeProtection.validatePassword(String)`, um zu prüfen, ob ein angegebenes Passwort zum Ändern korrekt ist. Sie gibt `true` bei Übereinstimmung und andernfalls `false` zurück.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# Eine neue Arbeitsmappe von Grund auf erstellen
workbook = Workbook()
# Einen Beispielwert in die Zelle A1 des ersten Arbeitsblatts schreiben
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data")
# Den Schreibschutz konfigurieren: Das Passwort zum Ändern und den Autor festlegen
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd")
workbook.getSettings().getWriteProtection().setAuthor("AuthorName")
# Die Arbeitsmappe speichern, damit der Schreibschutz übernommen wird
workbook.save("WriteProtectedWorkbook.xlsx")
# Das Passwort zum Ändern mit dem korrekten Passwort überprüfen
is_correct_valid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd")
print("ValidatePassword(\"ModifyPwd\") returned: " + str(is_correct_valid))
# Das Passwort zum Ändern mit einem falschen Passwort überprüfen, um den anderen Zweig zu demonstrieren
is_wrong_valid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd")
print("ValidatePassword(\"WrongPwd\") returned: " + str(is_wrong_valid))
jpype.shutdownJVM()
```

## Arbeitsmappenstruktur schützen und Schutz aufheben
Der Schutz der Arbeitsmappenstruktur verhindert, dass andere Benutzer ausgeblendete Arbeitsblätter anzeigen, neue Arbeitsblätter hinzufügen, Arbeitsblätter verschieben, löschen, ausblenden oder umbenennen. Der geschützte Zustand bezieht sich auf die Blattstruktur und nicht auf die Zelleninhalte innerhalb eines Blattes. Um den Strukturschutz anzuwenden, rufen Sie `workbook.protect(ProtectionType.STRUCTURE, "password")` auf. Um den Schutz aufzuheben, rufen Sie `workbook.unprotect("password")` auf und geben das korrekte Passwort an. Der Enum-Wert `ProtectionType.STRUCTURE` wird hier verwendet und ist von anderen Schutztypen wie `ProtectionType.WINDOWS` zu unterscheiden.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, ProtectionType
# Eine neue Arbeitsmappe erstellen
workbook = Workbook()
# Ein zweites Arbeitsblatt hinzufügen
workbook.getWorksheets().add()
# Einen Beispieldatenwert in Zelle A1 des ersten Arbeitsblatts schreiben
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data")
# Die Arbeitsmappenstruktur schützen
workbook.protect(ProtectionType.STRUCTURE, "StructPwd")
# Die Arbeitsmappe als structure_protected.xlsx speichern
file_path = "structure_protected.xlsx"
workbook.save(file_path)
# Die Datei in eine neue Workbook-Instanz neu laden
loaded_workbook = Workbook(file_path)
# Den Strukturschutz entfernen
loaded_workbook.unprotect("StructPwd")
# Bestätigungsmeldung drucken
print("Structure protection has been successfully removed from the workbook.")
jpype.shutdownJVM()
```

## Arbeitsblätter schützen und Schutz aufheben
Der Arbeitsblattschutz sperrt die Zellen eines Arbeitsblatts gegen versehentliche oder absichtliche Änderungen. Benutzer können gesperrte Zellen nicht bearbeiten, ohne das Passwort anzugeben. Dies ist der typische Schutz, der verwendet wird, um Formeln, Kopfzeilen oder bestimmte Dateneingabebereiche in gemeinsam genutzten Tabellen zu sichern. Um ein Arbeitsblatt zu schützen, rufen Sie `worksheet.protect(ProtectionType.ALL, "password")` auf. Die Verwendung von `ProtectionType.ALL` aktiviert jede verfügbare Schutzoption, wie z. B. das Auswählen gesperrter Zellen, das Formatieren von Zellen, das Einfügen von Zeilen und Spalten sowie das Löschen von Zeilen und Spalten. Um den Schutz aufzuheben, rufen Sie `worksheet.unprotect("password")` mit dem korrekten Passwort auf. Eine feiner abgestimmte Steuerung ist möglich, indem andere Schutztypen wie `ProtectionType.CONTENTS`, `ProtectionType.OBJECTS` und `ProtectionType.SCENARIOS` mit bitweisem ODER kombiniert werden.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, ProtectionType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sample Data")
worksheet.protect(ProtectionType.ALL, "SheetPwd", None)
workbook.save("sheet_protected.xlsx")
workbook_reloaded = Workbook("sheet_protected.xlsx")
sheet_reloaded = workbook_reloaded.getWorksheets().get(0)
sheet_reloaded.unprotect("SheetPwd")
print("Worksheet protection removed successfully.")
jpype.shutdownJVM()
```

## Digitale Signaturen hinzufügen und validieren
Eine digitale Signatur stellt für die Empfänger sicher, dass der Inhalt der Arbeitsmappe authentisch ist und seit der Signierung nicht verändert wurde. Aspose.Cells bietet Unterstützung für digitale Signaturen über den Namespace `Aspose.Cells.DigitalSignatures`. Der typische Workflow lädt eine `.pfx`-Zertifikatsdatei über `java.security.KeyStore`, kapselt sie in eine `Aspose.Cells.DigitalSignatures.DigitalSignature`, fügt die Signatur zu einer `DigitalSignatureCollection` hinzu und wendet die Sammlung über `workbook.addDigitalSignature(digitalSignatureCollection)` auf die Arbeitsmappe an. Die Eigenschaft `digitalSignature.getComments()` kann Signaturkontext wie Signierzeitpunkt und -zweck erfassen. Jede nach der Signierung an der Arbeitsmappe vorgenommene Änderung macht die Signatur ungültig, sodass ein Validierungsschritt auf Empfängerseite Manipulationen erkennen kann.

```python
import jpype
import jpype.imports
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, DigitalSignature, DigitalSignatureCollection
from java.security import KeyStore
from java.io import FileInputStream
from java.util import Date
# Zertifikat aus PFX-Datei mit Java KeyStore laden
key_store = KeyStore.getInstance("PKCS12")
fis = FileInputStream("signature.pfx")
key_store.load(fis, "pfx-password")
fis.close()
# Zertifikat abrufen
alias = key_store.aliases().nextElement()
certificate = key_store.getCertificate(alias)
# Digitale Signatur erstellen
signature = DigitalSignature(certificate, "Signed by Aspose.Cells", Date())
signatures = DigitalSignatureCollection()
signatures.add(signature)
# Arbeitsmappe erstellen und Signatur hinzufügen
workbook = Workbook()
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value")
workbook.addDigitalSignature(signatures)
workbook.save("signed_workbook.xlsx")
print("The workbook has been digitally signed.")
jpype.shutdownJVM()
```

## Verwandte Artikel
- [Excel-Dateien verschlüsseln und entschlüsseln](/cells/de/python-java/encrypt-and-decrypt-excel-files/)
- [Arbeitsmappenstruktur schützen und Schutz aufheben](/cells/de/python-java/protect-and-unprotect-workbook-structure/)
- [Arbeitsblatt schützen und Schutz aufheben](/cells/de/python-java/protect-and-unprotect-worksheet/)
- [Passwort zum Ändern mit Aspose.Cells überprüfen](/cells/de/python-java/check-password-to-modify-using-aspose-cells/)

{{< app/cells/assistant language="python" >}}