﻿---
title: ワークシートを CSV に変換
type: docs
weight: 30
url: /ja/java/convert-worksheet-to-csv/
---
## **Aspose.Cells - ワークシートを CSV に変換**
開発者がファイルを保存場所に保存する必要がある場合は、ファイル名 (完全な保存パスを含む) と目的のファイル形式 (**ファイル形式の種類**列挙) の呼び出し中**セーブ**方法**ワークブック**物体。

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook with Excel file path

Workbook workbook = new Workbook(dataPath + "workbook.xls");

//Save the document in PDF format

workbook.save(dataPath + "AsposeWorkbookCSV.csv", SaveFormat.CSV);

{{< /highlight >}}
## **Apache POI SS - HSSF & XSSF - ワークシートを CSV に変換**
以下のコードは、Aspose.Cells Java API と比較して、Apache POI HSSF および XSSF API を使用してワークシートを CSV に変換する方法を示しています。

**Java**

{{< highlight "java" >}}

 /**

\* 基本的な XLSX -> CSV をモデルにしたプロセッサ

\* POI サンプル プログラム XLS2CSVmra by Nick Burch

\* パッケージ org.apache.poi.hssf.eventusermodel.examples.

\* HSSF バージョンとは異なり、これは完全に無視されます

\* 行がありません。

\* <p/>

\* データ シートは SAX パーサーを使用して読み込まれ、

\* メモリ使用量が比較的小さいため、これは

\* 巨大なワークブックを読むことができます。スタイル テーブルと

\* 共有文字列テーブルはメモリに保持する必要があります。の

\* 標準の POI スタイル テーブル クラスが使用されますが、カスタム

\* (読み取り専用) クラスは共有文字列テーブルに使用されます

\* 標準の POI SharedStringsTable が非常に大きくなるため

\* 一意の文字列の数ですばやく。

\* <p/>

\* 問題を修正するパッチを提供してくれた Eric Smith に感謝します

\* 複数の "t" 要素を持つセルによってトリガーされます。

\* Excel がさまざまな形式を表す方法 (たとえば、1 つの単語

\* プレーンで 1 単語太字)。

\*

\* @作者 クリス・ロット

*/

public class ApacheXLSX2CSV {