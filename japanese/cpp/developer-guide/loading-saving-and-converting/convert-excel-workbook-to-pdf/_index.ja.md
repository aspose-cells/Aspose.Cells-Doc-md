---
title: Excel ワークブックを PDF に変換
type: docs
weight: 80
url: /ja/cpp/convert-excel-workbook-to-pdf/
---
##  **Excel ワークブックを PDF に変換する**
PDF ファイルは、組織、政府部門、個人の間で文書を交換するために広く使用されています。これは標準のドキュメント形式であり、ソフトウェア開発者はよく Microsoft Excel ファイルを PDF ドキュメントに変換する方法を見つけるように求められます。

Aspose.Cells は、Excel ファイルから PDF への変換をサポートし、変換時に高い視覚的忠実度を維持します。

{{% alert color="primary" %}} 

 Aspose.Cells は、API とバージョン番号に関する情報を出力ドキュメントに直接書き込みます。たとえば、Document を PDF にレンダリングすると、Aspose.Cells for C++ が**応用**値「Aspose.Cells」を持つフィールドと**PDF プロデューサー**値を含むフィールド（例：「Aspose.Cells v18.5.0」）。

Aspose.Cells for C++ に対して、出力ドキュメントからこの情報を変更または削除するように指示することはできないことに注意してください。

{{% /alert %}} 
###  **直接変換**
Aspose.Cells は、他のソフトウェアとは独立して、スプレッドシートから PDF への変換をサポートします。次のコマンドを使用して Excel ファイルを PDF に保存するだけです。[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラス'[保存](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)方法。の[保存](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)メソッドが提供するのは、[保存形式_PDF](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)ネイティブ Excel ファイルを PDF 形式に変換する列挙メンバー。

Excel スプレッドシートを PDF 形式に直接変換するには、以下の手順に従ってください。

1. のオブジェクトをインスタンス化します。[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)空のコンストラクターを呼び出してクラスを作成します。
1. 既存のテンプレート ファイルを開いて読み込むことも、ワークブックを最初から作成する場合はこの手順をスキップすることもできます。
1. Aspose.Cells' API を使用して、スプレッドシート上で作業 (データの入力、書式設定の適用、数式の設定、画像やその他の描画オブジェクトの挿入など) を実行します。
1. スプレッドシートのコードが完成したら、[ワークブック](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)クラス'[保存](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)スプレッドシートを保存するメソッド。

ファイル形式は PDF である必要があるため、SaveFormat 列挙から関連する PDF (事前定義された値) を選択して、最終的な PDF ドキュメントを生成します。

次のサンプルコードを参照してください。[サンプル Excel ファイル](67338368.xlsx)そして[出力PDF](67338369.pdf)ご参考に。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_DirectConversion-new.cpp" >}}
###  **高度な変換**
を使用することもできます。[PDF保存オプション](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)変換用のさまざまな属性を設定するクラス。のさまざまなプロパティを設定する**PDF保存オプション**クラスを使用すると、出力 PDF の印刷、フォント、セキュリティ、圧縮設定を制御できます。最も重要なプロパティは次のとおりです。[コンプライアンスの設定](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setcompliance/)これにより、Excel ファイルを PDF/A 準拠の PDF ファイルに保存できるようになります。
####  **ワークブックを PDF/A コンパイル済みファイルに保存**
次のコード スニペットは、**PDF保存オプション**Excel ファイルを PDF/A 準拠の PDF 形式で保存するクラス

次のサンプルコードとそのコードを参照してください。[出力PDF](67338370.pdf)ご参考に。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_A_CompliedFiles-new.cpp" >}}
####  **PDF 作成時刻を設定します**
とともに**IPdfSaveオプション**クラスでは、PDF の作成時間を取得または設定できます。

次のサンプルコードとそのコードを参照してください。[出力PDF](67338371.pdf)ご参考に。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_SetPDFCreationTime-new.cpp" >}}
