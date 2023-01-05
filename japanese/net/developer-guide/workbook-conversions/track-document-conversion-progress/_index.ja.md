---
title: ドキュメント変換の進行状況を追跡する
type: docs
weight: 970
url: /ja/net/track-document-conversion-progress/
---
## **考えられる使用シナリオ**

大きな Excel ファイルの変換には時間がかかる場合があります。この間、ロード画面だけでなく、ドキュメント変換の進行状況を表示して、アプリケーションの使いやすさを向上させたい場合があります。 Aspose.Cells は、ドキュメント変換プロセスの追跡をサポートします。**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipage Savingcallback)**インターフェース。の**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipage Savingcallback)**インターフェイスが提供する**[PageStartSaving](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipage Savingcallback/methods/pagestart Saving)**と**[PageEndSaving](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipage Savingcallback/methods/pageend Saving)**カスタム クラスに実装できるメソッド。 T で示されているように、どのページをレンダリングするかを制御することもできます。*estPageSavingCallback*カスタムクラス。

## **ドキュメント変換の進行状況を追跡する**

次のコード サンプルは、[ソースエクセルファイル](94896151.xlsx)を使用して、変換の進行状況をコンソールに出力します。*TestPageSavingCallback*を実装するカスタムクラス**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipage Savingcallback)**インターフェース。

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgress-1.cs" >}}

以下は、*TestPageSavingCallback*カスタムクラス。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgress-2.cs" >}}

## **コンソール出力**

ページ 11 のページ インデックス 0 の保存を開始</br>
ページ 11 のページ インデックス 0 の保存を終了します</br>
11 ページのページ インデックス 1 の保存を開始します</br>
ページ 11 のページ インデックス 1 の保存を終了します</br>
11 ページのページ インデックス 2 の保存を開始します</br>
ページ 11 のページ インデックス 2 の保存を終了します</br>
11 ページのページ インデックス 3 の保存を開始します</br>
ページ 11 のページ インデックス 3 の保存を終了します</br>
ページ 11 のページ インデックス 4 の保存を開始します</br>
ページ 11 のページ インデックス 4 の保存を終了します</br>
ページ 11 のページ インデックス 5 の保存を開始します</br>
ページ 11 のページ インデックス 5 の保存を終了します</br>
ページ 11 のページ インデックス 6 の保存を開始します</br>
ページ 11 のページ インデックス 6 の保存を終了します</br>
ページ 11 のページ インデックス 7 の保存を開始します</br>
ページ 11 のページ インデックス 7 の保存を終了します</br>
ページ 11 のページ インデックス 8 の保存を開始します</br>
ページ 11 のページ インデックス 8 の保存を終了します
