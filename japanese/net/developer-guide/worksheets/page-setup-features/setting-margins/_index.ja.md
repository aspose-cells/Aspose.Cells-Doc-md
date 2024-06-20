---
title: マージンの設定
type: docs
weight: 20
url: /ja/net/setting-margins/
description: この記事では、サンプルコードを使用してエクセルワークシートのマージンを設定する方法について学びます。C# API または .NET ライブラリを使用して、ページのセンター、ヘッダーとフッターマージンをプログラムで設定する方法も学びます。
keywords: C# の API や .NET ライブラリを使用して、{0} クラスのメンバーを使ってページのマージン（左、右、上、下）を設定します。ページマージンを指定するために使用されるいくつかのメソッドが以下にリストされています。
---

{{% alert color="primary" %}}

Aspose.CellsはMicrosoft Excelのページ設定オプションを完全にサポートしています。開発者は印刷プロセスを制御するためにワークシートのページ設定設定を構成する必要があります。このトピックでは、Aspose.Cellsを使用してページ余白を設定する方法について説明します。

{{% /alert %}}

## **マージンの設定**

Aspose.CellsにはExcelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)というクラスがあります。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)コレクションが含まれており、Excelファイルの各ワークシートにアクセスできます。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスで表されます。

[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスはワークシートのページ設定オプションを設定するために使用される[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)プロパティを提供します。[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)属性は、印刷されたワークシートの異なるページレイアウトオプションを設定するための[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)クラスのオブジェクトです。[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)クラスには、ページ設定オプションを設定するために使用されるさまざまなプロパティやメソッドが提供されています。

### **ページ余白**

ページの余白（左、右、上、下）を[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)クラスのメンバーを使用して設定します。以下にいくつかのメソッドをリストします。

- [**LeftMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/leftmargin)
- [**RightMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/rightmargin)
- [**TopMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/topmargin)
- [**BottomMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/bottommargin)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-1.cs" >}}

### **ページの中央に配置**

ページ上で何かを水平および垂直に中央揃えすることが可能です。これには、[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) クラスの有用なメンバー、[**CenterHorizontally**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centerhorizontally) および [**CenterVertically**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centervertically) があります。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.cs" >}}

### **ヘッダーとフッタのマージン**

[**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) クラスのメンバーでヘッダーとフッターの余白を設定するには、[**HeaderMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/headermargin) や [**FooterMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/footermargin) などを使用します。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.cs" >}}
