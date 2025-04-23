---
title: 名前付き範囲の削除
type: docs
weight: 90
url: /ja/python-net/delete-named-ranges/
description: Aspose.Cells for Pythonを使用して、ExcelまたはOpenOfficeファイルから定義された名前または名前付き範囲を削除する方法について学ぶことができます。
keywords: Python Excelライブラリ、Python重複した定義名の削除、Python重複した定義名の削除。
---

## **紹介**
Excelファイルに多くの定義名や名前付き範囲がある場合、参照されないためにいくつかをクリアする必要があります。

## **MS Excelで名前付き範囲を削除する**

Excelから名前付き範囲を削除するには、次の手順に従うことができます：
1. Microsoft Excelを開き、名前付き範囲が含まれているワークブックを開きます。
2. Excelリボンの「数式」タブに移動します。
3. 「定義された名前」グループの「名前マネージャー」ボタンをクリックします。これにより名前マネージャーのダイアログボックスが開きます。
4. 名前マネージャーのダイアログボックスで、削除したい名前付き範囲を選択します。
5. 「削除」ボタンをクリックします。プロンプトが表示されたら削除を確認します。
6. 「閉じる」ボタンをクリックして名前マネージャーのダイアログボックスを閉じます。
7. 変更を保存するためにワークブックを保存します。

## **Aspose.Cells for .Netを使用して名前付き範囲を削除する**
Aspose.Cells for .NETを使えば、リスト内の名前付き範囲や定義済み名前を[テキスト](https://reference.aspose.com/cells/python-net/aspose.cells/namecollection/remove_a_name/#str)で削除できます。

```python
from aspose.cells import Workbook
import aspose.cells
import os
import pytest
# The path to the documents directory
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Instantiate a new Workbook
workbook = Workbook(os.path.join(data_dir, "Book1.xlsx"))

# Get all the worksheets in the book
worksheets = workbook.worksheets

# Delete a named range by text
worksheets.names.remove_a_name("NamedRange")


# Save the workbook to retain the changes
workbook.save(os.path.join(data_dir, "Book2.xlsx"))
```

注意：定義された名前が数式によって参照されている場合、削除することはできません。定義名の数式の削除のみ可能です。

## **一部の名前付き範囲を削除する**
定義名を削除する際には、ファイル内のすべての数式によって参照されているかどうかを確認する必要があります。
名前付き範囲を削除のパフォーマンスを改善するために、一緒に何個かを削除することができます。

```python
from aspose.cells import Workbook
import aspose.cells
import os
import pytest
# Instantiate a new Workbook
workbook = Workbook("testcase/data/Book1.xlsx")

# Get all the worksheets in the book
worksheets = workbook.worksheets

# Delete some defined names
worksheets.names.remove_names_by_array(["NamedRange1", "NamedRange2"])

# Save the workbook to retain the changes
workbook.save("Book2.xlsx")
```


## **重複した定義名を削除する**
一部のExcelファイルは、いくつかの定義名が重複しているため壊れています。したがって、これらの重複した名前を削除してファイルを修復できます。

```python
from aspose.cells import Workbook
import aspose.cells
import os
import pytest
# Instantiate a new Workbook
workbook = Workbook("testcase/data/Book1.xlsx")

# Get all the worksheets in the book
worksheets = workbook.worksheets

# Delete duplicate defined names
worksheets.names.remove_duplicate_names()

# Save the workbook to retain the changes
workbook.save("Book2.xlsx")
```
