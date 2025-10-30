---
title: Estrazione di oggetti OLE dal workbook con C++
linktitle: Estrarre oggetti OLE dal file di lavoro
type: docs
weight: 110
url: /it/cpp/extract-ole-objects-from-workbook/
description: Impara come estrarre oggetti OLE da un workbook usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

A volte, è necessario estrarre oggetti OLE da un workbook. Aspose.Cells supporta l'estrazione e il salvataggio di tali oggetti OLE.

Questo articolo mostra come creare un'applicazione console in Visual Studio ed estrarre diversi oggetti OLE da un workbook con poche semplici righe di codice.

{{% /alert %}}

## **Estrarre oggetti OLE da un file di lavoro**

### **Creazione di un file di lavoro modello**

1. Crea un workbook in Microsoft Excel.
1. Aggiungi un documento Microsoft Word, un workbook Excel e un documento PDF come oggetti OLE sul primo foglio di lavoro.

|**Modello di documento con oggetti OLE (OleFile.xls)**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

Successivamente, estrai gli oggetti OLE e salvali sul disco rigido con i rispettivi tipi di file.

### **Scarica e installa Aspose.Cells**

1. [Scarica Aspose.Cells for C++](https://downloads.aspose.com/cells/cpp).
1. Installalo sul tuo computer di sviluppo.

Tutti i componenti Aspose, una volta installati, funzionano in modalità di valutazione. La modalità di valutazione non ha limiti di tempo e inserisce solo filigrane nei documenti prodotti.

### **Crea un Progetto**

Avvia **Visual Studio** e crea una nuova applicazione console. Questo esempio mostrerà un'applicazione console C++.

1. Aggiungi Riferimenti
   1. Aggiungi un riferimento al componente Aspose.Cells nel tuo progetto, ad esempio, aggiungi un riferimento a ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll.

### **Estrai oggetti OLE**

Il codice sotto fa il vero lavoro di trovare ed estrarre oggetti OLE. Gli oggetti OLE (file DOC, XLS e PDF) vengono salvati su disco.

```cpp
#include <iostream>
#include <fstream>
#include <memory>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the template file
    Workbook workbook(srcDir + u"oleFile.xlsx");

    // Get the OleObject Collection in the first worksheet
    OleObjectCollection oles = workbook.GetWorksheets().Get(0).GetOleObjects();

    // Loop through all the oleobjects and extract each object in the worksheet
    for (int i = 0; i < oles.GetCount(); i++)
    {
        OleObject ole = oles.Get(i);

        // Specify the output filename
        U16String fileName = srcDir + u"outOle" + U16String(std::to_string(i).c_str()) + u".";

        // Specify each file format based on the oleobject format type
        switch (ole.GetFileFormatType())
        {
            case FileFormatType::Doc:
                fileName += u"doc";
                break;
            case FileFormatType::Excel97To2003:
                fileName += u"Xlsx";
                break;
            case FileFormatType::Ppt:
                fileName += u"Ppt";
                break;
            case FileFormatType::Pdf:
                fileName += u"Pdf";
                break;
            case FileFormatType::Unknown:
                fileName += u"Jpg";
                break;
            default:
                // Handle other formats if needed
                break;
        }

        // Save the oleobject as a new excel file if the object type is xls
        if (ole.GetFileFormatType() == FileFormatType::Xlsx)
        {
            Vector<uint8_t> objectData = ole.GetObjectData();
            if (objectData.GetLength() > 0)
            {
                Workbook oleBook(objectData);
                oleBook.GetSettings().SetIsHidden(false);
                oleBook.Save(srcDir + u"outOle" + U16String(std::to_string(i).c_str()) + u".out.xlsx");
            }
        }
        // Create the files based on the oleobject format types
        else
        {
            Vector<uint8_t> objectData = ole.GetObjectData();
            if (objectData.GetLength() > 0)
            {
                std::ofstream fs(fileName.ToUtf8().c_str(), std::ios::binary);
                fs.write(reinterpret_cast<const char*>(objectData.GetData()), objectData.GetLength());
                fs.close();
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
