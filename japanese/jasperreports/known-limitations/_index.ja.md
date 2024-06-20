---
title: 既知の制限事項
type: docs
weight: 50
url: /ja/jasperreports/known-limitations/
---

{{% alert color="primary" %}} 

現在、Aspose.Cells for JasperReportsでサポートされていない機能のリストです：

- **自動インストーラーはありません**。Aspose.Cells for JasperReportsはZIPアーカイブとして配布されます。[インストール](/cells/ja/jasperreports/installation/)するには、適切な場所にファイルを展開し、おそらくいくつかのXML設定ファイルを編集する必要があります。将来的には自動インストーラーが提供されます。
- **ExcelがすべてのJasperReportsチャートタイプをサポートしていません**。JasperReportsの一部のチャートタイプはMicrosoft Excelのチャートと互換性がないため、例：XYBarChart、XYAreaChart、ThermometerChart、CandlestickChart、HighLowChart、MultipleAxisChart、MeterChart。これらのチャートは画像としてエクスポートされ、オリジナルのJasperReports XLSエクスポーターがチャートを処理する方法と同じです。（その他のチャートは編集可能なチャートとしてエクスポートされます。）

{{% /alert %}}
