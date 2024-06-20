---
title: EnableClipboardCopyPaste ve PasteType GridDesktop Özellikleri Kopyalama Yapıştırma Davranışı
type: docs
weight: 80
url: /tr/net/aspose-cells-griddesktop/copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties/
keywords: kopyala,yapıştır,GridPasteType
description: Bu makale, GridPasteType ın kullanımını yapıştırma işlemini Aspose.Cells.GridDesktop.GridDesktop.PasteType özelliğini kullanarak nasıl yapılacağını açıklar.
---

## **Olası Kullanım Senaryoları**
GridDesktop, Aspose.Cells.GridDesktop.GridDesktop.PasteType özelliği ile belirli kopya yapıştır türü seçenekleri sağlar. Bu seçenekler, Aspose.Cells.GridDesktop.Data.GridPasteType numaralandırmasıyla belirtilir. Bunlardan bazıları şunlardır

- GridPasteType.All

Kaynak hücrelerden hedef hücrelere her şeyi kopyalar ve yapıştırır.

- GridPasteType.Formulas

Kaynak hücrelerden hedef hücrelere formülleri kopyalar ve yapıştırır.

- GridPasteType.Comments

Kaynak hücrelerden hedef hücrelere yorumları kopyalar ve yapıştırır.

- GridPasteType.RowHeights

Kaynak hücrelerden hedef hücrelere satır yüksekliklerini kopyalar ve yapıştırır.

- GridPasteType.ColumnWidths

Kaynak hücrelerden hedef hücrelere sütun genişliklerini kopyalar ve yapıştırır.

vb.
## **EnableClipboardCopyPaste Özelliğini True Ayarlayarak PasteType Özelliğini Etkinleştirin**
Aspose.Cells.GridDesktop.GridDesktop.PasteType özelliği, özelliğini true olarak ayarlarsanız sadece Aspose.Cells.GridDesktop.GridDesktop.EnableClipboardCopyPaste özelliği olarak çalışır, bu ekran görüntüsünde gösterildiği gibi.

![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_1.png)
## **EnableClipboardCopyPaste ve PasteType Özelliklerinin Davranışı**
EnableClipboardCopyPaste false ve PasteType All olduğunda, B3 hücresinin kopyalandığı ve C5 hücresine yapıştırıldığı aşağıdaki ekran görüntüsünde gösterildiği gibi.

![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_3.png)

EnableClipboardCopyPaste true ve PasteType All olduğunda, Windows'tan bir resmi kopyaladıktan sonra B3 hücresinin C5 hücresine yapıştırıldığı aşağıdaki ekran görüntüsünde gösterildiği gibi, aynı zamanda resmi C5 hücresine de kopyalar.

![yapılacak:resmi kopyala](resmikopya.png)

![yapıştırdıktan sonra kopya](yapıştırması.png)


