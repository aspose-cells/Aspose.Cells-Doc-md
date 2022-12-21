---
title: ワークブックの読み込み中に VBA プロジェクトをフィルター処理する
type: docs
weight: 70
url: /ja/java/filter-vba-project-while-loading-a-workbook/
---
## **考えられる使用シナリオ**
一部の .xlsm/.xslb ファイルには、非常に大量のマクロ (または非常に長いマクロ) が含まれています。 Aspose.Cells は、そのようなワークブックを開くときに、この (メタ) データを無条件に読み込みます。多数のワークブックのシート名のみを抽出する必要があるため、そのような不要なコンテンツをスキップする必要がある場合は、LoadDataFilterOptions を使用してこれを制御する必要がある場合があります。このフィルタは、新しいオプション LoadDataFilterOptions.VBA の導入によって提供されます。
## **サンプルコード**
次のサンプル コードは、VBA のみがフィルター処理されるようにブックを読み込みます。この機能をテストするためのサンプル ファイルは、次のリンクからダウンロードできます。

[sampleMacroEnabledWorkbook.xlsm](79527951.xlsm)

// ロード オプションを設定します。VBA はロードしません。
LoadOptions loadOptions = new LoadOptions(LoadFormat.AUTO);
loadOptions.setLoadFilter(new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.VBA));

// 読み込みオプションを使用して、サンプルの Excel ファイルからワークブック オブジェクトを作成します
Workbook book = new Workbook(srcDir + "sampleMacroEnabledWorkbook.xlsm", loadOptions);

// 出力を pdf 形式で保存します
book.save(outDir + "OutputSampleMacroEnabledWorkbook.xlsm", SaveFormat.XLSM);
