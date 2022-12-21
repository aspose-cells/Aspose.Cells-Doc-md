---
title: Excel ファイルのレンダリング中にフォントの置換に関する警告を受け取る
type: docs
weight: 120
url: /ja/java/get-warnings-for-font-substitution-while-rendering-excel-file/
---
{{% alert color="primary" %}}

Microsoft Excel ファイルを PDF にレンダリングすると、Aspose.Cells がフォントに置き換わる場合があります。 Aspose.Cells は、開発者に特定のフォントが置き換えられたことを警告を発することで知らせる機能を提供します。これは、Aspose.Cells でレンダリングされた PDF が実際の Excel ファイルと異なる理由を特定し、適切なアクションを取るのに役立つ便利な機能です。たとえば、不足しているフォントをインストールして、レンダリング結果が同じに見えるようにすることができます。

Excel ファイルを PDF にレンダリングする際にフォントの置換に関する警告を表示するには、IWarningCallback インターフェイスを実装し、実装したインターフェイスで PdfSaveOptions.setWarningCallback() メソッドを設定します。

{{% /alert %}}

以下のスクリーンショットは、次のコードで使用されるソース Excel ファイルを示しています。 Microsoft Excel では適切に表示されないフォントのセル A6 と A7 にテキストが含まれています。

![todo:画像_代替_文章](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)

Aspose.Cells は、以下に示すように、セル A6 および A7 のフォントを適切なフォントに置き換えます。

![todo:画像_代替_文章](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)

## **ソースファイルをダウンロードして PDF を出力**

ソースの Excel ファイルと出力の PDF は、次のリンクからダウンロードできます。

- [ソース.xlsx](5472700.xlsx)
- [output.pdf](5472699.pdf)

次のコードは、[**IWarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback)を設定します。[**PdfSaveOptions.setWarningCallback()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#WarningCallback)実装されたインターフェイスを持つメソッド。これで、任意のセルで任意のフォントが置換されるたびに、Aspose.Cells が WarningCallback.warning() メソッド内で警告を発します。

{{< highlight "java" >}}

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

## **警告出力**

ソース ファイルの変換後、次の警告がデバッグ コンソールに出力されます。

{{< highlight "java" >}}

WARNING INFO: Font substitution: Font [ Athene Logos; Regular ]has been substituted in Cell [ A6 ]in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ]has been substituted in Cell [ A7 ]in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合は、スプレッドシートを PDF 形式にレンダリングする直前に Workbook.calculateFormula メソッドを呼び出すことをお勧めします。そうすることで、数式に依存する値が再計算され、正しい値が PDF に表示されます。

{{% /alert %}}
