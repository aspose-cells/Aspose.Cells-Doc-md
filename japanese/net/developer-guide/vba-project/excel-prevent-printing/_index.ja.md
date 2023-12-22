---
title: ユーザーが Excel ファイルを印刷できないようにする方法
type: docs
weight: 600
url: /ja/net/how-to-prevent-printing-excel/
description: ユーザーが Aspose.Cells for .NET API を通じて Excel を印刷できないようにする方法について説明します。
keywords: excel printing, prevent printing excel, how to prevent users from printing excel, excel prevent printing, prevent printing workbook, Prevent users from printing the whole workbook with VBA. 
---
##  **考えられる使用シナリオ**
私たちの日常業務では、Excel ファイルに重要な情報が含まれている場合がありますが、社内データの拡散を保護するために、会社はそれらを印刷することを許可していません。この文書では、他の人が Excel ファイルを印刷できないようにする方法について説明します。

##  **ユーザーが MS-Excel でファイルを印刷できないようにする方法**
次の VBA コードを適用して、印刷する特定のファイルを保護できます。
1. 他の人に印刷を許可していないワークブックを開きます。
1. Excel リボンの [開発者] タブを選択し、[コントロール] セクションの [コードの表示] ボタンをクリックします。または、ALT + F11 キーを押したままにして、Microsoft Visual Basic for Applications ウィンドウを開くこともできます。
<br>
<img src="1.png" width=70% />
1. 次に、左側のプロジェクト エクスプローラーで ThisWorkbook をダブルクリックしてモジュールを開き、いくつかの VBA コードを追加します。
<br>
<img src="2.png" width=70% />
1. 次に、このコードを保存して閉じ、ワークブックに戻り、サンプル ファイルを印刷すると、印刷が許可されず、次の警告ボックスが表示されます。
<br>
<img src="3.png" width=70% />

##  **ユーザーが Aspose.Cells for .NET を使用して Excel ファイルを印刷できないようにする方法**

次のサンプル コードは、ユーザーが Excel ファイルを印刷できないようにする方法を示しています。

1. をロードします[サンプルファイル](sample.xlsx).
1. Workbook の VbaProject プロパティから VbaModuleCollection オブジェクトを取得します。
1. 「ThisWorkbook」名を使用して VbaModule オブジェクトを取得します。
1. VbaModuleのcodesプロパティを設定します。
1. サンプルファイルを次の場所に保存します[xlsm形式](out.xlsm).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "VBA-Prevent-printing-excel.cs" >}}