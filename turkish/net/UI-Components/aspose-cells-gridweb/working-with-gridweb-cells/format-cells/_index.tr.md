---
title: Biçim Cells
type: docs
weight: 40
url: /tr/net/format-grid-cells/
---
{{% alert color="primary" %}} 

Bu konu, hücrelerin nasıl biçimlendirileceği hakkında ayrıntılı bir tartışma sağlar.

Aspose.Cells.GridWeb kontrolünün Stil iletişim kutusu kullanılarak GUI modunda hücrelerin biçimlendirilmesini kapsar. Ayrıca hücrelerin programlı olarak nasıl formatlanacağını da gösterir. Yazı tipi, kenarlık ve sayı biçimi gibi farklı biçim ayarları tartışılır, örneklerle gösterilir.

{{% /alert %}} 
## **Stil İletişim Kutusunu Kullanarak Cells'i Biçimlendirme**
 Cells biçimlendirilebilir[programlı olarak](/cells/tr/net/format-cells/)ancak Aspose.Cells.GridWeb kontrolünde hücreleri WYSIWYG biçiminde biçimlendirmenin en kolay yolu Stil iletişim kutusunu kullanmaktır.

Stil iletişim kutusunu kullanmak için:
 Bir hücre aralığı seçin, ardından sağ tıklayın ve seçin**Biçim Cell**. 

**Format Seçme Cell** 

![yapılacaklar:resim_alternatif_metin](format-cells_1.png)



 Stil iletişim kutusu görüntülenir.

**Stil iletişim kutusu, hücreleri biçimlendirmek için kullanılır** 

![yapılacaklar:resim_alternatif_metin](format-cells_2.png)

Stil iletişim kutusu, kullanıcıların yazı tipi ve kenarlık ayarlarını özelleştirerek hücreleri biçimlendirmesine olanak tanır.
### **Yazı Tipi Ayarlarını Özelleştirme**
Stil iletişim kutusunu kullanarak aşağıdaki yazı tipi ayarlarını özelleştirebilirsiniz:

- Yazı tipi adı, listeden istediğiniz yazı tipini seçin.
- Yazı tipi stili, kalın, italik vb. gibi bir yazı tipi stili uygulayın.
- Yazı tipi boyutu, punto cinsinden bir yazı tipi boyutu seçin.
- Metnin altını çiz, altını çiz.
- Üstü çizili, metne bir üstü çizili efekti uygulayın.
- Yatay hizalama, yatay hizalamayı seçin.
- Dikey hizalama, dikey hizalamayı seçin.
- Yazı tipi rengi, bir yazı tipi rengi seçin.
- Arka plan, arka plan için bir renk seçin.

Seçilen yazı tipi ayarlarını küçük bir ön izleme alanında kontrol edebilirsiniz.

**Özelleştirilmiş yazı tipi ayarları** 

![yapılacaklar:resim_alternatif_metin](format-cells_3.png)
### **Kenarlık Ayarlarını Özelleştirme**
Denetim, kullanıcıların Stil iletişim kutusundaki kenarlık ayarlarını özelleştirerek hücrelerin çevresine bir kenarlık çizmesine de olanak tanır.

Sınırla ilgili seçenekleri görüntülemek için:
 Tıklamak**Kenarlıklar** Stil iletişim kutusunda.
 Sınırla ilgili seçenekler görüntülenir.

**Stil iletişim kutusundaki kenarlık seçenekleri** 

![yapılacaklar:resim_alternatif_metin](format-cells_4.png)

Stil iletişim kutusundan aşağıdaki kenarlık seçenekleri seçilebilir:

- Sınır çizgisi stili, düz, kesikli vb. gibi kenarlık stilini seçin.
- Kenar çizgisi genişliği, kenarlık genişliğini piksel olarak seçin.
- Kenar çizgisi rengi, çizgi rengini seçin.
- Sınır çizgileri, sınır çizgilerinin numaralandırılmasını ve konumlandırılmasını seçin.

**Özel kenarlık ayarları** 

![yapılacaklar:resim_alternatif_metin](format-cells_5.png)
### **Ayarları Uygulamak**
 Tıklamak**Tamam** değişiklikleri uygulamak için Stil iletişim kutusunda.

**Yazı tipi ve kenarlık ayarları uygulandı** 

![yapılacaklar:resim_alternatif_metin](format-cells_6.png)


## **Cells'i API Kullanarak Biçimlendirme**
Cells, Aspose.Cells.GridWeb API ile programlı olarak da biçimlendirilebilir. Her hücrenin, bir GridTableItemStyle nesnesini temsil eden bir Style özelliği vardır. Yazı tipi ve kenarlık ayarlarını özelleştirmek için Style özelliğini kullanın.
### **Yazı Tipi Ayarı**
Yazı tipi ayarlarını programlı olarak özelleştirmek için:

1. Aspose.Cells.GridWeb denetimini bir Web Formuna ekleyin.
1. Bir çalışma sayfasına erişin.
1. Biçimlendirdiğiniz hücreye erişin.
1. Hücrenin stiline erişin.
1. Yazı tipi boyutunu punto olarak ayarlayın.
1. Yazı tipi stilini ayarlayın.
1. Ön plan ve arka plan renklerini ayarlayın.
1. Yatay ve dikey hizalamayı ayarlayın.
1. Stili hücreye geri ayarlayın.

**Çıktı: A1'de gösterilen özelleştirilmiş yazı tipi ayarları** 

![yapılacaklar:resim_alternatif_metin](format-cells_7.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyFontStyles.cs" >}}
### **Sınırları Ayarlama**
Kenarlıklar, tek tek hücrelere veya bir aralığa uygulanabilir.
#### **Tek kişilik Cell**
Tek bir hücrenin kenarlıklarını ayarlamak için:

1. Aspose.Cells.GridWeb denetimini bir Web Formuna ekleyin.
1. Bir çalışma sayfasına erişin.
1. Biçimlendirmek üzere olduğunuz hücreye erişin.
1. Hücrenin Stil nesnesine erişin.
1. Kenarlık stilini ayarlayın.
1. Kenarlık genişliğini piksel cinsinden ayarlayın.
1. Kenarlık rengini ayarlayın.
1. Stili hücreye ayarlayın.

**Tek bir hücrede özelleştirilmiş kenarlık ayarları** 

![yapılacaklar:resim_alternatif_metin](format-cells_8.png)

{{% alert color="primary" %}} 

Hücrenin Style.TopBorderStyle, Style.BottomBorderStyle, Style.LeftBorderStyle, Style.RightBorderStyle özellikleri ile her kenar çizgisi için farklı stiller ayarlamak mümkündür.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyBorderStyles.cs" >}}
#### **Cells aralığı**
Bir hücre aralığında kenarlıklar ayarlamak için:

1. Web Formunuza Aspose.Cells.GridWeb denetimi ekleyin
1. İstediğiniz bir çalışma sayfasına erişin
1. WebBorderStyle sınıfından bir nesne oluşturun
1. Kenarlığın Stilini Kesintisiz veya Kesikli vb. olarak ayarlayın.
1. Kenarlığın Genişliğini piksel olarak ayarlayın
1. Kenarlığın Rengini Ayarla
1. Belirli bir hücre aralığına WebBorderStyle nesnesinde depolanan kenarlık ayarlarını uygulayın

**Özel kenarlık ayarlarına sahip bir dizi hücre** 

![yapılacaklar:resim_alternatif_metin](format-cells_9.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyRangeBorderStyles.cs" >}}
### **Sayı Biçimlerini Ayarlama**
 Aspose.Cells.GridWeb ayar numarası biçimlerini destekler. 59 yerleşik sayı biçimi vardır. Bunları görmek için lütfen buna bakın[desteklenen sayı biçimlerinin listesi](/cells/tr/net/list-of-supported-number-formats/).

Tüm yerleşik sayı biçimleri, NumberType numaralandırmasındadır. Yerleşik bir sayı biçimi kullanmak için, bir hücrenin nesnesinin SetNumberType yöntemini kullanarak NumberType'ı NumberType numaralandırmasından bir sayı biçimine ayarlayın.

Özel sayı biçimini ayarlamak için hücrenin SetCustom yöntemini kullanın.

**B1 ve B2'de uygulanan sayı biçimi ayarları** 

![yapılacaklar:resim_alternatif_metin](format-cells_10.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyNumberFormats.cs" >}}
