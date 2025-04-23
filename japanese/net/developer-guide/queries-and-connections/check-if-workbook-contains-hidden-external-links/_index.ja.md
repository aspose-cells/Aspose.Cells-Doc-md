---
title: ワークブックに非表示の外部リンクが含まれているかどうかを確認
type: docs
weight: 230
url: /ja/net/check-if-workbook-contains-hidden-external-links/
---

## **可能な使用シナリオ**
ワークブックには、Microsoft Excelで表示できない非表示の外部リンクが含まれることがあります。Aspose.Cellsは、表示されるか非表示であろうと、すべての外部リンクを取得しますが、[ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible) プロパティをチェックして、外部リンクが表示されるかどうかを確認できます。
## **ワークブックに非表示の外部リンクが含まれる [ソースExcelファイル](5115413.xlsx) をロードする以下のサンプルコードでは、Microsoft Excelで表示されない非表示の外部リンクが含まれています。 [ExternalLink.DataSource](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/datasource) および [ExternalLink.IsReferred](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isreferred) プロパティを出力した後、[ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible) プロパティを出力します。以下のコンソール出力では、すべての外部リンクが非表示であることがわかります。**
[元のExcelファイル](5115413.xlsx)を読み込み、非表示の外部リンクが含まれています。これらのリンクはMicrosoft Excelで表示することはできませんが、ワークブック内に存在します。 [ExternalLink.DataSource](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/datasource)および[ExternalLink.IsReferred](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isreferred)プロパティを印刷した後、[ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible)プロパティを印刷します。以下のコンソール出力では、すべての外部リンクが表示されていないことがわかります。
### **サンプルコード**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckHiddenExternalLinks-CheckHiddenExternalLinks.cs" >}}
### **コンソール出力**
与えられた [サンプルExcelファイル](5115413.xlsx) で上記のサンプルコードを実行した場合の、コンソール出力は次のとおりです。



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
{{< app/cells/assistant language="csharp" >}}
