---
title: Excel で互換性チェッカーを無効にする
type: docs
weight: 170
url: /ja/net/disable-compatibility-checker-in-excel/
description: この記事では、Aspose.Cells for .NET API を通じて互換性チェッカーを無効にする方法を説明します。
keywords: C# Disable Compatibility Checker, Excel Disable Compatibility Checker in C#, Disable Compatibility Checker in Workbook. 
---
##  C# の Excel ワークシートで互換性チェッカーを無効にする

{{% alert color="primary" %}}

Microsoft 以前のファイル形式でファイルを保存する際の Excel の互換性チェック フラグにより、機能上の問題や忠実度の損失が発生する可能性があります。互換性チェックは、Microsoft Office Excel 2007 および Microsoft Excel 2010 の機能です。

Excel 2007 または Excel 2010 の以前のバージョン (Excel 97 から Excel 2003) でブックを保存すると、互換性チェックによってブックがスキャンされ、以前のバージョンでサポートされていない機能が含まれているかどうかが確認されます。互換性問題の処理方法を決定できるように、互換性チェッカーにはオプションを含むダイアログ ボックスが表示されます。また、ワークブックの問題に関するレポートを作成したり、機能を無効にしたりするために使用することもできます。

場合によっては、特定のスプレッドシートの互換性チェッカーを無効にする必要があります。 Aspose.Cells' API を使用すると、これをプログラムで実行できるため、ユーザーが Microsoft Excel にファイルを手動で再保存するときに表示される互換性チェック ダイアログ ボックスにイライラしたり混乱したりすることがなくなります。

{{% /alert %}}

##  **Microsoft Excel を使用して互換性チェッカーを無効にする方法**

Microsoft Excel (たとえば、Microsoft Excel 2007/2010) で互換性チェッカーを無効にするには:

-  (Excel 2007) Office ボタンで、 をクリックします。**準備**してから**互換性チェッカーを実行**し、**このブックを保存するときに互換性をチェックするをオフにします**オプション。
- (Excel 2010) [ファイル] タブで、 をクリックします。**[情報]**、[**問題の確認**]、[**互換性の確認**] をクリックし、最後に [**このブックを保存するときに互換性を確認する] のチェックを外します。**オプション。

##  **Aspose.Cells API を使用して互換性チェッカーを無効にする方法**

をセットする[**Workbook.Settings.CheckComptilibility**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcompatibility)財産を**間違い**Microsoft Excel の互換性チェッカーを無効にします。

###  **コード例**

次のコード例は、Aspose.Cells for .NET で互換性チェッカーを無効にする方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DisableCompatibilityChecker-1.cs" >}}
