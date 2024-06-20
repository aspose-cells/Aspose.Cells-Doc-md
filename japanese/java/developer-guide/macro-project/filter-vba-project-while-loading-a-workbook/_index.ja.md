---
title: ワークブックを読み込む際にVBAプロジェクトをフィルタリングする
type: docs
weight: 70
url: /ja/java/filter-vba-project-while-loading-a-workbook/
---

## **可能な使用シナリオ**
.xlsm/.xslbファイルには非常に大量のマクロ（または非常に長いマクロ）が含まれている場合があります。 Aspose.Cellsはそのようなワークブックを開くときに、この（メタ）データを無条件に読み込みます。大量のワークブックからシート名のみを抽出する必要がある場合には、LoadDataFilterOptionsを使用してこれを制御する必要があります。このフィルタは、新しいオプションLoadDataFilterOptions.VBAを導入することで提供されています。
## **サンプルコード**
次のサンプルコードでは、VBAのみがフィルタリングされるようにワークブックを読み込みます。この機能をテストするためのサンプルファイルは、次のリンクからダウンロードできます。

[sampleMacroEnabledWorkbook.xlsm](79527951.xlsm)

// ロードオプションを設定し、VBAを読み込まない
LoadOptions loadOptions = new LoadOptions(LoadFormat.AUTO);
loadOptions.setLoadFilter(new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.VBA));

// ロードオプションを使用してサンプルのExcelファイルからワークブックオブジェクトを作成する
Workbook book = new Workbook(srcDir + "sampleMacroEnabledWorkbook.xlsm", loadOptions);

// 出力をPDF形式で保存
book.save(outDir + "OutputSampleMacroEnabledWorkbook.xlsm", SaveFormat.XLSM);
