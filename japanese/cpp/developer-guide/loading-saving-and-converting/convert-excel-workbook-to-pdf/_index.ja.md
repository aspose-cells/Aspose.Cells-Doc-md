---
title: Excel ワークブックを PDF に変換
type: docs
weight: 80
url: /ja/cpp/convert-excel-workbook-to-pdf/
---
## **Excel ワークブックを PDF に変換する**
PDF ファイルは、組織、政府部門、および個人の間でドキュメントを交換するために広く使用されています。これは標準的なドキュメント形式であり、ソフトウェア開発者は、Microsoft Excel ファイルを PDF ドキュメントに変換する方法を見つけるように求められることがよくあります。

Aspose.Cells は、Excel ファイルの PDF への変換をサポートし、変換で高い視覚的忠実度を維持します。

{{% alert color="primary" %}} 

 Aspose.Cells は、出力ドキュメントに API とバージョン番号に関する情報を直接書き込みます。たとえば、Document を PDF にレンダリングすると、Aspose.Cells for C++ が**応用**値が「Aspose.Cells」のフィールドと**PDF プロデューサー**値を持つフィールド、例えば「Aspose.Cells v18.5.0」。

出力ドキュメントからこの情報を変更または削除するように Aspose.Cells for C++ に指示することはできないことに注意してください。

{{% /alert %}} 
### **直接変換**
Aspose.Cells は、他のソフトウェアとは独立してスプレッドシートから PDF への変換をサポートします。を使用して Excel ファイルを PDF に保存するだけです。[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)クラス'[セーブ](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)方法。の[セーブ](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)メソッドは、[SaveFormat_Pdf](https://reference.aspose.com/cells/cpp/namespace/aspose.cells#a11cae527e4e68f1adcac8f47ea64481a)ネイティブ Excel ファイルを PDF 形式に変換する列挙型メンバー。

以下の手順に従って、Excel スプレッドシートを PDF 形式に直接変換します。

1. のオブジェクトをインスタンス化する[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)空のコンストラクターを呼び出してクラスを作成します。
1. ワークブックを最初から作成する場合は、既存のテンプレート ファイルを開いて読み込むか、この手順をスキップできます。
1. Aspose.Cells' API を使用して、スプレッドシートで任意の作業 (データの入力、書式の適用、数式の設定、画像やその他の描画オブジェクトの挿入など) を実行します。
1. スプレッドシート コードが完成したら、[Iワークブック](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)クラス'[セーブ](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)スプレッドシートを保存するメソッド。

ファイル形式は PDF である必要があるため、SaveFormat 列挙から関連する PDF (定義済みの値) を選択して、最終的な PDF ドキュメントを生成します。

次のサンプル コードを参照してください。[サンプル Excel ファイル](67338368.xlsx)と[出力 PDF](67338369.pdf)ご参考までに。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_DirectConversion.cpp" >}}
### **高度な変換**
また、[IPdfSaveOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_pdf_save_options)クラスを使用して、変換用にさまざまな属性を設定します。のさまざまなプロパティの設定**IPdfSaveOptions**クラスを使用すると、出力 PDF の印刷、フォント、セキュリティ、および圧縮設定を制御できます。最も重要なプロパティは次のとおりです。[コンプライアンスの設定](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_pdf_save_options#a2158ff23d7c071f8224b1cd063233c07)これにより、Excel ファイルを PDF/A 準拠の PDF ファイルに保存できます。
#### **ワークブックを PDF/A コンパイル済みファイルに保存する**
次のコード スニペットは、**IPdfSaveOptions**Excel ファイルを PDF/A 準拠の PDF 形式で保存するクラス

次のサンプル コードとそのコードを参照してください。[出力 PDF](67338370.pdf)ご参考までに。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_A_CompliedFiles.cpp" >}}
#### **PDF 作成時刻を設定します**
とともに**IPdfSaveOptions**クラスでは、PDF の作成時刻を取得または設定できます。

次のサンプル コードとそのコードを参照してください。[出力 PDF](67338371.pdf)ご参考までに。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertExcelWorkbookToPDF_SetPDFCreationTime.cpp" >}}
