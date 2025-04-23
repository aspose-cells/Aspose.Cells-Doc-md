---
title: Utilizzo dell API LightCells con C++
linktitle: Utilizzo dell API LightCells
type: docs
weight: 160
url: /it/cpp/using-lightcells-api/
description: Scopri come utilizzare l API LightCells in C++ per leggere e scrivere in modo efficiente grandi file Excel con minimale utilizzo di memoria.
---

{{% alert color="primary" %}} 

A volte è necessario leggere e scrivere file Microsoft Excel di grandi dimensioni con un enorme elenco di dati o contenuti nel foglio di lavoro. La LightCells API è utile per la creazione di enormi fogli di calcolo Excel: con essa, è necessaria una quantità di memoria inferiore e si ottiene una migliore performance ed efficienza.

{{% /alert %}} 

# Architettura basata su eventi
Aspose.Cells fornisce la LightCells API, progettata principalmente per manipolare i dati delle celle uno per uno senza costruire un blocco di modello di dati completo (utilizzando la collezione di celle ecc.) in memoria. Funziona in modalità basata su eventi.

Per salvare i workbook, fornisci il contenuto della cella cella per cella durante il salvataggio e il componente lo salva direttamente nel file di output.

Quando si leggono file di template, il componente analizza ogni cella e fornisce il loro valore uno per uno.

In entrambe le procedure, un oggetto Cell viene elaborato e quindi scartato, l'oggetto Workbook non detiene la collezione. In questa modalità, quindi, si risparmia memoria durante l'importazione ed esportazione di un file Microsoft Excel che ha un ampio set di dati che altrimenti utilizzerebbe molta memoria.

Anche se la LightCells API elabora le celle allo stesso modo per i file XLSX e XLS (non carica effettivamente tutte le celle in memoria ma elabora una cella e poi la scarta), salva la memoria in modo più efficace per i file XLSX rispetto ai file XLS a causa dei diversi modelli di dati e delle strutture dei due formati.

Tuttavia, **per i file XLS**, per risparmiare memoria, gli sviluppatori possono specificare una posizione temporanea per salvare i dati temporanei generati durante il processo di salvataggio. Comunemente, **utilizzando LightCells API per salvare i file XLSX può risparmiare il 50% o più di memoria** rispetto al metodo comune, **salvare i file XLS può risparmiare circa il 20-40% di memoria**.

## Scrittura di un ampio file Excel
Aspose.Cells fornisce un'interfaccia, `LightCellsDataProvider`, che deve essere implementata nel tuo programma. L'interfaccia rappresenta il fornitore di dati per il salvataggio di grandi file di fogli di calcolo in modalità leggera.

Quando si salva un workbook in questa modalità, `StartSheet(int)` viene verificato durante il salvataggio di ogni foglio di lavoro. Per un foglio, se `StartSheet` restituisce true, allora tutti i dati e le proprietà di righe e celle di questo foglio devono essere forniti da questa implementazione. In primo luogo, viene chiamato `NextRow()` per ottenere il prossimo indice di riga da salvare. Se viene restituito un indice di riga valido (l'indice di riga deve essere in ordine crescente per le righe da salvare), allora viene fornito un oggetto `Row` che rappresenta questa riga per impostare le sue proprietà tramite `StartRow(Row)`.

Per una riga, `NextCell()` viene verificato prima. Se viene restituito un indice di colonna valido (l'indice di colonna deve essere in ordine crescente per tutte le celle di una riga da salvare), allora viene fornito un oggetto `Cell` che rappresenta quella cella per l'implementazione di impostare i suoi dati e proprietà tramite `StartCell(Cell)`. Dopo aver impostato i dati della cella, la cella viene salvata direttamente nel file di foglio di calcolo generato e la cella successiva viene verificata e processata.

### Scrivere un grande file Excel: Esempio
Si prega di vedere il seguente codice di esempio per vedere il funzionamento dell'API LightCells. Aggiungere, rimuovere o aggiornare i segmenti di codice in base alle proprie esigenze.

Il programma crea un file enorme con **10.000 (matrice 10000x30) record** in un foglio di lavoro e li riempie con dati fittizi. Puoi specificare la tua matrice modificando le variabili `rowsCount` e `colsCount` nel metodo `Main()`.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class TestDataProvider : public LightCellsDataProvider {
private:
    int _row = -1;
    int _column = -1;
    int maxRows;
    int maxColumns;
    Workbook _workbook;

public:
    TestDataProvider(Workbook workbook, int maxRows, int maxColumns)
        : _workbook(workbook), maxRows(maxRows), maxColumns(maxColumns) {}

    bool IsGatherString() override {
        return false;
    }

    int NextCell() override {
        ++_column;
        if (_column < this->maxColumns)
            return _column;
        else {
            _column = -1;
            return -1;
        }
    }

    int NextRow() override {
        ++_row;
        if (_row < this->maxRows) {
            _column = -1;
            return _row;
        }
        else
            return -1;
    }

    void StartCell(Cell& cell) override {
        cell.PutValue(_row + _column);
        if (_row != 1) {
            cell.SetFormula(u"=Rand() + A2");
        }
    }

    void StartRow(Row& row) override {}

    bool StartSheet(int sheetIndex) override {
        return sheetIndex == 0;
    }
};

void WriteUsingLightCellsAPI() {
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    int rowsCount = 10000;
    int colsCount = 30;

    Workbook workbook;
    OoxmlSaveOptions ooxmlSaveOptions;

    TestDataProvider dataProvider(workbook, rowsCount, colsCount);
    ooxmlSaveOptions.SetLightCellsDataProvider(&dataProvider);

    workbook.Save(outDir + u"output.out.xlsx", ooxmlSaveOptions);

    std::cout << "File saved successfully using LightCells API!" << std::endl;
}

int main() {
    Aspose::Cells::Startup();
    WriteUsingLightCellsAPI();
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Lettura di grandi file Excel
Aspose.Cells fornisce un'interfaccia, `LightCellsDataHandler`, che deve essere implementata nel tuo programma. L'interfaccia rappresenta il fornitore di dati per la lettura di grandi file di fogli di calcolo in modalità leggera.

Quando si legge un workbook in questa modalità, `StartSheet` viene verificato durante la lettura di ogni foglio di lavoro. Se `StartSheet` restituisce true, allora tutti i dati e le proprietà delle celle nelle righe e colonne del foglio vengono controllati e processati da questa implementazione. Per ogni riga, viene chiamato `StartRow` per verificare se necessita di essere processata. Se una riga deve essere processata, prima vengono lette le sue proprietà e l'utente può accedere alle sue proprietà con `ProcessRow`. Se anche le celle della riga devono essere processate, allora `ProcessRow` deve restituire true e quindi `StartCell` viene chiamato per ogni cella esistente nella riga per verificare se una cella deve essere processata. Se una cella deve essere processata, si chiama `ProcessCell` per processare la cella tramite l'implementazione di questa interfaccia.

### Lettura di grandi file Excel: Esempio
Si prega di vedere il seguente codice di esempio per vedere il funzionamento dell'API LightCells. Aggiungere, rimuovere o aggiornare i segmenti di codice in base alle proprie esigenze.

Il programma legge un enorme file con milioni di record in un foglio di lavoro. Ci vuole un po' di tempo per leggere ogni foglio nel workbook. Il codice di esempio legge il file e recupera il numero totale di celle, il conteggio delle stringhe e il conteggio delle formule in ogni foglio di lavoro.

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

class LightCellsDataHandlerVisitCells : public LightCellsDataHandler
{
private:
    int cellCount;
    int formulaCount;
    int stringCount;

public:
    LightCellsDataHandlerVisitCells() : cellCount(0), formulaCount(0), stringCount(0) {}

    int GetCellCount() const { return cellCount; }
    int GetFormulaCount() const { return formulaCount; }
    int GetStringCount() const { return stringCount; }

    bool StartSheet(Worksheet& sheet) override
    {
        std::cout << "Processing sheet[" << sheet.GetName().ToUtf8() << "]" << std::endl;
        return true;
    }

    bool StartRow(int32_t rowIndex) override
    {
        return true;
    }

    bool ProcessRow(Row& row) override
    {
        return true;
    }

    bool StartCell(int32_t columnIndex) override
    {
        return true;
    }

    bool ProcessCell(Cell& cell) override
    {
        cellCount++;
        if (cell.IsFormula())
        {
            formulaCount++;
        }
        else if (cell.GetType() == CellValueType::IsString)
        {
            stringCount++;
        }
        return false;
    }
};

void Run()
{
    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create load options and set the light cells data handler
    LoadOptions opts;
    auto handler = std::make_shared<LightCellsDataHandlerVisitCells>();
    opts.SetLightCellsDataHandler(handler.get());

    // Load the workbook with the specified options
    Workbook wb(srcDir + u"LargeBook1.xlsx", opts);

    // Get the total number of sheets
    int sheetCount = wb.GetWorksheets().GetCount();

    // Output the results
    std::cout << "Total sheets: " << sheetCount << ", cells: " << handler->GetCellCount()
              << ", strings: " << handler->GetStringCount() << ", formulas: " << handler->GetFormulaCount() << std::endl;
}

int main()
{
    Aspose::Cells::Startup();
    Run();
    Aspose::Cells::Cleanup();
    return 0;
}
```
