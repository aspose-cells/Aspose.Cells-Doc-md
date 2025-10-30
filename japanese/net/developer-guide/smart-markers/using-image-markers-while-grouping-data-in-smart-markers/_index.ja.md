---
title: SmartMarkersで画像マーカーを使用する方法
type: docs
weight: 30
url: /ja/net/how-to-use-image-markers-in-smart-markers/
alias: [/net/using-image-markers-while-grouping-data-in-smart-markers/]
---

## **可能な使用シナリオ**
画像マーカーは、テンプレートシステム（例：FoxPro、Handlebars、現代的なUIフレームワーク）で、画像やビジュアル資産を動的に挿入するための特殊なプレースホルダーです。時には、スマートマーカーを使用して画像を挿入する必要があります。Aspose.Cellsでは、画像をスマートマーカーに追加することが可能です。

## **SmartMarkersで画像パラメータ**
画像を操作するためのスマートマーカーのパラメータ。

- **Picture:FitToCell** - 画像をセルの行の高さと列の幅に自動調整します。
- **Picture:ScaleN** - 高さと幅をNパーセントにスケーリングします。
- **Picture:Width:Nin&Height:Nin** - 画像を高さNインチ、幅Nインチでレンダリングします。LeftとTopの位置（ポイント単位）も指定できます。

## **スマートマーカーで画像マーカーを使用する方法**
次のサンプルコードをご覧ください。これにより、スマートマーカーを使用して画像を挿入する方法が示されています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-ImageMarkers-1.cs" >}}

## **スマートマーカーでデータをグループ化しながら画像マーカーを使用する方法**
次のサンプルでは、ブックを作成し、セルD2、E2、およびF2に次のSmart Markerタグを追加します。

{{< highlight java >}}

&=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

次に、データソースにデータを入れ、[WorkbookDesigner.Process()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) メソッドを呼び出してSmart Markerタグを処理します。コードはこれらの画像 [moon.png](5115492.png) および [moon2.png](5115491.png) を使用していますが、任意の画像を使用できます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}

{{< app/cells/assistant language="csharp" >}}
