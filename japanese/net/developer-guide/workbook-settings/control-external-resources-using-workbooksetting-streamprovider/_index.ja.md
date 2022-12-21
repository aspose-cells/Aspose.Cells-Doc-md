---
title: WorkbookSetting.StreamProvider を使用して外部リソースを制御する
type: docs
weight: 10
url: /ja/net/control-external-resources-using-workbooksetting-streamprovider/
---
## **考えられる使用シナリオ**

Excel ファイルには、リンクされた画像などの外部リソースが含まれている場合があります。Aspose.Cells を使用すると、これらの外部リソースを制御できます。[**Workbook.Settings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider)の実装を取ります[**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)インターフェース。リンクされた画像などの外部リソースを含むワークシートをレンダリングしようとするときはいつでも、[**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)インターフェイスが呼び出され、外部リソースに対して適切なアクションを実行できるようになります。

## **WorkbookSetting.StreamProvider を使用して外部リソースを制御する**

次のサンプル コードは、[**Workbook.Settings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) .それは[サンプル Excel ファイル](61767863.xlsx)リンクされた画像が含まれています。コードは、リンクされた画像を次のように置き換えます[Aspose ロゴ](61767862.png)を使用して、シート全体を単一の画像にレンダリングします[**シートレンダリング**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)クラス。次のスクリーンショットは、サンプルの Excel ファイルとその[レンダリングされた出力イメージ](61767865.png)参考までに。ご覧のとおり、壊れたリンク画像は Aspose ロゴに置き換えられています。

![todo:画像_代替_文章](control-external-resources-using-workbooksetting-streamprovider_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.cs" >}}
