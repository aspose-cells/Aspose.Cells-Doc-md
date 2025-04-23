---
title: Verwendung der LightCells API mit C++
linktitle: Verwendung der LightCells API
type: docs
weight: 160
url: /de/cpp/using-lightcells-api/
description: Lernen Sie, wie Sie die LightCells API in C++ verwenden, um große Excel Dateien effizient mit minimalem Speicherverbrauch zu lesen und zu schreiben.
---

{{% alert color="primary" %}} 

Manchmal müssen Sie große Microsoft Excel-Dateien mit einer riesigen Menge an Daten oder Inhalten im Arbeitsblatt lesen und schreiben. Die LightCells API ist nützlich, um große Excel-Tabellenkalkulationen zu erstellen: Sie benötigen weniger Speicher und erhalten eine bessere Leistung und Effizienz.

{{% /alert %}} 

# Ereignisgesteuerte Architektur
Aspose.Cells bietet die LightCells API, die hauptsächlich darauf ausgelegt ist, Zellendaten einzeln zu manipulieren, ohne ein vollständiges Datenmodell (Verwendung der Zellensammlung usw.) in den Speicher zu laden. Es funktioniert im ereignisgesteuerten Modus.

Um Arbeitsmappen zu speichern, geben Sie den Zellinhalt einzeln an, wenn Sie speichern, und das Komponente speichert ihn direkt in die Ausgabedatei.

Beim Lesen von Vorlagendateien analysiert die Komponente jede Zelle und gibt deren Wert einzeln an.

In beiden Verfahren wird ein Cell-Objekt verarbeitet und dann verworfen, das Workbook-Objekt hält die Sammlung nicht. In diesem Modus wird daher Speicher gespart, wenn Microsoft Excel-Dateien importiert und exportiert werden, die einen großen Datensatz haben, der ansonsten viel Speicher verwenden würde.

Obwohl die LightCells API die Zellen für XLSX- und XLS-Dateien auf dieselbe Weise verarbeitet (sie lädt nicht alle Zellen tatsächlich in den Speicher, sondern verarbeitet eine Zelle und verwirft sie dann), spart sie für XLSX-Dateien effektiver Speicher als für XLS-Dateien aufgrund der unterschiedlichen Datenmodelle und Strukturen der beiden Formate.

Für XLS-Dateien können Entwickler jedoch spezifisch einen temporären Speicherort angeben, um während des Speichervorgangs generierte temporäre Daten zu speichern. **Die Verwendung der LightCells API zum Speichern von XLSX-Dateien kann in der Regel etwa 50 % oder mehr Speicher sparen** als die herkömmliche Methode, **das Speichern von XLS-Dateien kann etwa 20-40 % Speicher sparen**.

## Schreiben einer großen Excel-Datei
Aspose.Cells stellt eine Schnittstelle, `LightCellsDataProvider`, bereit, die in Ihrem Programm implementiert werden muss. Das Interface repräsentiert den Datenanbieter für das Speichern großer Tabellenkalkulationsdateien im leichten Modus.

Beim Speichern einer Arbeitsmappe mit diesem Modus wird `StartSheet(int)` beim Speichern jeder Arbeitsblatt in der Arbeitsmappe überprüft. Für ein Blatt wird, wenn `StartSheet(int)` wahr ist, dann alle Daten und Eigenschaften der Zeilen und Zellen dieses Blatts durch diese Implementierung bereitgestellt. Zunächst wird `NextRow()` aufgerufen, um den nächsten zu speichernden Zeilenindex zu erhalten. Wenn ein gültiger Zeilenindex zurückgegeben wird (der Zeilenindex muss in aufsteigender Reihenfolge für die zu speichernden Zeilen sein), wird ein `Row`-Objekt, das diese Zeile repräsentiert, bereitgestellt, um seine Eigenschaften durch `StartRow(Row)` festzulegen.

Für eine Zeile wird zuerst `NextCell()` überprüft. Wird ein gültiger Spaltenindex zurückgegeben (der Spaltenindex muss in aufsteigender Reihenfolge für alle Zellen einer Zeile sein, damit sie gespeichert werden), wird ein `Cell`-Objekt, das diese Zelle repräsentiert, bereitgestellt, um seine Daten und Eigenschaften durch `StartCell(Cell)` festzulegen. Nachdem die Daten der Zelle gesetzt wurden, wird die Zelle direkt in die erstellte Tabellenkalkulationsdatei gespeichert, und die nächste Zelle wird überprüft und verarbeitet.

### Schreiben einer großen Excel-Datei: Beispiel
Bitte sehen Sie sich den folgenden Beispielcode an, um die Funktionsweise der LightCells API zu sehen. Fügen Sie Codeausschnitte hinzu, entfernen Sie diese oder aktualisieren Sie sie gemäß Ihren Anforderungen.

Das Programm erstellt eine riesige Datei mit **10.000 (10000x30 Matrix) Datensätzen** in einem Arbeitsblatt und füllt sie mit Dummy-Daten. Sie können Ihre eigene Matrix festlegen, indem Sie die Variablen `rowsCount` und `colsCount` in der `Main()`-Methode ändern.

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

## Lesen großer Excel-Dateien
Aspose.Cells stellt eine Schnittstelle bereit, `LightCellsDataHandler`, die in Ihrem Programm implementiert werden muss. Die Schnittstelle repräsentiert den Datenanbieter zum Lesen großer Tabellenkalkulationsdateien im Leichtgewichtmodus.

Beim Lesen einer Arbeitsmappe in diesem Modus wird `StartSheet` beim Lesen jedes Arbeitsblatts überprüft. Für ein Blatt, wenn `StartSheet` wahr ist, werden alle Daten und Eigenschaften der Zellen in den Zeilen und Spalten des Blatts überprüft und durch diese Schnittstelle verarbeitet. Für jede Zeile wird `StartRow` aufgerufen, um zu überprüfen, ob sie verarbeitet werden muss. Wenn eine Zeile verarbeitet werden muss, werden ihre Eigenschaften zuerst gelesen, und der Entwickler kann auf ihre Eigenschaften mit `ProcessRow` zugreifen. Wenn auch die Zellen der Zeile verarbeitet werden sollen, sollte `ProcessRow` true zurückgeben, und dann wird `StartCell` für jede vorhandene Zelle in der Zeile aufgerufen, um zu überprüfen, ob eine Zelle verarbeitet werden muss. Wenn eine Zelle verarbeitet werden soll, wird `ProcessCell` aufgerufen, um die Zelle durch die Implementierung dieser Schnittstelle zu verarbeiten.

### Lesen großer Excel-Dateien: Beispiel
Bitte sehen Sie sich den folgenden Beispielcode an, um die Funktionsweise der LightCells API zu sehen. Fügen Sie Codeausschnitte hinzu, entfernen Sie diese oder aktualisieren Sie sie gemäß Ihren Anforderungen.

Das Programm liest eine riesige Datei mit Millionen von Datensätzen in einem Arbeitsblatt. Es dauert etwas Zeit, um jede Tabelle im Arbeitsbuch zu lesen. Der Beispielcode liest die Datei und ruft die Gesamtanzahl der Zellen, die Zeichenfolgenanzahl und die Formelanzahl in jedem Arbeitsblatt ab.

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
