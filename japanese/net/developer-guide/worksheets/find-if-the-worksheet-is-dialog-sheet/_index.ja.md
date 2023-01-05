---
title: ワークシートがダイアログ シートかどうかを調べる
type: docs
weight: 90
url: /ja/net/find-if-the-worksheet-is-dialog-sheet/
---
## **考えられる使用シナリオ**

ダイアログ シートは、ダイアログ ボックスを含む古い形式のシートです。このようなシートは、このスクリーンショットに示すように、2003 などの古いバージョンの Microsoft Excel で挿入できます。 Microsoft Excel 2016 など、新しいバージョンの VBA で挿入することもできます。

![todo:画像_代替_文章](find-if-the-worksheet-is-dialog-sheet_1.png)

シートがダイアログ シートであるか、他のタイプのシートであるかを確認できます。[**Worksheet.Type**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)Aspose.Cells 提供のプロパティ。列挙値を返す場合[**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype)の場合は、ダイアログ シートを扱っていることを意味します。

## **ワークシートがダイアログ シートかどうかを調べる**

次のサンプル コードは、[サンプル Excel ファイル](64716820.xlsx)ダイアログシートが含まれています。それはチェックします[**Worksheet.Type**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)プロパティはそれを[**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype)メッセージを出力します。詳細については、以下のサンプル コードのコンソール出力を参照してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-FindIfWorksheetIsDialogSheet.cs" >}}

## **コンソール出力**

{{< highlight "java" >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
