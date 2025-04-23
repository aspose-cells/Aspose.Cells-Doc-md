---
title: ファイルを開くさまざまな方法
type: docs
weight: 10
url: /ja/python-net/different-ways-to-open-files/
description: この記事は、Aspose.Cells for Python via .NET APIを使用してExcelファイルを開く方法を説明します。
keywords: PythonでExcelファイルをExcelなしで開くにはどうすればよいですか。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NETを使えば、ファイルを簡単に開くことができ、データの取得やデザイナーテンプレートを使った開発の高速化も可能です。

{{% /alert %}}

## **パスを使用してExcelファイルを開く方法**

開発者は、ローカルコンピュータのファイルパスを指定して、[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスのコンストラクターを使用してMicrosoft Excelファイルを開くことができます。パスを文字列として渡すだけです。Aspose.Cells for Python via .NETは自動的にファイル形式を検出します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilesThroughPath-1.py" >}}

## **ストリームを使用してExcelファイルを開く方法**

また、ストリームとしてExcelファイルを開くことも簡単です。ファイルを含む*Stream*オブジェクトを引数に取るコンストラクタのオーバーロードバージョンを使用します。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilesThroughStream-1.py" >}}

## **データだけを含むファイルを開く方法**

データのみを含むファイルを開くには、関連する属性とオプションを設定するために、[**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions)および[**LoadFilter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter)クラスを使用して、ロードするテンプレートファイルのクラスの関連属性とオプションを設定してください。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilewithDataOnly-1.py" >}}

