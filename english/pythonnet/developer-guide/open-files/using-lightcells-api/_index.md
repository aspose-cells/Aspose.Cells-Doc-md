---
title: Using LightCells API with Python via .NET
linktitle: Using LightCells API
type: docs
weight: 160
url: /python-net/using-lightcells-api/
description: Learn how to read and write large Excel files efficiently using Python via .NET with Aspose.Cells' LightCells API for optimized memory usage and performance.
---

{{% alert color="primary" %}} 

When working with large Microsoft Excel files containing massive datasets, the LightCells API provides an efficient solution for Python.NET developers. This event-driven approach minimizes memory usage while maintaining high performance for both reading and writing operations.

{{% /alert %}} 

## **Event Driven Architecture**
Aspose.Cells for Python via .NET implements LightCells API through an event-driven model that processes cells individually rather than loading the entire workbook into memory. Key features:

- Processes one cell at a time during read/write operations
- Discards processed cells immediately after handling
- Particularly memory-efficient for XLSX files (50%+ memory savings)
- Effective for XLS files (20-40% memory reduction)

## **Writing Large Excel Files**
To create massive spreadsheets efficiently:

1. Implement the `LightCellsDataProvider` abstract base class
2. Use sequential processing of rows and cells
3. Handle data generation through callback methods

### **Python.NET Implementation Example**
This example creates a 10,000x30 cell spreadsheet:

```python
import clr
clr.AddReference("Aspose.Cells")
from Aspose.Cells import Workbook, SaveFormat, LightCellsDataProvider
from System import Array
import datetime

class LargeFileDataProvider(LightCellsDataProvider):
    def __init__(self, rows_count, cols_count):
        self.rows_count = rows_count
        self.cols_count = cols_count
        self.row_index = -1
        
    def start_sheet(self, sheet_index):
        return sheet_index == 0  # Process first worksheet

    def next_row(self):
        self.row_index += 1
        return self.row_index if self.row_index < self.rows_count else -1

    def start_row(self, row):
        row.is_blank = False
        row.height = 30

    def next_cell(self):
        if self.current_col_index < self.cols_count - 1:
            self.current_col_index += 1
            return self.current_col_index
        return -1

    def start_cell(self, cell):
        cell.put_value(f"Row{self.row_index}_Col{self.current_col_index}")
        cell.set_style(None)

# Usage
provider = LargeFileDataProvider(10000, 30)
workbook = Workbook()
workbook.save("large_file.xlsx", SaveFormat.Xlsx, provider)
```

```python
import os
from aspose.cells import Workbook, OoxmlSaveOptions, LightCellsDataProvider

class TestDataProvider(LightCellsDataProvider):
    def __init__(self, workbook, max_rows, max_columns):
        self._workbook = workbook
        self.max_rows = max_rows
        self.max_columns = max_columns
        self._row = -1
        self._column = -1

    def is_gather_string(self):
        return False

    def next_cell(self):
        self._column += 1
        if self._column < self.max_columns:
            return self._column
        else:
            self._column = -1
            return -1

    def next_row(self):
        self._row += 1
        if self._row < self.max_rows:
            self._column = -1
            return self._row
        else:
            return -1

    def start_cell(self, cell):
        cell.put_value(self._row + self._column)
        if self._row != 1:
            cell.formula = "=Rand() + A2"

    def start_row(self, row):
        pass

    def start_sheet(self, sheet_index):
        return sheet_index == 0

def run():
    # The path to the documents directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "data")
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Specify matrix dimensions
    rows_count = 10000
    cols_count = 30

    workbook = Workbook()
    ooxml_save_options = OoxmlSaveOptions()
    ooxml_save_options.light_cells_data_provider = TestDataProvider(
        workbook, rows_count, cols_count
    )

    # Save workbook with light cells processing
    output_path = os.path.join(data_dir, "output.out.xlsx")
    workbook.save(output_path, ooxml_save_options)

if __name__ == "__main__":
    run()
```

## **Reading Large Excel Files**
For efficient processing of massive files:

1. Implement the `LightCellsDataHandler` abstract base class
2. Process rows and cells through event callbacks
3. Access cell data incrementally

### **Python.NET Implementation Example**
This example analyzes cell statistics:

```python
import clr
clr.AddReference("Aspose.Cells")
from Aspose.Cells import Workbook, LoadFormat, LightCellsDataHandler
from System import Array

class LargeFileAnalyzer(LightCellsDataHandler):
    def __init__(self):
        self.cell_count = 0
        self.string_count = 0
        self.formula_count = 0

    def start_sheet(self, worksheet):
        return True  # Process all sheets

    def start_row(self, row_index, row):
        return True  # Process all rows

    def process_row(self, row):
        return True  # Process cells

    def start_cell(self, column_index, cell):
        self.cell_count += 1
        if cell.is_string:
            self.string_count += 1
        elif cell.is_formula:
            self.formula_count += 1
        return True

# Usage
analyzer = LargeFileAnalyzer()
workbook = Workbook("large_file.xlsx", LoadFormat.Xlsx, analyzer)
print(f"Total Cells: {analyzer.cell_count}")
print(f"String Cells: {analyzer.string_count}")
print(f"Formula Cells: {analyzer.formula_count}")
```

```python
import os
from aspose.cells import LoadOptions, Workbook, LightCellsDataHandler, CellValueType

def run():
    # The path to the documents directory.
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "data")
    
    opts = LoadOptions()
    v = LightCellsDataHandlerVisitCells()
    opts.light_cells_data_handler = v
    wb = Workbook(os.path.join(data_dir, "LargeBook1.xlsx"), opts)
    sheet_count = wb.worksheets.count
    print(f"Total sheets: {sheet_count}, cells: {v.cell_count}, strings: {v.string_count}, formulas: {v.formula_count}")

class LightCellsDataHandlerVisitCells(LightCellsDataHandler):
    def __init__(self):
        self._cell_count = 0
        self._formula_count = 0
        self._string_count = 0
        
    @property
    def cell_count(self):
        return self._cell_count
    
    @property
    def formula_count(self):
        return self._formula_count
    
    @property
    def string_count(self):
        return self._string_count
    
    def start_sheet(self, sheet):
        print(f"Processing sheet[{sheet.name}]")
        return True
    
    def start_row(self, row_index):
        return True
    
    def process_row(self, row):
        return True
    
    def start_cell(self, column_index):
        return True
    
    def process_cell(self, cell):
        self._cell_count += 1
        if cell.is_formula:
            self._formula_count += 1
        elif cell.type == CellValueType.IS_STRING:
            self._string_count += 1
        return False
```

## **Key Considerations**
- Process cells in strict row/column order
- Maintain state between callback methods
- Use appropriate memory management for very large datasets
- Prefer XLSX format for optimal memory efficiency
- Handle temporary storage for XLS files when needed

[API Reference](https://reference.aspose.com/cells/python-net/) | [GitHub Examples](https://github.com/aspose-cells)