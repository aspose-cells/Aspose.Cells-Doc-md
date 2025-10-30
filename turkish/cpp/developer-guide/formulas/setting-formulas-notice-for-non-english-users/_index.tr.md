---
title: Formülleri Ayarla  İngilizce olmayan Kullanıcılar İçin Bildirim C++ ile
linktitle: Formülleri Ayarlama  Diğer Dillerde Kullanıcılar İçin Dikkat
type: docs
weight: 10
url: /tr/cpp/setting-formulas-notice-for-non-english-users/
description: İngilizce (ABD) tarzında Aspose.Cells for C++ te formülleri nasıl ayarlayacağınızı öğrenin, İngilizce olmayan kullanıcılar için.
---

{{% alert color="primary" %}} 

Aspose.Cells, Microsoft Excel'in çoğu formülü/fonksiyonunu destekler. Geliştiriciler bu formülleri API veya [tasarımcı tabloları](/cells/tr/cpp/what-is-a-designer-spreadsheet/) kullanarak kullanabilir. Aspose.Cells, matematiksel, dize, Boolean, tarih/zaman, istatistik, veritabanı, arama ve referans formüllerinin büyük bir setini destekler. Formüllerin İngilizce (ABD) tarzında belirtilmesi gerekir.

{{% /alert %}} 

## **İngilizce Olmayan Kullanıcılar için Uyarı**
Aspose.Cells ile formül oluşturan diğer dillerdeki kullanıcıların dikkat etmesi gereken iki ipucu bulunmaktadır:

1. Formüller İngilizce olarak girilmelidir. Örneğin, Almanca "=SUMME()" yerine İngilizce olarak "=SUM()" kullanın.
1. Her zaman fonksiyon parametrelerini ayırmak için virgül (,) kullanın. Bazı dil seçenekleri veya ayarlarında, fonksiyon parametreleri ayırıcı noktalı virgüldür ancak Aspose.Cells İngilizce tarzı virgül kullanır. Örneğin, "=IF (C5=0,0,C3/C4)" kullanın, "=IF(C5=0;0;C3/C4)" değil.
{{< app/cells/assistant language="cpp" >}}
