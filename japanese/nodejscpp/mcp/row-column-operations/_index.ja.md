---
title: Excelの行と列の操作
linktitle: 行と列の操作
type: docs
weight: 50
url: /ja/nodejs-cpp/mcp/row-column-operations
keywords: "Excel行操作、Excel列操作、Excelレイアウト管理、行の挿入、列の削除、Excelセルのサイズ変更"
description: "Excel行と列の操作  行や列の挿入、削除、サイズ変更、表示/非表示をAI自動化で"
---

# Excelの行と列の操作

AIによる自動化を利用して**Excelの行と列の操作**を管理。完璧なスプレッドシートレイアウト管理のために、**Excelの行**と**列**の挿入、削除、サイズ変更、非表示/表示を行います。

## 利用可能なツール

- `row_column_operations` - **Excelの行/列操作**（挿入、削除、サイズ変更、非表示/表示）を**AI Excel**とともに
- `row_column_operations_batch` - **Excel MCP**を使用した複数の**Excelの行/列操作**をバッチで実行

## 単一操作

### 行の挿入
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "reports/layout-test.xlsx",
    "sheet_name": "Data",
    "operation": "insert_rows",
    "rows": "5",
    "count": 2
  }
}
```

### 列の削除
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "reports/cleanup.xlsx",
    "sheet_name": "Sheet1",
    "operation": "delete_columns",
    "columns": "C:D"
  }
}
```

### 行の高さ設定
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "reports/formatted.xlsx",
    "sheet_name": "Report",
    "operation": "set_row_height",
    "rows": "1",
    "height": 30
  }
}
```

### 列の幅を設定する
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "reports/formatted.xlsx",
    "sheet_name": "Report",
    "operation": "set_column_width",
    "columns": "A:F",
    "width": 15
  }
}
```

## 一括操作

### 総合レイアウト設定
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/professional-layout.xlsx",
    "sheet_name": "Summary Report",
    "operations": [
      {
        "operation": "set_row_height",
        "rows": "3",
        "height": 30
      },
      {
        "operation": "set_row_height",
        "rows": "4:6",
        "height": 20
      },
      {
        "operation": "set_column_width",
        "columns": "C",
        "width": 20
      },
      {
        "operation": "set_column_width",
        "columns": "D:G",
        "width": 15
      },
      {
        "operation": "auto_fit_rows",
        "rows": "7:10"
      }
    ]
  }
}
```

### 挿入および削除操作
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/restructure.xlsx",
    "sheet_name": "Sheet1",
    "operations": [
      {
        "operation": "insert_rows",
        "rows": "5",
        "count": 2
      },
      {
        "operation": "insert_columns",
        "columns": "D",
        "count": 1
      },
      {
        "operation": "delete_rows",
        "rows": "8:9"
      }
    ]
  }
}
```

### 非表示と再表示操作
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/visibility.xlsx",
    "sheet_name": "Sheet1",
    "operations": [
      {
        "operation": "hide_rows",
        "rows": "15:16"
      },
      {
        "operation": "hide_columns",
        "columns": "H:I"
      },
      {
        "operation": "unhide_rows",
        "rows": "15"
      },
      {
        "operation": "unhide_columns",
        "columns": "H"
      }
    ]
  }
}
```

### 自動調整操作
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/auto-sized.xlsx",
    "sheet_name": "Data",
    "operations": [
      {
        "operation": "auto_fit_columns",
        "columns": "A:F"
      },
      {
        "operation": "auto_fit_rows",
        "rows": "1:20"
      }
    ]
  }
}
```

## 操作タイプ一覧

### 挿入操作
- `insert_rows` - 指定位置に新しい行を挿入
- `insert_columns` - 指定位置に新しい列を挿入

### 削除操作  
- `delete_rows` - 指定した行を削除
- `delete_columns` - 指定した列を削除

### サイズ変更操作
- `set_row_height` - 行の高さをポイント単位で設定
- `set_column_width` - 列の幅を文字数で設定
- `auto_fit_rows` - 内容に合わせて行の高さを自動調整
- `auto_fit_columns` - 内容に合わせて列の幅を自動調整

### 表示操作
- `hide_rows` - 指定した行を非表示
- `unhide_rows` - 非表示の行を表示
- `hide_columns` - 指定した列を非表示
- `unhide_columns` - 非表示の列を表示

## 範囲の指定

### 行の範囲
- `"1"` - 単一の行（行1）
- `"1:3"` - 行の範囲（行1から3）
- `"5:10"` - 複数の連続した行

### 列の範囲
- `"A"` - 単一の列（列A）
- `"A:C"` - 範囲の列（列AからC）
- `"D:F"` - 複数の連続した列

## 高度な例

### レポートヘッダーの設定
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/header-setup.xlsx",
    "sheet_name": "Report",
    "operations": [
      {
        "operation": "set_row_height",
        "rows": "1:2",
        "height": 35
      },
      {
        "operation": "set_column_width",
        "columns": "A",
        "width": 25
      },
      {
        "operation": "set_column_width",
        "columns": "B:E",
        "width": 12
      },
      {
        "operation": "set_column_width",
        "columns": "F",
        "width": 18
      }
    ]
  }
}
```

### データ表のレイアウト
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/data-table.xlsx",
    "sheet_name": "Data",
    "operations": [
      {
        "operation": "insert_rows",
        "rows": "1",
        "count": 1
      },
      {
        "operation": "set_row_height",
        "rows": "1",
        "height": 25
      },
      {
        "operation": "auto_fit_columns",
        "columns": "A:J"
      },
      {
        "operation": "set_row_height",
        "rows": "2:100",
        "height": 18
      }
    ]
  }
}
```

### プレゼンテーションレイアウト
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/presentation.xlsx",
    "sheet_name": "Summary",
    "operations": [
      {
        "operation": "hide_columns",
        "columns": "B:C"
      },
      {
        "operation": "hide_rows",
        "rows": "10:15"
      },
      {
        "operation": "set_column_width",
        "columns": "A",
        "width": 30
      },
      {
        "operation": "set_column_width",
        "columns": "D:G",
        "width": 15
      }
    ]
  }
}
```

## 測定ガイドライン

### 行の高さ（ポイント）
- `15` - 標準の行の高さ
- `20` - 読みやすさのためのやや高め
- `25` - 見出しに適したサイズ
- `30` - 大きめの見出し
- `40` - タイトル用の超大サイズ

### 列幅（文字数）
- `8` - 細い列（日付、コード）
- `12` - 標準的なデータ列
- `15` - 中くらいのテキスト列
- `20` - 幅広のテキスト列
- `25` - 説明用の超広列
- `30` - 長いテキスト用の非常に広い列

## ベストプラクティス

1. **見出しのサイズ**: 強調のために見出しを高く、広く設定
2. **データの一貫性**: データ行は一貫した行高を使用
3. **自動調整**: 動的コンテンツのサイズ調整には自動フィットを使用
4. **未使用の部分を隠す**: 空の行や列は隠して見た目をすっきりさせる
5. **論理的なグループ化**: 関連するリサイズ操作をバッチ処理

## 一般的なパターン

### レポート設定パターン
1. タイトル行を上部に挿入
2. 見出し行の高さを設定
3. データ列を自動調整
4. 標準のデータ行高さを設定
5. 使用していない領域を非表示

### データインポートパターン
1. 新しいデータのために行を挿入
2. 内容に合わせて列を自動調整
3. 行の高さを標準化
4. 計算列を非表示

### プレゼンテーションパターン
1. 詳細行/列を非表示
2. 要約領域を拡大
3. プレゼンテーションに適したサイズを設定
4. 関連するデータのみを表示

## エラー処理

### 無効な行範囲
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1", 
    "operation": "set_row_height",
    "rows": "0",
    "height": 20
  }
}
```
**結果**: エラー - 行番号は1から始まります

### 無効な列範囲
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "operation": "set_column_width", 
    "columns": "ZZ",
    "width": 10
  }
}
```
**結果**: 成功する可能性あり、しかし一般的な用途範囲外

### 必須パラメータが欠落しています
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "operation": "set_row_height",
    "rows": "1"
  }
}
```
**結果**: エラー - 高さパラメータが必要です 
{{< app/cells/assistant language="nodejs-cpp" >}}
