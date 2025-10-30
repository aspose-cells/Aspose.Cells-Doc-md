---
title: Tabella pivot e dati di origine con C++
linktitle: Tabella Pivot e Dati di Origine
type: docs
weight: 30
url: /it/cpp/pivot-table-and-source-data/
description: Impara come cambiare dinamicamente i dati di origine di una tabella pivot usando Aspose.Cells con C++.
---

## **Dati di Origine della Tabella Pivot**

Ci sono momenti in cui si desidera creare report di Microsoft Excel con tabelle pivot che prendono dati da diverse fonti di dati (come un database) che non sono noti al momento della progettazione. Questo articolo fornisce un approccio per cambiare dinamicamente la fonte dati di una tabella pivot.

### **Cambiare i Dati di Origine di una Tabella Pivot**

1. Creazione di un nuovo modello di design.
   1. Creare un nuovo file di modello di design come nella schermata qui sotto.
   1. Definire quindi un intervallo nominato, **DataSource**, che si riferisce a questo intervallo di celle.

      **Creazione di un modello di design e definizione di un intervallo nominato, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)

1. Creazione di una Tabella Pivot basata su questo intervallo nominato.
   1. In Microsoft Excel, scegliere **Dati**, quindi **Tabella Pivot** e **Rapporto Tabella Pivot**.
   1. Creare una tabella pivot basata sull'intervallo nominato creato nel primo passaggio.

      **Creazione di una tabella pivot basata sull'intervallo nominato, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_2.png)


   1. Trascinare il campo corrispondente sulla riga e sulla colonna della tabella pivot, quindi creare la tabella pivot risultante come nella schermata qui sotto.

   **Creazione di una tabella pivot basata su un campo corrispondente** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)


1. Fare clic con il tasto destro sulla tabella pivot e selezionare **Opzioni Tabella**.
   1. Seleziona **Aggiorna all'apertura** nelle impostazioni delle **Opzioni dati**.

      **Impostare le opzioni della tabella pivot** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)


Ora puoi salvare questo file come il file del modello del tuo designer.

1. Popolazione di nuovi dati e modifica dei dati di origine di una tabella pivot.
   1. Una volta creato il modello del designer, utilizza il codice seguente per modificare i dati di origine della tabella pivot.

Eseguendo il codice di esempio sottostante si cambia il dato di origine della tabella pivot.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Populating new data to the worksheet cells
    worksheet.GetCells().Get(u"A9").PutValue(u"Golf");
    worksheet.GetCells().Get(u"B9").PutValue(u"Qtr4");
    worksheet.GetCells().Get(u"C9").PutValue(7000);

    // Changing named range "DataSource"
    Range range = worksheet.GetCells().CreateRange(0, 0, 9, 3);
    range.SetName(u"DataSource");

    // Saving the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    std::cout << "File saved successfully!" << std::endl;

    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
