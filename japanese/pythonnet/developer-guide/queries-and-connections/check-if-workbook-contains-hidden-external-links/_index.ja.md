---
title: ワークブックに非表示の外部リンクが含まれているかどうかを確認
type: docs
weight: 230
url: /ja/python-net/check-if-workbook-contains-hidden-external-links/
---

## **可能な使用シナリオ**
場合によっては、ワークブックに外部リンクが含まれていることがあり、これらは隠されていて Microsoft Excel では閲覧できません。Aspose.Cells for Python via .NET では、可視・非可視にかかわらずすべての外部リンクを取得します。ただし、[ExternalLink.is_visible](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/is_visible) プロパティで外部リンクが表示されているかどうかを確認できます。

## **ワークブックに非表示の外部リンクが含まれる [ソースExcelファイル](5115413.xlsx) をロードする以下のサンプルコードでは、Microsoft Excelで表示されない非表示の外部リンクが含まれています。 [ExternalLink.DataSource](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/datasource) および [ExternalLink.IsReferred](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isreferred) プロパティを出力した後、[ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible) プロパティを出力します。以下のコンソール出力では、すべての外部リンクが非表示であることがわかります。**
以下のサンプルコードは、隠された外部リンクを含む [source excel file](5115413.xlsx) をロードします。これらのリンクは Microsoft Excel では閲覧できませんが、ワークブック内に存在します。[ExternalLink.data_source](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/data_source) と [ExternalLink.is_referred](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/is_referred) のプロパティを出力した後、[ExternalLink.is_visible](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/is_visible) のプロパティも出力します。以下のコンソール出力では、すべての外部リンクが見えません。

### **サンプルコード**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-CheckHiddenExternalLinks.py" >}}

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

{{< app/cells/assistant language="python-net" >}}
