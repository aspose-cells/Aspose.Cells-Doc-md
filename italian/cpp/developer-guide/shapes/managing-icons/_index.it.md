---
title: Aggiungi icone al foglio di lavoro con C++
linktitle: Gestione delle icone
type: docs
weight: 100
url: /it/cpp/insert-svg-to-excel/
description: Impara come aggiungere icone ai fogli di lavoro Excel usando Aspose.Cells con C++.
---

## Aggiungere Icone al Foglio di Lavoro in Aspose.Cells

Se hai bisogno di utilizzare [Aspose.Cells](https://products.aspose.com/cells/) per aggiungere 'icone' in un file Excel, allora questo documento può offrirti un aiuto.

L'interfaccia Excel corrispondente all'operazione di inserimento icona è la seguente:

![](1.png)

- Seleziona la posizione dell'icona da inserire nel foglio di lavoro
- Clicca sinistro su *Inserisci*->*Icone*
- Nella finestra che si apre, seleziona l'icona nel rettangolo rosso nella figura sopra
- Clic sinistro *Inserisci*, verrà inserito nel file Excel.

L'effetto è il seguente:

![](2.png)

Qui abbiamo preparato *codice di esempio* per aiutarti a inserire icone usando [Aspose.Cells](https://products.aspose.com/cells/). C'è anche un *file di esempio* necessario [sample.xlsx] e un [file di risorse] di icona [icon.zip]. Abbiamo usato l'interfaccia di Excel per inserire un'icona con lo stesso effetto di visualizzazione del [file di risorse](icon.zip) nel [file di esempio](sample.xlsx).

### C++

```cpp
#include <iostream>
#include <fstream>
#include <vector>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    U16String fileName = u"icon.svg";
    std::ifstream fsSource(fileName.ToUtf8(), std::ios::binary);
    if (!fsSource) {
        std::cerr << "Failed to open file: " << fileName.ToUtf8() << std::endl;
        return -1;
    }

    fsSource.seekg(0, std::ios::end);
    size_t fileSize = fsSource.tellg();
    fsSource.seekg(0, std::ios::beg);

    std::vector<uint8_t> bytes(fileSize);
    fsSource.read(reinterpret_cast<char*>(bytes.data()), fileSize);
    fsSource.close();

    Aspose::Cells::Vector<uint8_t> asposeBytes(bytes.size());
    if (!bytes.empty()) {
        memcpy(asposeBytes.GetData(), bytes.data(), bytes.size());
    }

    Workbook workbook(u"sample.xlsx");
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    sheet.GetShapes().AddIcons(3, 0, 7, 0, 100, 100, asposeBytes, Aspose::Cells::Vector<uint8_t>());

    Cell c = sheet.GetCells().Get(8, 7);
    c.PutValue(u"Insert via Aspose.Cells");
    Style s = c.GetStyle();
    s.GetFont().SetColor(Color::Blue());
    c.SetStyle(s);

    workbook.Save(u"sample2.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```

Quando esegui il codice sopra nel tuo progetto, otterrai i seguenti risultati:

![](3.png)
