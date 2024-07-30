---
title: 印刷オプションの設定
type: docs
weight: 40
url: /ja/python-net/setting-print-options/
description: この記事では、Aspose.Cells for Python via .NET APIを使用してExcelワークシートのページ設定機能の印刷オプションをプログラムで設定する方法を説明します。印刷エリア、印刷タイトル、ページ順序を設定できます。
keywords: Python Excelライブラリ、PythonでExcelの印刷範囲を設定、PythonでExcelの印刷タイトルを設定、PythonでExcelのページ順序を設定、Pythonで印刷オプションを設定する方法、Pythonで印刷エリアを設定する方法、Pythonで印刷タイトルを設定する方法。 
---

{{% alert color="primary" %}}

Microsoft Excel のページ設定設定には、ワークシートページが印刷される方法を制御するいくつかの印刷オプション (またはシートオプションとも呼ばれる) が含まれています。

{{% /alert %}}

## **印刷オプションの設定方法**

これらの印刷オプションにより、ユーザーは次のような操作を行うことができます:

- ワークシート上の特定の印刷範囲を選択する。
- タイトルを印刷する。
- グリッド線を印刷する。
- 行/列見出しを印刷します。
- 下書き品質を実現する。
- コメントを印刷する。
- セルエラーを印刷する。
- ページ順序を定義する。

Aspose.Cells for Python via .NETは、Microsoft Excelが提供するすべての印刷オプションをサポートしており、開発者は[**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)クラスが提供するプロパティを使用してこれらのオプションを簡単に構成できます。これらのプロパティの使用方法については、以下で詳しく説明されています。

## **印刷エリアを設定する方法**

デフォルトでは、印刷エリアにはデータを含むワークシートのすべての領域が組み込まれます。開発者はワークシートの特定の印刷エリアを設定することができます。

特定の印刷エリアを選択するには、[**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) クラスの [**print_area**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_area/) プロパティを使用します。このプロパティに、印刷エリアを定義するセル範囲を割り当てます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPrintArea-1.py" >}}

## **印刷タイトルを設定する方法**

Aspose.Cells for Python via .NETでは、印刷されるワークシートのすべてのページで行見出しと列見出しを繰り返すように指定できます。これを行うには、[**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)クラスの[**print_title_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_columns/)プロパティと[**print_title_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_title_rows)プロパティを使用します。

繰り返す行または列は、その行番号または列番号を渡すことで定義されます。たとえば、行は$1:$2と定義され、列は$A:$Bと定義されます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPrintTitle-1.py" >}}

## **その他の印刷オプションの設定方法**

[**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) クラスには、以下の一般的な印刷オプションを設定するためのいくつかの他のプロパティも提供されています:

- [**print_grid_lines**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_gridlines/): グリッド線を印刷するかどうかを定義するブール型のプロパティ。
- [**print_headings**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_headings/): 行および列見出しを印刷するかどうかを定義するブール型のプロパティ。
- [**black_and_white**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/black_and_white/): ブラックアンドホワイトモードでワークシートを印刷するかどうかを定義するブールプロパティ。
- [**print_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_comments/): ワークシート上に印刷コメントを表示するか、ワークシートの最後に表示するかを定義する。
- [**print_draft**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_draft/): グラフィックを排除してシートを印刷するかどうかを定義するブールプロパティ。
- [**print_errors**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_errors): 表示されるままのセルエラー、空白、ダッシュ、またはN/A として印刷するかを定義する。

Aspose.Cellsは、[**print_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_comments/) と [**print_errors**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_errors) プロパティを設定するために、[**PrintCommentsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printcommentstype) と [**PrintErrorsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printerrorstype) という2つの列挙型を提供しています。これらの列挙型には、それぞれ [**print_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_comments/) と [**print_errors**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/print_errors) プロパティに割り当てるための事前に定義された値が含まれています。

[**PrintCommentsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printcommentstype) 列挙型の事前に定義された値は、以下にその説明とともにリストされています。

|**コメント印刷タイプ**|**説明**|
| :- | :- |
|PRINT_IN_PLACE|ワークシートに表示されているコメントを印刷することを指定します。
|PRINT_NO_COMMENTS|コメントを印刷しないことを指定します。
|PRINT_SHEET_END|ワークシートの末尾にコメントを印刷することを指定します。

[**PrintErrorsType**](https://reference.aspose.com/cells/python-net/aspose.cells/printerrorstype) 列挙型の事前に定義された値は、以下にその説明とともにリストされています。



|**エラー印刷タイプ**|**説明**|
| :- | :- |
|PRINT_ERRORS_BLANK|エラーを印刷しないことを指定します。
|PRINT_ERRORS_DASH|エラーを"--"として印刷することを指定します。
|PRINT_ERRORS_DISPLAYED|表示されているようにエラーを印刷することを指定します。
|PRINT_ERRORS_NA|エラーを"#N/A"として印刷することを指定します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-OtherPrintOptions-1.py" >}}

## **ページ順序の設定方法**

[**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) クラスは、ワークシートを印刷するための複数のページの順序を設定するために使用される [**Order**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/order) プロパティを提供します。ページを順に印刷するためには、次の2つの可能性があります。

- **Down then over:** 右側のページを印刷する前に、すべてのページを下に印刷します。
- **Over then down:** 下側のページを印刷する前に、左から右のページを印刷します。

Aspose.Cellsは、[**PrintOrderType**](https://reference.aspose.com/cells/python-net/aspose.cells/printordertype) という列挙型を提供し、すべての事前に定義された順序タイプが含まれています。

列挙型 [**PrintOrderType**](https://reference.aspose.com/cells/python-net/aspose.cells/printordertype) の事前に定義された値は、以下にその説明とともにリストされています。

|**印刷順序タイプ**|**説明**|
| :- | :- |
|DOWN_THEN_OVER|下から順に印刷することを表します。
|OVER_THEN_DOWN|上から順に印刷することを表します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetPageOrder-1.py" >}}
