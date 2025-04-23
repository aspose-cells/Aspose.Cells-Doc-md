---
title: ドキュメント変換の進行状況を追跡
type: docs
weight: 970
url: /ja/net/track-document-conversion-progress/
---

## **可能な使用シナリオ**

大きなExcelファイルを変換する際、時間がかかることがあります。この時間に、単なる読み込み画面ではなくドキュメント変換の進行状況を表示したい場合があります。Aspose.Cellsでは、[**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)インタフェースを提供することで、カスタムクラスで実装できる[**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)インタフェースが提供されます。T*estPageSavingCallback*カスタムクラスで示されているように、レンダリングされるページを制御することもできます。

## **文書変換の進行状況を追跡する**

次のコードサンプルは、[ソースExcelファイル](94896151.xlsx)をロードし、*TestPageSavingCallback*カスタムクラスを使用してコンソールに変換進行状況を表示します。

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgress-1.cs" >}}

*TestPageSavingCallback*カスタムクラスのコードは次のとおりです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgress-2.cs" >}}

## **コンソール出力**

{{< highlight java >}}

Start saving page index 0 of pages 11</br>
End saving page index 0 of pages 11</br>
Start saving page index 1 of pages 11</br>
End saving page index 1 of pages 11</br>
Start saving page index 2 of pages 11</br>
End saving page index 2 of pages 11</br>
Start saving page index 3 of pages 11</br>
End saving page index 3 of pages 11</br>
Start saving page index 4 of pages 11</br>
End saving page index 4 of pages 11</br>
Start saving page index 5 of pages 11</br>
End saving page index 5 of pages 11</br>
Start saving page index 6 of pages 11</br>
End saving page index 6 of pages 11</br>
Start saving page index 7 of pages 11</br>
End saving page index 7 of pages 11</br>
Start saving page index 8 of pages 11</br>
End saving page index 8 of pages 11

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
