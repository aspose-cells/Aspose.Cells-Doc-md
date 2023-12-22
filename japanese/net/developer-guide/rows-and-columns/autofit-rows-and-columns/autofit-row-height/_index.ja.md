---
title: ファイルのロード時に行の高さを自動的に調整する AutoFit
type: docs
weight: 120
url: /ja/net/autofit-row-height/
description: 高さがカスタマイズされていない行を調整する方法を学びます。
keywords: AutoFit Row Height when loading file, automatically adjust the row height when opening excel file. 
---
##  **考えられる使用シナリオ**
行の高さはコンテンツのフォントと自動的に一致しますが、キャッシュされた行の高さがファイル内のコンテンツの高さと一致しない場合、MS Excel はファイルのロード時に行の高さを自動的に調整しますが、Aspose.Cells は調整しません。パフォーマンスを向上させるために自動的に調整されます。ファイルをロードするときに行の高さを自動的に一致させるために Aspose.Cells プログラムを使用する必要がある場合は、パラメーターを使用して目的を達成できます。[LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/).

以下の画像データをご参照ください。 11 行目のキャッシュ行の高さは 15 であることがわかりますが、ファイルの読み込み時に Excel が行の高さを自動的に調整しました。
<br>
<img src="1.png" width=70% />

##  **Aspose.Cellsを使用して行の高さを調整します**
ファイルを直接ロードして PDF に保存すると、キャッシュ ラインの高さが 15 しかないため、データは PDF に完全に表示されません。
<br>
<img src="2.png" width=70% />
<br>
パラメータを設定すると[LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/)ファイルをロードするときに true に設定すると、Aspose.Cells は行の高さを自動的に調整します。調整された行の高さは、テキスト表示要件を効果的に満たすことができます。
<br>
<img src="3.png" width=70% />

##  **C# サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rows-autofit-row-height.cs" >}}