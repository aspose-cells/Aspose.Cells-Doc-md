---
title: ワークシートがダイアログ シートかどうかを調べる
type: docs
weight: 100
url: /ja/java/find-if-the-worksheet-is-dialog-sheet/
---
## **考えられる使用シナリオ**

ダイアログ シートは、ダイアログ ボックスを含む古い形式のシートです。このようなシートは、このスクリーンショットに示すように、2003 などの古いバージョンの Microsoft Excel で挿入できます。 Microsoft Excel 2016 など、新しいバージョンの VBA で挿入することもできます。

![todo:画像_代替_文章](find-if-the-worksheet-is-dialog-sheet_1.png)

シートがダイアログ シートであるか、他のタイプのシートであるかを確認できます。[**Worksheet.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type)Aspose.Cells 提供のプロパティ。列挙値を返す場合[**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG)の場合は、ダイアログ シートを扱っていることを意味します。

## **ワークシートがダイアログ シートかどうかを調べる**

次のサンプル コードは、[サンプル Excel ファイル](64716841.xlsx)ダイアログシートが含まれています。それはチェックします[**Worksheet.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type)プロパティはそれを[**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG)メッセージを出力します。詳細については、以下のサンプル コードのコンソール出力を参照してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-FindIfWorksheetIsDialogSheet.java" >}}

## **コンソール出力**

{{< highlight "java" >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
