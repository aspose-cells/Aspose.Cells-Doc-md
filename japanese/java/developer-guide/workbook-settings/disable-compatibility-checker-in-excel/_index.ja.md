---
title: Excelでの互換性チェッカーを無効にする
type: docs
weight: 270
url: /ja/java/disable-compatibility-checker-in-excel/
---

{{% alert color="primary" %}}

Microsoft Excelの互換性チェッカーは、ファイルを以前のファイル形式で保存すると、ファイルの保存によって機能の問題や忠実度の低下が発生する可能性があると警告します。互換性チェッカーは、Microsoft Office Excel 2007、2010、および2013の機能です。

以前のバージョンのワークブックをExcel 2007またはExcel 2010からExcel 97からExcel 2003に保存する場合、互換性チェッカーは、以前のバージョンではサポートされていない機能が含まれていないかどうかをワークブックをスキャンします。互換性の問題についての決定を支援するために、互換性チェッカーはオプションを含むダイアログボックスを表示します。また、ワークブックの問題に関するレポートを作成したり、機能を無効にすることもできます。

特定のスプレッドシートの互換性チェッカーを無効にする必要がある場合があります。Aspose.CellsのAPIを使用すると、Microsoft Excelで手動でファイルを再保存するときに互換性チェッカーダイアログボックスが表示されないようにこれを動的に行うことができます。

{{% /alert %}}

## **Microsoft Excel の使用**

Microsoft Excel（例: Microsoft Excel 2007/2010）で互換性チェッカーを無効にする場合:

- （Excel 2007）[Office] ボタンをクリックし、「準備」、[互換性の確認] をクリックし、「このブックを保存するときに互換性を確認する」オプションをクリアします.
- （Excel 2010 & 2013）ファイルタブをクリックし、「情報」、[問題を確認] 、[互換性を確認] の順にクリックし、「このブックを保存するときに互換性を確認する」オプションをクリアします.

## **Aspose.CellsのAPIを使用しています**

Microsoft Excelの互換性チェッカーを無効にするには、[**WorkbookSettings.CheckComptiliblity**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckComptiliblity)プロパティを**False**に設定します。

テンプレートXLSファイルがあるとします。ユーザーがMS Excel 2007/2010/2013で保存または再保存すると、以下のスクリーンショットに示すように、互換性チェッカーダイアログボックスが表示されます。

![todo:image_alt_text](disable-compatibility-checker-in-excel_1.png)

次のコードは、Aspose.Cells for Javaで互換性チェッカーを無効にする方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableCompatibilityChecker-DisableCompatibilityChecker.java" >}}
