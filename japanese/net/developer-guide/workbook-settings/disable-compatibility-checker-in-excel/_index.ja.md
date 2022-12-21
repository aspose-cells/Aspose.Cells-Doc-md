---
title: Excel で互換性チェックを無効にする
type: docs
weight: 170
url: /ja/net/disable-compatibility-checker-in-excel/
keywords: c# excel disable compatibility checke
---
## C# で Excel ワークシートの互換性チェックを無効にする

{{% alert color="primary" %}}

Microsoft 以前のファイル形式でファイルを保存する際の Excel の互換性チェック フラグにより、機能上の問題が発生したり、忠実度が失われたりする可能性があります。互換性チェックは、Microsoft Office Excel 2007 および Microsoft Excel 2010 の機能です。

以前のバージョン (Excel 97 から Excel 2003、Excel 2007 または Excel 2010) でブックを保存すると、互換性チェックはブックをスキャンして、以前のバージョンでサポートされていない機能が含まれているかどうかを確認します。互換性の問題を処理する方法を決定するのに役立つように、互換性チェックではオプションを含むダイアログ ボックスが表示されます。ワークブックの問題に関するレポートを作成したり、機能を無効にしたりするためにも使用できます。

場合によっては、特定のスプレッドシートの互換性チェックを無効にする必要があります。 Aspose.Cells' API を使用すると、これをプログラムで実行できるため、Microsoft Excel でファイルを手動で再保存するときに互換性チェック ダイアログ ボックスが表示されてイライラしたり混乱したりすることはありません。

{{% /alert %}}

## **Microsoft エクセルを使う**

Microsoft Excel (たとえば、Microsoft Excel 2007/2010) で互換性チェックを無効にするには:

-  (Excel 2007) [Office] ボタンで、**準備**、 それから**互換性チェックを実行する**をクリアします。**このブックを保存するときに互換性を確認してください**オプション。
-  (Excel 2010) [ファイル] タブで、**情報**、 それから**問題を確認する** 、 クリック**互換性を確認する**、そして最後に、**このブックを保存するときに互換性を確認してください**オプション。

## **Aspose.Cells API の使用**

をセットする[**Workbook.Settings.CheckComptibility**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcompatibility)プロパティへ**間違い** Microsoft Excel の互換性チェックを無効にします。

### **コード例**

次のコード例は、Aspose.Cells for .NET で互換性チェックを無効にする方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DisableCompatibilityChecker-1.cs" >}}
