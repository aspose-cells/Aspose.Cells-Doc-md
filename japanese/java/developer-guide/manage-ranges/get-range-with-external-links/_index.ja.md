---
title: 外部リンクで範囲を取得
type: docs
weight: 140
url: /ja/java/get-range-with-external-links/
---
## **外部リンクで範囲を取得**

多くの場合、Excel ファイルは外部リンクを使用して他の Excel ファイルのデータにアクセスします。 Aspose.Cells を使用すると、これらの外部リンクを取得するオプションが提供されます。[**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)） 方法。の[**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) メソッドは型の配列を返します[**参照エリア**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea).の[**参照エリア**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea)クラスは[**外部ファイル名**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName)外部ファイルの名前を返すプロパティ。の[**参照エリア**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea)クラスは次のメンバーを公開します。

- [**EndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndColumn): エリアの終了列
- [**行末**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndRow)エリアの最後の行
- [**外部ファイル名**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName)これが外部参照の場合、外部ファイル名を取得します
- [**IsArea**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsArea): 領域かどうかを示します
- [**IsExternalLink**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsExternalLink): 外部リンクかどうかを示します
- [**シート名**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#SheetName)この参照がどのシートにあるかを示します
- [**開始列**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartColumn)エリアの開始列
- [**開始行**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartRow)エリアの開始行

以下のサンプル コードは、[**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) メソッドを使用して、外部リンクを含む範囲を取得します。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetRangeWithExternalLinks-1.java" >}}
