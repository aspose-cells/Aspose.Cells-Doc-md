---
title: Excel XP 以降の高度な保護設定
type: docs
weight: 30
url: /ja/net/advanced-protection-settings-since-excel-xp/
---
{{% alert color="primary" %}}

Excel 2002 または XP のリリース以降、Microsoft には多くの高度な保護設定が追加されました。

{{% /alert %}}

## **序章**

これらの保護設定により、ユーザーは次のことが制限または許可されます。

- 行または列を削除します。
- コンテンツ、オブジェクト、またはシナリオを編集します。
- セル、行、または列をフォーマットします。
- 行、列、またはハイパーリンクを挿入します。
- ロックまたはロック解除されたセルを選択します。
- ピボット テーブルなどを使用します。

Aspose.Cells は、Excel XP 以降のバージョンで提供されるすべての高度な保護設定をサポートしています。

### **Excel XP 以降のバージョンを使用した高度な保護設定**

Excel XP で使用可能な保護設定を表示するには:

1. から**ツール**メニュー、選択**保護**に続く**プロテクトシート**.ダイアログが表示されます。

Excel 2016 で使用できる保護設定を表示するには

1. から**ファイル**メニュー、選択**ブックの保護**に続く**現在のシートを保護**.
1. を選択**プロテクトシート**の中に**レビュー**メニュー。

上記の手順に従うと、ワークシート機能を許可または制限したり、ワークシートにパスワードを適用したりできるダイアログが表示されます。

### **Aspose.Cells を使用した高度な保護設定**

Aspose.Cells は、すべての高度な保護設定をサポートしています。

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)Excel ファイル内の各ワークシートにアクセスできるコレクション。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。

の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスが提供する[**保護**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection)これらの高度な保護設定を適用するために使用されるプロパティ。の[**保護**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection)プロパティは実際にはのオブジェクトです[**保護**](https://reference.aspose.com/cells/net/aspose.cells/protection)制限を無効または有効にするためのいくつかのブール型プロパティをカプセル化するクラス。

以下は小さなアプリケーション例です。 Excel ファイルを開き、Excel XP 以降のバージョンでサポートされている高度な保護設定のほとんどを使用します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-AdvancedProtectionSettings-1.cs" >}}

{{% alert color="primary" %}}

に電話しないでください[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス'[**守る**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index)使用時の方法[**保護**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection)財産。また、高度な保護設定は Excel XP 以降のバージョンでのみサポートされているため、ファイルを Excel97To2003 または Xlsx 形式で保存してください。

{{% /alert %}}

### **Cell ロックの問題**

ユーザーによるセルの編集を制限する場合は、保護設定を適用する前にセルをロックする必要があります。そうしないと、ワークシートが保護されていてもセルを編集できます。 Microsoft Excel XP では、次のダイアログでセルをロックできます。

|**Excel XP でセルをロックするためのダイアログ**|
|:- |
|![todo:画像_代替_文章](advanced-protection-settings-since-excel-xp_1.png)|

Aspose.Cells API を使用してセルをロックすることもできます。各セルは得ることができます[**スタイル**](https://reference.aspose.com/cells/net/aspose.cells/style)ブール値のプロパティを含むフォーマット、[**ロックされています**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked).をセットする[**ロックされています**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)プロパティへ**真実**また**間違い**セルをロックまたはロック解除します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-LockCell-1.cs" >}}
