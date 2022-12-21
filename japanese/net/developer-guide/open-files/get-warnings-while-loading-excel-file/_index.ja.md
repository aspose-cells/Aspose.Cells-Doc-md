---
title: Excel ファイルの読み込み中に警告を受け取る
type: docs
weight: 110
url: /ja/net/get-warnings-while-loading-excel-file/
---
## **考えられる使用シナリオ**

ときどき、ユーザーがワークブックを読み込もうとすることがあります。ワークブックは多少壊れていますが、読み込めます。このような場合、Aspose.Cells はワークブックの読み込み中に警告をスローします。これらの警告は、実装することでキャッチできます。**[IWarningCallback](https://reference.aspose.com/cells/net/aspose.cells/iwarningcallback)**インターフェイスと設定**[LoadOptions.WarningCallback](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/warningcallback)**財産。

## **Excel ファイルの読み込み中に警告を受け取る**

次のサンプル コードは、Excel ファイルの読み込み中に警告を取得する方法を説明しています。コードは[サンプルエクセルファイル](sampleDuplicateDefinedName.xlsx)投げる**[DuplicateDefinedName](https://reference.aspose.com/cells/net/aspose.cells/warningtype)**ロード時の警告。この警告は、**[IWarningCallback.Warning()](https://reference.aspose.com/cells/net/aspose.cells/iwarningcallback/methods/warning)**コンソールに警告メッセージを出力するメソッド。次に、コードはワークブックを次のように保存します。[出力エクセルファイル](outputDuplicateDefinedName.xlsx)Microsoft Excel でサンプルの Excel ファイルを開くと、このスクリーンショットに示すように、この警告も表示されます。さらに理解を深めるために、以下に示すコードのコンソール出力も確認してください。

![todo:画像_代替_文章](get-warnings-while-loading-excel-file_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-GetWarningsWhileLoadingExcelFile.cs" >}}

## **コンソール出力**

上記のコードを提供されたコマンドで実行したときのコンソール出力は次のとおりです。[サンプルエクセルファイル](sampleDuplicateDefinedName.xlsx).

{{< highlight "java" >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
