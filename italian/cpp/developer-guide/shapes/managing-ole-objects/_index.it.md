---
title: Gestione di oggetti OLE con C++
linktitle: Gestione degli Oggetti OLE
type: docs
weight: 50
url: /it/cpp/managing-ole-objects/
description: Impara come aggiungere, estrarre e manipolare oggetti OLE nei fogli di lavoro usando Aspose.Cells con C++.
---

## **Introduzione**

OLE (Object Linking and Embedding) è il framework Microsoft per una tecnologia di documento composto. In breve, un documento composto è qualcosa come una scrivania che può contenere oggetti visivi e informativi di ogni tipo: testo, calendari, animazioni, suoni, video in movimento, 3D, notizie continuamente aggiornate, controlli, e così via. Ogni oggetto della scrivania è un'entità di programma indipendente che può interagire con un utente e comunicare anche con altri oggetti sulla scrivania.

OLE (Object Linking and Embedding) è supportato da molti programmi diversi ed è utilizzato per rendere il contenuto creato in un programma disponibile in un altro. Ad esempio, puoi inserire un documento di Microsoft Word in Microsoft Excel. Per vedere che tipi di contenuto puoi inserire, fai clic su **Oggetto** nel menu **Inserisci**. Solo i programmi installati sul computer e che supportano gli oggetti OLE appaiono nella casella del **Tipo di oggetto**.

### **Inserimento di oggetti OLE nel foglio di lavoro**

Aspose.Cells supporta l'aggiunta, l'estrazione e la manipolazione di oggetti OLE nei fogli di lavoro. Per questo motivo, Aspose.Cells ha la classe [**OleObjectCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobjectcollection/), usata per aggiungere un nuovo oggetto OLE alla lista di raccolta. Un'altra classe, [**OleObject**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/), rappresenta un oggetto OLE. Ha alcuni membri importanti:

- La proprietà [**ImageData**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getimagedata/) specifica i dati dell'immagine (icona) di tipo array di byte. L'immagine verrà visualizzata per mostrare l'oggetto OLE nel foglio di lavoro.
- La proprietà [**ObjectData**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getobjectdata/) specifica i dati dell'oggetto sotto forma di array di byte. Questi dati verranno visualizzati nel loro programma correlato quando fai doppio clic sull'icona dell'oggetto OLE.

L'esempio seguente mostra come aggiungere un/i oggetto(i) OLE in un foglio di lavoro.

```c++
#include <iostream>
#include <fstream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

std::vector<uint8_t> ReadFileToVector(const U16String& filePath) {
    std::ifstream file(filePath.ToUtf8(), std::ios::binary | std::ios::ate);
    if (!file) return {};
    std::streamsize size = file.tellg();
    file.seekg(0, std::ios::beg);
    std::vector<uint8_t> buffer(size);
    if (size > 0)
        file.read(reinterpret_cast<char*>(buffer.data()), size);
    return buffer;
}

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    U16String imagePath = srcDir + u"logo.jpg";
    std::vector<uint8_t> imageData = ReadFileToVector(imagePath);

    U16String objectPath = srcDir + u"book1.xls";
    std::vector<uint8_t> objectData = ReadFileToVector(objectPath);
    Vector<uint8_t> data(objectData.data(), static_cast<int32_t>(objectData.size()));
    sheet.GetOleObjects().Add(14, 3, 200, 220, data);
    if (sheet.GetOleObjects().GetCount() > 0) {
        sheet.GetOleObjects().Get(0).SetObjectData(data);
    }

    workbook.Save(outDir + u"output.out.xls");
    std::cout << "OLE object added successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Estrazione degli oggetti OLE nel Workbook**

Nell'esempio seguente viene mostrato come estrarre gli oggetti OLE in un Workbook. L'esempio ottiene diversi oggetti OLE da un file XLS esistente e salva file diversi (DOC, XLS, PPT, PDF, ecc.) in base al tipo di formato file dell'oggetto OLE.

Dopo aver eseguito il codice, possiamo salvare file diversi in base ai rispettivi tipi di formato degli oggetti OLE.

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the template file
    Workbook workbook(srcDir + u"book1.xls");

    // Get the OleObject Collection in the first worksheet
    OleObjectCollection oles = workbook.GetWorksheets().Get(0).GetOleObjects();

    // Loop through all the oleobjects and extract each object
    for (int32_t i = 0; i < oles.GetCount(); i++)
    {
        OleObject ole = oles.Get(i);

        // Specify the output filename
        U16String fileName = srcDir + u"ole_" + U16String(std::to_string(i).c_str()) + u".";

        // Specify each file format based on the oleobject format type
        switch (ole.GetFileFormatType())
        {
        case FileFormatType::Doc:
            fileName += u"doc";
            break;
        case FileFormatType::Xlsx:
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
            Workbook oleBook(objectData);
            oleBook.GetSettings().SetIsHidden(false);
            oleBook.Save(srcDir + u"Excel_File" + U16String(std::to_string(i).c_str()) + u".out.xlsx");
        }
        else
        {
            // Create the files based on the oleobject format types
            std::ofstream fs(fileName.ToUtf8().c_str(), std::ios::binary);
            Vector<uint8_t> objectData = ole.GetObjectData();
            fs.write(reinterpret_cast<const char*>(objectData.GetData()), objectData.GetLength());
            fs.close();
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Estrazione del file MOL incorporato**

Aspose.Cells supporta l'estrazione di oggetti di tipi poco comuni come MOL (file di dati molecolari contenente informazioni su atomi e legami). Il seguente frammento di codice dimostra l'estrazione di un file MOL incorporato e il suo salvataggio su disco utilizzando questo [file Excel di esempio](94896196.xlsx).

```c++
#include <iostream>
#include <fstream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"EmbeddedMolSample.xlsx");

    int index = 1;

    WorksheetCollection sheets = workbook.GetWorksheets();
    for (int i = 0; i < sheets.GetCount(); i++)
    {
        Worksheet sheet = sheets.Get(i);
        OleObjectCollection oles = sheet.GetOleObjects();

        for (int j = 0; j < oles.GetCount(); j++)
        {
            OleObject ole = oles.Get(j);

            std::wstring indexWStr = std::to_wstring(index);
            U16String fileName = outDir + u"OleObject" + U16String(reinterpret_cast<const char16_t*>(indexWStr.c_str())) + u".mol";

            std::ofstream fs(fileName.ToUtf8(), std::ios::binary);
            if (fs.is_open())
            {
                Vector<uint8_t> objectData = ole.GetObjectData();
                fs.write(reinterpret_cast<const char*>(objectData.GetData()), objectData.GetLength());
                fs.close();
                index++;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Argomenti Avanzati**
- [Accesso e modifica dell'etichetta di visualizzazione dell'oggetto Ole collegato](/cells/it/cpp/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [Aggiornare automaticamente l'oggetto OLE tramite Microsoft Excel usando Aspose.Cells](/cells/it/cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [Estrarre gli oggetti OLE dal Workbook](/cells/it/cpp/extract-ole-objects-from-workbook/)
- [Ottieni o Imposta l'Identificatore di Classe dell'Oggetto OLE Incorporato](/cells/it/cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [Inserimento di un file WAV come oggetto Ole](/cells/it/cpp/inserting-a-wav-file-as-an-ole-object/)
{{< app/cells/assistant language="cpp" >}}
