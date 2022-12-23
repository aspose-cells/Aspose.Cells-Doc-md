---
title: Dolgu Ayarları
type: docs
weight: 50
url: /tr/net/cells-fill-settings/
---
## **Renkler ve Arka Plan Desenleri**

Microsoft Excel, hücrelerin ön plan (anahat) ve arka plan (dolgu) renklerini ve arka plan desenlerini ayarlayabilir.

Aspose.Cells de bu özellikleri esnek bir şekilde destekler. Bu konuda Aspose.Cells kullanarak bu özellikleri kullanmayı öğreniyoruz.

### **Renkleri ve Arka Plan Desenlerini Ayarlama**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf bir sağlar[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) Toplamak. İçindeki her öğe[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) koleksiyon bir nesneyi temsil eder[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)sınıf.

 bu[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) var[**Stil Al**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle/index) ve[**SetStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle/index) bir hücrenin biçimlendirmesini almak ve ayarlamak için kullanılan yöntemler. bu[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style)class, hücrelerin ön plan ve arka plan renklerini ayarlamak için özellikler sağlar. Aspose.Cells bir sağlar[**ArkaplanTürü**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)Aşağıda verilen önceden tanımlanmış bir dizi arka plan deseni içeren numaralandırma.

|**Arka Plan Desenleri**|**Açıklama**|
|:- |:- |
|çapraz çapraz|Çapraz çapraz tarama modelini temsil eder|
|Çapraz Şerit|Çapraz şerit desenini temsil eder|
|Gri6|%6,25 gri deseni temsil eder|
|Gray12|%12,5 gri deseni temsil eder|
|Gri25|%25 gri deseni temsil eder|
|gri50|%50 gri modeli temsil eder|
|gri75|%75 gri deseni temsil eder|
|Yatay Şerit|Yatay şerit desenini temsil eder|
|Hiçbiri|arka planı temsil etmez|
|TersDiagonalŞerit|Ters diyagonal şerit desenini temsil eder|
|Sağlam|Katı modeli temsil eder|
|KalınDiagonalCrossshatch|Kalın çapraz tarama desenini temsil eder|
|İnceÇapraz Çapraz|İnce çapraz tarama modelini temsil eder|
|İnce Çapraz Şerit|İnce çapraz şerit desenini temsil eder|
|İnceYatayCrossshatch|İnce yatay çapraz tarama modelini temsil eder|
|İnce Yatay Şerit|İnce yatay şerit desenini temsil eder|
|İnce Ters Çapraz Şerit|İnce ters köşegen şerit desenini temsil eder|
|İnceDikeyŞerit|İnce dikey şerit desenini temsil eder|
|Dikey Şerit|Dikey şerit desenini temsil eder|

Aşağıdaki örnekte, A1 hücresinin ön plan rengi ayarlanmıştır ancak A2, dikey şerit arka plan deseniyle hem ön plan hem de arka plan renklerine sahip olacak şekilde yapılandırılmıştır.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndBackground-1.cs" >}}

### **Bilmeniz Önemli**

{{% alert color="primary" %}}

-  Bir hücrenin ön plan veya arka plan rengini ayarlamak için[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnenin[**Ön plan rengi**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) veya[**Arka plan rengi**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundcolor) özellikler. Her iki özellik de yalnızca şu durumlarda geçerli olacaktır:[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnenin[**Desen**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)özellik yapılandırılır.
-  bu[**Ön plan rengi**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor)özelliği hücrenin gölge rengini ayarlar.
 bu[**Desen**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern)özelliği, ön plan veya arka plan rengi için kullanılan arka plan deseninin türünü belirtir. Aspose.Cells bir numaralandırma sağlar,[**ArkaplanTürü**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)önceden tanımlanmış bir dizi arka plan deseni içerir.
-  eğer seçersen*ArkaplanTürü.Yok* gelen değer[**ArkaplanTürü**](https://reference.aspose.com/cells/net/aspose.cells/backgroundtype)numaralandırma, ön plan rengi uygulanmaz.
 Aynı şekilde, arka plan rengini seçerseniz arka plan rengi uygulanmaz.*ArkaplanTürü.Yok* veya*ArkaplanTürü.Katı* değerler.
-  Hücrenin gölgeleme/dolgu rengini alırken, eğer[**Stil.Desen**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/pattern) dır-dir*ArkaplanTürü.Yok*, [**Stil.Ön PlanRenk**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundcolor) geri dönücek*Renk.Boş*.

{{% /alert %}}

### **Degrade Dolgu Efektlerini Uygulama**

 İstediğiniz Degrade Dolgu Efektlerini hücreye uygulamak için[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesnenin[**SetTwoColorGradient**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/settwocolorgradient)buna göre yöntem.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ApproachesToFormatData-ApplyingGradientFillEffects-1.cs" >}}

## **Renkler ve Palet**

Palet, bir görüntü oluştururken kullanılabilecek renk sayısıdır. Bir sunumda standartlaştırılmış bir paletin kullanılması, kullanıcının tutarlı bir görünüm oluşturmasına olanak tanır. Her Microsoft Excel (97-2003) dosyası, bir grafikteki hücrelere, yazı tiplerine, kılavuz çizgilerine, grafik nesnelerine, dolgulara ve çizgilere uygulanabilen 56 renk paletine sahiptir.

Aspose.Cells ile paletin mevcut renklerinin yanı sıra özel renklerin de kullanılması mümkündür. Özel bir renk kullanmadan önce palete ekleyin.

Bu konuda palete özel renklerin nasıl ekleneceği anlatılmaktadır.

### **Palete Özel Renkler Ekleme**

Aspose.Cells, Microsoft Excel'in 56 renk paletini destekler. Palette tanımlanmayan özel bir renk kullanmak için rengi palete ekleyin.

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir sağlar[**Paleti Değiştir**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) paleti değiştirmek üzere özel bir renk eklemek için aşağıdaki parametreleri alan yöntem:

- Özel Renk, eklenecek özel renk.
- Dizin, özel rengin değiştireceği paletteki rengin dizini. 0-55 arasında olmalıdır.

Aşağıdaki örnek, bir yazı tipine uygulamadan önce palete özel bir renk (Orkide) ekler.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

Palet sadece 56 renk içerir. Palete özel bir renk eklediğinizde, palet değiştirilir ve önceki renkle biçimlendirilmiş dosyadaki herhangi bir öğe değiştirilir. Bu yüzden paleti değiştirirken lütfen çok dikkatli olun. Ayrıca, bu yalnızca XLS (Excel 97 - 2003) dosya biçimindeki sınırlamadır, çünkü XLSX veya diğer gelişmiş MS Excel (2007/2010 veya 2013) dosya biçimleri için böyle bir sınırlama yoktur.

{{% /alert %}}
