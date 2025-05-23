---
title: X軸 vs カテゴリ軸
description: Aspose.Cells for Python via .NETでX軸とカテゴリ軸の違いを理解する方法を学習します。ガイドでは、使い方やプロパティの違い、設定方法について解説します。
keywords: Aspose.Cells for Python via .NET、X軸、カテゴリ軸、違い、用途、プロパティ、設定。
type: docs
weight: 180
url: /ja/python-net/X-axis-vs-category-axis/
---

## **可能な使用シナリオ**
X軸には異なるタイプがあります。Y軸が値タイプの軸であるのに対し、X軸はカテゴリタイプの軸または値タイプの軸であることができます。値軸を使用すると、データは連続的に変化する数値データとして扱われ、マーカーは数値に応じて軸上の位置に配置されます。カテゴリ軸を使用すると、データは数値ではないテキストラベルの連続として扱われ、マーカーはシーケンス内の位置に応じて軸上の位置に配置されます。以下のサンプルは、値軸とカテゴリ軸の違いを示しています。
サンプルデータは以下の[サンプルテーブルファイル](sample.png)で表示されています。最初の列にはX軸データが含まれており、これはカテゴリまたは値として扱うことができます。数字は等間隔ではなく、数値の順序に従っているわけでもありません。

![todo:image_alt_text](sample.png)

## **Microsoft ExcelのようにX軸とカテゴリ軸を処理する**
このデータを2種類のチャートで表示します。最初のチャートはXY（散布）チャートでXを値軸とし、次のチャートはラインチャートでXをカテゴリ軸とします。

![todo:image_alt_text](compare.png)
## **サンプルコード**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-X-axis-vs-category-axis.py" >}}
