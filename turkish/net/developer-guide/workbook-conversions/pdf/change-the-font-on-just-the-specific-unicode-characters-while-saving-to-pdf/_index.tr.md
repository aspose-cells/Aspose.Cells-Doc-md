---
title: PDF'ye kaydederken Yazı Tipini yalnızca belirli Unicode karakterlerinde değiştirin
type: docs
weight: 260
url: /tr/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---
{{% alert color="primary" %}} 

 Bazı Unicode karakterler, kullanıcı tarafından belirlenen yazı tipi tarafından görüntülenemez. Böyle bir Unicode karakter**Bölünemez Tire** (U+2011) ve Unicode numarası 8209'dur. Bu karakter ile görüntülenemez.**Times New Roman** , ancak diğer yazı tipleriyle birlikte görüntülenebilir.**Arial Unicode MS**.

Böyle bir karakter, Times New Roman gibi belirli bir yazı tipindeki bir kelime veya cümlenin içinde geçtiğinde, Aspose.Cells, tüm kelimenin veya cümlenin yazı tipini, bu karakteri Arial Unicode gibi MS'e görüntüleyebilecek yazı tipine değiştirir.

Ancak bu, bazı kullanıcılar için istenmeyen bir davranıştır ve tüm kelime veya cümlenin yazı tipini değiştirmek yerine yalnızca belirli bir karakterin yazı tipinin değiştirilmesini isterler.

Bu sorunu çözmek için Aspose.Cells, PdfSaveOptions.IsFontSubstitutionCharGranularity özelliğini sağlar; bu özellik, yalnızca görüntülenemeyen belirli bir karakterin yazı tipinin görüntülenebilir yazı tipine dönüştürülmesi ve kelimenin veya cümlenin geri kalanının orijinal yazı tipinde kalması için doğru olarak ayarlanması gerekir.

{{% /alert %}} 
## **Örnek**
Aşağıdaki ekran görüntüsü, aşağıdaki örnek kod tarafından oluşturulan iki çıktı PDF'sini karşılaştırır.

Biri PdfSaveOptions.IsFontSubstitutionCharGranularity özelliği ayarlanmadan, diğeri ise PdfSaveOptions.IsFontSubstitutionCharGranularity özelliği true olarak ayarlandıktan sonra oluşturuldu.

İlk Pdf'de görebileceğiniz gibi, tüm cümlenin yazı tipi, Kırılmayan Tire nedeniyle Times New Roman'dan Arial Unicode MS'ye değişti. İkinci Pdf'de ise sadece Kırılmaz Tire'nin yazı tipi değişmiştir.

|**İlk Pdf Dosyası**|
|:- |
|![yapılacaklar:resim_alternatif_Metin](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**İkinci Pdf Dosyası**|
|:- |
|![yapılacaklar:resim_alternatif_Metin](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **Basit kod**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ChangeFontUnicodeCharacterToPdf-ChangeFontUnicodeCharacterWhileSavingToPdf.cs" >}}



