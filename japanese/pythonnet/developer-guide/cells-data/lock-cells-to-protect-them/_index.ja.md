---
title: Python.NETを使用してセルをロックして保護する
linktitle: セルをロックして保護する
type: docs
weight: 130
url: /ja/python-net/how-to-lock-cells-to-protect-them/
description: Aspose.Cells for Python via .NETを使用して、特定のセルをロックしたり、ワークシートを保護したりする方法を学びましょう。
keywords: Pythonを使ったExcelのセルのロック、シートの保護、セル保護のチュートリアル
---

## **可能な使用シナリオ**
セルをロックして保護することは、Microsoft ExcelやGoogle Sheetsなどのスプレッドシートアプリケーションで一般的な慣行であり、重要な理由がいくつかあります：

1. 誤って変更を防ぐ：重要なデータや数式の誤った編集を防止します。
2. データの整合性を維持：重要なデータが一貫性を保ったまま正確に保たれるようにします。
3. 制御されたアクセス：共同作業環境での編集権限を管理します。
4. 数式の保護：重要な計算を変更から守ります。
5. ビジネスルールの強制：データ保護要件に準拠します。
6. ユーザー誘導：複雑なスプレッドシート内で明確に編集可能な領域を提供します。

## **Excelでセルをロックして保護する方法**
Microsoft Excelでセルをロックする方法は次のとおりです：

1. ロックするセルを選択：セルを選択するか、シート全体をロックします。
1. セルの書式設定ダイアログを開く：右クリック > 「セルの書式設定」または Ctrl+1。
<br>
<img src="1.png" width=60% />
1. セルをロック： 「保護」タブ > 「ロック済み」にチェック > 「OK」をクリック。
1. シートを保護：「レビュー」タブ > 「シートの保護」 > パスワード/権限を設定 > 「OK」をクリック。
<br>
<img src="2.png" width=60% />

## **Pythonを使用したセルのロックと保護の方法**

Aspose.Cells for Python via .NETはプログラムによるセルの保護を可能にします。以下の手順に従ってください：
1. [サンプルファイル](sample.xlsx)を読み込む
2. すべてのセルのロックを解除（保護されていない状態はデフォルトでは適用されません）
3. 特定のセルをロック
4. セルのロックを強制するためにシートを保護

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("sample.xlsx")
worksheet = workbook.worksheets[0]

# Unlock all cells first
style = ac.Style()
style.is_locked = False
style_flag = ac.StyleFlag()
style_flag.locked = True
worksheet.cells.apply_style(style, style_flag)

# Lock specific cells
worksheet.cells["A1"].get_style().is_locked = True
worksheet.cells["B2"].get_style().is_locked = True

# Enable worksheet protection
worksheet.protect(ac.ProtectionType.ALL)

# Save protected workbook
workbook.save("output.xlsx")
```

## **結果出力**
この実装では、指定されたセル（A1とB2）をロックし、他のセルは編集可能に保ちます。シート保護によってこれらの設定が適用されます。

<br>
<img src="3.png" width=60% />

```python
from aspose.cells import Workbook, ProtectionType, StyleFlag

# Load the Excel file
workbook = Workbook("sample.xlsx")

# Access the first worksheet
sheet = workbook.worksheets[0]

# Unlock all cells first
unlock_style = workbook.create_style()
unlock_style.is_locked = False

style_flag = StyleFlag()
style_flag.locked = True
sheet.cells.apply_style(unlock_style, style_flag)

# Lock specific cells (A1 and B2)
lock_style = workbook.create_style()
lock_style.is_locked = True

sheet.cells.get("A1").set_style(lock_style)
sheet.cells.get("B2").set_style(lock_style)

# Protect the worksheet to enforce locking
sheet.protect(ProtectionType.ALL)

# Save the modified workbook
workbook.save("output_locked.xlsx")
```
