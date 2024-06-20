---
title: 選択したチャート項目をExcelチャートにレンダリングする
type: docs
weight: 30
url: /ja/reportingservices/render-selected-chart-items-to-excel-charts/
---

{{% alert color="primary" %}} 

レポート内の一部のチャートのみをExcelチャートにレンダリングするには:

1. **Aspose.Cells.ReportingServices.xml** ファイルを開きます。
1. **Aspose.Cells.ReportingServices.xml** ファイルの構成パラメータを変更します。
1. 希望するレポートの構成情報を追加します。
1. エクスポートしたいチャート項目の情報を追加します。これらの項目は静止画像としてエクスポートされます。

例:

{{< highlight java >}}

 <Chart >

<Report name= "Employee Sales Summary 2008">

<ChartItem name="Chart1" type="image"/>

</Report >

</Chart> 

{{< /highlight >}}

**画像としてエクスポートされるチャート** 

![todo:image_alt_text](render-selected-chart-items-to-excel-charts_1.png)

**編集可能なExcelチャートとしてエクスポートされるチャート** 

![todo:image_alt_text](render-selected-chart-items-to-excel-charts_2.png)

{{% /alert %}}
