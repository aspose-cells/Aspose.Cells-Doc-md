---
title: 余白の設定
type: docs
weight: 20
url: /ja/net/setting-margins/
description: この記事では、サンプル コードを使用して Excel ワークシートの余白を設定する方法を説明します。また、C# API または .NET ライブラリを使用して、ページ設定のページ中央の余白、ヘッダーおよびフッターの余白をプログラムで設定する方法も学習します。
keywords: set excel worksheet margin to center c#, set worksheet header and footer margin c#
---
{{% alert color="primary" %}}

Aspose.Cells は、Microsoft Excel のページ設定オプションを完全にサポートしています。開発者は、印刷プロセスを制御するためにワークシートのページ設定を構成する必要がある場合があります。このトピックでは、Aspose.Cells を使用してページ余白を構成する方法について説明します。

{{% /alert %}}

##  **余白の設定**

 Aspose.Cells はクラスを提供します。[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 、Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスに含まれるのは[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートへのアクセスを許可するコレクション。ワークシートは次のように表されます。[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。

の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスが提供するのは、[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)ワークシートのページ設定オプションを設定するために使用されるプロパティ。の[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)属性はのオブジェクトです[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)開発者が印刷されたワークシートにさまざまなページ レイアウト オプションを設定できるようにするクラス。の[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)クラスは、ページ設定オプションを設定するために使用されるさまざまなプロパティとメソッドを提供します。

###  **ページ余白**

ページの余白 (左、右、上、下) を設定するには、次のコマンドを使用します。[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)クラスのメンバー。ページ余白を指定するために使用されるメソッドのいくつかを以下に示します。

- [**左マージン**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/leftmargin)
- [**右マージン**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/rightmargin)
- [**トップマージン**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/topmargin)
- [**ボトムマージン**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/bottommargin)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-1.cs" >}}

###  **ページの中央**

ページ上で水平方向および垂直方向に何かを中央に配置することができます。このために、次の便利なメンバーがいます。[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)クラス、[**水平方向に中央揃え**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centerhorizontally)と[**垂直中央に配置**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centervertically).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.cs" >}}

###  **ヘッダーとフッターの余白**

ヘッダーとフッターの余白を設定します。[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)クラスのメンバーなど[**ヘッダマージン**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/headermargin)と[**フッターマージン**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/footermargin).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.cs" >}}
