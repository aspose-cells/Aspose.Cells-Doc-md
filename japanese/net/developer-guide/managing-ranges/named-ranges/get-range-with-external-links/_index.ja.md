---
title: 外部リンクを含む範囲を取得
type: docs
weight: 120
url: /ja/net/get-range-with-external-links/
---

## **外部リンク付きの範囲を取得する**

多くの場合、Excel ファイルは外部リンクを使用して他の Excel ファイルからデータにアクセスします。Aspose.Cells では、[**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas) メソッドを使用してこれらの外部リンクを取得することができます。[**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas) メソッドは、[**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea) タイプの配列を返します。[**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea) クラスでは、外部ファイル名を返す [**ExternalFileName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename) プロパティが提供されています。[**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea) クラスでは、次のようなメンバーを公開しています。

- [**EndColumn**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endcolumn)：領域の終了列
- [**EndRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endrow)：領域の終了行
- [**ExternalFileName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename)：これが外部参照である場合は外部ファイル名を取得します
- [**IsArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isarea)：これが領域であるかどうかを示します
- [**IsExternalLink**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isexternallink)：これが外部リンクであるかどうかを示します
- [**SheetName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/sheetname)：この参照が存在するシートを示します
- [**StartColumn**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startcolumn)：領域の開始列
- [**StartRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startrow)：エリアの開始行

以下のサンプルコードは、[**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas) メソッドを使用して外部リンクを持つ範囲を取得する方法を示しています。

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-GetRangeWithExternalLinks-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
