---
title: テキスト条件付き書式の追加方法
description: C#でAspose.Cellsライブラリを使用してテキスト条件付き書式を適用する方法。これらの基準を調整することで、セルの見た目や表示をより細かく制御できます。
keywords: Aspose.Cells、テキスト条件付き書式、C#、条件付き、書式設定
type: docs
weight: 70
url: /ja/net/how-to-add-text-conditional-formatting/
---

## **可能な使用シナリオ**
スプレッドシートでのテキストベースの条件付き書式は、特定のテキスト基準を満たすセルを強調表示するのに役立ちます。これにより、データ分析が向上し、大規模なデータセットから主要な情報を見つけやすくなります。テキスト条件付き書式を使用する理由は次のとおりです：

1. 特定のテキストをハイライト：特定の語句や文字列、文字に基づいて書式を適用できます。例："Urgent」や「Completed」などの単語を含むセルをハイライトして、タスクを簡単に区別できます。
1. パターンや傾向の識別："High"、"Medium"、"Low"などのカテゴリやステータスに基づいて作業の進捗や優先順位を視覚的に区別できます。
1. エラーやデータ入力の警告：誤字や未完成のテキスト、不正な値などの不一致や誤りを示すために書式を設定できます。多くのテキスト入力を含むデータセットに特に有効です。
1. 読みやすさの向上：テキストに色付けしたり、スタイルを変更したり（太字、イタリックなど）して、重要な情報を目立たせ、シート全体の可読性を向上させます。
1. 動的なフィードバック：特定の条件に一致したときに書式を自動的に調整するルールを設定できます。これにより、データの変更に応じて手動で書式を更新する必要がなくなります。

要するに、テキスト条件付き書式は、関連情報、エラー、トレンドを素早く把握できるため、テキストデータの管理と解釈に役立つ強力なツールです。

## **Excelを使用したテキスト条件付き書式の追加方法**
Excelに条件付き書式を追加するには、次の手順に従います：

1. セル範囲を選択：条件付き書式を適用したいセルをハイライトします。
1. 条件付き書式メニューを開く：Excelリボンのホームタブに移動します。「スタイル」グループの条件付き書式をクリックします。
1. 「新しいルール」を選択：ドロップダウンメニューから「新しいルール」を選びます。
1. 「セルの値を特定の条件で書式設定」を選択：新しい書式ルールダイアログで、「ルールの種類を選択してください」セクションの中から「セルの値を特定の条件で書式設定」を選びます。
1. ルールの条件を設定："セルを書式設定"セクションで、ドロップダウンから「特定のテキスト」を選択します。条件に応じて「含む」「始める」「終わる」を選び、書式設定したいテキスト（例：「Urgent」「Completed」など）を入力します。
1. 書式の選択：書式ボタンをクリックします。セルの書式設定ダイアログで、フォントの色、背景色、その他の書式オプションを選択できます。
1. ルールを適用：希望の書式を設定したら、「OK」をクリックしてルールを適用します。もう一度「OK」をクリックして新しい書式ルールダイアログを閉じます。
1. 結果を確認：指定したテキストを含むセルに書式が適用され、関連情報を簡単に見つけやすくなります。


## **「Aspose.Cells for .NET」を使用したテキスト条件付き書式の追加方法**

Aspose.Cellsは、Excel 2007以降の条件付き書式をXLSX形式のセル上でランタイムに完全にサポートします。これらの例は、「BeginsWith」「ContainsBlank」「ContainsText」などの高度な条件付き書式のタイプの練習例です。

### **指定されたテキストで始まる場合にセルの書式設定**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-BeginsWith.cs" >}}

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text.cs" >}}
### **空白を含む場合にセルの書式設定**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-ContainsBlank.cs" >}}

### **エラーを含む場合にセルの書式設定**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-ContainsErrors.cs" >}}

### **特定のテキストを含む場合にセルの書式設定**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-ContainsText.cs" >}}

### **重複する値を含む場合にセルの書式設定**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-DuplicateValues.cs" >}}

### **指定されたテキストで終わる場合にセルの書式設定**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-EndsWith.cs" >}}

### **空白を含まない場合にセルの書式設定**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-NotContainsBlank.cs" >}}

### **エラーを含まない場合にセルの書式設定**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-NotContainsErrors.cs" >}}

### **指定されたテキストを含まない場合にセルの書式設定**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-NotContainsText.cs" >}}

### **ユニークな値を含む場合にセルの書式設定**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-UniqueValues.cs" >}}

{{< app/cells/assistant language="csharp" >}}
