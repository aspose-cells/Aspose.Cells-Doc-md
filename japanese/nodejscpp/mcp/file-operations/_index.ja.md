---
title: Excelファイルとデータ操作
linktitle: ファイルとデータ操作
type: docs
weight: 10
url: /ja/nodejs-cpp/mcp/file-operations
keywords: "Excelファイル操作、Excelデータ操作、Excelブック作成、Excelワークシート、Excelデータ読み取り、Excelデータ書き込み"
description: "Excelファイルとデータ操作  ブック作成、ワークシート管理、AI自動化によるExcelデータの読み取りと書き込み"
---

# Excelファイルとデータ操作

AI搭載の自動化を利用して**Excelファイル**と**データ操作**を管理します。**Excelブック**の作成、**ワークシート**の管理、および**Excelデータ**の読み書きを行います。

## 利用可能なツール

- `create_workbook` - **AI Excel**自動化を用いた新しい**Excelブック**の作成
- `create_worksheet` - 既存の**Excelブック**に**Excelワークシート**を追加
- `get_workbook_info` - **Excelブック**のメタデータと情報取得
- `read_data_from_excel` - **AI搭載**の精度で**Excelワークシート**からデータを読み取り
- `write_data_to_excel` - **Excel MCP**を通じて**Excelワークシート**にデータを書き込み

## Excelブックの作成

### 基本的なブック作成
```json
{
  "tool": "create_workbook",
  "parameters": {
    "filepath": "reports/sales-report.xlsx"
  }
}
```

### カスタムシート付きブック作成
```json
{
  "tool": "create_workbook",
  "parameters": {
    "filepath": "reports/financial-report.xlsx",
    "sheet_name": "Financial Data"
  }
}
```

## ワークシートの管理

### 新しいワークシートの追加
```json
{
  "tool": "create_worksheet",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Summary Report"
  }
}
```

### ブック情報の取得
```json
{
  "tool": "get_workbook_info",
  "parameters": {
    "filepath": "reports/sales-report.xlsx"
  }
}
```

## Excelデータの書き込み

### ヘッダーとデータの書き込み
```json
{
  "tool": "write_data_to_excel",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Sales Data",
    "data": [
      ["Product", "Category", "Unit Price", "Quantity", "Total", "Status"],
      ["Laptop Pro", "Electronics", 1299.99, 5, "", "In Stock"],
      ["Wireless Mouse", "Electronics", 89.99, 15, "", "In Stock"],
      ["Office Chair", "Furniture", 299.99, 8, "", "Low Stock"]
    ]
  }
}
```

### カスタム位置にデータを書き込みます
```json
{
  "tool": "write_data_to_excel",
  "parameters": {
    "filepath": "reports/analysis.xlsx",
    "sheet_name": "Data Analysis",
    "start_cell": "C3",
    "data": [
      ["Name", "Score", "Grade", "Double Score", "Bonus"],
      ["Alice", 95, "A", "", ""],
      ["Bob", 87, "B", "", ""],
      ["Charlie", 92, "A", "", ""]
    ]
  }
}
```

## Excelデータを読む

### 使用範囲を全て読む
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Sales Data"
  }
}
```

### 特定の範囲を読む
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/analysis.xlsx",
    "sheet_name": "Data Analysis",
    "start_cell": "C3",
    "end_cell": "G6"
  }
}
```

### デフォルト位置から読む
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/basic-data.xlsx",
    "sheet_name": "Sheet1",
    "start_cell": "A1"
  }
}
```

## 完全なワークフロー例

### 1. 最初のExcelレポートを作成
```json
{
  "tool": "create_workbook",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Monthly Sales"
  }
}
```

### 2. サマリーシートを追加
```json
{
  "tool": "create_worksheet",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Summary"
  }
}
```

### 3. 販売データを書き込み
```json
{
  "tool": "write_data_to_excel",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Monthly Sales",
    "data": [
      ["Month", "Product", "Sales", "Target", "Variance"],
      ["January", "Product A", 5000, 4500, ""],
      ["January", "Product B", 3200, 3000, ""],
      ["February", "Product A", 5500, 4500, ""],
      ["February", "Product B", 3400, 3000, ""]
    ]
  }
}
```

### 4. データを検証
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Monthly Sales",
    "start_cell": "A1",
    "end_cell": "E5"
  }
}
```

### 5. ワークブックの構造を確認
```json
{
  "tool": "get_workbook_info",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx"
  }
}
```

## ベストプラクティス

1. **ファイルパス**: 相対パスを使用してポータビリティを向上させる
2. **シート名**: 説明的な名前を使用する
3. **データ構造**: 明確なヘッダーでデータを整理する
4. **範囲の読み取り**: 大きなデータセットには範囲を指定する
5. **エラー処理**: 操作前にファイルの存在を確認する

## 一般的なパターン

### データインポートパターン
1. ワークブックを作成
2. 生データの入力
3. 確認のために読み戻す
4. 数式で処理する

### 複数シートのレポート
1. メインシートを含むブックを作成
2. 集計/分析シートを追加
3. 各シートにデータを書き込み
4. 数式でシートをリンク

### データ検証
1. データを書き込む
2. 特定範囲を読み戻す
3. データの整合性を検証する
4. 欠損値に対処する 
{{< app/cells/assistant language="nodejs-cpp" >}}
