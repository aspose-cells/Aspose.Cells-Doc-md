---
title: テーブルおよび範囲
type: docs
weight: 30
url: /ja/cpp/tables-and-ranges/
---

## **紹介**
Microsoft Excelでテーブルを作成し、それをそのままの機能で使用しない場合があります。代わりに、テーブルの機能を失わずに、テーブルのように見えるものが欲しいことがあります。フォーマットを維持するため、テーブルのデータを通常のデータ範囲に変換することができます。Aspose.Cellsは、テーブルとリストオブジェクトのためのこのMicrosoft Excelの機能をサポートしています。
## **Microsoft Excel の使用**
表をフォーマットを保持したまま範囲に素早く変換するには、**範囲に変換** 機能を使用します。Microsoft Excel 2007/2010では:

1. 表内のどこかをクリックして、アクティブなセルが表の列内にあることを確認します。
1. **デザイン** タブの **ツール** グループで、**範囲に変換** をクリックします。

{{% alert color="primary" %}} 

表を範囲に変換した後は、表の機能は利用できなくなります。たとえば、行ヘッダーにはソートとフィルターの矢印が含まれなくなり、数式で使用されたテーブル名を参照する構造化参照は通常のセル参照に変わります。

{{% /alert %}} 
## **Aspose.Cellsの使用**
次のコードスニペットは、Aspose.Cellsを使用して同じ機能を示しています。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-C-main-ConvertTableToRange-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
