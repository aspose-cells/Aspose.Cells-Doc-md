---
title: 選択したチャート アイテムを Excel チャートにレンダリングする
type: docs
weight: 30
url: /ja/reportingservices/render-selected-chart-items-to-excel-charts/
---
{{% alert color="primary" %}} 

レポート内の一部のグラフのみを Excel グラフに表示するには:

1. 開く**Aspose.Cells.ReportingServices.xml**ファイル。
1. の構成パラメータを変更します。**Aspose.Cells.ReportingServices.xml**ファイル。
1. 必要なレポート構成情報を追加します。
1. 編集可能なグラフとしてエクスポートしたくないグラフ アイテムの情報を追加します。これらのアイテムは静止画像としてエクスポートされます。

例えば：

{{< highlight "java" >}}

 <Chart >

<Report name= "Employee Sales Summary 2008">

<ChartItem name="Chart1" type="image"/>

</Report >

</Chart> 

{{< /highlight >}}

**画像としてエクスポートされたグラフ** 

![todo:画像_代替_文章](render-selected-chart-items-to-excel-charts_1.png)

**編集可能な Excel チャートとしてエクスポートされたチャート** 

![todo:画像_代替_文章](render-selected-chart-items-to-excel-charts_2.png)

{{% /alert %}}
