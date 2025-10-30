---
title: Excelセル操作
linktitle: セル操作
type: docs
weight: 60
url: /ja/nodejs-cpp/mcp/cell-operations
keywords: "Excelセル操作、Excelセルの結合、Excelのコピー＆ペースト、Excelセルの操作、AIを使ったExcelセル操作"
description: "Excelセル操作  結合、コピー/ペースト、セルのクリア、AI自動化による高度なセル操作"
---

# Excelセル操作

AI搭載の自動化で高度な**Excelセル操作**を実行。セルの結合、コピー/ペースト、内容のクリア、セルの正確な操作を行います。

## 利用可能なツール

- `cell_operations` - **AI搭載のExcelセル操作**（結合、コピー/ペースト、クリア）
- `cell_operations_batch` - **スプレッドシートMCP**を使った複数の**Excelセル操作**の一括実行

## 単一セル操作

### セルの結合
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/merged-layout.xlsx",
    "sheet_name": "Report",
    "operation": "merge_cells",
    "range": "A1:C1"
  }
}
```

### セルの結合解除
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/unmerged.xlsx",
    "sheet_name": "Data",
    "operation": "unmerge_cells",
    "range": "A1:C1"
  }
}
```

### セルのコピー
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/data-copy.xlsx",
    "sheet_name": "Source",
    "operation": "copy_cells",
    "source_range": "A1:D5"
  }
}
```

### 値の貼り付け
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/data-copy.xlsx",
    "sheet_name": "Target",
    "operation": "paste_values",
    "destination_range": "A1"
  }
}
```

### 内容のクリア
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/cleanup.xlsx",
    "sheet_name": "Data",
    "operation": "clear_contents",
    "range": "A1:Z100"
  }
}
```

## バッチセル操作

### 完了したマージとコピーのワークフロー
```json
{
  "tool": "cell_operations_batch", 
  "parameters": {
    "filepath": "reports/financial-report.xlsx",
    "sheet_name": "Sheet1",
    "operations": [
      {
        "operation": "merge_cells",
        "range": "A7:C7"
      },
      {
        "operation": "paste_values",
        "source_range": "A1:F1",
        "destination_range": "A9"
      },
      {
        "operation": "paste_formats",
        "source_range": "A1:F1", 
        "destination_range": "A12"
      }
    ]
  }
}
```

### シート間操作
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/multi-sheet.xlsx",
    "sheet_name": "Summary",
    "operation": "paste_values",
    "source_range": "A1:F5",
    "source_sheet": "Data",
    "destination_range": "A1"
  }
}
```

### データクリーニング操作
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "reports/cleanup-demo.xlsx",
    "sheet_name": "Data",
    "operations": [
      {
        "operation": "clear_contents",
        "range": "A1:A10"
      },
      {
        "operation": "clear_formats",
        "range": "B1:B10"
      },
      {
        "operation": "clear_all",
        "range": "C1:C10"
      }
    ]
  }
}
```

## 操作タイプの参照

### マージ操作
- `merge_cells` - セルを1つに結合
- `unmerge_cells` - 結合したセルを個別のセルに分割
- `merge_across` - 行をまたいでセルを結合しながらも、別々の行を保持

### コピー/貼り付け操作
- `copy_cells` - セル範囲をクリップボードにコピー
- `paste_values` - 値のみ貼り付け（書式や数式なし）
- `paste_formulas` - 数式のみ貼り付け（値や書式なし）
- `paste_formats` - 書式のみ貼り付け（値や数式なし）
- `transpose_paste` - 転置して貼り付け（行↔列）

### クリア操作
- `clear_contents` - セルの内容をクリア（書式は保持）
- `clear_formats` - セルの書式をクリア（内容は保持）
- `clear_all` - 内容と書式の両方をクリア

## 高度な例

### レポートタイトル設定
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "reports/title-report.xlsx",
    "sheet_name": "Report",
    "operations": [
      {
        "operation": "merge_cells",
        "range": "A1:F1"
      },
      {
        "operation": "merge_cells",
        "range": "A2:F2"
      },
      {
        "operation": "merge_cells",
        "range": "A3:C3"
      },
      {
        "operation": "merge_cells",
        "range": "D3:F3"
      }
    ]
  }
}
```

### データテンプレート作成
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "templates/data-template.xlsx",
    "sheet_name": "Template",
    "operations": [
      {
        "operation": "copy_cells",
        "source_range": "A1:F1"
      },
      {
        "operation": "paste_formats",
        "destination_range": "A10"
      },
      {
        "operation": "paste_formats",
        "destination_range": "A20"
      },
      {
        "operation": "paste_formats",
        "destination_range": "A30"
      }
    ]
  }
}
```

### データ統合
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "reports/consolidated.xlsx",
    "sheet_name": "Summary",
    "operations": [
      {
        "operation": "paste_values",
        "source_range": "A1:E10",
        "source_sheet": "Q1Data",
        "destination_range": "A2"
      },
      {
        "operation": "paste_values",
        "source_range": "A1:E10",
        "source_sheet": "Q2Data", 
        "destination_range": "A12"
      },
      {
        "operation": "paste_values",
        "source_range": "A1:E10",
        "source_sheet": "Q3Data",
        "destination_range": "A22"
      }
    ]
  }
}
```

### 数式と書式の分離
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "reports/separated.xlsx",
    "sheet_name": "Analysis",
    "operations": [
      {
        "operation": "paste_formulas",
        "source_range": "A1:F10",
        "source_sheet": "Calculations",
        "destination_range": "A1"
      },
      {
        "operation": "paste_formats",
        "source_range": "A1:F10", 
        "source_sheet": "Formatting",
        "destination_range": "A1"
      }
    ]
  }
}
```

## シート間操作

### シート間コピー
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/multi-sheet-copy.xlsx",
    "sheet_name": "Destination",
    "operation": "paste_values",
    "source_range": "A1:D10",
    "source_sheet": "Source",
    "destination_range": "B2"
  }
}
```

### 集計シート作成
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "reports/summary-creation.xlsx",
    "sheet_name": "Summary",
    "operations": [
      {
        "operation": "paste_values",
        "source_range": "A1:C5",
        "source_sheet": "January",
        "destination_range": "A2"
      },
      {
        "operation": "paste_values",
        "source_range": "A1:C5",
        "source_sheet": "February",
        "destination_range": "E2"
      },
      {
        "operation": "paste_values",
        "source_range": "A1:C5",
        "source_sheet": "March",
        "destination_range": "I2"
      }
    ]
  }
}
```

## データ変換

### 転置データ
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/transposed.xlsx",
    "sheet_name": "Data",
    "operation": "transpose_paste",
    "source_range": "A1:E5",
    "destination_range": "G1"
  }
}
```

### 値のみコピー
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "reports/values-only.xlsx",
    "sheet_name": "Clean Data",
    "operations": [
      {
        "operation": "copy_cells",
        "source_range": "A1:F20",
        "source_sheet": "Raw Data"
      },
      {
        "operation": "paste_values",
        "destination_range": "A1"
      }
    ]
  }
}
```

## ベストプラクティス

1. **戦略的マージ**: ヘッダーとタイトルのマージには使用、データ領域には使用しない
2. **コピーして貼り付け前に範囲をコピー**: コピー操作前に必ず範囲をコピー
3. **適切にクリア**: 必要に応じて最適なクリア操作を選択
4. **シート間計画**: 複数シート操作の計画を立てて衝突を避ける
5. **一括操作**: 関連する操作をまとめてパフォーマンス向上

## 一般的な使用例

### レポートヘッダー
- タイトル用にセルを結合
- ヘッダ書式をコピー
- 一貫したスタイル設定を適用

### データクリーンアップ
- 古いコンテンツをクリア
- 書式設定を削除
- セル状態をリセット

### テンプレート作成
- 書式パターンをコピー
- データなしで構造を貼り付ける
- 再利用可能なレイアウトを作成

### データ統合
- 複数のシートからデータを結合
- 式の衝突を避けるため値だけ貼り付け
- データの配置を転置

## エラー処理

### 無効なマージ範囲
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "operation": "merge_cells",
    "range": "A1"
  }
}
```
**結果**：エラー - 1つのセルをマージできません

### ソース範囲がありません
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "operation": "paste_values",
    "destination_range": "A1"
  }
}
```
**結果**：エラー - コピーされたデータがありません

### シートの参照エラー
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "operation": "paste_values",
    "source_range": "A1:B2",
    "source_sheet": "NonExistentSheet",
    "destination_range": "A1"
  }
}
```
**結果**：エラー - ソースシートが見つかりません 
{{< app/cells/assistant language="nodejs-cpp" >}}
