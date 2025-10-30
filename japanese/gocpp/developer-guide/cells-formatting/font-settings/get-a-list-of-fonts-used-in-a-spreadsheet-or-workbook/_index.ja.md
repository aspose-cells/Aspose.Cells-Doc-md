---
title: Golang経由のC++でスプレッドシートまたはブックで使用されているフォントの一覧を取得
linktitle: フォントのリストを取得
description: Aspose.Cellsは、スプレッドシートファイルの操作に使用されるC++ライブラリです。スプレッドシートまたはワークブックで使用されているフォントのリストを取得でき、ドキュメント内で使用されているフォント情報を取得することが可能です。この記事では、Aspose.Cellsライブラリを使用してフォントのリストを取得する方法を紹介します。
keywords: Aspose.Cells、スプレッドシート、ワークブック、フォント、リスト
type: docs
weight: 20
url: /ja/go-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **可能な使用シナリオ**

レンダリング目的でワークブックで使用されているフォントを知ることはしばしば必要です。ワークブックをPDFや画像に変換する場合、Aspose.Cells は必要なすべてのフォントがシステムにインストールされているか、または **fonts ディレクトリ** に存在する必要があります。Aspose.Cells が必要なフォントを見つけられない場合、他の適切なフォントで置き換えようとします。これにより、PDFや画像の不要なレンダリングが発生し、適切なフォントの検索に処理時間がかかります。

このような場合に対処するためには、ワークブックで使用されているフォントを知っておく必要があります。その後、Windows 環境の場合はシステムにフォントをインストールし、Windows やLinux 環境の場合はフォントディレクトリに配置する必要があります。

Aspose.Cells では、ワークブックやスプレッドシートで使用されているフォントのリストを返す [**Workbook.GetFonts**](https://reference.aspose.com/cells/go-cpp/workbook/getfonts/) メソッドが提供されています。

## **スプレッドシートまたはブックで使用されているフォントのリストを取得する**

次のサンプルコードは、元のExcelファイルをロードし、それに使用されているフォントのリストを取得します。ダミーフォントがいくつか追加されているダミーワークシートが含まれています。コードがワークブック内のすべてのフォントを印刷すると、これらのダミーフォントも印刷されます。以下のスクリーンショットは、[サンプルExcelファイル](25395211.xlsx)とダミーフォントのリストを示しています。

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetAListOfFontsUsedInASpreadsheetOrWorkbook.go" >}}
## **コンソール出力**

与えられた [サンプルエクセルファイル](25395211.xlsx) を使用して上記のサンプルコードを実行した場合のコンソール出力は次のとおりです。

{{< highlight java >}}

Aspose.Cells.Font [ Calibri; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Arial; 10; Regular; Color [A=255, R=0, G=0, B=0] ]

Aspose.Cells.Font [ Calibri; 10; Bold; Color [Black] ]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=128, G=128, B=128] ]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Calibri; 36; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 20; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Calibri; 11; Italic; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [Black] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 12; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Dummy-Arial-X; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Arial-Y; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Arial-Z; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-I; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-II; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-III; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Calibri; 10.5; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 20; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104] ]

{{< /highlight >}}
