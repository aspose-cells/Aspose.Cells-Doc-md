---
title: EnableClipboardCopyPaste ve PasteType GridDesktop Özelliklerinin Kopyala Yapıştırma Davranışı
type: docs
weight: 80
url: /tr/net/copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties/
---
##  **Olası Kullanım Senaryoları**
GridDesktop, Aspose.Cells.GridDesktop.GridDesktop.PasteType özelliği ile farklı türde kopyala yapıştır türü seçenekleri sunar. Bu seçenekler Aspose.Cells.GridDesktop.Data.GridPasteType numaralandırmasıyla belirtilir. Bunlardan bazıları aşağıdaki gibidir

- GridPasteType.All

Kaynak hücrelerden hedef hücrelere kadar her şeyi kopyalayıp yapıştırır.

- GridPasteType.Formulas

Formülleri kaynak hücrelerden hedef hücrelere kopyalayıp yapıştırır.

- GridPasteType.Comments

Yorumları kaynak hücrelerden hedef hücrelere kopyalayıp yapıştırır.

- GridPasteType.RowHeights

Satır yüksekliklerini kaynak hücrelerden hedef hücrelere kopyalayıp yapıştırır.

- GridPasteType.ColumnWidths

Sütun genişliklerini kaynak hücrelerden hedef hücrelere kopyalayıp yapıştırır.

vesaire.
##  **PasteType Özelliğini Etkinleştirmek için EnableClipboardCopyPaste Özelliğini True Olarak Ayarlayın**
Aspose.Cells.GridDesktop.GridDesktop.PasteType özelliği yalnızca Aspose.Cells.GridDesktop.GridDesktop.EnableClipboardCopyPaste özelliğini bu ekran görüntüsünde gösterildiği gibi true olarak ayarlarsanız çalışır.

![yapılacak şey:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_1.png)
##  **EnableClipboardCopyPaste ve PasteType Özelliklerinin Davranışı**
EnableClipboardCopyPaste'in yanlış ve PasteType'ın Tümü olduğu göz önüne alındığında, aşağıdaki ekran görüntüsü B3 hücresinin kopyalanıp C5 hücresine yapıştırıldığını gösterir.

![yapılacak şey:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_3.png)

EnableClipboardCopyPaste'in doğru ve PasteType'ın All olduğu göz önüne alındığında, Windows'tan bir görüntü kopyaladıktan sonra. Aşağıdaki ekran görüntüsü, B3 hücresi kopyalanıp C5 hücresine yapıştırıldığında görüntüyü C5 hücresine de kopyaladığını göstermektedir.

![yapılacak:görüntüyü kopyala](copyimage.png)

![yapılacaklar: kopyaladıktan sonra yapıştır](aftercopy.png)


