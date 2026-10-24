---
title: Mit C++ schützen und ungünstig machen
linktitle: Verschlüsselung und Schutz
description: Dieser Abschnitt bietet eine Einführung in die Verschlüsselung und Entschlüsselung von Excel-Dateien sowie den Schutz von Excel-Daten mithilfe von C++-Code und behandelt die Dateiverschlüsselung, den Schreibschutz, den Schutz der Arbeitsmappenstruktur, den Schutz des Arbeitsblatts und digitale Signaturen
keywords: Aspose.Cells, Aspose.Cells for C++, verschlüsseln, entschlüsseln, Passwort, schützen, Schutz aufheben, Arbeitsmappenschutz, Arbeitsblattschutz, schreibgeschützt, digitale Signatur, C++
type: docs
weight: 68
url: /de/cpp/protect-and-unprotect/
alias: [/cpp/security-features/]
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel-Arbeitsmappen speichern häufig sensible Finanz-, Geschäfts- oder Personendaten, die vor unbefugtem Zugriff geschützt werden müssen. Aspose.Cells for C++ bietet eine umfassende Sammlung von Schutzfunktionen, die den Funktionsumfang von Microsoft Excel abbilden, sodass Sie Ihre Daten auf Datei-, Arbeitsmappen- und Arbeitsblattebene sichern können.

{{% alert color="primary" %}}
Aspose.Cells for C++ bietet eine breite Palette von Schutzfunktionen auf Datei- bis Datenebene, die den Funktionen von MS Excel ähneln. Dazu gehören das Verschlüsseln von Dateien mit einem Passwort, die Durchsetzung eines schreibgeschützten Zugriffs durch ein Passwort zum Ändern, der Schutz der Arbeitsmappenstruktur, der Schutz von Arbeitsblättern und das digitale Signieren von Arbeitsmappen.
{{% /alert %}}

## Excel-Dateien verschlüsseln und entschlüsseln
Ein Passwort für eine Excel-Datei verhindert, dass unbefugte Benutzer die Arbeitsmappe öffnen oder ihren Inhalt einsehen. Weisen Sie zum Verschlüsseln einer Arbeitsmappe `workbook.GetSettings().SetPassword()` eine Passwortzeichenfolge zu und speichern Sie die Arbeitsmappe anschließend. Aspose.Cells schreibt die Datei in verschlüsselter Form. Um eine verschlüsselte Arbeitsmappe zur Entschlüsselung zu öffnen, instanziieren Sie ein `LoadOptions`-Objekt, setzen Sie `LoadOptions.SetPassword()` auf dasselbe Passwort, das bei der Verschlüsselung verwendet wurde, und übergeben Sie das Objekt an den `Workbook`-Konstruktor. Aspose.Cells wendet das angegebene Passwort transparent an, sodass der restliche Code mit dem entschlüsselten Inhalt arbeiten kann, als wäre die Datei eine reguläre Arbeitsmappe.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cell cell = sheet.GetCells().Get(u"A1");
    cell.PutValue(u"Confidential Data");
    workbook.GetSettings().SetPassword(U16String("OpenPassword123"));
    workbook.Save(u"encrypted.xlsx");
    LoadOptions loadOptions;
    loadOptions.SetPassword(U16String("OpenPassword123"));
    Workbook decryptedWorkbook(u"encrypted.xlsx", loadOptions);
    U16String cellValue = decryptedWorkbook.GetWorksheets().Get(0).GetCells().Get(u"A1").GetStringValue();
    std::cout << "Decrypted cell A1 value: " << cellValue.ToUtf8() << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Schreibschutz (Passwort zum Ändern)
Excel unterstützt zwei unterschiedliche Passwortebenen. Das erste ist ein Passwort zum Öffnen, das die Datei selbst verschlüsselt und im vorherigen Abschnitt behandelt wurde. Das zweite ist ein Passwort zum Ändern, das Benutzer nicht daran hindert, die Arbeitsmappe zu öffnen. Stattdessen empfiehlt Excel, die Datei im schreibgeschützten Modus zu öffnen, sofern das Passwort zum Ändern nicht angegeben wird. Konfigurieren Sie dieses Verhalten in Aspose.Cells über `workbook.GetSettings().GetWriteProtection()`. Setzen Sie dessen Eigenschaft `Password` auf das Passwort zum Ändern und dessen Eigenschaft `Author`, um die Person zu kennzeichnen, die den Schutz angewendet hat. Mit der Methode `WriteProtection.ValidatePassword()` können Sie überprüfen, ob ein angegebenes Passwort zum Ändern korrekt ist. Sie gibt bei einer Übereinstimmung `true` und andernfalls `false` zurück.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    Cell a1 = cells.Get(u"A1");
    a1.PutValue(u"Sample Data");
    workbook.GetSettings().GetWriteProtection().SetPassword(u"ModifyPwd");
    workbook.GetSettings().GetWriteProtection().SetAuthor(u"AuthorName");
    workbook.Save(u"WriteProtectedWorkbook.xlsx");
    bool isCorrectValid = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"ModifyPwd");
    std::cout << "ValidatePassword(\"ModifyPwd\") returned: " << (isCorrectValid ? "True" : "False") << std::endl;
    bool isWrongValid = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"WrongPwd");
    std::cout << "ValidatePassword(\"WrongPwd\") returned: " << (isWrongValid ? "True" : "False") << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Schutz der Arbeitsmappenstruktur anwenden und aufheben
Der Schutz der Arbeitsmappenstruktur verhindert, dass andere Benutzer ausgeblendete Arbeitsblätter einsehen, neue Arbeitsblätter hinzufügen oder Arbeitsblätter verschieben, löschen, ausblenden oder umbenennen. Der Schutzstatus bezieht sich auf die Blattstruktur und nicht auf den Zellinhalt in den einzelnen Blättern. Rufen Sie zum Anwenden des Strukturschutzes `workbook.Protect(ProtectionType::Structure, "password")` auf. Rufen Sie zum Aufheben des Schutzes `workbook.Unprotect("password")` mit dem richtigen Passwort auf. Der Aufzählungswert `ProtectionType::Structure` wird hier verwendet und ist von anderen Schutztypen wie `ProtectionType::Windows` zu unterscheiden.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Erstellen Sie eine neue Arbeitsmappe
    Workbook workbook;
    // Fügen Sie ein zweites Arbeitsblatt hinzu
    workbook.GetWorksheets().Add();
    // Schreiben Sie einen Beispielwert in die Zelle A1 des ersten Arbeitsblatts
    workbook.GetWorksheets().Get(0).GetCells().Get(0, 0).PutValue(u"Sample Data");
    // Schützen Sie die Struktur der Arbeitsmappe
    workbook.Protect(ProtectionType::Structure, u"StructPwd");
    // Speichern Sie die Arbeitsmappe als structure_protected.xlsx
    U16String filePath = u"structure_protected.xlsx";
    workbook.Save(filePath);
    // Laden Sie die Datei in eine neue Workbook-Instanz
    Workbook loadedWorkbook(filePath);
    // Entfernen Sie den Strukturschutz
    loadedWorkbook.Unprotect(u"StructPwd");
    // Bestätigungsnachricht ausgeben
    std::cout << "Structure protection has been successfully removed from the workbook." << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Arbeitsblätter schützen und Schutz aufheben
Der Arbeitsblattschutz sperrt die Zellen eines Arbeitsblatts gegen versehentliche oder absichtliche Änderungen. Benutzer können gesperrte Zellen nicht bearbeiten, ohne das Passwort anzugeben. Dies ist der übliche Schutz, mit dem Formeln, Überschriften oder festgelegte Bereiche für die Dateneingabe in freigegebenen Arbeitsmappen gesichert werden. Rufen Sie zum Schützen eines Arbeitsblatts `worksheet.Protect(ProtectionType::All, "password")` auf. `ProtectionType::All` aktiviert alle verfügbaren Schutzoptionen, etwa das Auswählen gesperrter Zellen, das Formatieren von Zellen, das Einfügen von Zeilen und Spalten sowie das Löschen von Zeilen und Spalten. Rufen Sie zum Aufheben des Schutzes `worksheet.Unprotect("password")` mit dem richtigen Passwort auf. Eine feinere Steuerung ist möglich, indem Sie andere Schutztypen wie `Contents`, `Objects` und `Scenarios` mithilfe einer bitweisen ODER-Verknüpfung kombinieren.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Sample Data");
    sheet.Protect(ProtectionType::All, u"SheetPwd");
    workbook.Save(u"sheet_protected.xlsx");
    Workbook workbookReloaded(u"sheet_protected.xlsx");
    Worksheet sheetReloaded = workbookReloaded.GetWorksheets().Get(0);
    sheetReloaded.Unprotect(u"SheetPwd");
    std::cout << "Worksheet protection removed successfully.\n";
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Digitale Signaturen hinzufügen und validieren
Eine digitale Signatur gewährleistet gegenüber den Empfängern, dass der Inhalt der Arbeitsmappe authentisch ist und seit der Signierung nicht verändert wurde. Aspose.Cells unterstützt digitale Signaturen über den Namespace `Aspose::Cells::DigitalSignatures`. Der typische Workflow lädt eine `.pfx`-Zertifikatsdatei, kapselt sie in einer `Aspose::Cells::DigitalSignatures::DigitalSignature`, fügt die Signatur zu einer `DigitalSignatureCollection` hinzu und wendet die Sammlung mithilfe von `workbook.AddDigitalSignature(DigitalSignatureCollection)` auf die Arbeitsmappe an. Mit der Eigenschaft `DigitalSignature.GetComments()` kann der Kontext der Signierung erfasst werden, einschließlich Zeitpunkt und Zweck. Jede nach der Signierung an der Arbeitsmappe vorgenommene Änderung macht die Signatur ungültig, sodass ein Validierungsschritt auf der Empfängerseite Manipulationen erkennen kann.

```cpp
#include "Aspose.Cells.h"
#include <chrono>
#include <ctime>
using namespace Aspose::Cells;
using namespace Aspose::Cells::DigitalSignatures;
int main() {
    Aspose::Cells::Startup();
    std::time_t t = std::time(nullptr);
    std::tm tm{};
    localtime_s(&tm, &t);
    Date currentDate{0};
    currentDate.year = tm.tm_year + 1900;
    currentDate.month = tm.tm_mon + 1;
    currentDate.day = tm.tm_mday;
    currentDate.hour = tm.tm_hour;
    currentDate.minute = tm.tm_min;
    currentDate.second = tm.tm_sec;
    DigitalSignature signature(u"signature.pfx", u"pfx-password", u"Signed by Aspose.Cells", currentDate);
    DigitalSignatureCollection signatures;
    signatures.Add(signature);
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Sample Value");
    workbook.AddDigitalSignature(signatures);
    workbook.Save(u"signed_workbook.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Verwandte Artikel
- [Excel-Dateien verschlüsseln und entschlüsseln](/cells/de/cpp/encrypt-and-decrypt-excel-files/)
- [Arbeitsmappenstruktur schützen und Schutz aufheben](/cells/de/cpp/protect-and-unprotect-workbook-structure/)
- [Arbeitsblatt schützen und Schutz aufheben](/cells/de/cpp/protect-and-unprotect-worksheets/)
- [Freigegebene Arbeitsmappe mit Passwort schützen oder Schutz aufheben](/cells/de/cpp/password-protect-or-unprotect-the-shared-workbook/)
- [Passwort zum Ändern mit Aspose.Cells überprüfen](/cells/de/cpp/check-password-to-modify-using-aspose-cells/)
- [Dateiformat verschlüsselter Office Open XML – OOXML-Dateien erkennen](/cells/de/cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Excel-Dateien verschlüsseln](/cells/de/cpp/encrypting-excel-files/)
- [Wie man ein Dateiformat erkennt und prüft, ob die Datei verschlüsselt ist](/cells/de/cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="cpp" >}}