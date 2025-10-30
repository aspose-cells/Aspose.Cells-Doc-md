---
title: ExcelからTIFFへの変換進行状況をC++経由のGolangでトラッキング
linktitle: ExcelからTIFFへの変換の進行状況を追跡
type: docs
weight: 190
url: /ja/go-cpp/track-conversion-progress-of-excel-to-tiff/
description: Aspose.Cells for C++を使用してExcelファイルのTIFFへの変換進捗を追跡する方法を学びます。
---

## **可能な使用シナリオ**

大きなExcelファイルの変換には時間がかかる場合があります。その間、読み込み画面だけでなくドキュメント変換の進行状況を表示したい場合があります。Aspose.Cellsは[**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/)インターフェースを提供することでドキュメント変換の進捗追跡をサポートしています。[**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/)インターフェースは[**PageStartSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pagestartsaving/)および[**PageEndSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pageendsaving/)メソッドを提供しており、カスタムクラスに実装可能です。また、どのページをレンダリングするかも制御可能です（*TestPageSavingCallback*カスタムクラス参照）。

## **ExcelからTIFFへの変換の進行状況を追跡**

次のコード例は、[**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/)インターフェースを実装した*TestPageSavingCallback*カスタムクラスを使用して、[ソースExcelファイル](95584311.xlsx)を読み込み、その変換進捗をコンソールに出力します。生成された出力ファイルも添付します。

[Output File](95584312.tiff)

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackConversionProgressOfExcelToTiff.go" >}}
以下は*TestTiffPageSavingCallback* カスタムクラスのコードです。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackConversionProgressOfExcelToTiff-1.go" >}}
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
