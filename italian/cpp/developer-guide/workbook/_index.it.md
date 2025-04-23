---
title: Gestisci Workbook con C++
linktitle: Workbook
type: docs
weight: 60
url: /it/cpp/managing-workbooks-and-worksheets/
description: Impara come Gestire un Workbook tramite le API Aspose.Cells for C++.
keywords: Come Gestire un Workbook in C++, Gestisci Workbook e fogli di lavoro usando C++, Opera su workbook e fogli di lavoro in C++.
---

{{% alert color="primary" %}}

Aspose.Cells for C++ fornisce un'API potente e flessibile per gestire workbook e fogli di lavoro. Questa sezione spiega come creare, aprire e manipolare workbooks e fogli di lavoro programmaticamente.

{{% /alert %}}

## **Creazione di un nuovo foglio di lavoro**
Per creare un nuovo workbook:

1. Crea un'istanza della classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/).
2. Aggiungi fogli di lavoro al workbook usando la classe [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/).
3. Salva il workbook usando il metodo [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/).

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    // Create a new workbook
    Aspose::Cells::Workbook workbook;

    // Add a worksheet to the workbook
    workbook.GetWorksheets().Add();

    // Save the workbook
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();

    return 0;

}
```

## **Apertura di un Workbook Esistente**
Per aprire un workbook esistente:

1. Crea un'istanza della classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) e passa il percorso del file al costruttore.
2. Accedi ai fogli di lavoro usando la classe [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/).
3. Modifica il workbook secondo necessità.
4. Salva il workbook usando il metodo [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/).

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    Aspose::Cells::Workbook workbook("input.xlsx");
    auto worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).SetValue("Hello, World!");
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;

}
```

## **Gestione dei Fogli di Lavoro**
Aspose.Cells for C++ offre un'ampia gamma di metodi per gestire i fogli di lavoro, inclusa l’aggiunta, la rimozione e la rinomina dei fogli.

### **Aggiunta di un Foglio di Lavoro**
Per aggiungere un nuovo foglio di lavoro:

1. Accedere alla classe [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) dal workbook.
2. Usare il metodo [Add](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/) per aggiungere un nuovo foglio di lavoro.

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    // Create a new workbook
    Aspose::Cells::Workbook workbook;

    // Add a new worksheet
    workbook.GetWorksheets().Add("NewSheet");

    // Save the workbook
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();

    return 0;

}
```

### **Rimozione di un foglio di lavoro**
Per rimuovere un foglio di lavoro:

1. Accedere alla classe [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) dal workbook.
2. Usare il metodo [RemoveAt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat/) per rimuovere un foglio di lavoro in base all'indice.

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    // Open an existing workbook
    Aspose::Cells::Workbook workbook("input.xlsx");

    // Remove the first worksheet
    workbook.GetWorksheets().RemoveAt(0);

    // Save the workbook
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();

    return 0;

}
```

### **Rinomina un foglio di lavoro**
Per rinominare un foglio di lavoro:

1. Accedere alla classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) dal workbook.
2. Usare il metodo [SetName](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setname/) per rinominare il foglio di lavoro.

```cpp
#include <Aspose.Cells.h>

int main() {
    Aspose::Cells::Startup();
    Aspose::Cells::Workbook workbook("input.xlsx");
    auto worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName("RenamedSheet");
    workbook.Save("output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;

}
```

## **Conclusioni**
Aspose.Cells for C++ fornisce un insieme completo di strumenti per la gestione di workbook e fogli di lavoro. Che tu abbia bisogno di creare un nuovo workbook, aprirne uno esistente o manipolare i fogli di lavoro, Aspose.Cells rende semplice lavorare con i file Excel programmaticamente.
