---
title: Excel フォントとテキストの書式設定
linktitle: フォントとテキストの書式設定
type: docs
weight: 30
url: /ja/nodejs-cpp/mcp/font-formatting
keywords: "Excelのフォント書式設定、Excelのテキスト書式設定、Excelのフォント設定、AIによるExcelフォントスタイリング、Excelフォントの自動化"
description: "Excelのフォントとテキストの書式設定  フォントスタイル、色、サイズ、およびテキスト効果をAI自動化で適用"
---

# Excelフォントとテキスト書式設定

AIによる自動化を備えた**Excelフォント書式設定**を適用します。洗練されたスプレッドシートのために、フォント、色、サイズ、特殊効果で**Excelテキスト**をスタイル付けします。

## 利用可能なツール

- `font_settings` - **Excelフォントスタイリング**（フォント、サイズ、太字、斜体、色など）を**AI Excel**の正確さで設定
- `font_settings_batch` - **Excelフォント設定**を複数の範囲に一括適用する**スプレッドシートMCP**

## 単一フォント操作

### 基本フォントスタイリング
```json
{
  "tool": "font_settings",
  "parameters": {
    "filepath": "reports/styled-report.xlsx",
    "sheet_name": "Data",
    "range": "A1:F1",
    "font_name": "Arial",
    "font_size": 14,
    "bold": true,
    "font_color": "#FFFFFF"
  }
}
```

### テキスト効果
```json
{
  "tool": "font_settings",
  "parameters": {
    "filepath": "reports/effects-demo.xlsx",
    "sheet_name": "Sheet1",
    "range": "A2",
    "italic": true,
    "underline": true,
    "strikethrough": true,
    "font_color": "#FF0000"
  }
}
```

### 特殊文字
```json
{
  "tool": "font_settings",
  "parameters": {
    "filepath": "reports/scientific.xlsx",
    "sheet_name": "Formulas",
    "range": "A3",
    "font_size": 10,
    "subscript": true
  }
}
```

## バッチフォント操作

### 見出しの完全なスタイリング
```json
{
  "tool": "font_settings_batch",
  "parameters": {
    "filepath": "reports/professional-report.xlsx",
    "sheet_name": "Summary Report",
    "font_ranges": [
      {
        "range": "C3:G3",
        "font_name": "Arial Black",
        "font_size": 16,
        "bold": true,
        "italic": true,
        "underline": true,
        "font_color": "#FF0000"
      },
      {
        "range": "D4:D6",
        "font_name": "Calibri",
        "font_size": 12,
        "bold": true,
        "font_color": "#0066CC"
      },
      {
        "range": "E4:E6",
        "font_name": "Times New Roman",
        "italic": true,
        "font_color": "#006600"
      }
    ]
  }
}
```

### 特殊テキスト効果の紹介
```json
{
  "tool": "font_settings_batch",
  "parameters": {
    "filepath": "reports/text-effects.xlsx",
    "sheet_name": "Effects Demo",
    "font_ranges": [
      {
        "range": "A3",
        "font_size": 10,
        "subscript": true
      },
      {
        "range": "B3",
        "font_size": 10,
        "superscript": true
      },
      {
        "range": "C3",
        "strikethrough": true,
        "underline": true,
        "font_color": "#CC0000"
      }
    ]
  }
}
```

### プロフェッショナルレポートのスタイリング
```json
{
  "tool": "font_settings_batch",
  "parameters": {
    "filepath": "reports/financial-report.xlsx",
    "sheet_name": "Sheet1",
    "font_ranges": [
      {
        "range": "A1:F1",
        "font_name": "Arial",
        "font_size": 14,
        "bold": true,
        "font_color": "#FFFFFF"
      },
      {
        "range": "A5:F5",
        "bold": true,
        "font_size": 12
      },
      {
        "range": "F2:F5",
        "bold": true,
        "font_color": "#006600"
      }
    ]
  }
}
```

## フォントパラメータリファレンス

### フォントファミリー
- `"Arial"` - クリーンでモダンなサンセリフ体
- `"Calibri"` - Microsoft Officeのデフォルト
- `"Times New Roman"` - 伝統的なセリフ体
- `"Arial Black"` - 太字のディスプレイフォント
- `"Courier New"` - 等幅フォント

### フォントサイズ
- `8` - とても小さな文字
- `10` - 小さな文字
- `11` - デフォルトサイズ
- `12` - 標準本文
- `14` - 大きい文字
- `16` - 見出しサイズ
- `18` - 大きな見出し

### フォントカラー（16進数コード）
- `"#000000"` - 黒
- `"#FFFFFF"` - 白
- `"#FF0000"` - 赤
- `"#0066CC"` - 青
- `"#006600"` - 緑
- `"#FF6600"` - オレンジ
- `"#800080"` - 紫

### テキスト効果
- `bold: true` - 太字
- `italic: true` - 斜体
- `underline: true` - 下線付き
- `strikethrough: true` - 刪除線
- `subscript: true` - 添字（H₂O）
- `superscript: true` - 上付き（x²）

## 高度なフォントスタイリング

### 科学的表記の例
```json
{
  "tool": "font_settings_batch",
  "parameters": {
    "filepath": "reports/scientific.xlsx",
    "sheet_name": "Formulas",
    "font_ranges": [
      {
        "range": "A1",
        "font_name": "Times New Roman",
        "font_size": 12,
        "bold": true
      },
      {
        "range": "B1",
        "font_size": 10,
        "subscript": true
      },
      {
        "range": "C1",
        "font_size": 10,
        "superscript": true
      }
    ]
  }
}
```

### 色分けされたデータ
```json
{
  "tool": "font_settings_batch",
  "parameters": {
    "filepath": "reports/color-coded.xlsx",
    "sheet_name": "Status Report",
    "font_ranges": [
      {
        "range": "A2:A5",
        "font_color": "#008000",
        "bold": true
      },
      {
        "range": "B2:B5",
        "font_color": "#FF8C00",
        "italic": true
      },
      {
        "range": "C2:C5",
        "font_color": "#DC143C",
        "strikethrough": true
      }
    ]
  }
}
```

## ベストプラクティス

1. **一貫性**：レポート全体で同じフォントファミリーを使用
2. **階層構造**：フォントサイズを使って視覚的な階層を作成
3. **読みやすさ**：文字と背景のコントラストを十分に確保
4. **効果**：強調のためにテキスト効果を控えめに使用
5. **専門性**：レポートには標準的なビジネスフォントを使用

## 一般的な用途

### レポートヘッダー
- 太字、大きなフォントサイズ
- 対比のある色
- プロフェッショナルなフォントファミリー

### データの強調
- 重要な値には太字または斜体を使用
- ステータス指標に色分けを使用
- 廃止されたデータには取り消し線を使用

### 科学的文書
- 化学式には下付き文字を使用
- 数学式のための上付き文字
- コードやデータのためのモノスペース

## エラー処理

### 無効なフォントファミリー
```json
{
  "tool": "font_settings",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "range": "A1",
    "font_name": "NonExistentFont"
  }
}
```
**結果**: デフォルトのシステムフォントにフォールバック

### 無効なカラーコード
```json
{
  "tool": "font_settings",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "range": "A1",
    "font_color": "invalid-color"
  }
}
```
**結果**: デフォルトの黒色を使用 
{{< app/cells/assistant language="nodejs-cpp" >}}
