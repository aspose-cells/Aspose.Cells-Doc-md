---
title: GridDesktop'ta Sütunları ve Satırları Sildikten Sonra Olayları Yönetme
type: docs
weight: 80
url: /tr/net/handling-events-after-deleting-columns-and-rows-in-griddesktop/
---
## **Olası Kullanım Senaryoları**
GridDesktop için Aspose.Cells, aşağıdaki ekran görüntüsünde gösterildiği gibi AfterDeleteColumns ve AfterDeleteRows gibi iki yeni etkinlik ekledi. Bu olaylar, sırasıyla sütunları ve satırları sildiğinizde tetiklenir.

![yapılacaklar:resim_alternatif_Metin](handling-events-after-deleting-columns-and-rows-in-griddesktop_1.png)
## **GridDesktop'ta Sütunları ve Satırları Sildikten Sonra Olayları Yönetme**
Aşağıdaki örnek kod, AfterDeleteColumns ve AfterDeleteRows olaylarından nasıl yararlanılacağını açıklar. Bazı sütunları veya satırları sildiğinizde, verilen işlev çağrılacak ve silinen sütun veya satırın dizinini görüntüleyen bir mesaj kutusu gösterecektir.
## **Basit kod**
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
