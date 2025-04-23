---
title: Excelファイルの印刷を防止する方法
type: docs
weight: 600
url: /ja/net/how-to-prevent-printing-excel/
description: Aspose.Cells for .NET APIを使用してExcelファイルの印刷を防止する方法を学びます。
keywords: excel印刷、excel印刷を防ぐ、Excelファイルの印刷を防ぐ方法、excel印刷を防ぐ、ブック全体の印刷を防ぐ、VBAでブック全体の印刷を防ぐ。 
---

## **可能な使用シナリオ**
日常業務では、Excelファイルに重要な情報が含まれていることがあります。内部データの流出を防ぐため、会社はそれらを印刷することを許可していません。このドキュメントでは、Excelファイルの印刷を他者に防止する方法について説明します。

## **MS-Excelでファイルの印刷を防ぐ方法**
指定したファイルを印刷できないようにするために、次のVBAコードを適用できます。
1. 印刷を許可しないブックを開きます。
1. Excelリボンの**開発**タブを選択し、「**コントロール**」セクションの「**View Code**」ボタンをクリックします。または、ALT + F11 キーを押して、**Microsoft Visual Basic for Applications**ウィンドウを開くことができます。
<br>
<img src="1.png" width=70% />
1. 左側のプロジェクトエクスプローラで**ThisWorkbook**をダブルクリックしてモジュールを開き、いくつかのVBAコードを追加します。
<br>
<img src="2.png" width=70% />
1. 保存してこのコードを閉じ、ブックに戻り、サンプルファイルを印刷すると、印刷することは許可されず、次の警告ボックスが表示されます。
<br>
<img src="3.png" width=70% />

## **Aspose.Cells for .NETを使用してExcelファイルの印刷を防止する方法**

次のサンプルコードは、Excelファイルの印刷を防止する方法を示しています:

1. [サンプルファイル](sample.xlsx)をロードする。
1. WorkbookのVbaProjectプロパティからVbaModuleCollectionオブジェクトを取得します。
1. "ThisWorkbook"名を使用してVbaModuleオブジェクトを取得します。
1. VbaModuleのcodesプロパティを設定します。
1. サンプルファイルを[xlsm形式](out.xlsm)で保存します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "VBA-Prevent-printing-excel.cs" >}}
{{< app/cells/assistant language="csharp" >}}
