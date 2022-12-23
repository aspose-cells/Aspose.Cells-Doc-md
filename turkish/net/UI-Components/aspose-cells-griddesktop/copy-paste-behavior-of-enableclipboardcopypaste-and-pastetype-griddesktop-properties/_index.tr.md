---
title: EnableClipboardCopyPaste ve PasteType GridDesktop Özelliklerinin Kopyala Yapıştır Davranışı
type: docs
weight: 80
url: /tr/net/copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties/
---
## **Olası Kullanım Senaryoları**
GridDesktop, Aspose.Cells.GridDesktop.GridDesktop.PasteType özelliği ile farklı tiplerde kopyala yapıştır türü seçenekleri sunar. Bu seçenekler Aspose.Cells.GridDesktop.Data.GridPasteType numaralandırması ile belirtilir. Bunlardan bazıları aşağıdaki gibidir

- GridPasteType.All

Kaynak hücrelerden hedef hücrelere kadar her şeyi kopyalayıp yapıştırır.

- GridPasteType.Formulas

Kaynak hücrelerden formülleri kopyalayıp hedef hücrelere yapıştırır.

- GridPasteType.Comments

Yorumları kaynak hücrelerden kopyalayıp hedef hücrelere yapıştırır.

- GridPasteType.RowHeights

Kaynak hücrelerden hedef hücrelere satır yüksekliklerini kopyalayıp yapıştırır.

- GridPasteType.ColumnWidths

Kaynak hücrelerden hedef hücrelere sütun genişliklerini kopyalar ve yapıştırır.

vb.
## **PasteType Özelliğini Etkinleştirmek İçin EnableClipboardCopyPaste Özelliğini True Olarak Ayarlayın**
Aspose.Cells.GridDesktop.GridDesktop.PasteType özelliği, yalnızca Aspose.Cells.GridDesktop.GridDesktop.EnableClipboardCopyPaste özelliğini bu ekran görüntüsünde gösterildiği gibi doğru ayarlarsanız çalışır.

![yapılacaklar:resim_alternatif_metin](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_1.png)
## **EnableClipboardCopyPaste ve PasteType Özelliklerinin Davranışı**
EnableClipboardCopyPaste öğesinin false ve PasteType öğesinin All olduğu göz önüne alındığında, aşağıdaki ekran görüntüsü, B3 hücresinin kopyalanıp C5 hücresine yapıştırıldığında, hücre biçimlendirmesinin kopyalanmadığını ve yalnızca B3 hücresinin içeriğinin kopyalandığını gösterir.

![yapılacaklar:resim_alternatif_metin](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_2.png)

EnableClipboardCopyPaste'in true ve PasteType'ın All olduğu göz önüne alındığında, aşağıdaki ekran görüntüsü, B3 hücresinin kopyalanıp C5 hücresine yapıştırıldığında, B3 hücresinin biçimlendirmesini de C5 hücresine kopyaladığını gösterir.

![yapılacaklar:resim_alternatif_metin](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_3.png)


