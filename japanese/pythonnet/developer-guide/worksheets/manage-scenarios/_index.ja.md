---
title: Python via .NETを使用してワークシートからシナリオを作成、操作または削除する方法
linktitle: シナリオの管理
type: docs
weight: 190
url: /ja/python-net/create-manipulate-or-remove-scenarios-from-worksheets/
description: Aspose.Cells for Python via .NET APIを使用して、Excelワークシートのシナリオを作成、変更、削除する方法を学びます。
keywords: Python Excelシナリオ、ワークシートのシナリオ管理Python、シナリオの追加Python、シナリオの削除Excel Python、シナリオの修正Python
---

{{% alert color="primary" %}}

時には、スプレッドシートでシナリオを作成、操作、削除する必要があります。シナリオは、名前付きの「もしも？」モデルで、変数入力セルとそれにリンクされた1つ以上の数式を含みます。シナリオを作成する前に、少なくとも1つの数式を含み、さまざまな値を受け入れるセルに依存するワークシートを設計してください。この例は、Aspose.Cells for Python via .NETを使用してワークシートのシナリオを管理する方法を示します。

{{% /alert %}}

Aspose.Cellsは、シナリオを操作するためのいくつかのクラスを提供します：
- [**ScenarioCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/scenariocollection/)
- [**Scenario**](https://reference.aspose.com/cells/python-net/aspose.cells/scenario/)
- [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/scenarioinputcellcollection/)
- [**ScenarioInputCell**](https://reference.aspose.com/cells/python-net/aspose.cells/scenarioinputcell/)

シナリオにアクセスするには[**Worksheet.scenarios**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/scenarios/)プロパティを使用します。以下のコードは次のことを示します：
1. シナリオが含まれるExcelファイルを開く
2. 既存のシナリオを削除する
新しいシナリオを追加

変更されたワークブックを保存します

```python
import os
from aspose.cells import Workbook

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Instantiate the Workbook and load an Excel file
workbook = Workbook(os.path.join(data_dir, "aspose-sample.xlsx"))
# Access first worksheet
worksheet = workbook.worksheets[0]

if len(worksheet.scenarios) > 0:
    # Remove the existing first scenario from the sheet
    worksheet.scenarios.remove_at(0)

    # Create a scenario
    i = worksheet.scenarios.add("MyScenario")
    # Get the scenario
    scenario = worksheet.scenarios[i]
    # Add comment to it
    scenario.comment = "Test sceanrio is created."
    # Get the input cells for the scenario
    sic = scenario.input_cells
    # Add the scenario on B4 (as changing cell) with default value
    sic.add(3, 1, "1100000")

    output_path = os.path.join(data_dir, "outBk_scenarios1.out.xlsx")

    # Save the Excel file
    workbook.save(output_path)
    print(f"\nProcess completed successfully.\nFile saved at {output_path}")
```

