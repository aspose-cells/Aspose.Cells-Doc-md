---
title: AI搭載機能
type: docs
weight: 200
url: /ja/net/ai-powered-features/
keywords: AI、スプレッドシート、AI機能、AIの力、Excel AI、OpenAI、Cells AI。
description: この記事は、スプレッドシートファイルの処理にAI搭載機能を使用するためのステップバイステップガイドです。
---


# 新規ユーザーガイド：Cells AIの操作方法

セルAIへようこそ！このガイドでは、セルAIライブラリの設定と使用の基本ステップをご案内します。

## 目次
1. [AIモデルの設定](#configure-ai-model)
2. [AIインスタンスの作成](#create-ai-instance)
3. [AIによるファイル処理](#process-files-with-ai)
4. [プロキシ設定の利用](#use-proxy-settings-if-you-can-not-access-the-ai-server-directly)

---

## Prerequisites

Before using Cells AI, ensure you have the following:
- A valid **API Key** from OpenAI or the other AI provider of your choice.
- A .NET development environment set up for C# programming.

## Configure AI Model

To start using Cells AI, you need to set up an AI model. You can either create a new model or use one of the predefined models.

### Example:
#### Setup a new AI model
```csharp
Config.Model = new Model("gpt-4-32k");
```
#### 既定のAIモデルを使用
```csharp
Config.Model = Model.Gpt4OMini;
```

## AIインスタンスの作成

セルAIのインスタンスを初期化するには、APIルートURLとAPIキーを入力してください。必要に応じて完全なAPI URLも提供できます。

### 例：
#### AIチャットルートURLで初期化
```csharp
String APIKey = "sk-xxxxx";
String APIRootUrl = "https://api.openai.com/";
CellsAI cellsAI = new CellsAI(APIRootUrl, APIKey);
```
#### AIチャット完全URLで初期化
```csharp
String APIKey = "sk-xxxxx";
String FullAPIRootUrl = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions";
CellsAI cellsAI = new CellsAI(FullAPIRootUrl, true, APIKey);
```

## AIによるファイル処理

AIモデルを設定し、AIインスタンスを作成したら、スプレッドシートファイルの処理に使用できます。

### スプレッドシートを要約：
#### スプレッドシートの概要を取得する
```csharp
// Get summary of the spreadsheet
string summary = cellsAI.SpreadsheetSummarize("c:/student.xlsx");
```

#### 要約をTextWriterに出力することも可能です：
```csharp
// Use TextWriter way, Output summary to a TextWriter (Console)
TextWriter writer = Console.Out;
await cellsAI.SpreadsheetSummarize("c:/student.xlsx", writer);
```
### スプレッドシートに関する質問をする：
#### スプレッドシートの内容について質問できます：
```csharp
// Ask a question about the spreadsheet
await cellsAI.SpreadsheetQuestion("c:/student.xlsx", "Who is the best student?", writer);
```
### ユーザリクエストに基づいてスプレッドシートを作成：
#### 例：

特定のリクエストに基づき新しいスプレッドシートを作成できます。たとえば、週間の食事プランを生成するなど：
```csharp
await cellsAI.BuildSpreadsheet("Provide weekly daily three-meal recipes, including nutritional value, preparation methods, ingredients, and cost, one day per row, and add total cost at last row.", null, "c:/foodsweekly.xlsx");
```

または、過去のデータを基に売上予測を行うことも可能です：

```csharp
await cellsAI.BuildSpreadsheet("Based on the sales history data from row 3 to row 10, predict the sales situation for the next year. Add it in row 11.", "c:/Sales Report Year.xlsx", "c:/Sales Report Forcast.xlsx");

```
または、生徒のスコアをランキング付きで更新する：
```csharp
await cellsAI.BuildSpreadsheet("Add a new column named \"Ranking\" and fill in the content of this column based on the students' total scores ranking", "c:\\student_score.xlsx", "c:\\student_score_with_rank.xlsx");
```
ローカライズされたリクエストでAIモデルを使用する：

AlibabaのQianwen AIモデルや他のローカライズされたAIモデルを使用できます。ロケールを指定する方法は以下の通りです：
```csharp
// Set to use QwenPlus AI model
Config.Model = Model.QwenPlus;
// Set locale info (e.g., Chinese)
Config.Locale = "zh";

// User request in Chinese
string userRequest = "增加新的一列,列名称是\"排名\" 并根据学生的总分大小排名填入这一列的内容";
string outfile = "D:\\学生排行.xlsx";
string inputfile = "D:\\student_score_zh.xlsx";
await cellsAI.BuildSpreadsheet(userRequest, inputfile, outfile);

```

### Excelの数式の取得：
#### スプレッドシートから直接Excelの数式をクエリできます：
```csharp
// Get formula from the spreadsheet
string formula = cellsAI.GetExcelFormula("c:/student.xlsx", "get the total score for Xiaomin");
```
## AIサーバーに直接アクセスできない場合はプロキシ設定を使用してください

プロキシの背後で作業している場合は、Cells AIがサーバーに接続できるようにプロキシ設定を構成できます。

```csharp
// Set up proxy for Cells AI
string proxyAddress = "http://127.0.0.1:58591";
WebProxy proxy = new WebProxy(proxyAddress)
{
    BypassProxyOnLocal = false,  
    UseDefaultCredentials = false,
};

// Apply the proxy setting
cellsAI.Proxy = proxy;
```

## 追加機能とカスタマイズ
Cells AIは、AIモデルの調整、ロケール設定、データ出力の修正など、さまざまなカスタマイズを可能にします。APIを探索し、特定のユースケースに合わせて異なる設定を試してみてください。

## 結論
Cells AIは、スプレッドシートの処理、自動化、AIの活用を可能にし、Excelベースのアプリケーションに役立ちます。  

詳細については、 [APIドキュメント](https://reference.aspose.com/cells/net/aspose.cells.ai/) または [サポートフォーラム](https://forum.aspose.com/c/cells/9) を参照してください。

ハッピーコーディング！
