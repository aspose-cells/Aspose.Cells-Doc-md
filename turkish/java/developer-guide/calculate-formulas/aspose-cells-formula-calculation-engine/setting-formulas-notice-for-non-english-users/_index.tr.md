---
title: Formülleri Ayarlama  Diğer Dillerde Kullanıcılar İçin Dikkat
type: docs
weight: 20
url: /tr/java/setting-formulas-notice-for-non-english-users/
---

{{% alert color="primary" %}} 

Aspose.Cells, Microsoft Excel'in bir parçası olan çoğu formül/fonksiyonu destekler. Geliştiriciler bu formülleri API veya [tasarımcı elektronik tablolar](/cells/tr/java/what-is-a-designer-spreadsheet/) ile kullanabilir. Aspose.Cells, matematik, dize, Boolean, tarih/saat, istatistiksel, veritabanı, arama ve başvuru formüllerinin geniş bir setini destekler. Formüller, İngilizce (ABD) stili kullanılarak belirtilmelidir.

Aspose.Cells ile formül oluşturan diğer dillerdeki kullanıcıların dikkat etmesi gereken iki ipucu bulunmaktadır:

1. Formüller İngilizce olarak girilmelidir.
   Örneğin, Almanca "=SUMME()" yerine İngilizce "=SUM()" kullanın.
2. Her zaman fonksiyon parametrelerini ayırmak için bir virgül (,) kullanın.
   Bazı dil seçenekleri veya ayarlar için fonksiyon parametrelerinin ayırıcısı noktalı virgül olabilir, ancak Aspose.Cells İngiliz stil virgül kullanır. Örneğin, "=IF(C5=0,0,C3/C4)" yerine "=IF(C5=0;0;C3/C4)" kullanın. 

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
