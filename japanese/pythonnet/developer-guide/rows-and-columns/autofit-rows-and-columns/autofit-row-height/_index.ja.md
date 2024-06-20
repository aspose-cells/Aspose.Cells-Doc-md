---
title: Excel ファイルを読み込む際に自動的に行の高さを調整する
type: docs
weight: 120
url: /ja/python-net/autofit-row-height/
description: Aspose.Cells for Python via .NET API を使用してカスタムされていない高さの行を自動的に調整する方法を学ぶ。
keywords: Python Excel ライブラリ、Python ファイルを開いて行の高さを自動的に合わせる、Python ファイルを開くと行の高さが自動的に調整される。 
---

## **可能な使用シナリオ**
行の高さは自動的にコンテンツのフォントに合わせられますが、キャッシュされた行の高さがファイル内のコンテンツの高さと一致しない場合、MS Excel はファイルをロードする際に行の高さを自動的に調整しますが、Aspose.Cells for Python via .NET はパフォーマンスを向上させるために自動的に調整しません。Aspose.Cells for Python via .NET プログラムを使用してファイルをロードする際に行の高さを自動的に一致させる必要がある場合は、[LoadOptions.AutoFitterOptions.only_auto](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/only_auto/) パラメータを使用して、この目標を達成できます。

次の画像データを参照してください。 行11のキャッシュ行の高さは15であることがわかりますが、Excel はファイルを読み込む際に行の高さを自動的に調整しました。
<br>
<img src="1.png" width=70% />

## **Aspose.Cells for Python Excel ライブラリを使用して行の高さを調整する方法**
ファイルを直接読み込んで PDF に保存すると、キャッシュ行の高さが15であるため、PDF にデータが完全に表示されません。
<br>
<img src="2.png" width=70% />
<br>
ファイルを読み込む際に、[LoadOptions.AutoFitterOptions.only_auto](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/only_auto/) パラメータを true に設定すると、Aspose.Cells for Python via .NET は行の高さを自動的に調整します。調整された行の高さはテキストの表示要件を効果的に満たすことができます。
<br>
<img src="3.png" width=70% />

## **Python サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Rows-autofit-row-height.py" >}}
