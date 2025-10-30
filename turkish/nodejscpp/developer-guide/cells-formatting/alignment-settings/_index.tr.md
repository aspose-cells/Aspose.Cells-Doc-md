---
title: Uyum Ayarları
linktitle: Uyum Ayarları
description: Aspose.Cells kütüphanesinde, Node.js aracılığıyla C++ kullanarak hücre hizalaması ayarlarını kullanabilirsiniz. Bu belge, Aspose.Cells kullanarak hücre hizalaması ayarları için detaylı adımlar ve örnek kodlar sağlar.
keywords: Aspose.Cells, hücre hizalaması, yatay hizalama, dikey hizalama, metin kaydırma Node.js üzerinden C++
type: docs
weight: 20
url: /tr/nodejs-cpp/cells-alignment-settings/
---

## **Hizalama Ayarlarının Yapılandırılması**

### **Microsoft Excel'deki hizalama ayarları**

Hücreleri biçimlendirmek için Microsoft Excel kullanan herkes, Microsoft Excel'deki hizalama ayarlarına aşinadır.

Yukarıdaki şekilden görebileceğiniz gibi, farklı türde hizalama seçenekleri bulunmaktadır:

- Metin hizalama (yatay ve dikey)
- Girinti
- Yönlendirme
- Metin kontrol
- Metin yönü

Bu tüm hizalama ayarları, Aspose.Cells tarafından tamamen desteklenir ve aşağıda daha detaylı olarak tartışılmaktadır.

### **Aspose.Cells'te hizalama ayarları**

Aspose.Cells, Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) sınıfı, Excel dosyasındaki her sayfaya erişim sağlayan [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) koleksiyonunu içerir. Bir sayfa, [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) sınıfı, [**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) koleksiyonunu sağlar. [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) koleksiyonundaki her öğe [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) sınıfının bir nesnesini temsil eder.

Aspose.Cells, hücre biçimlendirmesini almak ve ayarlamak için kullanılan [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) ve [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) metodlarını sağlar. [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) sınıfı, hizalama ayarlarını yapılandırmak için faydalı özellikler sağlar.

Herhangi bir metin hizalama türünü [**TextAlignmentType**](https://reference.aspose.com/cells/nodejs-cpp/textalignmenttype) enumerasyonu kullanarak seçebilirsiniz. [**TextAlignmentType**](https://reference.aspose.com/cells/nodejs-cpp/textalignmenttype) enumerasyonundaki önceden tanımlı metin hizalama türleri şunlardır:

|**Metin Hizalama Türleri**|**Açıklama**|
| :- | :- |
|Bottom|, alt metin hizalamasını temsil eder
|Center|, merkez metin hizalamasını temsil eder
|CenterAcross|, metin hizalamasını çapraz merkezlemeyi temsil eder
|Distributed|, dağıtılmış metin hizalamasını temsil eder
|Fill|, doldurma metin hizalamasını temsil eder
|General|, genel metin hizalamasını temsil eder
|Justify|, düzgün metin hizalamasını temsil eder
|Left|, sol metin hizalamasını temsil eder
|Right|, sağ metin hizalamasını temsil eder
|Top|, üst metin hizalamasını temsil eder
|JustifiedLow|, Arapça metin için ayarlanmış bir kashida uzunluğuyla metni hizalar.
|ThaiDistributed|, Özellikle Tayland metnini dağıtır, çünkü her karakter bir kelime olarak kabul edilir.

{{% alert color="primary" %}}

Justify dağıtılmış ayarı uygulamak için [**Style.setIsJustifyDistributed(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsJustifyDistributed-boolean-) metodunu kullanabilirsiniz.

{{% /alert %}}

#### **Yatay Hizalama**

Metni yatay olarak hizalamak için [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesinin [**setHorizontalAlignment**](https://reference.aspose.com/cells/nodejs-cpp/style/#setHorizontalAlignment-textalignmenttype-) metodunu kullanın.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-HorizontalAlignment.js" >}}



#### **Dikey Hizalama**

Yatay hizalamanın aynısı gibi, metni dikey olarak hizalamak için [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesinin [**setVerticalAlignment**](https://reference.aspose.com/cells/nodejs-cpp/style/#setVerticalAlignment-textalignmenttype-) metodunu kullanın.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-VerticalAlignment.js" >}}


#### **Girinti**

Bir hücredeki metnin girinti seviyesini [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesinin [**setIndentLevel**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIndentLevel-number-) metodu ile ayarlamak mümkündür.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-Indentation.js" >}}



#### **Yönlendirme**

Bir hücredeki metnin yönünü (rotasyonunu) [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesinin [**setRotationAngle**](https://reference.aspose.com/cells/nodejs-cpp/style/#setRotationAngle-number-) metodu ile ayarlayın.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-Orientation.js" >}}

#### **Metin Kontrolü**

Aşağıdaki bölüm metin kaydırma, sığdırmayı daraltma ve diğer biçimlendirme seçeneklerini ayarlayarak metni nasıl kontrol edeceğinizi tartışmaktadır.

##### **Metni Kaydırma**

Bir hücredeki metni kaydırmak, okunabilirliği artırır: hücrenin yüksekliği, tüm metni sığdıracak şekilde ayarlanır, kesmek veya bitişik hücrelere taşmak yerine. Metin kaydırmayı açık veya kapalı yapmak için [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesinin [**setIsTextWrapped(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsTextWrapped-boolean-) metodunu kullanın.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-WrapText.js" >}}


##### **Sığdırmayı Daraltma**

Bir alan içinde metni sığdırmak için bir seçenek, metin boyutunu hücrenin boyutlarına uyacak şekilde küçültmektir. Bu, [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesinin [**setShrinkToFit(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setShrinkToFit-boolean-) metodunu **doğru** olarak ayarlayarak yapılır.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-ShrinkToFit.js" >}}


##### **Hücreleri Birleştirme**

Microsoft Excel gibi, Aspose.Cells de birkaç hücreyi birleştirmenize destek sağlar. Aspose.Cells, bu işlem için iki yaklaşım sunar. Birincisi, [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) koleksiyonunun [**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-) metodunu çağırmaktır. [**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-) metodu, hücreleri birleştirmek için aşağıdaki parametreleri alır:

- İlk satır: Birleştirmeye başlamak için ilk satır.
- İlk sütun: Birleştirmeye başlamak için ilk sütun.
- Satır sayısı: Birleştirilecek satır sayısı.
- Sütun sayısı: Birleştirilecek sütun sayısı.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-MergeCells.js" >}}


Diğer yöntem, öncelikle [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) koleksiyonunun [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) metodunu çağırıp, birleştirilecek hücrelerin aralığını oluşturmaktır. [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) metodu, yukarıda bahsedilen [**merge**](https://reference.aspose.com/cells/nodejs-cpp/cells/#merge-number-number-number-number-) metoduyla aynı parametreleri alır ve bir [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) nesnesi döner. [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) nesnesi ayrıca, [**merge**](https://reference.aspose.com/cells/nodejs-cpp/range/#merge--) metodunu sağlayarak, belirtilen aralığı [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) nesnesinde birleştirir.

##### **Metin Yönü**

Hücrelerdeki metnin okuma sırasını ayarlamak mümkündür. Okuma sırası, karakterlerin, kelimelerin vb. görüntülendiği görsel sıradır. Örneğin, İngilizce soldan sağa bir dil iken Arapça sağdan sola bir dildir.

Okuma sırası, [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) nesnesinin [**TextDirection**](https://reference.aspose.com/cells/nodejs-cpp/style/#setTextDirection-textdirectiontype-) özelliğiyle ayarlanır. Aspose.Cells, önceden tanımlanmış metin yönü türleri sağlar, bunlar [**TextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/textdirectiontype) enumerasyonunda bulunur.

|**Metin Yönü Türleri**|**Açıklama**|
| :- | :- |
|Context|Girilen ilk karakterin diline uygun okuma sırası|
|LeftToRight|Soldan sağa okuma sırası|
|RightToLeft|Sağdan sola okuma sırası|

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-TextDirection.js" >}}


## **Gelişmiş Konular**
- [Hücre Düzenini Değiştirme ve Mevcut Biçimlendirmeyi Koruma](/cells/tr/nodejs-cpp/change-cells-alignment-and-keep-existing-formatting/)
- [Satır Sonları ve Metin Kaydırma](/cells/tr/nodejs-cpp/line-breaks-and-text-wrapping/)

{{< app/cells/assistant language="nodejs-cpp" >}}
