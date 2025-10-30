---
title: Formüller Ayarlama  İngilizce olmayan kullanıcılar için Uyarı JavaScript ile C++ kullanarak
linktitle: Formülleri Ayarlama  Diğer Dillerde Kullanıcılar İçin Dikkat
type: docs
weight: 10
url: /tr/javascript-cpp/setting-formulas-notice-for-non-english-users/
---  

{{% alert color="primary" %}} 

Aspose.Cells, Microsoft Excel'in çoğu formülü/fonksiyonunu destekler. Geliştiriciler bu formülleri API veya [tasarımcı elektronik tablolar](/cells/tr/javascript-cpp/what-is-a-designer-spreadsheet/) aracılığıyla kullanabilir. Aspose.Cells, çok büyük bir matematiksel, dizeden, boolean, tarih/saat, istatistik, veritabanı, arama ve referans formülleri kümesi destekler. Formüller İngilizce (ABD) tarzında belirtilmelidir.

{{% /alert %}} 

## **İngilizce Olmayan Kullanıcılar için Uyarı**
Aspose.Cells ile formül oluşturan diğer dillerdeki kullanıcıların dikkat etmesi gereken iki ipucu bulunmaktadır:

1. Formüller İngilizce olarak girilmelidir. Örneğin, Almanca "=SUMME()" yerine İngilizce olarak "=SUM()" kullanın.
1. Her zaman fonksiyon parametrelerini ayırmak için virgül (,) kullanın. Bazı dil seçenekleri veya ayarlarında, fonksiyon parametreleri ayırıcı noktalı virgüldür ancak Aspose.Cells İngilizce tarzı virgül kullanır. Örneğin, "=IF (C5=0,0,C3/C4)" kullanın, "=IF(C5=0;0;C3/C4)" değil.
