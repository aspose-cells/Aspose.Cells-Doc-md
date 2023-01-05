---
title: Excel の変換の進行状況を TIFF に追跡する
type: docs
weight: 140
url: /ja/java/track-conversion-progress-of-excel-to-tiff/
---
## **考えられる使用シナリオ**

大きな Excel ファイルの変換には時間がかかる場合があります。この間、ロード画面だけでなく、ドキュメント変換の進行状況を表示して、アプリケーションの使いやすさを向上させたい場合があります。 Aspose.Cells は、ドキュメント変換プロセスの追跡をサポートします。**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**インターフェース。の**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**インターフェイスが提供する**[PageStartSaving](https://reference.aspose.com/cells/java/com.aspose.cells/ipage Savingcallback#pageStartSaving(com.aspose.cells.PageStartSavingArgs))**と**[PageEndSaving](https://reference.aspose.com/cells/java/com.aspose.cells/ipage Savingcallback#pageEndSaving(com.aspose.cells.PageEndSavingArgs))**カスタム クラスに実装できるメソッド。で示されているように、どのページをレンダリングするかを制御することもできます。*TestTiffPageSavingCallback*カスタムクラス。

## **Excel の変換の進行状況を TIFF に追跡する**

次のコード サンプルは、[ソースエクセルファイル](sampleUseWorkbookRenderForImageConversion.xlsx)を使用して、変換の進行状況をコンソールに出力します。*TestTiffPageSavingCallback*を実装するカスタムクラス**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**インターフェース。参照用に、生成された出力ファイルを添付します。

[出力ファイル](DocumentConversionProgressForTiff_out.tiff)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.java" >}}

以下は、*TestTiffPageSavingCallback*カスタムクラス。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-2.java" >}}

## **コンソール出力**

ページ 10 のページ インデックス 0 の保存を開始します</br>
ページ 10 のページ インデックス 0 の保存を終了します</br>
ページ 10 のページ インデックス 1 の保存を開始します</br>
10 ページ中のページ インデックス 1 の保存を終了</br>
ページ 10 のページ インデックス 2 の保存を開始します</br>
ページ 10 のページ インデックス 2 の保存を終了します</br>
10 ページのページ インデックス 3 の保存を開始します</br>
ページ 10 のページ インデックス 3 の保存を終了します</br>
ページ 10 のページ インデックス 4 の保存を開始します</br>
ページ 10 のページ インデックス 4 の保存を終了します</br>
ページ 10 のページ インデックス 5 の保存を開始します</br>
ページ 10 のページ インデックス 5 の保存を終了します</br>
ページ 10 のページ インデックス 6 の保存を開始します</br>
ページ 10 のページ インデックス 6 の保存を終了します</br>
ページ 10 のページ インデックス 7 の保存を開始します</br>
ページ 10 のページ インデックス 7 の保存を終了します</br>
ページ 10 のページ インデックス 8 の保存を開始します</br>
ページ 10 のページ インデックス 8 の保存を終了します
