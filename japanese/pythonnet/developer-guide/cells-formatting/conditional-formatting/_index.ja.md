---
title: Excel および ODS ファイルの条件付き書式を設定する。
linktitle: 条件付き書式
type: docs
weight: 60
url: /ja/python-net/conditional-formatting/
description: PythonでExcelとODSファイルに条件付き書式を適用する方法。
keywords: 条件付き書式の適用 
---

## **紹介**

条件付き書式は、Microsoft Excel の高度な機能で、セルやセル範囲に書式を適用し、その値や数式に応じて書式を変更することができます。たとえば、セルの値が 500 より大きいときにのみ太字にすることができます。セルの値が条件を満たした場合、指定された書式が適用されます。セルの値が書式条件を満たさない場合は、セルのデフォルトの書式が使用されます。Microsoft Excel では、**書式**、**条件付き書式** を選択して、条件付き書式ダイアログを開きます。

Aspose.Cells for Python via .NET は、セルに条件付き書式をランタイムで適用することをサポートしています。詳しく説明します。また、Excelが色スケール条件付き書式に使用する色の計算方法も解説します。

## **条件付き書式の適用**

Aspose.Cells for Python via .NET は、いくつかの方法で条件付き書式をサポートしています：

- デザイナー スプレッドシートを使用
- コピー メソッドを使用
- 実行時に条件付き書式を作成

### **デザイナー スプレッドシートを使用**

開発者は、Microsoft Excelに条件付き書式を含むデザイナースプレッドシートを作成し、その後Aspose.Cells for Python via .NETで開きます。Aspose.Cells for Python via .NETは、そのデザイナースプレッドシートを読み込み、保存し、条件付き書式設定を保持します。

### **コピー メソッドを使用**

Aspose.Cells for Python via .NET は、開発者がワークシート内のセル間で条件付き書式設定をコピーできるように、[**Range.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy)メソッドを提供します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UsingCopyMethod-1.py" >}}

## **ランタイムで条件付き書式を適用**

Aspose.Cells for Python via .NET では、実行時に条件付き書式を追加および削除できます。以下のコード例は、条件付き書式を設定する方法を示しています：

1. ワークブックをインスタンス化してください。
1. 空の条件付き書式を追加してください。
1. 書式を適用する範囲を設定してください。
1. 書式の条件を定義してください。
1. ファイルを保存します。

この後に、フォント設定や罫線設定、パターン設定などの他の小さな例が続きます。

Microsoft Excel 2007は、より高度な条件付き書式を追加しており、Aspose.Cells for Python via .NETもこれをサポートしています。ここでの例は、シンプルな書式設定の使用方法を示し、Microsoft Excel 2007の例ではより高度な条件付き書式の適用方法を示しています。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConditionalFormattingatRuntime-1.py" >}}

### **フォントの設定**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SettingFontStyle-1.py" >}}

{{% alert color="primary" %}}

フォントスタイル、テキストの色、下線スタイル、取り消し線スタイルのみを変更できます。

{{% /alert %}}

### **境界線の設定**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetBorder-1.py" >}}

{{% alert color="primary" %}}

アウトライン境界線には細い線スタイルのみを使用できます。対角線は許可されていません。

{{% /alert %}}

### **パターンの設定**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetPattern-1.py" >}}

## **高度なトピック**
- [2色系規則と3色系規則の条件付き書式設定を追加する](/cells/ja/python-net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [ワークシートで条件付き書式設定を適用する](/cells/ja/python-net/apply-conditional-formatting-in-worksheets/)
- [条件付き書式設定を使用して、交互に行と列に影を付ける](/cells/ja/python-net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [条件付き書式データバーイメージの生成](/cells/ja/python-net/generate-conditional-formatting-databars-images/)
- [条件付き書式で使用されるアイコンセット、データバー、またはカラースケールオブジェクトの取得](/cells/ja/python-net/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)

{{< app/cells/assistant language="csharp" >}}
{{< app/cells/assistant language="python-net" >}}
