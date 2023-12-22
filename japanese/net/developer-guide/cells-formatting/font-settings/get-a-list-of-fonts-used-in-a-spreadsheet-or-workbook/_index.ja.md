---
title: スプレッドシートまたはワークブックで使用されているフォントのリストを取得する
description: Aspose.Cells は、スプレッドシート ファイルを操作するための .NET ライブラリです。スプレッドシートまたはワークブックで使用されているフォントのリストの取得をサポートしているため、ユーザーはドキュメントで使用されているフォント情報を取得できます。この記事では、Aspose.Cells ライブラリを使用してフォントのリストを取得する方法を説明します。
keywords: Aspose.Cells, Spreadsheet, Workbook, Font, List
type: docs
weight: 20
url: /ja/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---
##  **考えられる使用シナリオ**

多くの場合、レンダリングの目的でワークブックで使用されているフォントを知ることが必要になります。ワークブックを PDF またはイメージに変換する場合、Aspose.Cells では、必要なフォントがすべてシステムにインストールされているか、*fonts ディレクトリ** に存在する必要があります。 Aspose.Cells が必要なフォントを見つけられない場合、システムまたはフォント ディレクトリに存在し、実際のフォントを置き換えることができる他の適切なフォントで置き換えようとします。これにより、PDF または画像の望ましくないレンダリングが発生するだけでなく、適切なフォントを見つけるのに処理時間がかかります。

このようなケースに対処するには、ワークブックでどのフォントが使用されているかを把握し、Windows 環境の場合はそれらのフォントをシステムにインストールするか、Windows または Linux 環境の場合はフォント ディレクトリに配置する必要があります。

 Aspose.Cells は、**[Workbook.GetFonts](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getfonts)**ワークブックまたはスプレッドシートで使用されているすべてのフォントのリストを返すメソッド。

##  **スプレッドシートまたはワークブックで使用されているフォントのリストを取得する**

次のサンプル コードは、ソース Excel ファイルをロードし、その中で使用されているフォントのリストを取得します。説明のためにいくつかのダミー フォントが追加されたダミー ワークシートが 1 つあります。コードはブック内のすべてのフォントを印刷するときに、それらのダミー フォントも印刷します。次のスクリーンショットは、[サンプルエクセルファイル](25395211.xlsx)ダミーフォントがどのようにリストされるか。

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

##  **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-GetListOfFontsUsedInSpreadsheetOrWorkbook.cs" >}}

##  **コンソール出力**

以下は、指定されたコマンドを使用して実行した場合の上記のサンプル コードのコンソール出力です。[サンプルエクセルファイル](25395211.xlsx).

{{< highlight "java" >}}

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
