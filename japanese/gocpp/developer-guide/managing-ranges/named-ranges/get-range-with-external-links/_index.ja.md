---
title: Golangを使用したC++で外部リンクを含む範囲を取得
linktitle: 外部リンクを含む範囲を取得
type: docs
weight: 120
url: /ja/go-cpp/get-range-with-external-links/
description: Aspose.Cellsを利用して、Golangを使用したC++でExcelファイル内の外部リンクを持つ範囲を取得する方法を学びます。
---

## **外部リンク付きの範囲を取得する**

多くの場合、Excelファイルは他のExcelファイルの外部リンクを通じてデータにアクセスしています。Aspose.Cellsは、[**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/)メソッドを使ってこれらの外部リンクを取得できます。[**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/)メソッドは[**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/)タイプの配列を返します。[**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/)クラスは外部ファイルの名前を返す[**GetExternalFileName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getexternalfilename/)プロパティを持ちます。[**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/)クラスは以下のメンバーを公開しています。

- [**GetEndColumn()**](https://reference.aspose.com/cells/go-cpp/referredarea/getendcolumn/): 範囲の終了列
- [**GetEndRow()**](https://reference.aspose.com/cells/go-cpp/referredarea/getendrow/): 範囲の終了行
- [**GetExternalFileName()**](https://reference.aspose.com/cells/go-cpp/referredarea/getexternalfilename/): これが外部参照の場合、外部ファイル名を取得します
- [**IsArea**](https://reference.aspose.com/cells/go-cpp/referredarea/isarea/): これはエリアであるかどうかを示します
- [**IsExternalLink**](https://reference.aspose.com/cells/go-cpp/referredarea/isexternallink/): これは外部リンクであるかどうかを示します
- [**GetSheetName()**](https://reference.aspose.com/cells/go-cpp/referredarea/getsheetname/): この参照が含まれるシートを示します
- [**GetStartColumn()**](https://reference.aspose.com/cells/go-cpp/referredarea/getstartcolumn/): エリアの開始列
- [**GetStartRow()**](https://reference.aspose.com/cells/go-cpp/referredarea/getstartrow/): エリアの開始行

以下に示すサンプルコードは、外部リンクを含む範囲を取得するための[**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/)メソッドの使用例です。

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetRangeWithExternalLinks.go" >}}
