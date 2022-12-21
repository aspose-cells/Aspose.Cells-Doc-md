---
title: Excel で互換性チェックを無効にする
type: docs
weight: 270
url: /ja/java/disable-compatibility-checker-in-excel/
---
{{% alert color="primary" %}}

Microsoft 以前のファイル形式でファイルを保存すると、Excel の互換性チェックで、ファイルを保存すると機能上の問題が発生したり、忠実度が失われたりする可能性があるというフラグが立てられます。互換性チェックは、Microsoft Office Excel 2007、2010 & 2013 の機能です。

以前のバージョン (Excel 97 から Excel 2003、Excel 2007 または Excel 2010) でブックを保存すると、互換性チェックはブックをスキャンして、以前のバージョンでサポートされていない機能が含まれているかどうかを確認します。互換性の問題を処理する方法を決定するのに役立つように、互換性チェックではオプションを含むダイアログ ボックスが表示されます。ワークブックの問題に関するレポートを作成したり、機能を無効にしたりするためにも使用できます。

場合によっては、特定のスプレッドシートの互換性チェックを無効にする必要があります。 Aspose.Cells' API を使用すると、これを動的に実行できるため、Microsoft Excel でファイルを手動で再保存するときに互換性チェック ダイアログ ボックスが表示されてユーザーがイライラしたり混乱したりすることはありません。

{{% /alert %}}

## **Microsoft エクセルを使う**

Microsoft Excel (たとえば、Microsoft Excel 2007/2010) で互換性チェックを無効にするには:

-  (Excel 2007) [Office] ボタンで、**準備**、 それから**互換性チェックを実行する**をクリアします。**このブックを保存するときに互換性を確認してください**オプション。
- (Excel 2010 & 2013) [ファイル] タブで、**情報**、 それから**問題を確認する** 、 クリック**互換性を確認する**、そして最後に、**このブックを保存するときに互換性を確認してください**オプション。

## **Aspose.Cells API の使用**

をセットする[**WorkbookSettings.CheckComptibility**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckComptiliblity)プロパティへ**間違い** Microsoft Excel の互換性チェックを無効にします。

テンプレートの XLS ファイルがあるとします。ユーザーが MS Excel 2007/2010/2013 で保存または再保存すると、下のスクリーンショットに示すように、[互換性チェック] ダイアログ ボックスが表示されます。

![todo:画像_代替_文章](disable-compatibility-checker-in-excel_1.png)

次のコードは、Aspose.Cells for Java で互換性チェックを無効にする方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableCompatibilityChecker-DisableCompatibilityChecker.java" >}}
