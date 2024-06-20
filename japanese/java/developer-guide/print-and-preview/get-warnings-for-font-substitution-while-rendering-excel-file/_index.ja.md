---
title: Excelファイルをレンダリングする際にフォントの置換ワーニングを取得
type: docs
weight: 120
url: /ja/java/get-warnings-for-font-substitution-while-rendering-excel-file/
---

{{% alert color="primary" %}}

Microsoft ExcelファイルをPDFにレンダリングする際に、Aspose.Cellsがフォントを置換することがあります。Aspose.Cellsには、特定のフォントが置換されたことを開発者に伝える機能が用意されています。これは便利な機能であり、Aspose.CellsによるPDFのレンダリング結果が実際のExcelファイルと異なる理由を特定して適切な対策を取るのに役立ちます。たとえば、不足しているフォントをインストールして、レンダリング結果が同じに見えるようにすることができます。

ExcelファイルをPDFにレンダリングする際にフォント置換のワーニングを取得したい場合は、IWarningCallbackインタフェースを実装し、PdfSaveOptions.setWarningCallback()メソッドを実装したインタフェースに設定します。

{{% /alert %}}

以下のスクリーンショットは、次のコードで使用されるソースExcelファイルを示しています。A6セルとA7セルには、Microsoft Excelによって適切にレンダリングされないフォントのテキストが含まれています。

![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)

Aspose.Cellsは、セルA6とA7のフォントを適切なフォントで置き換えます。

![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)

## **ソースファイルと出力PDFのダウンロード**

以下のリンクからソースExcelファイルと出力PDFをダウンロードできます

- [source.xlsx](5472700.xlsx)
- [output.pdf](5472699.pdf)

[**IWarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback)を実装して[**PdfSaveOptions.setWarningCallback()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#WarningCallback)メソッドを実装するコードは以下の通りです。これにより、セル内でフォントが置換されるたびに、Aspose.CellsはWarningCallback.warning()メソッド内で警告を発生させます。

{{< highlight java >}}

 public class WarningCallback implements IWarningCallback {

    @Override

    public void warning(WarningInfo info) {

        if(info.getWarningType() == WarningType.FONT_SUBSTITUTION)

        {

            System.out.println("WARNING INFO: " + info.getDescription());

        }

    }

}

//........

//........

static void Run() throws Exception

{

    Workbook workbook = new Workbook("source.xlsx");

    PdfSaveOptions options = new PdfSaveOptions();

    options.setWarningCallback(new WarningCallback());

    workbook.save("output.pdf", options);

}

{{< /highlight >}}

## **警告の出力**

ソースファイルを変換した後、次の警告がデバッグコンソールに出力されます:

{{< highlight java >}}

WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、スプレッドシートをPDF形式にレンダリングする直前にWorkbook.calculateFormulaメソッドを呼び出すのがベストです。これにより、数式に依存する値が再計算され、正しい値がPDFに表示されます。 

{{% /alert %}}
