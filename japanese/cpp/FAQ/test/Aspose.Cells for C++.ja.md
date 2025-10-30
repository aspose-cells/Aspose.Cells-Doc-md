# Excelファイルフォーマット用のC++ライブラリ

![バージョン23.11.0](https://img.shields.io/badge/nuget-v23.11.0-blue) ![NuGet](https://img.shields.io/nuget/dt/Aspose.Cells.Cpp)

[![バナー](https://raw.githubusercontent.com/Aspose/aspose.github.io/master/img/banners/aspose_cells-for-cpp-banner.png)](https://releases.aspose.com/cells/cpp/)

[製品ページ](https://products.aspose.com/cells/cpp/) | [ドキュメント](https://docs.aspose.com/cells/cpp/) | [デモ](https://products.aspose.app/cells/family) | [APIリファレンス](https://reference.aspose.com/cells/cpp) | [例](https://github.com/aspose-cells/Aspose.Cells-for-C) | [ブログ](https://blog.aspose.com/category/cells/) | [リリース](https://releases.aspose.com/cells/cpp/) | [無料サポート](https://forum.aspose.com/c/cells) | [一時ライセンス](https://purchase.aspose.com/temporary-license/)

[Aspose.Cells for C++](https://products.aspose.com/cells/cpp/) は、Microsoft Excelファイルを必要とせずに作成、操作、処理、変換するためのネイティブC++ライブラリです。

開発者は、独自のC++アプリケーションから、スプレッドシートの行、列、データ、数式、ピボットテーブル、ワークシート、テーブル、チャート、および描画オブジェクトを操作することができます。

## Aspose.Cells for C++とは？

Aspose.Cells for C++ は、ネイティブC++オンプレミスAPIであり、スプレッドシートの作成、操作、変換機能をC++アプリケーションに統合するためのものです。Microsoft Excel (XLS、XLSX、XLSB、CSVなど) およびOpenOffice/LibreOffice (ODS) の多くの一般的なスプレッドシートファイル形式をサポートしています。

Aspose.Cells for C++ を使用して、Microsoft Visual StudioなどのC++をサポートする開発環境で64ビットアプリケーションを開発できます。Aspose.Cells for C++ は、単にコピーして展開できるネイティブアセンブリです。他のサービスやモジュールの心配は不要です。

Aspose.Cells for C++ を使用すると、Microsoft Excelで組み込みおよびカスタムの文書プロパティを操作できます。ExcelワークブックをPDF/A準拠のファイルに高品質に変換できます。数式、ピボットテーブル、ワークシート、テーブル、範囲、チャート、OLEオブジェクトなど、さまざまな要素と作業できます。

## Excelファイル処理機能

- Microsoft Excelを使用せずにスプレッドシートファイルを開く。
- ローカルコンピュータ上のパスまたはストリームを使用して、[スプレッドシートファイルを開く](https://docs.aspose.com/cells/cpp/different-ways-to-open-files/)。
- ワークシートをさまざまな画像形式に[変換](https://docs.aspose.com/cells/cpp/converting-worksheet-to-different-image-formats/)。
- 好みに応じて、[条件付き書式](https://docs.aspose.com/cells/cpp/apply-conditional-formatting-in-worksheet/)を適用。
- スプレッドシート内の[ピボットテーブル](https://docs.aspose.com/cells/cpp/manipulate-pivot-table/)を操作。
- フォーマットを失わずにテーブルを範囲に[変換](https://docs.aspose.com/cells/cpp/tables-and-ranges/)。
- 行と列のインデックスを指定してセルの名前を取得し、同様にその名前から[セルの行と列のインデックス](https://docs.aspose.com/cells/cpp/names-and-indices/)を取得。
- [ピラミッドチャート、折れ線グラフ、バブルチャート](https://docs.aspose.com/cells/cpp/creating-and-customizing-charts/)、またはカスタムチャートを作成。
- サポートされているチャートタイプを画像やPDFに[レンダリング](https://docs.aspose.com/cells/cpp/chart-rendering/)。
- ワークシートにOLEオブジェクトを[挿入](https://docs.aspose.com/cells/cpp/inserting-ole-objects-into-the-worksheet/)。
- ワークシートに含まれるすべてのOLEオブジェクトにアクセスし、[抽出](https://docs.aspose.com/cells/cpp/extracting-ole-objects-from-worksheet/)。

## サポートされる読み書き形式

**Microsoft Excel:** XLS, XLSX, XLSB, SpreadsheetML\
**Text:** CSV, TSV, TabDelimited\
**OpenDocument:** ODS\
**その他:** HTML、MHTML

## スプレッドシート文書の保存形式

**Microsoft Excel:** XLSM, XLTX, XLTM, XLAM\
**Portable Document Format:** PDF, XPS\
**Text:** CSV, TSV, TabDelimited\
**画像:** SVG、JPEG、PNG、BMP、GIF\
**Web:** HTML, MHTML\
**メタファイル:** EMF\
**その他** DIF

## はじめに

Aspose.Cells for C++を試してみる準備はできていますか？ 単純にVisual Studioのパッケージ マネージャー コンソールから`Install-Package Aspose.Cells.Cpp`を実行して、NuGetパッケージを取得します。 既にAspose.Cells for C++をお持ちでバージョンをアップグレードしたい場合は、最新バージョンを取得するために`Update-Package Aspose.Cells.Cpp`を実行してください。

### C++を使ってXLSをXLSX、XLSB、CSVに変換

以下のスニペットを実行して、APIが環境でどのように機能するかを確認するか、他の一般的な使用シナリオについては[GitHubリポジトリ](https://github.com/aspose-cells/Aspose.Cells-for-C)を確認してください。

```c++
U16String dir(u"your path");
// load the file to be converted
Workbook book(dir + u"template.xls");
// save in different formats
book.Save(dir + u"output.xlsx", SaveFormat::Xlsx);
book.Save(dir + u"output.xlsb", SaveFormat::Xlsb);
book.Save(dir + u"output.csv", SaveFormat::CSV);
book.Save(dir + u"output.json", SaveFormat::Json);
```

### C++でカスタムExcelチャートを作成

```c++
// create a new workbook
Workbook workbook;

// get first worksheet which is created by default
Worksheet worksheet = workbook.GetWorksheets().Get(0);

// add sample data
worksheet.GetCells().Get(u"A1").PutValue(50);
worksheet.GetCells().Get(u"A2").PutValue(100);
worksheet.GetCells().Get(u"A3").PutValue(150);
worksheet.GetCells().Get(u"A4").PutValue(110);
worksheet.GetCells().Get(u"B1").PutValue(260);
worksheet.GetCells().Get(u"B2").PutValue(12);
worksheet.GetCells().Get(u"B3").PutValue(50);
worksheet.GetCells().Get(u"B4").PutValue(100);

// add a chart to the worksheet
int chartIndex = worksheet.GetCharts().Add(Aspose::Cells::Charts::ChartType::Column, 5, 0, 20, 8);

// access the instance of the newly added chart
Chart chart = worksheet.GetCharts().Get(chartIndex);

// add SeriesCollection (chart data source) to the chart ranging from A1 to B4
chart.GetNSeries().Add(u"A1:B4", true);

// set the chart type of 2nd NSeries to display as line chart
chart.GetNSeries().Get(1).SetType(
	Aspose::Cells::Charts::ChartType::Line);

// save the Excel file
workbook.Save(u"output.xlsx");
```

[製品ページ](https://products.aspose.com/cells/cpp/) | [ドキュメント](https://docs.aspose.com/cells/cpp/) | [デモ](https://products.aspose.app/cells/family) | [APIリファレンス](https://reference.aspose.com/cells/cpp) | [例](https://github.com/aspose-cells/Aspose.Cells-for-C) | [ブログ](https://blog.aspose.com/category/cells/) | [リリース](https://releases.aspose.com/cells/cpp/) | [無料サポート](https://forum.aspose.com/c/cells) | [一時ライセンス](https://purchase.aspose.com/temporary-license/)
{{< app/cells/assistant language="cpp" >}}
