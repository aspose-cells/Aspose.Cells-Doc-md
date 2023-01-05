---
title: Ayar Formülleri - İngilizce Dışı Kullanıcılar İçin Uyarı
type: docs
weight: 20
url: /tr/java/setting-formulas-notice-for-non-english-users/
---
{{% alert color="primary" %}} 

 Aspose.Cells, Microsoft Excel'in parçası olan formüllerin/işlevlerin çoğunu destekler. Geliştiriciler bu formülleri API veya[tasarımcı elektronik tabloları](/cells/tr/java/what-is-a-designer-spreadsheet/)Aspose.Cells, çok sayıda matematiksel, dizi, Boolean, tarih/saat, istatistik, veritabanı, arama ve referans formüllerini destekler. Formüller, İngilizce (ABD) stili kullanılarak belirtilmelidir.

İngilizce olmayan kullanıcıların Aspose.Cells ile formül oluştururken izlemesi gereken iki ipucu vardır:

1. Formüller İngilizce olarak girilmelidir.
 Örneğin, Almanca "=SUMME()" yerine İngilizce "=SUMME()" kullanın.
1. İşlev parametrelerini ayırmak için her zaman virgül (,) kullanın.
 Bazı dil seçenekleri veya ayarları için, işlev parametrelerinin sınırlayıcısı noktalı virgüldür ancak Aspose.Cells, İngiliz stili virgül kullanır. Örneğin, "=EĞER(C5=0;0;C3/C4)" yerine "=EĞER (C5=0,0,C3/C4)" kullanın

{{% /alert %}}
