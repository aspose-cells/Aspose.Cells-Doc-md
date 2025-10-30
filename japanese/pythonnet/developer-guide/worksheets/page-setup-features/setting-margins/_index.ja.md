---
title: マージンの設定
type: docs
weight: 20
url: /ja/python-net/setting-margins/
description: この資料では、サンプルコードを使ってExcelワークシートの余白を設定する方法を学びます。また、Aspose.Cells for Python via .NET APIを使用してページセットアップのページ中央、ヘッダー、フッターマージンをプログラムで設定する方法も解説します。
keywords: Python Excelライブラリ、PythonでExcelワークシートの余白を中央に設定、Pythonを使用したヘッダーとフッターマージンの設定。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET は、Microsoft Excelのページ設定オプションを完全にサポートしています。開発者は印刷プロセスを制御するためにワークシートのページ設定を構成する必要があります。このトピックでは、Aspose.Cells for Python via .NET を使用したページ余白の設定方法について説明します。

{{% /alert %}}

## **余白の設定方法**

Aspose.Cells for Python via .NET は、Excelファイルを表すクラス [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) を提供します。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) クラスは、Excelファイル内の各ワークシートにアクセスできる [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) コレクションを含みます。ワークシートは [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) クラスで表されます。

[**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)クラスはワークシートのページ設定オプションを設定するために使用される[**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/page_setup/)プロパティを提供します。[**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/page_setup)属性は、印刷されたワークシートの異なるページレイアウトオプションを設定するための[**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)クラスのオブジェクトです。[**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)クラスには、ページ設定オプションを設定するために使用されるさまざまなプロパティやメソッドが提供されています。

## **ページ余白の設定方法**

ページの余白（左、右、上、下）を[**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)クラスのメンバーを使用して設定します。以下にいくつかのメソッドをリストします。

- [**left_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/left_margin/)
- [**right_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/right_margin/)
- [**top_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/top_margin/)
- [**bottom_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/bottom_margin/)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-1.py" >}}

## **ページ上で中央揃えにする方法**

ページ上で何かを水平および垂直に中央揃えすることが可能です。これには、[**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) クラスの有用なメンバー、[**center_horizontally**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/center_horizontally/) および [**center_vertically**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/center_vertically/) があります。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.py" >}}

## **ヘッダーとフッターの余白を設定する方法**

[**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) クラスのメンバーでヘッダーとフッターの余白を設定するには、[**header_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/header_margin) や [**footer_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/footer_margin) などを使用します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.py" >}}
{{< app/cells/assistant language="python-net" >}}
