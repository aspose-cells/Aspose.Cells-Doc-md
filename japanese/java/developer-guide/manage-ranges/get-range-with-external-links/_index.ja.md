---
title: 外部リンクを含む範囲を取得
type: docs
weight: 140
url: /ja/java/get-range-with-external-links/
---

## **外部リンク付きの範囲を取得する**

多くの場合、Excelファイルは外部リンクを使用して他のExcelファイルからデータにアクセスします。Aspose.Cellsでは、[**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean))メソッドを使用してこれらの外部リンクを取得するオプションを提供します。[**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean))メソッドは、[**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea)型の配列を返します。[**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea)クラスは、外部ファイルの名前を返す[**ExternalFileName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName)プロパティを提供します。[**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea)クラスは、以下のメンバーを公開します。

- [**EndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndColumn)：領域の終了列
- [**EndRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndRow)：領域の終了行
- [**ExternalFileName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName)：これが外部参照である場合は外部ファイル名を取得します
- [**IsArea**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsArea)：これが領域であるかどうかを示します
- [**IsExternalLink**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsExternalLink)：これが外部リンクであるかどうかを示します
- [**SheetName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#SheetName)：この参照が存在するシートを示します
- [**StartColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartColumn)：領域の開始列
- [**StartRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartRow)：エリアの開始行

以下に示すサンプルコードは、外部リンクを持つ範囲を取得するために[**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean))メソッドを使用する方法を示しています。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetRangeWithExternalLinks-1.java" >}}
