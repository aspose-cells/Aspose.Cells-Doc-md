---
title: 列と行を削除した後のイベント処理を行う
type: docs
weight: 80
url: /ja/net/aspose-cells-griddesktop/handle-events-after-delete-columns-and-rows-in-griddesktop/
keywords: GridDesktop、delete row、delete column、events
description: この記事では、GridDesktopで行/列を削除した後のイベント処理について紹介しています。
---

## **可能な使用シナリオ**
Aspose.Cells for GridDesktop には、列を削除した後のAfterDeleteColumnsと行を削除した後のAfterDeleteRowsの2つの新しいイベントが追加されています。これらのイベントは、それぞれ列と行を削除したときに発生します。

![todo:image_alt_text](handling-events-after-deleting-columns-and-rows-in-griddesktop_1.png)
## **GridDesktopで列と行を削除した後のイベント処理**
次のサンプルコードは、列または行を削除したときにAfterDeleteColumnsとAfterDeleteRowsイベントを使用する方法を説明しています。いくつかの列や行を削除するたびに、指定された関数が呼び出され、削除された列または行のインデックスが表示されるメッセージボックスが表示されます。
## **サンプルコード**
{{< highlight java >}}

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
