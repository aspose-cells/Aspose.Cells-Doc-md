---
title: ワークブックに非表示の外部リンクが含まれているかどうかを確認する
type: docs
weight: 230
url: /ja/net/check-if-workbook-contains-hidden-external-links/
---
## **考えられる使用シナリオ**
ワークブックには、Microsoft Excel で表示できない非表示の外部リンクが含まれている場合があります。 Aspose.Cells は、表示されているかどうかに関係なく、すべての外部リンクを取得します。ただし、次のことを確認できます。[ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible)外部リンクが表示されているかどうかを確認するプロパティ
## **ワークブックに非表示の外部リンクが含まれているかどうかを確認する**
次のサンプル コードは、[ソースエクセルファイル](5115413.xlsx)非表示の外部リンクが含まれています。これらのリンクは Microsoft Excel では表示できませんが、ブック内には存在します。印刷後[ExternalLink.DataSource](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/datasource)と[ExternalLink.IsReferred](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isreferred)プロパティ、それは[ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible)財産。以下のコンソール出力では、外部リンクがすべて表示されていないことがわかります。
### **サンプルコード**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckHiddenExternalLinks-CheckHiddenExternalLinks.cs" >}}
### **コンソール出力**
以下は、上記のサンプル コードを特定のコマンドで実行したときのコンソール出力です。[サンプルエクセルファイル](5115413.xlsx).



{{< highlight "java" >}}

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
