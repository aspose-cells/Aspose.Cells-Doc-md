---
title: Hücre Biçimi
type: docs
weight: 40
url: /tr/net/aspose-cells-gridweb/format-grid-cell/
keywords: Bu makale, GridWeb de bir hücre (GridCell) için stil biçimi nasıl ayarlayacağınızı veya uygulayacağınızı tanıtır.
description: Bu makale, GridWeb deki bir hücrede stili nasıl ayarlayacağınızı veya uygulayacağınızı tanıtıyor.
---

{{% alert color="primary" %}} 

Bu konu, hücreleri nasıl biçimlendireceğiniz hakkında detaylı bir tartışma sunar.

Aspose.Cells.GridWeb kontrolünün Stil iletişim kutusunu kullanarak GUI modunda hücreleri biçimlendirme konusunu kapsar. Ayrıca, hücreleri programlı olarak biçimlendirmenin nasıl yapıldığını gösterir. Font, kenar ve numara biçimi gibi farklı biçim ayarları örneklerle anlatılmıştır.

{{% /alert %}} 
## **Stil İletişim Kutusu Kullanarak Hücreleri Biçimlendirme**
Hücreler [programlı olarak](/cells/tr/net/aspose-cells-gridweb/format-cells/) biçimlendirilebilir ancak Aspose.Cells.GridWeb kontrolünde hücreleri en kolay biçimlendirmenin yolu, Stil iletişim kutusunu kullanmaktır.

Stil iletişim kutusunu kullanmak için:
Hücre aralığını seçin, ardından sağ tıklayarak **Hücre Biçimi**'ni seçin. 

**Biçim Hücresi Seçme** 

![todo:image_alt_text](format-cells_1.png)



Stil iletişim kutusu görüntülenir. 

**Stil iletişim kutusu, hücreleri biçimlendirmek için kullanılır** 

![todo:image_alt_text](format-cells_2.png)

Stil iletişim kutusu, kullanıcıların yazı tipi ve kenarlık ayarlarını özelleştirerek hücreleri biçimlendirmelerine olanak tanır.
### **Yazı Tipi Ayarlarını Özelleştirme**
Stil iletişim kutusu kullanılarak aşağıdaki yazı tipi ayarlarını özelleştirebilirsiniz:

- Yazı tipi, listeden istenen yazı tipini seçin.
- Yazı stili, kalın, eğik vb. gibi bir yazı stili uygulayın.
- Yazı boyutu, punto cinsinden bir yazı boyutu seçin.
- Altı çizili, metni altı çizili hale getirin.
- Üstü çizili, metne üstü çizili bir efekt uygulayın.
- Yatay hizalama, yatay hizalamayı seçin.
- Dikey hizalama, dikey hizalamayı seçin.
- Yazı rengi, bir yazı rengi seçin.
- Arka plan, arka plan için bir renk seçin.

Seçili yazı tipi ayarlarını küçük bir önizleme alanında kontrol edebilirsiniz.

**Özelleştirilmiş yazı tipi ayarları** 

![todo:image_alt_text](format-cells_3.png)
### **Kenarlık Ayarlarını Özelleştirme**
Kontrol, ayrıca hücrelerin etrafına kenarlık çizmelerini Stil iletişim kutusunda kenarlık ayarlarını özelleştirerek oluşturmasına izin verir.

Kenarlık ile ilgili seçenekleri görüntülemek için:
**Kenarlık**'ı Stil iletişim kutusunda tıklayın.
Kenarlık ile ilgili seçenekler görüntülenir. 

**Stil iletişim kutusundaki kenarlık seçenekleri** 

![todo:image_alt_text](format-cells_4.png)

Aşağıdaki kenarlık seçenekleri Stil iletişim kutusundan seçilebilir:

- Kenarlık çizgi stili, düz, kesikli vb. gibi kenarlık stiline göre seçin.
- Kenarlık çizgi genişliği, kenarlık genişliğini piksel cinsinden seçin.
- Kenarlık çizgi rengi, çizgi rengini seçin.
- Kenar çizgileri, kenar çizgilerinin numaralandırmasını ve konumlandırmasını seçin.

**Özelleştirilmiş kenarlık ayarları** 

![todo:image_alt_text](format-cells_5.png)
### **Ayarları Uygulama**
Değişiklikleri uygulamak için Stil iletişim kutusunda **Tamam**'ı tıklayın.

**Yazı tipi ve kenarlık ayarları uygulandı** 

![todo:image_alt_text](format-cells_6.png)


## **API Kullanarak Hücreleri Biçimlendirme**
Hücreler ayrıca Aspose.Cells.GridWeb API ile programlı olarak biçimlendirilebilir. Her hücrenin bir Stil özelliği vardır, bu özellik bir GridTableItemStyle nesnesini temsil eder. Yazı tipi ve kenarlık ayarlarını özelleştirmek için Stil özelliğini kullanın.
### **Yazı Tipi Ayarı**
Programlı olarak yazı tipi ayarlarını özelleştirmek için:

1. Aspose.Cells.GridWeb denetimini bir Web Formuna ekleyin.
1. Bir çalışsayı açın.
1. Biçimlendirme yapmak istediğiniz hücreye erişin.
1. Hücrenin stiline erişin.
1. Punto cinsinden yazı tipi boyutunu ayarlayın.
1. Yazı tipi stilini ayarlayın.
1. Ön plan ve arka plan renklerini ayarlayın.
1. Yatay ve dikey hizalamayı ayarlayın.
1. Stili hücreye geri ayarlayın.

**Çıktı: A1'de özelleştirilmiş yazı tipi ayarları gösterilir** 

![todo:image_alt_text](format-cells_7.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyFontStyles.cs" >}}
### **Kenarlık Ayarı**
Kenarlıklar tek tek hücrelere veya bir aralığa uygulanabilir.
#### **Tekil Hücre**
Bir tek hücrenin kenarlıklarını ayarlamak için:

1. Aspose.Cells.GridWeb denetimini bir Web Formuna ekleyin.
1. Bir çalışsayı açın.
1. Biçimlendirmek istediğiniz hücreye erişin.
1. Hücrenin Stil nesnesine erişin.
1. Kenarlık stili ayarlayın.
1. Kenarlık genişliğini piksel cinsinden ayarlayın.
1. Kenarlık rengini ayarlayın.
1. Stili hücreye ayarlayın.

**Tek bir hücrede özelleştirilmiş kenarlık ayarları** 

![todo:image_alt_text](format-cells_8.png)

{{% alert color="primary" %}} 

Hücrenin Stil.TopBorderStyle, Stil.BottomBorderStyle, Stil.LeftBorderStyle, Stil.RightBorderStyle özellikleri ile her kenar çizgisi için farklı stiller belirlenebilir.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyBorderStyles.cs" >}}
#### **Hücrelerin Aralığı**
Bir hücreler aralığına kenarlıklar eklemek için:

1. Web Formunuza Aspose.Cells.GridWeb denetimini ekleyin
1. İstenilen çalışma sayfasına erişin
1. WebBorderStyle sınıfından bir nesne örneği oluşturun
1. Sınırın Stilini Düz veya Kesik vb. olarak ayarlayın.
1. Sınırın Genişliğini piksel cinsinden ayarlayın
1. Sınırın Rengini ayarlayın
1. WebBorderStyle nesnesinde depolanan sınır ayarlarını belirtilen hücre aralığına uygulayın

**Özel sınır ayarlarına sahip bir hücre aralığı** 

![todo:image_alt_text](format-cells_9.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyRangeBorderStyles.cs" >}}
### **Sayı Biçimlerini Ayarlama**
Aspose.Cells.GridWeb numara formatlarını destekler. 59 adet yerleşik numara formatı bulunmaktadır. Onları görmek için lütfen şu [desteklenen numara formatları listesine](/cells/tr/net/aspose-cells-gridweb/list-of-supported-number-formats/) başvurun.

Tüm yerleşik numara formatları NumberType numaralandırmasında bulunmaktadır. Bir yerleşik numara formatını kullanmak için, hücrenin SetNumberType yöntemini NumberType numaralandırmasından bir numara formatına ayarlayın.

Özel numara formatını ayarlamak için hücrenin SetCustom yöntemini kullanın.

**B1 ve B2 üzerine uygulanan numara formatı ayarları** 

![todo:image_alt_text](format-cells_10.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-FormatCells.aspx-ApplyNumberFormats.cs" >}}
