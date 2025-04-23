---
title: 異なるページ用に異なるヘッダーとフッターの設定
type: docs
weight: 35
url: /ja/python-net/setting-different-headers-and-footers-for-pages-to-Excel/
description: この記事は、Aspose.Cells for Python APIを使用してExcelのページ設定のさまざまなヘッダーとフッターをプログラム的に設定するサンプルコードを提供します。最初のページ、奇数ページ、偶数ページのヘッダーとフッターを設定できます。
keywords: Python Excelライブラリを使い、PythonでExcelのヘッダーとフッターの最初のページ、奇数ページ、偶数ページ用を設定します。
---

{{% alert color="primary" %}}

ExcelはExcel 2007以降、最初のページ、奇数ページ、偶数ページ用に異なるヘッダーとフッターの設定をサポートしています。
Aspose.Cells for Python via .NETも同じ機能をサポートしています。

{{% /alert %}}

## **MS Excelで異なるヘッダーとフッターを設定するにはどうすればよいですか**

**![異なるヘッダーとフッターの設定](difpage.png)**

1. **ページレイアウト > 印刷タイトル > ヘッダー/フッター**をクリックします。
1. **奇数と偶数のページを異なるものとする** または **最初のページを異なるものとする** をチェックします。
1. 異なるヘッダーとフッターを入力します。

## **Aspose.Cells for Python Excelライブラリを使用して、異なるヘッダーとフッターを設定する方法**

Aspose.Cells for Python via .NETは、Excelと同じ動作をします。
1. [PageSetup.is_hf_diff_odd_even](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_odd_even/) と [PageSetup.is_hf_diff_first](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_first/) のフラグを設定します 
1. 異なるヘッダーとフッターを入力します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-DiffHeaderFooter.py" >}}
