# Excelファイルフォーマット用Goライブラリ

![バージョン 24.11.0](https://img.shields.io/badge/go-v24.11.0-blue)

[製品ページ](https://products.aspose.com/cells/go-cpp/) | [ドキュメント](https://docs.aspose.com/cells/go-cpp/) | [デモ](https://products.aspose.app/cells/family) | [APIリファレンス](https://reference.aspose.com/cells/go-cpp) | [例](https://github.com/aspose-cells/aspose-cells-go-cpp) | [ブログ](https://blog.aspose.com/category/cells/) | [リリース](https://releases.aspose.com/cells/go-cpp/) | [無料サポート](https://forum.aspose.com/c/cells) | [一時的ライセンス](https://purchase.aspose.com/temporary-license/)

[Aspose.Cells for Go via C++](https://products.aspose.com/cells/go-cpp/)は、Microsoft Officeや自動化を必要とせずに、Microsoft Excelファイルを作成、操作、処理、変換するネイティブGoライブラリです。Excel Go APIは、Excel 97-2003（XLS）、Excel 2007-2013/2016（XLSX、XLSM、XLSB）、OpenOffice XML、CSV、TSVなどの他の形式もサポートしています。

開発者が自身のGoアプリケーションからスプレッドシートの行、列、データ、数式、ピボットテーブル、ワークシート、テーブル、チャート、描画オブジェクトを操作できるようにします。

## Aspose.Cells for Go via C++とは何ですか？

Aspose.Cells for Go via C++は、Go環境でスプレッドシートの作成、操作、変換機能を統合するためのネイティブなオンプレミスAPIです。Microsoft Excel（XLS、XLSX、XLSB、CSVなど）およびOpenOffice/LibreOffice（ODS）の多くの人気ファイル形式に対応しています。

Aspose.Cells for Go via C++を使用して、Microsoft Visual StudioなどのGoをサポートする任意の開発環境で64ビットアプリケーションを開発できます。Aspose.Cells for Go via C++はネイティブアセンブリであり、単にコピーして展開できます。他のサービスやモジュールについて気にする必要はありません。

Aspose.Cells for Go via C++を使用して、Microsoft Excelの内蔵およびカスタムドキュメントプロパティを操作できます。ExcelのワークブックをPDF/A準拠のファイルに高品質に変換します。数式、ピボットテーブル、ワークシート、テーブル、範囲、チャート、OLEオブジェクトなどと作業します。

## Excelファイル処理機能

- Microsoft Excelを使用せずにスプレッドシートファイルを開く。
- [ローカルコンピュータのパスまたはストリームを通じてExcelファイルを開く](https://docs.aspose.com/cells/go/different-ways-to-open-files/)
- [ワークシートを異なる画像形式に変換](https://docs.aspose.com/cells/go/converting-worksheet-to-different-image-formats/)
- [条件付き書式を適用](https://docs.aspose.com/cells/go/apply-conditional-formatting-in-worksheet/)
- [ピボットテーブルを操作](https://docs.aspose.com/cells/go/manipulate-pivot-table/)
- [テーブルを範囲に変換](https://docs.aspose.com/cells/go/tables-and-ranges/)し、フォーマットを失わない
- 行と列のインデックスを提供してセルの名前を取得し、同様に[名前から行と列のインデックスを取得](https://docs.aspose.com/cells/go/names-and-indices/)できます。
- [ピラミッドチャート、折れ線チャート、バブルチャート](https://docs.aspose.com/cells/go/creating-and-customizing-charts/) やカスタムチャートを作成
- [サポートされているチャートタイプを画像またはPDFにレンダリング](https://docs.aspose.com/cells/go/chart-rendering/)
- [ワークシートにOLEオブジェクトを挿入](https://docs.aspose.com/cells/go/inserting-ole-objects-into-the-worksheet/)
- [ワークシート内のすべてのOLEオブジェクトにアクセスし抽出](https://docs.aspose.com/cells/go/extracting-ole-objects-from-worksheet/)

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

Aspose.Cells for Go via C++を試す準備はできましたか？ 単に `go get -u github.com/aspose-cells/aspose-cells-go-cpp` を実行し、Goファイルから `github.com/aspose-cells/aspose-cells-go-cpp` をインポートしてください。すでにAspose.Cells for Go via C++を持っていてバージョンをアップグレードしたい場合は、`go get github.com/aspose-cells/aspose-cells-go-cpp@v24.12.0` を実行して最新バージョンを取得してください。

### Goを使ったXLSからXLSX、XLSB、CSVへの変換

以下のスニペットを実行してAPIの動作を確認するか、他の一般的な使用例については [GitHubリポジトリ](https://github.com/aspose-cells/aspose-cells-go-cpp) を確認してください。

```Go
lic, _ := NewLicense()
lic.SetLicense_String(os.Getenv("LicensePath"))
workbook, err1 := NewWorkbook_String("Book1.xlsx")
if err1 != nil {
    println(err1)
}
workbook.Save_String("Book1.pdf")
workbook.Save_String("Book1.png")
workbook.Save_String("Book1.txt")
workbook.Save_String("Book1.ods")
workbook.Save_String("Book1.md")
workbook.Save_String("Book1.json")
workbook.Save_String("Book1.html")
```

### Goを使ったカスタムExcelチャートの作成

```Go
package main

import (
 . "asposecells"
 "os"
)

func main() {
 lic, _ := NewLicense()
 lic.SetLicense_String(os.Getenv("LicensePath"))

 workbook, _ := NewWorkbook()
 worksheets, _ := workbook.GetWorksheets()
 worksheet, _ := worksheets.Get_Int(0)
 cells, _ := worksheet.GetCells()
 cell, _ := cells.Get_String("A1")
 cell.PutValue_Int(50)
 cell, _ = cells.Get_String("A2")
 cell.PutValue_Int(100)
 cell, _ = cells.Get_String("A3")
 cell.PutValue_Int(150)
 cell, _ = cells.Get_String("B1")
 cell.PutValue_Int(4)
 cell, _ = cells.Get_String("B2")
 cell.PutValue_Int(20)
 cell, _ = cells.Get_String("B3")
 cell.PutValue_Int(50)
 charts, _ := worksheet.GetCharts()
 chartIndex, _ := charts.Add_ChartType_Int_Int_Int_Int(ChartType_Pyramid, 5, 0, 20, 8)
 chart, _ := charts.Get_Int(chartIndex)
 series, _ := chart.GetNSeries()
 series.Add_String_Bool("A1:B3", true)
 workbook.Save_String("CreateChart.xlsx")
}

```

[製品ページ](https://products.aspose.com/cells/go-cpp/) | [ドキュメント](https://docs.aspose.com/cells/go-cpp/) | [デモ](https://products.aspose.app/cells/family) | [APIリファレンス](https://reference.aspose.com/cells/go-cpp) | [例](https://github.com/aspose-cells/aspose-cells-go-cpp) | [ブログ](https://blog.aspose.com/category/cells/) | [リリース](https://releases.aspose.com/cells/go-cpp/) | [無料サポート](https://forum.aspose.com/c/cells) | [一時的ライセンス](https://purchase.aspose.com/temporary-license/)
