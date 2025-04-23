---
title: スプレッドシートまたはワークブックで使用されるフォントのリストを取得する
description: Aspose.Cellsは、スプレッドシートファイルを操作するためのPythonライブラリです。ドキュメント内で使用されているフォントのリストを取得することをサポートしており、ドキュメントで使用されているフォント情報を得ることができます。この記事では、Aspose.Cells for Python via .NETライブラリを使ってフォントのリストを取得する方法を紹介します。
keywords: Aspose.Cells for Python via .NET、スプレッドシート、ワークブック、フォント、リスト
type: docs
weight: 20
url: /ja/python-net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **可能な使用シナリオ**

作業中のワークブックの使用フォントを知ることは重要です。PDFや画像に変換する際は、必要なすべてのフォントがシステムにインストールされているか、または**フォントディレクトリ**に存在している必要があります。Aspose.Cells for Python via .NETが必要なフォントを見つけられない場合は、システムやフォントディレクトリに存在する適切なフォントに置き換えられます。これは、PDFや画像のレンダリング結果に影響を与え、処理時間も増加します。

このような場合に対処するためには、ワークブックで使用されているフォントを知っておく必要があります。その後、Windows 環境の場合はシステムにフォントをインストールし、Windows やLinux 環境の場合はフォントディレクトリに配置する必要があります。

Aspose.Cells for Python via .NETは、ワークブックやスプレッドシートで使用されているすべてのフォントのリストを返す[**Workbook.get_fonts**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/get_fonts)メソッドを提供します。

## **スプレッドシートまたはブックで使用されているフォントのリストを取得する**

次のサンプルコードは、元のExcelファイルをロードし、それに使用されているフォントのリストを取得します。ダミーフォントがいくつか追加されているダミーワークシートが含まれています。コードがワークブック内のすべてのフォントを印刷すると、これらのダミーフォントも印刷されます。以下のスクリーンショットは、[サンプルExcelファイル](25395211.xlsx)とダミーフォントのリストを示しています。

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-GetListOfFontsUsedInSpreadsheetOrWorkbook.py" >}}

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

