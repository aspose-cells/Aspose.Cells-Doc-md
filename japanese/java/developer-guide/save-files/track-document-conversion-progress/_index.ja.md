---
title: ドキュメント変換の進行状況を追跡
type: docs
weight: 120
url: /ja/java/track-document-conversion-progress/
---

## **可能な使用シナリオ**

大きなExcelファイルを変換するときは時間がかかることがあります。この間、アプリケーションの使いやすさを向上させるために、単なるローディング画面ではなく文書変換の進行状況を表示したいと思うかもしれません。Aspose.Cellsは、[**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback) インターフェースを提供することで文書変換の進行状況を追跡できます。[**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback) インターフェースは、カスタムクラスで実装することができる [**PageStartSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageStartSaving-com.aspose.cells.PageStartSavingArgs-) と [**PageEndSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageEndSaving-com.aspose.cells.PageEndSavingArgs-) のメソッドを提供します。また、*TestPageSavingCallback* カスタムクラスで示されているように、どのページをレンダリングするかを制御することもできます。

## **文書変換の進行状況を追跡する**

次のコードサンプルは、*TestPageSavingCallback* カスタムクラスを実装して、[**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback) インターフェースを使用して、[ソースのExcelファイル](PagesBook1.xlsx)をロードし、変換の進行状況をコンソールに印刷します。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-1.java" >}}

*TestPageSavingCallback*カスタムクラスのコードは次のとおりです。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-2.java" >}}

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
{{< app/cells/assistant language="java" >}}
