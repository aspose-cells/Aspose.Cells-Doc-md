---
title: Sütun ve Satır Silme Sonrası Olayları İşleme
type: docs
weight: 80
url: /tr/net/aspose-cells-griddesktop/handle-events-after-delete-columns-and-rows-in-griddesktop/
keywords: GridDesktop,olaylar,satır silme,sütun silme
description: Bu makale, GridDesktop ta satır/sütun silme sonrası olayları tanıtır.
---

## **Olası Kullanım Senaryoları**
Aspose.Cells için GridDesktop, aşağıdaki ekran görüntüsünde gösterildiği gibi AfterDeleteColumns ve AfterDeleteRows olmak üzere iki yeni olay ekledi. Bu olaylar, sırasıyla sütun ve satırları sildiğinizde tetiklenir.

![todo:image_alt_text](handling-events-after-deleting-columns-and-rows-in-griddesktop_1.png)
## **Sütun ve Satırları Silme Sonrası Olayları İşleme**
Aşağıdaki örnek kod, AfterDeleteColumns ve AfterDeleteRows olaylarından nasıl yararlanılacağını açıklar. Bazı sütunlar veya satırlar silindiğinde, verilen işlev çağrılacak ve silinen sütun veya satırın dizinini gösteren bir iletişim kutusu gösterecektir.
## **Örnek Kod**
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
