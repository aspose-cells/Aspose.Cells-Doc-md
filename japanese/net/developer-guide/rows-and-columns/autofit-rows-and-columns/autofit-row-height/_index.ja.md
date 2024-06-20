---
title: Excel ファイルを読み込む際に自動的に行の高さを調整する
type: docs
weight: 120
url: /ja/net/autofit-row-height/
description: 高さがカスタム設定されていない行を自動的に調整する方法を学ぶ
keywords: ファイルを読み込むと行の高さが自動的にコンテンツのフォントに一致しますが、キャッシュされた行の高さがファイルのコンテンツの高さと一致しない場合、MS Excel はファイルを読み込む際に行の高さを自動的に調整しますが、Aspose.Cells はパフォーマンスを向上させるために自動的には調整しません。 Aspose.Cells プログラムを使用してファイルを読み込む際に行の高さを自動的に一致させる必要がある場合は、[LoadOptions.AutoFitterOptions.OnlyAuto](https //reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/) パラメータを使用して目標を達成できます。 
---

## **可能な使用シナリオ**
行の高さはコンテンツのフォントに自動的に合わせられますが、キャッシュされた行の高さがファイルの内容の高さに合っていない場合、MS Excelはファイルをロードする際に自動的に行の高さを調整しますが、Aspose.Cellsは、パフォーマンスを向上させるために自動的に調整しません。ファイルをロードするときにAspose.Cellsプログラムが行の高さを自動的に合わせる必要がある場合は、パラメータ[LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/)を使用して目標を達成できます。

次の画像データを参照してください。 行11のキャッシュ行の高さは15であることがわかりますが、Excel はファイルを読み込む際に行の高さを自動的に調整しました。
<br>
<img src="1.png" width=70% />

## **Aspose.Cells を使用して行の高さを調整する**
ファイルを直接読み込んで PDF に保存すると、キャッシュ行の高さが15であるため、PDF にデータが完全に表示されません。
<br>
<img src="2.png" width=70% />
<br>
ファイルを読み込む際に [LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/) パラメータを true に設定すると、Aspose.Cells は行の高さを自動的に調整します。 調整された行の高さは、テキストの表示要件を効果的に満たすことができます。
<br>
<img src="3.png" width=70% />

## **C# サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rows-autofit-row-height.cs" >}}
