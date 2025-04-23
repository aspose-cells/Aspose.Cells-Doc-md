---
title: Verwalten Sie VBA Codes in einer Excel Arbeitsmappe mit Makros in C++
linktitle: Makro Projekt
type: docs
weight: 200
url: /de/cpp/manage-vba-project/
description: Fügen Sie ein VBA Modul hinzu und bearbeiten Sie VBA oder Makros mit der Aspose.Cells Bibliothek in C++.
---

## **Ein VBA-Modul in C++ hinzufügen**
{{% alert color="primary" %}}

Aspose.Cells ermöglicht es, ein neues VBA-Modul und Makro-Code mithilfe von Aspose.Cells hinzuzufügen. Verwenden Sie die [**Workbook.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/add/)-Methode, um das neue VBA-Modul innerhalb der Arbeitsmappe hinzuzufügen.

{{% /alert %}}

Der folgende Beispielcode erstellt eine neue Arbeitsmappe, fügt ein neues VBA-Modul und Makro-Code hinzu und speichert die Ausgabe im XLSM-Format. Sobald Sie die XLSM-Datei in Microsoft Excel öffnen und die Menübefehle **Entwickler > Visual Basic** anklicken, sehen Sie ein Modul namens "TestModule" und innerhalb dieses Moduls den folgenden Makro-Code.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Hier ist der Beispielcode zum Erzeugen der Ausgabe-XLSM-Datei mit VBA-Modul und Makrocode.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add VBA Module
    int32_t idx = workbook.GetVbaProject().GetModules().Add(worksheet);

    // Access the VBA Module, set its name and codes
    VbaModule module = workbook.GetVbaProject().GetModules().Get(idx);
    module.SetName(u"TestModule");

    U16String codes = u"Sub ShowMessage()\r\n"
                      u"    MsgBox \"Welcome to Aspose!\"\r\n"
                      u"End Sub";
    module.SetCodes(codes);

    // Save the workbook
    U16String outputPath = outDir + u"output_out.xlsm";
    workbook.Save(outputPath, SaveFormat::Xlsm);

    std::cout << "VBA module added and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **VBA oder Makro in C++ bearbeiten**

{{% alert color="primary" %}} 

Sie können VBA- oder Makrocode mit Aspose.Cells modifizieren. Aspose.Cells hat den folgenden Namensraum und Klassen hinzugefügt, um das VBA-Projekt in der Excel-Datei zu lesen und zu modifizieren.

- Aspose::Cells::Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Dieser Artikel zeigt Ihnen, wie Sie den VBA- oder Makrocode in der Quell-Excel-Datei mithilfe von Aspose.Cells ändern können.

{{% /alert %}} 

Der folgende Beispielcode lädt die Quell-Excel-Datei, die den folgenden VBA- oder Makro-Code enthält:

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

Nach Ausführung des Aspose.Cells-Beispiels wird der VBA- oder Makro-Code wie folgt geändert:

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

Sie können die [Quell-Excel-Datei](5112508.xlsm) und die [Ausgabe-Excel-Datei](5112511.xlsm) über die angegebenen Links herunterladen.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"sample.xlsm";
    U16String outputFilePath = outDir + u"output_out.xlsm";

    Workbook workbook(inputFilePath);

    VbaProject vbaProject = workbook.GetVbaProject();
    VbaModuleCollection modules = vbaProject.GetModules();

    for (int i = 0; i < modules.GetCount(); ++i)
    {
        VbaModule module = modules.Get(i);
        U16String code = module.GetCodes();
        U16String searchStr = u"This is test message.";
        U16String replaceStr = u"This is Aspose.Cells message.";

        if (code.IndexOf(searchStr) != -1)
        {
            U16String newCode;
            const char16_t* codeData = code.GetData();
            const char16_t* searchData = searchStr.GetData();
            int codeLen = code.GetLength();
            int searchLen = searchStr.GetLength();

            int pos = 0;
            int searchPos;

            while ((searchPos = code.IndexOf(searchStr)) != -1)
            {
                for (int j = pos; j < searchPos; j++)
                {
                    newCode += codeData[j];
                }

                newCode += replaceStr;

                pos = searchPos + searchLen;
            }

            for (int j = pos; j < codeLen; j++)
            {
                newCode += codeData[j];
            }

            module.SetCodes(newCode);
        }
    }

    workbook.Save(outputFilePath);

    std::cout << "VBA module codes updated successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Fortgeschrittene Themen**
- [Eine Bibliotheksreferenz zum VBA-Projekt in der Arbeitsmappe hinzufügen](/cells/de/cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [Makro einem Formularsteuerelement zuweisen](/cells/de/cpp/assign-macro-to-form-control/)
- [Überprüfen Sie, ob die digitale Signatur des VBA-Codes gültig ist](/cells/de/cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [Überprüfen Sie, ob der VBA-Code signiert ist](/cells/de/cpp/check-if-vba-code-is-signed/)
- [Überprüfen, ob das VBA-Projekt in einer Arbeitsmappe signiert ist](/cells/de/cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [Überprüfen Sie, ob das VBA-Projekt geschützt und zum Anzeigen gesperrt ist](/cells/de/cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Kopieren Sie den VBA-Makro UserForm-DesignerStorage von der Vorlage in die Zieldatei](/cells/de/cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Digitales Signieren eines VBA-Codeprojekts mit Zertifikat](/cells/de/cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [Exportieren Sie das VBA-Zertifikat in eine Datei oder einen Stream](/cells/de/cpp/export-vba-certificate-to-file-or-stream/)
- [VBA-Projekt beim Laden einer Arbeitsmappe filtern](/cells/de/cpp/filter-vba-project-while-loading-a-workbook/)
- [Herausfinden, ob das VBA-Projekt geschützt ist](/cells/de/cpp/find-out-if-vba-project-is-protected/)
- [Passwortschutz des VBA-Projekts der Excel-Arbeitsmappe](/cells/de/cpp/password-protect-the-vba-project-of-excel-workbook/)
