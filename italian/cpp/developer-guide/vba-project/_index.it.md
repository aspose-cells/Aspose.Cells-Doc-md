---
title: Gestisci Codici VBA di workbook Excel abilitato alle macro con C++
linktitle: Progetto macro
type: docs
weight: 200
url: /it/cpp/manage-vba-project/
description: Aggiungi un Modulo VBA e modifica VBA o Macro con la libreria Aspose.Cells in C++.
---

## **Aggiungi un Modulo VBA in C++**
{{% alert color="primary" %}}

Aspose.Cells ti permette di aggiungere un nuovo Modulo VBA e Codice Macro usando Aspose.Cells. Usa il metodo [**Workbook.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/add/) per aggiungere il nuovo Modulo VBA all’interno del workbook.

{{% /alert %}}

Il codice di esempio seguente crea un nuovo workbook, aggiunge un nuovo Modulo VBA e Codice Macro e salva l’output nel formato XLSM. Una volta aperto il file XLSM in Microsoft Excel e cliccati i comandi di menu **Sviluppatore > Visual Basic**, vedrai un modulo chiamato "TestModule" e al suo interno il seguente codice macro.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Qui si trova il codice di esempio per generare il file XLSM di output con un modulo VBA e un codice macro.

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

## **Modifica VBA o Macro in C++**

{{% alert color="primary" %}} 

È possibile modificare il codice VBA o macro utilizzando Aspose.Cells. Aspose.Cells ha aggiunto i seguenti namespace e classi per leggere e modificare il progetto VBA nel file Excel.

- Aspose::Cells::Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Questo articolo ti mostrerà come modificare il codice VBA o Macro all'interno del file Excel di origine usando Aspose.Cells.

{{% /alert %}} 

Il seguente codice di esempio carica il file Excel sorgente che contiene il codice VBA o Macro:

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

Dopo l'esecuzione del codice di esempio Aspose.Cells, il codice VBA o Macro sarà modificato così:

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

Puoi scaricare il [file Excel di origine](5112508.xlsm) e il [file Excel di output](5112511.xlsm) dai link forniti.

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

## **Argomenti Avanzati**
- [Aggiungi un Riferimento alla Libreria nel Progetto VBA nel Workbook](/cells/it/cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [Assegna una Macro al controllo del modulo](/cells/it/cpp/assign-macro-to-form-control/)
- [Verifica se la firma digitale del codice VBA è valida](/cells/it/cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [Verifica se il codice VBA è firmato](/cells/it/cpp/check-if-vba-code-is-signed/)
- [Verifica se il Progetto VBA in un Workbook è Firmato](/cells/it/cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [Verifica se il progetto VBA è protetto e bloccato per la visualizzazione](/cells/it/cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Copia il DesignerStorage del modulo utente VBA Macro dal modello al foglio di lavoro di destinazione](/cells/it/cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Firma digitalmente un progetto di codice VBA con un certificato](/cells/it/cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [Esporta il certificato VBA su file o flusso](/cells/it/cpp/export-vba-certificate-to-file-or-stream/)
- [Filtra il Progetto VBA durante il Caricamento di un Workbook](/cells/it/cpp/filter-vba-project-while-loading-a-workbook/)
- [Scopri se il progetto VBA è protetto](/cells/it/cpp/find-out-if-vba-project-is-protected/)
- [Proteggi con password il progetto VBA del foglio di lavoro Excel](/cells/it/cpp/password-protect-the-vba-project-of-excel-workbook/)
{{< app/cells/assistant language="cpp" >}}
