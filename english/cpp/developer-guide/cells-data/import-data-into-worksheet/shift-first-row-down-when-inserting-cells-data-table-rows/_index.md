---
title: Shift First Row down when inserting Cells Data Table Rows with C++
linktitle: Shift First Row down when inserting Cells Data Table Rows
type: docs
weight: 270
url: /cpp/shift-first-row-down-when-inserting-cells-data-table-rows/
description: Learn how to shift first row down when inserting Cells Data Table Rows through the Aspose.Cells for C++ API.
keywords: C++ shift the first row down when inserting a table into the worksheet, shift first row down, shift first row down when adding a table into worksheet
---

## **Possible Usage Scenarios**

Aspose.Cells allows you to shift the first row down when inserting a table into the worksheet. This document explains how you may accomplish the task using Aspose.Cells APIs.

## **Shift First Row down when inserting Cells Data Table Rows**

The following sample code illustrates how to shift the first row down when inserting a table into the worksheet. We use a simple template Excel file in code to demonstrate the feature. You can exercise the feature by setting the boolean [**ImportTableOptions.ShiftFirstRowDown**](https://reference.aspose.com/cells/cpp/aspose.cells/importtableoptions/shiftfirstrowdown/) attribute to **True**/**False** to better understand it. Please see the [sample Excel file](45056031.xlsx), [output Excel False file](45056032.xlsx), and [output Excel True file](45056033.xlsx) for your reference.

## **Screenshot**

![todo:image_alt_text](shift-first-row-down-when-inserting-cells-data-table-rows_1.png)

## **Sample Code**

```c++
#include <iostream>
#include <vector>
#include <string>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CellsDataTable : public ICellsDataTable {
private:
    int m_index = -1;

    static const std::vector<std::u16string> colsNames;
    static const std::vector<std::u16string> col0data;
    static const std::vector<std::u16string> col1data;
    static const std::vector<std::u16string> col2data;
    static const std::vector<std::u16string> col3data;
    static const std::vector<std::vector<std::u16string>> colsData;

public:
    Object GetItem(int columnIndex) const override {
        return Object(U16String(colsData[columnIndex][m_index]));
    }

    Object GetItem(const U16String& columnName) const override {
        throw std::runtime_error("Not implemented");
    }

    std::vector<U16String> GetColumns() const override {
        return std::vector<U16String>(colsNames.begin(), colsNames.end());
    }

    int GetCount() const override {
        return col0data.size();
    }

    void BeforeFirst() override {
        m_index = -1;
    }

    bool Next() override {
        if (m_index + 1 >= static_cast<int>(col0data.size()))
            return false;
        m_index++;
        return true;
    }
};

const std::vector<std::u16string> CellsDataTable::colsNames = { u"Pet", u"Fruit", u"Country", u"Color" };
const std::vector<std::u16string> CellsDataTable::col0data = { u"Dog", u"Cat", u"Duck" };
const std::vector<std::u16string> CellsDataTable::col1data = { u"Apple", u"Pear", u"Banana" };
const std::vector<std::u16string> CellsDataTable::col2data = { u"UK", u"USA", u"China" };
const std::vector<std::u16string> CellsDataTable::col3data = { u"Red", u"Green", u"Blue" };
const std::vector<std::vector<std::u16string>> CellsDataTable::colsData = { col0data, col1data, col2data, col3data };

class ShiftFirstRowDownWhenInsertingCellsDataTableRows {
public:
    static void Run() {
        U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
        U16String outDir(u"..\\Data\\02_OutputDirectory\\");

        auto cellsDataTable = std::make_shared<CellsDataTable>();

        Workbook wb(srcDir + u"sampleImportTableOptionsShiftFirstRowDown.xlsx");
        Worksheet ws = wb.GetWorksheets().Get(0);

        ImportTableOptions opts;
        opts.SetShiftFirstRowDown(false);

        ws.GetCells()->ImportData(cellsDataTable, 2, 2, opts);

        wb.Save(outDir + u"outputImportTableOptionsShiftFirstRowDown-False.xlsx");
        std::cout << "Data imported successfully without shifting the first row down." << std::endl;
    }
};

int main() {
    Aspose::Cells::Startup();
    ShiftFirstRowDownWhenInsertingCellsDataTableRows::Run();
    Aspose::Cells::Cleanup();
    return 0;
}
```