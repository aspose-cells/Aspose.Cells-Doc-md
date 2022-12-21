---
title: 外部リンクで範囲を取得
type: docs
weight: 120
url: /ja/net/get-range-with-external-links/
---
## **外部リンクで範囲を取得**

多くの場合、Excel ファイルは外部リンクを使用して他の Excel ファイルのデータにアクセスします。 Aspose.Cells を使用すると、これらの外部リンクを取得するオプションが提供されます。[**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas)方法。の[**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas)メソッドは型の配列を返します[**参照エリア**](https://reference.aspose.com/cells/net/aspose.cells/referredarea).の[**参照エリア**](https://reference.aspose.com/cells/net/aspose.cells/referredarea)クラスは[**外部ファイル名**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename)外部ファイルの名前を返すプロパティ。の[**参照エリア**](https://reference.aspose.com/cells/net/aspose.cells/referredarea)クラスは次のメンバーを公開します。

- [**EndColumn**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endcolumn): エリアの終了列
- [**行末**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endrow)エリアの最後の行
- [**外部ファイル名**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename)これが外部参照の場合、外部ファイル名を取得します
- [**IsArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isarea): 領域かどうかを示します
- [**IsExternalLink**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isexternallink): 外部リンクかどうかを示します
- [**シート名**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/sheetname)この参照がどのシートにあるかを示します
- [**開始列**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startcolumn)エリアの開始列
- [**開始行**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startrow)エリアの開始行

以下のサンプル コードは、[**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas)外部リンクで範囲を取得するメソッド。

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-GetRangeWithExternalLinks-1.cs" >}}
