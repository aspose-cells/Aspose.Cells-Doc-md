---
title: カスタム定義クラスをExcelに変換する
type: docs
weight: 30
url: /ja/python-net/convert-customer-defined-classes-to-excel/
description: Aspose.Cells for Python via .NET APIを使用して、カスタム定義クラスをExcelに変換します。
keywords: Pythonを使用してカスタム定義クラスをExcelに変換、Pythonでカスタム定義クラスをExcelにインポート via NET、Pythonでカスタム定義クラスをxlsxに変換、カスタム定義クラスをExcelにインポートするためのロード。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET APIを使用すれば、カスタム定義クラスをExcel、OpenOffice、Pdf、Json、その他多くのフォーマットに変換可能です。

{{% /alert %}}

## **カスタム定義クラスをExcelに変換**
クラスのコレクションがあり、その情報をExcelファイルにインポートしたい場合は、Pythonのリフレクション機構を用いてクラスデータとそのメンバー変数の名前を両方含める便利な方法です。事前にクラスのメタデータを知る必要はありません。
Aspose.Cells for Python via .NETを使って、ユーザー定義クラスリストのデータをExcelファイルにインポートする方法を示すコード例です。
ファイルImportCustomObject.pyは、インポートするクラス情報を定義しており、Pythonのリフレクション機構を使用してクラスデータとメンバ変数名を特定のセル範囲に含めます。
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "ImportCustomObject.py" >}}

TestImportCustomObject.pyは、簡単な使用例を示しています。この例を参考にしたり、少し修正したりして独自のデータをインポートできます。
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "TestImportCustomObject.py" >}}
