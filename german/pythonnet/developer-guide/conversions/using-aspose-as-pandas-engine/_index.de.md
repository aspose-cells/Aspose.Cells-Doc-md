---
title: Verwendung von Aspose.Cells for Python via .NET als Pandas Excel Engine
type: docs
weight: 40
url: /de/python-net/using-aspose-as-pandas-engine/
description: Verwendung von Aspose.Cells for Python via .NET als Pandas Excel Engine.
keywords: Verwendung von Aspose.Cells für Python via .NET als Pandas Excel Engine.
---

{{% alert color="primary" %}}

Dieses Handbuch zeigt, wie man [Aspose.Cells für Python via .NET](https://products.aspose.com/cells/python-net/) als benutzerdefinierte Excel-Engine innerhalb der `pandas`-Bibliothek integriert, sodass Sie `.xlsx`, `.xls` usw. Dateien mit hoher Präzision parsen können.

{{% /alert %}}

## Warum Aspose.Cells für Python via .NET verwenden?

Aspose.Cells bietet:

- Erweiterte Excel-Unterstützung (Formeln, Diagramme, Formatierung, zusammengefasste Zellen usw.)
- Unterstützung für mehrere Formate: `.xls`, `.xlsx`, `.xlsb`, `.ods`, `.csv`, `.html`
- Bessere Genauigkeit bei komplexen Tabellenblättern im Vergleich zu `openpyxl` oder `xlrd`

---

## Prerequisites

- [Install a C compiler](https://pandas.pydata.org/docs/dev/development/contributing_environment.html#step-1-install-a-c-compiler)
- Here, we use the Windows platform as an example for explanation.If you have installed Visual Studio 2022 on your Windows system, you can open the **x64 Native Tools Command Prompt for VS 2022** and run the `cl` command to check the version of the C++ compiler. Make sure the compiler version is **19.3x or higher** before proceeding with the following build steps.
- Make sure that you have [cloned the repository](https://github.com/pandas-dev/pandas.git)
```bash
git clone https://github.com/pandas-dev/pandas.git
```
- `cd` zum Quellverzeichnis von pandas, das Sie gerade mit dem Klon-Befehl erstellt haben

---

## Step 1: Create an isolated environment

```bash
# Set up virtual environment
python -m venv .venv
.\.venv\Scripts\activate      # on Windows
# source .venv/bin/activate  # on Linux/macOS

# Install aspose-cells-python
pip install aspose-cells-python
# Install the build dependencies
python -m pip install -r requirements-dev.txt
```

---

## Step 2: Create Aspose engine adapter
Create a new file:\
`pandas/io/excel/_asposecells.py`\
Add the following content:

```python
# pandas/io/excel/_asposecells.py
import pandas as pd
from aspose.cells import Workbook

class AsposeCellsExcelReader:
    def __init__(self, filepath_or_buffer, sheet_name=0, header=0, **kwargs):
        self.filepath = filepath_or_buffer
        self.sheet_name = sheet_name
        self.header = header

    def parse(self, sheet_name, header=0, **kwargs):
        wb = Workbook(self.filepath)
        worksheet = wb.worksheets[sheet_name] if isinstance(sheet_name, int) else wb.worksheets.get(sheet_name)
        # Get the Cells collection from the worksheet
        cells = worksheet.cells

        # Calculate number of columns: max_col - min_col (both are 0-based)
        col_count = cells.max_data_column - cells.min_data_column

        # Initialize a list to hold all the row data
        output_data = []

        # Get the index of the first row that contains data
        first_data_row_Index = cells.min_data_row

        # Iterate through all the rows
        for row in cells.rows:
            if row is None:
                continue  # Skip if the row is not initialized

            row_data = []
            for cell in row:
                row_data.append(cell.value)
            output_data.append(row_data)

        # Prepare the column names
        columns = []
        if header is not None:
            row = cells.rows[first_data_row_Index]
            for cell in row:
                columns.append(cell.value)
            # Remove the header row from the data
            output_data = output_data[1:]
        else:
            # If no header, generate default column names like "Unnamed: 0", "Unnamed: 1", ...
            columns = [f"Unnamed: {i}" for i in range(col_count + 1)]

        # Convert the data into a pandas DataFrame
        return pd.DataFrame(output_data, columns=columns)

    def close(self):
        pass  # Required by pandas API
```

---

## Step 3: Register the Aspose Engine in Pandas

In `pandas/io/excel/_base.py`, find the `class ExcelFile` class, and add
Add the following import line after the existing `from pandas.io.excel._xlrd import XlrdReader`:

```python
from pandas.io.excel._asposecells import AsposeCellsExcelReader
```
und dann den folgenden Code in ` _engines: Mapping[str, Any]` hinzufügen

```python
_engines: Mapping[str, Any] = {
    ...
    "asposecells": AsposeCellsExcelReader,
}
```

---

## Step 4: Build and install pandas
```bash
# build and install pandas
python -m pip install -ve . --no-build-isolation
```

> ✅ Wenn Sie während des Build-Prozesses einen Kompilierungsfehler erhalten, z.B.: **Cython.Compiler.Errors.InternalError: Internal compiler error: 'free_threading_config.pxi' nicht gefunden**, können Sie versuchen, den folgenden Befehl auszuführen und dann erneut zu kompilieren.
```bash
# remove all untracked files, directories, and ignored files from the working directory.
git clean -xfd 
```

---


## Step 5: Use the Engine
You can use the following [Excel file](test.xlsx) for testing.
```python
import pandas as pd
# asposecells
df = pd.read_excel("test.xlsx", engine="asposecells", sheet_name=0, header=0)
# print and check DataFrame
print(df)
```
Nach der Ausführung sollten Sie ein Ergebnis wie dieses erhalten.

![todo:image_alt_text](result.png)


---

## Notes

- For production use, a valid Aspose.Cells for Python via .NET license is required.
- This approach is ideal for testing or local enhancement of `read_excel` behavior.
- You can also use `Aspose.Cells for Python via .NET` directly outside of pandas if desired.

---

## Siehe auch

- [Aspose.Cells für Python via .NET Dokumentation](https://docs.aspose.com/cells/python-net/)
- [pandas](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html) [`read_excel()`](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html) [API](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)

{{< app/cells/assistant language="python-net" >}}
