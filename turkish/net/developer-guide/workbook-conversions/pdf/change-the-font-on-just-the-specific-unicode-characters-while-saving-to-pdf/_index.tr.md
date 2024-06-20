---
title: PDF ye kaydederken belirli Unicode karakterlerinin yazı tipini değiştirin
type: docs
weight: 260
url: /tr/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---

{{% alert color="primary" %}} 

Bazı Unicode karakterleri, kullanıcı tarafından belirtilen yazı tipiyle gösterilemez. Bu tür bir Unicode karakteri **Non-breaking Hyphen** (U+2011) adında ve Unicode numarası 8209'dur. Bu karakter **Times New Roman** ile görüntülenemez, ancak **Arial Unicode MS** gibi diğer yazı tipleriyle görüntülenebilir.

Böyle bir karakter, belirli bir yazı tipinde (örneğin Times New Roman) bulunursa, Aspose.Cells, bu karakterin görüntülenemeyen yazı tipi gibi Arial Unicode MS gibi bir yazı tipine değiştirir.

Ancak, bazı kullanıcılar için bu istenmeyen bir davranıştır ve yalnızca belirli karakterin yazı tipinin tüm kelimenin veya cümlenin yazı tipini değiştirmek yerine yalnızca değişmesini isterler.

Bu sorunla başa çıkmak için Aspose.Cells, yalnızca görüntülenemeyen belirli karakterin yazı tipinin değiştirilmesi için PdfSaveOptions.IsFontSubstitutionCharGranularity özelliğini true olarak ayarlamalıdır. Kelimenin geri kalanının veya cümlenin orijinal yazı tipinde kalması gerekir.

{{% /alert %}} 
## **Örnek**
Aşağıdaki ekran görüntüsü, aşağıdaki örnek kodu ile oluşturulan iki PDF'yi karşılaştırır.

Birincisi PdfSaveOptions.IsFontSubstitutionCharGranularity özelliğini ayarlamadan oluşturulmuştur ve diğeri PdfSaveOptions.IsFontSubstitutionCharGranularity özelliğini true olarak ayarladıktan sonra oluşturulmuştur.

İlk Pdf'de, tüm cümlenin yazı tipi Non-Breaking Hyphen yüzünden Times New Roman'dan Arial Unicode MS'ye değişmiştir. İkinci Pdf'de ise yalnızca Non-Breaking Hyphen'ın yazı tipi değişmiştir.

|**İlk Pdf Dosyası**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**İkinci Pdf Dosyası**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **Örnek Kod**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ChangeFontUnicodeCharacterToPdf-ChangeFontUnicodeCharacterWhileSavingToPdf.cs" >}}



