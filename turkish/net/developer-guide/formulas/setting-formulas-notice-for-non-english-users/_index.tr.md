---
title: Formülleri Ayarlama  Diğer Dillerde Kullanıcılar İçin Dikkat
type: docs
weight: 10
url: /tr/net/setting-formulas-notice-for-non-english-users/
---

{{% alert color="primary" %}} 

Aspose.Cells, Microsoft Excel'in bir parçası olan çoğu formül/fonksiyonu destekler. Geliştiriciler, bu formülleri API veya [tasarımcı elektronik tablolar](/cells/tr/net/what-is-a-designer-spreadsheet/) ile kullanabilir. Aspose.Cells, büyük bir matematiksel, dize, Mantıksal, tarih/saat, istatistiksel, veritabanı, bakış ve referans formül kümesini destekler. Formüllerin İngilizce (ABD) biçiminde belirtilmesi gerekmektedir.

{{% /alert %}} 
## **İngilizce Olmayan Kullanıcılar için Uyarı**
Aspose.Cells ile formül oluşturan diğer dillerdeki kullanıcıların dikkat etmesi gereken iki ipucu bulunmaktadır:

1. Formüller İngilizce olarak girilmelidir. Örneğin, Almanca "=SUMME()" yerine İngilizce olarak "=SUM()" kullanın.
1. Fonksiyon parametrelerini ayırmak için her zaman bir virgül (,) kullanın. Bazı dil seçenekleri veya ayarlar için fonksiyon parametrelerinin ayırıcısı noktalı virgül olabilir, ancak Aspose.Cells İngilizce biçimli virgülü kullanır. Örneğin, "=IF(C5=0;0;C3/C4)" değil, "=IF (C5=0,0,C3/C4)" kullanın.
