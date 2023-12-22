---
title: Doldurma Ayarları
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmaya yönelik bir .NET kitaplığıdır. Hücrelerin doldurma ayarlarının yapılmasını destekleyerek kullanıcıların hücrelerin arka planını ve stilini özelleştirmesine olanak tanır. Bu makalede hücre doldurma ayarlarını yapmak için Aspose.Cells kitaplığının nasıl kullanılacağı anlatılacaktır.
keywords: Aspose.Cells, Cells, Fill Settings, Background, Style
type: docs
weight: 50
url: /tr/net/cells-fill-settings/
---
##  **Renkler ve Arka Plan Desenleri**

Microsoft Excel, hücrelerin ön plan (anahat) ve arka plan (dolgu) renklerini ve arka plan desenlerini ayarlayabilir.

Aspose.Cells de bu özellikleri esnek bir şekilde desteklemektedir. Bu konumuzda Aspose.Cells'i kullanarak bu özellikleri kullanmayı öğreniyoruz.

###  **Renkleri ve Arka Plan Desenlerini Ayarlama**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bu bir Microsoft Excel dosyasını temsil eder.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**Çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Excel dosyasındaki her çalışma sayfasına erişime izin veren koleksiyon. Bir çalışma sayfası şu şekilde temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf.[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Toplamak. İçindeki her öğe[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyon bir nesneyi temsil eder[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)sınıf.

[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) var[**GetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) Ve[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) Hücrenin biçimlendirmesini almak ve ayarlamak için kullanılan yöntemler.[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style)sınıf, hücrelerin ön plan ve arka plan renklerini ayarlamaya yönelik özellikler sağlar. Aspose.Cells şunları sağlar:[**Arka Plan Türü**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)Aşağıda verilen, önceden tanımlanmış bir dizi arka plan deseni türünü içeren numaralandırma.

|**Arka Plan Desenleri**|**Tanım**|
| :- | :- |
|Çapraz Çapraz Çizgi|Çapraz çizgi desenini temsil eder|
|Çapraz Şerit|Çapraz şerit desenini temsil eder|
|Gri6|%6,25 gri deseni temsil eder|
|Gri12|%12,5 gri deseni temsil eder|
|Gri25|%25 gri deseni temsil eder|
|Gri50|%50 gri deseni temsil eder|
|Gri75|%75 gri deseni temsil eder|
|Yatay Şerit|Yatay şerit desenini temsil eder|
|Hiçbiri|Hiçbir arka planı temsil etmez|
|Ters Çapraz Şerit|Ters çapraz şerit desenini temsil eder|
|Sağlam|Katı deseni temsil eder|
|KalınDiyagonalÇapraz|Kalın çapraz çizgi desenini temsil eder|
|İnceDiagonalÇaprazhatch|İnce çapraz çizgi desenini temsil eder|
|İnce Çapraz Şerit|İnce çapraz şerit desenini temsil eder|
|İnceYatayÇapraz|İnce yatay çapraz çizgi desenini temsil eder|
|İnceYatayŞerit|İnce yatay şerit desenini temsil eder|
|İnceTersDiagonalŞerit|İnce ters çapraz şerit desenini temsil eder|
|İnceDikeyŞerit|İnce dikey şerit desenini temsil eder|
|Dikey Şerit|Dikey şerit desenini temsil eder|

Aşağıdaki örnekte, A1 hücresinin ön plan rengi ayarlanmıştır ancak A2, dikey şerit arka plan deseniyle hem ön plan hem de arka plan renklerine sahip olacak şekilde yapılandırılmıştır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndBackground-1.cs" >}}

###  **Bilmeniz Önemli**

{{% alert color="primary" %}}

-  Bir hücrenin ön plan veya arka plan rengini ayarlamak için[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnenin[**Ön plan rengi**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) veya[**Arka plan rengi**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundcolor) özellikler. Her iki özellik de yalnızca aşağıdaki durumlarda geçerli olacaktır:[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnenin[**Model**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)özellik yapılandırılmıştır.
- [**Ön plan rengi**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor)özelliği hücrenin gölge rengini ayarlar.
[**Model**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)özelliği, ön plan veya arka plan rengi için kullanılan arka plan deseninin türünü belirtir. Aspose.Cells bir numaralandırma sağlar,[**Arka Plan Türü**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype). önceden tanımlanmış bir dizi arka plan deseni türünü içerir.
-  Eğer seçerseniz*Arka Plan Türü. Yok* gelen değer[**Arka Plan Türü**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)numaralandırmada ön plan rengi uygulanmaz.
 Aynı şekilde, arka plan rengini seçerseniz arka plan rengi uygulanmaz.*Arka Plan Türü. Yok* veya*Arka Plan Türü. Katı* değerler.
-  Hücrenin gölgeleme/dolgu rengini alırken, eğer[**Stil.Desen**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) *BackgroundType.None*'dur,[**Stil.Ön PlanRenk**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) *Renk.Empty* değerini döndürecektir.

{{% /alert %}}

###  **Degrade Dolgu Efektleri Uygulama**

 İstediğiniz Degrade Dolgu Efektlerini hücreye uygulamak için[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnenin[**İkiRenkDegradeyi Ayarla**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient)buna göre yöntem.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}

##  **Renkler ve Palet**

Palet, bir görüntü oluştururken kullanılabilecek renklerin sayısıdır. Bir sunumda standartlaştırılmış bir paletin kullanılması, kullanıcının tutarlı bir görünüm oluşturmasına olanak tanır. Her Microsoft Excel (97-2003) dosyasında, bir grafikteki hücrelere, yazı tiplerine, kılavuz çizgilerine, grafik nesnelerine, dolgulara ve çizgilere uygulanabilen 56 renkten oluşan bir palet bulunur.

Aspose.Cells ile paletin sadece mevcut renklerini değil, özel renklerini de kullanmak mümkün. Özel bir renk kullanmadan önce onu palete ekleyin.

Bu konuda palete özel renklerin nasıl ekleneceği anlatılmaktadır.

###  **Palete Özel Renkler Ekleme**

Aspose.Cells, Microsoft Excel'in 56 renk paletini destekler. Palette tanımlanmayan özel bir renk kullanmak için rengi palete ekleyin.

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Microsoft Excel dosyasını temsil eder.[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf sağlar[**Paleti Değiştir**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) Paleti değiştirmek amacıyla özel bir renk eklemek için aşağıdaki parametreleri alan yöntem:

- Özel Renk, eklenecek özel renk.
- Dizin, paletteki özel rengin yerini alacağı rengin dizini. 0-55 arasında olmalıdır.

Aşağıdaki örnek, bir yazı tipine uygulamadan önce palete özel bir renk (Orkide) ekler.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

Palette yalnızca 56 renk bulunur. Palete özel bir renk eklediğinizde palet değiştirilir ve dosyadaki önceki renkle biçimlendirilmiş herhangi bir öğe değiştirilir. Bu nedenle paleti değiştirirken lütfen çok dikkatli olun. Üstelik bu, yalnızca XLS (Excel 97 - 2003) dosya biçimindeki sınırlamadır; XLSX veya diğer gelişmiş MS Excel (2007/2010 veya 2013) dosya biçimleri için böyle bir sınırlama yoktur.

{{% /alert %}}
