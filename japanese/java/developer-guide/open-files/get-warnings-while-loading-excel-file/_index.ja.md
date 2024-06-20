---
title: Excelファイルの読み込み時に警告を取得する
type: docs
weight: 60
url: /ja/java/get-warnings-while-loading-excel-file/
---

## **可能な使用シナリオ**

ユーザーがロード可能なデータがあるが不正なワークブックを読み込もうとすることがあります。このような場合、Aspose.Cellsはワークブックを読み込む際に警告を発行します。これらの警告を[**IWarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback)インターフェースを実装して[**LoadOptions.WarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#WarningCallback)プロパティを設定することでキャッチすることができます。

## **Excelファイルの読み込み中に警告を受け取る**

Excelファイルを読み込みながら警告を取得する方法について以下のサンプルコードを説明します。このコードは、[サンプルエクセルファイル](sampleDuplicateDefinedName.xlsx)をロードし、ロード中に[**DuplicateDefinedName**](https://reference.aspose.com/cells/java/com.aspose.cells/warningtype#DUPLICATE_DEFINED_NAME)警告を発生させます。この警告は[**IWarningCallback.Warning()**](https://reference.aspose.com/cells/java/com.aspose.cells/iwarningcallback#warning(com.aspose.cells.WarningInfo))メソッドでキャッチされ、コンソールに警告メッセージが出力されます。その後、ワークブックを[出力エクセルファイル](outputDuplicateDefinedName.xlsx)として保存します。サンプルエクセルファイルをMicrosoft Excelで開くと、このような警告が表示されます。理解を深めるために以下のコンソール出力もチェックしてください。

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-WarningCallback-WarningCallback.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-GetWarningLoadingAnExcel-GetWarningLoadingAnExcel.java" >}}

## **コンソール出力**

提供された[サンプルエクセルファイル](sampleDuplicateDefinedName.xlsx)を使用して上記のコードを実行した際のコンソール出力は次のとおりです。

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
