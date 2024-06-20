---
title: ワークブックに非表示の外部リンクが含まれているかどうかを確認
type: docs
weight: 950
url: /ja/java/check-if-workbook-contains-hidden-external-links/
---

## **可能な使用シナリオ**
ワークブックにはMicrosoft Excelで表示されない隠れた外部リンクが含まれている場合があります。Aspose.Cellsは表示されているか非表示かに関係なくすべての外部リンクを取得します。ただし、外部リンクが見えるかどうかを確認するには、[ExternalLink.IsVisible](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsVisible) プロパティを確認できます。
## **ワークブックに非表示の外部リンクが含まれる [ソースExcelファイル](5115413.xlsx) をロードする以下のサンプルコードでは、Microsoft Excelで表示されない非表示の外部リンクが含まれています。 [ExternalLink.DataSource](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/datasource) および [ExternalLink.IsReferred](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isreferred) プロパティを出力した後、[ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible) プロパティを出力します。以下のコンソール出力では、すべての外部リンクが非表示であることがわかります。**
次のサンプルコードでは、Microsoft Excelで見ることができない隠れた外部リンクを含む[ソースExcelファイル](5472525.xlsx)をロードします。外部リンクデータソースと[ExternalLink.IsReferred](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsReferred) プロパティを表示し、[ExternalLink.IsVisible](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsVisible) プロパティを表示します。以下のコンソール出力では、すべての外部リンクが表示されていないことが分かります。
## **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckWorkbookContainsHiddenExternalLinks-CheckWorkbookContainsHiddenExternalLinks.java" >}}
## **コンソール出力**
以下は、与えられた[サンプルExcelファイル](5472525.xlsx)を使用して上記のサンプルコードを実行したときのコンソール出力です。



{{< highlight java >}}

 Data Source: C:\International\DDB\FAS 133\Swap Rates\GS_1M_3M_1_2_5_¥$_(B)IRSwaps_0400.xls

Is Referred: True

Is Visible: False

Data Source: C:\DIST DAY\MAY TEMPLATES\030601t.xls

Is Referred: True

Is Visible: False

Data Source: C:\AREVIEW\2002 Controllable\Autobrct.xls

Is Referred: True

Is Visible: False

Data Source: C:\CARDSFO\Main Files\Rate Forecast\FY 11\IFR 11 01 (New Model REPORTS 11.08.07).xls

Is Referred: True

Is Visible: False

{{< /highlight >}}
