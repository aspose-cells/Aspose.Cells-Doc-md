---
title: ExcelワークブックをPDFに変換する
type: docs
weight: 80
url: /ja/go-cpp/convert-excel-workbook-to-pdf/
---

## **ExcelワークブックをPDFに変換する**

Aspose.Cellsは、ExcelファイルをPDFに変換する機能をサポートし、変換時に高い視覚的忠実度を維持します。

{{% alert color="primary" %}}

 Aspose.CellsはAPIおよびバージョン番号の情報を出力ドキュメントに直接書き込みます。例えば、ドキュメントをPDFにレンダリングすると、Aspose.Cells for Go via C++は**Application**フィールドに'Aspose.Cells'を、**PDF Producer**フィールドに'aspose.Cells v24.12.0'のような値を設定します。

この情報の変更や削除については、Aspose.Cells for Go via C++に指示を出すことはできませんのでご了承ください。

{{% /alert %}}

### **直接変換**

以下の手順に従って、Excelスプレッドシートを直接PDF形式に変換します:

1. 空のコンストラクタを呼び出して [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) クラスのオブジェクトをインスタンス化します。
1. 既存のテンプレートファイルを開いたり読み込んだりするか、ワークブックをゼロから作成している場合は、この手順をスキップします。
1. Aspose.CellsのAPIを使用して、スプレッドシート上で作業を行います（入力データ、書式設定の適用、数式の設定、画像の挿入など）。
1. スプレッドシートのコードが完了したら、[Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) クラスの [Save](https://reference.aspose.com/cells/go-cpp/workbook/save/) メソッドを呼び出してスプレッドシートを保存します。

ファイル形式はPDFにすべきです。したがって、 [SaveFormat](https://reference.aspose.com/cells/ja) の列挙から適切なPDF（事前定義された値）を選択して最終的なPDFドキュメントを生成します。

以下のサンプルコード、サンプルExcelファイル([67338368.xlsx](#))、および[出力PDF](#)を参照してください。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveWorkbookAsPDF.go" >}}
