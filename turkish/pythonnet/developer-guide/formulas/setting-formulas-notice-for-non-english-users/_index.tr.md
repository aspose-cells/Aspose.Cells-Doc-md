---
title: Formülleri Ayarlama  Diğer Dillerde Kullanıcılar İçin Dikkat
type: docs
weight: 10
url: /tr/python-net/setting-formulas-notice-for-non-english-users/
---

{{% alert color="primary" %}} 

Aspose.Cells for Python via .NET, Microsoft Excel'in çoğu formülü/fonksiyonunu destekler. Geliştiriciler, bu formülleri ya API aracılığıyla ya da [tasarımcı elektronik tablolar](/cells/tr/net/what-is-a-designer-spreadsheet/) kullanarak uygulayabilir. Aspose.Cells for Python via .NET, matematiksel, dize, Boolean, tarih/zaman, istatistiksel, veritabanı, arama ve referans formülleriyle büyük bir desteğe sahiptir. Formüller İngilizce (ABD) tarzında belirtilmelidir.

{{% /alert %}} 

## **İngilizce Olmayan Kullanıcılar için Uyarı**
Aspose.Cells for Python via .NET ile formüller oluştururken uyulması gereken iki ipucu:

1. Formüller İngilizce olarak girilmelidir. Örneğin, Almanca "=SUMME()" yerine İngilizce olarak "=SUM()" kullanın.
1. Fonksiyon parametrelerini ayırmak için her zaman virgül (,) kullanın. Bazı dil seçenekleri veya ayarlar, fonksiyon parametreleri için ayraç olarak noktalı virgül kullanabilir, ancak Aspose.Cells for Python via .NET İngilizce tarzı virgül kullanır. Örneğin, "=IF (C5=0,0,C3/C4)" kullanın, "=IF(C5=0;0;C3/C4)" değil.

