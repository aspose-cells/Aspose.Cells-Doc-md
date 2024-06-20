---
title: WorkbookSetting.StreamProvider を使用して外部リソースを制御する
type: docs
weight: 10
url: /ja/net/control-external-resources-using-workbooksetting-streamprovider/
---

## **可能な使用シナリオ**

時には、Excelファイルにはリンクされた画像などの外部リソースが含まれています。Aspose.Cellsを使用すると、[**Workbook.Settings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider)というインターフェースの実装を使用して、これらの外部リソースを制御することができます。ワークシートに外部リソース（リンクされた画像など）を含む場合、[**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)インターフェースのメソッドが呼び出され、外部リソースに対する適切なアクションを取ることが可能になります。

## **[Workbook.Settings.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider)を使用して外部リソースを制御する**

次のサンプルコードは、[**Workbook.Settings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider)の使用方法を説明しています。[サンプルExcelファイル](61767863.xlsx)をロードし、リンクされた画像を[Asposeロゴ](61767862.png)で置き換え、[**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)クラスを使用してシート全体を単一の画像にレンダリングします。以下のスクリーンショットは、サンプルExcelファイルと[レンダリングされた出力画像](61767865.png)を参照のこと。壊れたリンクされた画像がAsposeロゴで置き換えられていることが分かります。

![todo:image_alt_text](control-external-resources-using-workbooksetting-streamprovider_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.cs" >}}
