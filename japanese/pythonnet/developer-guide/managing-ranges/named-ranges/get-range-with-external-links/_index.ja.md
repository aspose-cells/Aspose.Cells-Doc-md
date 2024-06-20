---
title: 外部リンクを含む範囲を取得
type: docs
weight: 120
url: /ja/python-net/get-range-with-external-links/
description: この記事では、Aspose.Cells for Python via .NET APIを使用して、外部リンクを持つ範囲を取得する方法が示されています。
keywords: Python Excelライブラリ、外部リンクを持つPythonの範囲を取得します。
---

## **外部リンク付きの範囲を取得する**

多くの場合、Excelファイルは他のExcelファイルからデータにアクセスします。Aspose.Cells for Python via .NETは、[**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool)メソッドを使用してこれらの外部リンクを取得するオプションを提供します。[**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool)メソッドは、[**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea)型の配列を返します。[**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea)クラスは外部ファイルの名前を返す[**external_file_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/external_file_name/)プロパティを提供します。[**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea)クラスは以下のメンバーを公開します。

- [**end_column**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/end_column/)：領域の終了列
- [**end_row**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/end_row/)：領域の終了行
- [**external_file_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/external_file_name/)：これが外部参照である場合は外部ファイル名を取得します
- [**is_area**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/is_area/)：これが領域であるかどうかを示します
- [**is_external_link**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/is_external_link/)：これが外部リンクであるかどうかを示します
- [**sheet_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/sheet_name/)：この参照が存在するシートを示します
- [**start_column**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/start_column)：領域の開始列
- [**start_row**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/start_row)：エリアの開始行

以下のサンプルコードは、[**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool) メソッドを使用して外部リンクを持つ範囲を取得する方法を示しています。

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Worksheets-GetRangeWithExternalLinks-1.py" >}}
