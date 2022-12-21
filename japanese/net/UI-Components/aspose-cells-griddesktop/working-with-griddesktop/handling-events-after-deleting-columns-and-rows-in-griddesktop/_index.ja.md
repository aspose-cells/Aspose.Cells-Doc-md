---
title: GridDesktop で列と行を削除した後のイベントの処理
type: docs
weight: 80
url: /ja/net/handling-events-after-deleting-columns-and-rows-in-griddesktop/
---
## **考えられる使用シナリオ**
次のスクリーンショットに示すように、GridDesktop の Aspose.Cells には、AfterDeleteColumns と AfterDeleteRows という 2 つの新しいイベントが追加されました。これらのイベントは、列と行をそれぞれ削除すると発生します。

![todo:画像_代替_文章](handling-events-after-deleting-columns-and-rows-in-griddesktop_1.png)
## **GridDesktop で列と行を削除した後のイベントの処理**
次のサンプル コードは、AfterDeleteColumns および AfterDeleteRows イベントを使用する方法を説明しています。いくつかの列または行を削除するたびに、指定された関数が呼び出され、削除された列または行のインデックスを表示するメッセージ ボックスが表示されます。
## **サンプルコード**
{{< highlight "java" >}}

 private void gridDesktop1_AfterDeleteColumnsAndRows(object sender, Aspose.Cells.GridDesktop.WorksheetEventArgs args)

{

    if(args.SheetEvents == Aspose.Cells.GridDesktop.WorksheetEvents.ColumnDeleted)

    {

        MessageBox.Show("Deleted Column Index: " + args.Index);

    }

    if (args.SheetEvents == Aspose.Cells.GridDesktop.WorksheetEvents.RowDeleted)

    {

        MessageBox.Show("Deleted Row Index: " + args.Index);

    }

}

{{< /highlight >}}
