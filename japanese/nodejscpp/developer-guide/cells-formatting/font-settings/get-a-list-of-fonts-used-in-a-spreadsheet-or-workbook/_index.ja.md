---
title: スプレッドシートまたはワークブックで使用されるフォントのリストを取得する
linktitle: スプレッドシートまたはワークブックで使用されるフォントのリストを取得する
description: Aspose.Cells for Node.js via C++を使用して、スプレッドシートまたはワークブックで使用されているフォントのリストを取得する方法を学びます。この記事では、ドキュメントからフォント情報を取得する方法を示します。
keywords: Aspose.Cells、Node.js via C++、スプレッドシート、ワークブック、フォント、リスト
type: docs
weight: 20
url: /ja/nodejs-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **可能な使用シナリオ**

レンダリング目的でワークブックで使用されているフォントを知ることはしばしば必要です。ワークブックをPDFや画像に変換する場合、Aspose.Cells は必要なすべてのフォントがシステムにインストールされているか、または **fonts ディレクトリ** に存在する必要があります。Aspose.Cells が必要なフォントを見つけられない場合、他の適切なフォントで置き換えようとします。これにより、PDFや画像の不要なレンダリングが発生し、適切なフォントの検索に処理時間がかかります。

そのようなケースに対処するには、ワークブックが使用しているフォントを知る必要があります。Windows環境の場合はシステムにそのフォントをインストールし、LinuxやWindows環境の場合はフォントディレクトリに配置します。

Aspose.Cells for Node.js via C++は、 [**Workbook.getFonts**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getFonts--)メソッドを提供しており、これによりワークブックやスプレッドシートで使用されている全フォントのリストを取得できます。

## **スプレッドシートまたはブックで使用されているフォントのリストを取得する**

次のサンプルコードは、元のExcelファイルをロードし、それに使用されているフォントのリストを取得します。ダミーフォントがいくつか追加されているダミーワークシートが含まれています。コードがワークブック内のすべてのフォントを印刷すると、これらのダミーフォントも印刷されます。以下のスクリーンショットは、[サンプルExcelファイル](25395211.xlsx)とダミーフォントのリストを示しています。

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-GetFontsListUsedInWorkbook.js" >}}


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
{{< app/cells/assistant language="nodejs-cpp" >}}
