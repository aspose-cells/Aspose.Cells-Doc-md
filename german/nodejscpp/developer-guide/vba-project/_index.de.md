---
title: Verwalten von VBA Codes in einer Excel Makro aktivierten Arbeitsmappe
linktitle: Makro Projekt
type: docs
weight: 200
url: /de/nodejs-cpp/manage-vba-project/
description: Fügen Sie ein VBA Modul hinzu und modifizieren Sie VBA oder Makros mit Aspose.Cells for Node.js via C++.
---

## **Fügen Sie in Node.js ein VBA-Modul hinzu**
{{% alert color="primary" %}}

Aspose.Cells ermöglicht es, mit Aspose.Cells for Node.js via C++ ein neues VBA-Modul und Makro-Code hinzuzufügen. Bitte verwenden Sie die [**Workbook.add(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#add-worksheet-)-Methode, um das neue VBA-Modul innerhalb der Arbeitsmappe hinzuzufügen.

{{% /alert %}}

Der folgende Beispielcode erstellt eine neue Arbeitsmappe, fügt ein neues VBA-Modul und Makro-Code hinzu und speichert die Ausgabe im XLSM-Format. Sobald Sie die XLSM-Ausgabedatei in Microsoft Excel öffnen und die Befehle **Entwickler > Visual Basic** klicken, sehen Sie ein Modul mit dem Namen "TestModule" und darin den folgenden Makro-Code.

{{< highlight javascript >}}
Sub ShowMessage() {
    MsgBox "Welcome to Aspose!"
}
{{< /highlight >}}

Hier ist der Beispielcode, um die XLSM-Ausgabedatei mit VBA-Modul und Makro-Code zu generieren.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create new workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add VBA Module
const idx = workbook.getVbaProject().getModules().add(worksheet);

// Access the VBA Module, set its name and codes
const module = workbook.getVbaProject().getModules().get(idx);
module.setName("TestModule");

module.setCodes("Sub ShowMessage()" + "\r\n" +
"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +
"End Sub");

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsm"), AsposeCells.SaveFormat.Xlsm);
```

## **Modifizieren von VBA oder Makros in Node.js**

{{% alert color="primary" %}} 

Sie können VBA- oder Makrocode mit Aspose.Cells for Node.js via C++ modifizieren. Aspose.Cells hat das folgende Modul und die Klassen hinzugefügt, um das VBA-Projekt in der Excel-Datei zu lesen und zu modifizieren.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Dieser Artikel zeigt Ihnen, wie Sie den VBA- oder Makrocode in der Quell-Excel-Datei mithilfe von Aspose.Cells ändern können.

{{% /alert %}} 

Der folgende Beispielcode lädt die Quelldatei mit Excel, die den VBA- oder Makro-Code enthält

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is test message."
}
{{< /highlight >}}

Nach der Ausführung des Beispielcodes von Aspose.Cells wird der VBA- oder Makrocode wie folgt modifiziert sein

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is Aspose.Cells message."
}
{{< /highlight >}}

Sie können die [Quell-Excel-Datei](5112508.xlsm) und die [Ausgabe-Excel-Datei](5112511.xlsm) über die angegebenen Links herunterladen.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsm"));

// Change the VBA Module Code
const modules = workbook.getVbaProject().getModules();
const moduleCount = modules.getCount();
for (let i = 0; i < moduleCount; i++) {
const module = modules.get(i);
const code = module.getCodes();
if (code.includes("This is test message.")) 
{
code = code.replace("This is test message.", "This is Aspose.Cells message.");
module.setCodes(code);
}
}


// Save the output Excel file
workbook.save(path.join(dataDir, "output_out.xlsm"));
```

## **Erweiterte Themen**
- [Fügen Sie einen Bibliotheksverweis zum VBA-Projekt im Arbeitsblatt hinzu](/cells/de/nodejs-cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [Makro einem Formularsteuerelement zuweisen](/cells/de/nodejs-cpp/assign-macro-to-form-control/)
- [Überprüfen Sie, ob die digitale Signatur des VBA-Codes gültig ist](/cells/de/nodejs-cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [Überprüfen Sie, ob der VBA-Code signiert ist](/cells/de/nodejs-cpp/check-if-vba-code-is-signed/)
- [Überprüfen Sie, ob das VBA-Projekt in einer Arbeitsmappe signiert ist](/cells/de/nodejs-cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [Überprüfen Sie, ob das VBA-Projekt geschützt und zum Anzeigen gesperrt ist](/cells/de/nodejs-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Kopieren Sie den VBA-Makro UserForm-DesignerStorage von der Vorlage in die Zieldatei](/cells/de/nodejs-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Digitales Signieren eines VBA-Codeprojekts mit Zertifikat](/cells/de/nodejs-cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [Exportieren Sie das VBA-Zertifikat in eine Datei oder einen Stream](/cells/de/nodejs-cpp/export-vba-certificate-to-file-or-stream/)
- [Filtern eines VBA-Projekts beim Laden einer Arbeitsmappe](/cells/de/nodejs-cpp/filter-vba-project-while-loading-a-workbook/)
- [Herausfinden, ob das VBA-Projekt geschützt ist](/cells/de/nodejs-cpp/find-out-if-vba-project-is-protected/)
- [Passwortschutz des VBA-Projekts der Excel-Arbeitsmappe](/cells/de/nodejs-cpp/password-protect-the-vba-project-of-excel-workbook/)

{{< app/cells/assistant language="nodejs-cpp" >}}
