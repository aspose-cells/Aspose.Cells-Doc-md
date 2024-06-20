---
title: ExcelからTIFFへの変換の進行状況を追跡
type: docs
weight: 190
url: /ja/net/track-conversion-progress-of-excel-to-tiff/
---

## **可能な使用シナリオ**

大きなExcelファイルを変換する際、時間がかかることがあります。この時間に、単なる読み込み画面ではなくドキュメント変換の進行状況を表示したい場合があります。Aspose.Cellsでは、[**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)インタフェースを提供することで、カスタムクラスで実装できる[**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)インタフェースが提供されます。T*estPageSavingCallback*カスタムクラスで示されているように、レンダリングされるページを制御することもできます。

## **ExcelからTIFFへの変換の進行状況を追跡**

以下のコードサンプルでは、[ソースのExcelファイル](95584311.xlsx)をロードし、*TestPageSavingCallback*を実装したカスタムクラスを使用して、変換の進行状況をコンソールに出力します。生成された出力ファイルは参照用に添付されています。

[Output File](95584312.tiff)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.cs" >}}

以下は*TestTiffPageSavingCallback* カスタムクラスのコードです。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-2.cs" >}}

## **コンソール出力**

{{< highlight java >}}

Start saving page index 0 of pages 10</br>
End saving page index 0 of pages 10</br>
Start saving page index 1 of pages 10</br>
End saving page index 1 of pages 10</br>
Start saving page index 2 of pages 10</br>
End saving page index 2 of pages 10</br>
Start saving page index 3 of pages 10</br>
End saving page index 3 of pages 10</br>
Start saving page index 4 of pages 10</br>
End saving page index 4 of pages 10</br>
Start saving page index 5 of pages 10</br>
End saving page index 5 of pages 10</br>
Start saving page index 6 of pages 10</br>
End saving page index 6 of pages 10</br>
Start saving page index 7 of pages 10</br>
End saving page index 7 of pages 10</br>
Start saving page index 8 of pages 10</br>
End saving page index 8 of pages 10</br>

{{< /highlight >}}
