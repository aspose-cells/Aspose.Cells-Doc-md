---
title: マージンの設定
type: docs
weight: 20
url: /ja/net/setting-margins/
---
{{% alert color="primary" %}}

Aspose.Cells は Microsoft Excel のページ設定オプションを完全にサポートします。開発者は、印刷プロセスを制御するためにワークシートのページ設定を構成する必要がある場合があります。このトピックでは、Aspose.Cells を使用してページの余白を構成する方法について説明します。

{{% /alert %}}

## **マージンの設定**

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。

の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスが提供する[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)ワークシートのページ設定オプションを設定するために使用されるプロパティ。の[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)属性はのオブジェクトです[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)開発者が印刷ワークシートにさまざまなページ レイアウト オプションを設定できるようにするクラス。の[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)クラスは、ページ設定オプションを設定するために使用されるさまざまなプロパティとメソッドを提供します。

### **ページ余白**

を使用して、ページの余白 (左、右、上、下) を設定します。[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)クラスのメンバー。ページ余白を指定するために使用されるメソッドのいくつかを以下に示します。

- [**左余白**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/leftmargin)
- [**右余白**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/rightmargin)
- [**トップマージン**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/topmargin)
- [**下余白**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/bottommargin)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-1.cs" >}}

### **ページの中央に配置**

ページの水平方向と垂直方向の中央に何かを配置することができます。このために、いくつかの便利なメンバーがあります[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)クラス、[**中央水平**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centerhorizontally)と[**中央垂直**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centervertically).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.cs" >}}

### **ヘッダーとフッターの余白**

でヘッダーとフッターの余白を設定します[**ページ設定**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)などのクラスメンバー[**ヘッダーマージン**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/headermargin)と[**フッターマージン**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/footermargin).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.cs" >}}
