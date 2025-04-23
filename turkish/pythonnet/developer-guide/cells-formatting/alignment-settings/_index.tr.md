---
title: Uyum Ayarları
description: Python için Aspose.Cells via .NET kütüphanesinde, metnin düzeni ve görünümünü ayarlamak için hücre hizalama ayarlarını kullanabilirsiniz. Yatay hizalama, dikey hizalama ve metin kaydırma gibi ayarları ayarlayarak, hücrelerdeki metnin nasıl akışına daha fazla kontrol sahibi olursunuz. Bu belge, Aspose.Cells for Python via .NET kullanarak hücre hizalama ayarlarını hızlıca kavramanıza yardımcı olacak ayrıntılı adımlar ve örnek kodlar sağlayacaktır.
keywords: Aspose.Cells for Python via .NET, hücre hizalaması, yatay hizalama, dikey hizalama, metin kaydırma
type: docs
weight: 20
url: /tr/python-net/cells-alignment-settings/
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

Tüm bu hizalama ayarları Aspose.Cells for Python via .NET tarafından tam olarak desteklenmekte olup, aşağıda daha ayrıntılı olarak tartışılmıştır.

### **Aspose.Cells for Python via .NET'de Hizalama ayarları**

Aspose.Cells for Python via .NET, bir Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) adlı bir sınıf sağlar. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, Excel dosyasındaki her bir çalışma sayfasına erişim sağlayan bir [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) koleksiyon içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sınıfı ise bir [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/) koleksiyonu sağlar. [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) sınıfı nesnesini temsil eder.

Aspose.Cells for Python via .NET, [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) ve [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) metodlarını cell biçimlendirmesini almak ve ayarlamak için sağlar. [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) sınıfı, hizalama ayarlarını yapılandırmak için kullanışlı özellikler sunar.

[**TextAlignmentType**](https://reference.aspose.com/cells/python-net/aspose.cells/textalignmenttype) numarasını kullanarak herhangi bir metin hizalama türünü seçin. [**TextAlignmentType**](https://reference.aspose.com/cells/python-net/aspose.cells/textalignmenttype) numarasındaki önceden tanımlanmış metin hizalama türleri:

|**Metin Hizalama Türleri**|**Açıklama**|
| :- | :- |
|GENEL|Genel metin hizalamasını temsil eder|
|ALT|Alt metin hizalamasını temsil eder|
|ORTA|Orta metin hizalamasını temsil eder|
|ORTA_GEÇİŞİ|Orta metin hizalaması, metinleri yatay olarak ortalar|
|DAĞITILMIŞ|Dağıtılmış metin hizalamasını temsil eder|
|DOLDUR|Doldurma metin hizalamasını temsil eder|
|MEŞH|Yüzde ayarlamasına göre hizalamayı sağlar|
|SOL|Sol metin hizalamasını temsil eder|
|SAĞ|Sağ metin hizalamasını temsil eder|
|ÜST|Üst metin hizalamasını temsil eder|
|DOĞRU_AL|Arapça metin için kashida uzunluğunu ayarlayarak hizalar|
|TAY_DAĞIT|Tayca metni özel olarak dağıtır, çünkü her karakter kelime olarak kabul edilir|

{{% alert color="primary" %}}

Ayrıca [**Style.is_justify_distributed**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_justify_distributed) özelliğini kullanarak düzgün dağıtılmış ayarını uygulayabilirsiniz.

{{% /alert %}}

#### **Yatay Hizalama**

Metni yatay olarak hizalamak için [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) nesnesinin [**horizontal_alignment**](https://reference.aspose.com/cells/python-net/aspose.cells/style/horizontal_alignment) özelliğini kullanın

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-TextAlignmentHorizontal-1.py" >}}

#### **Dikey Hizalama**

Yatay hizalama ile benzer şekilde metni dikey olarak hizalamak için [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) nesnesinin [**vertical_alignment**](https://reference.aspose.com/cells/python-net/aspose.cells/style/vertical_alignment) özelliğini kullanın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-TextAlignmentVertical-1.py" >}}

#### **Girinti**

Hücredeki metnin girinti seviyesini [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) nesnesinin [**indent_level**](https://reference.aspose.com/cells/python-net/aspose.cells/style/indent_level) özelliği ile ayarlamak mümkündür.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-Indentation-1.py" >}}

#### **Yönlendirme**

Hücrede metnin yönlendirmesini (döndürme) [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) nesnesinin [**rotation_angle**](https://reference.aspose.com/cells/python-net/aspose.cells/style/rotation_angle) özelliği ile ayarlayın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-Orientation-1.py" >}}

#### **Metin Kontrolü**

Aşağıdaki bölüm metin kaydırma, sığdırmayı daraltma ve diğer biçimlendirme seçeneklerini ayarlayarak metni nasıl kontrol edeceğinizi tartışmaktadır.

##### **Metni Kaydırma**

Hücrede metni kaydırmak onu okumayı kolaylaştırır: hücrenin yüksekliği, metni kesmek yerine veya yan hücrelere taşmak yerine tüm metni sığdırmak için ayarlanır. Metin kaydırma özelliğini [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) nesnesinin [**is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped) özelliği ile açın veya kapatın.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-LineBreakTextWrapping-WrapText-1.py" >}}

##### **Sığdırmayı Daraltma**

Bir alanın metnini kaydırmak için bir seçenek, metni hücre boyutlarına sığdırmak için metin boyutunu küçültmektir. Bu, **true** olarak [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) nesnesinin [**is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped) özelliği ile ayarlanır.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConfiguringAlignmentSettings-ShrinkingToFit-1.py" >}}

##### **Hücreleri Birleştirme**

Microsoft Excel gibi, Aspose.Cells for Python via .NET birkaç hücreyi bir araya getirip tek hücre yapmayı destekler. Aspose.Cells for Python via .NET bu işlemi gerçekleştirmek için iki yaklaşım sunar. Bir yol, [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/) koleksiyonunun [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/merge) metodunu çağırmaktır. [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/merge) metodu, hücreleri birleştirmek için aşağıdaki parametreleri alır:

- İlk satır: Birleştirmeye başlamak için ilk satır.
- İlk sütun: Birleştirmeye başlamak için ilk sütun.
- Satır sayısı: Birleştirilecek satır sayısı.
- Sütun sayısı: Birleştirilecek sütun sayısı.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Merging-MergingCellsInWorksheet.-1.py" >}}

Diğer yol, öncelikle [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/) koleksiyonunun [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range) yöntemini çağırmak ve birleştirilecek hücrelerin aralığını oluşturmaktır. [**create_range**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/create_range) yöntemi yukarıdaki [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/merge) yönteminin aynı parametre setini alır ve bir [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) nesnesi döndürür. [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) nesnesi ayrıca [**merge**](https://reference.aspose.com/cells/python-net/aspose.cells/range/merge) yöntemi sağlar, bu yöntem [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) nesnesinde belirtilen aralığı birleştirir.

##### **Metin Yönü**

Hücrelerdeki metnin okuma sırasını ayarlamak mümkündür. Okuma sırası, karakterlerin, kelimelerin vb. görüntülendiği görsel sıradır. Örneğin, İngilizce soldan sağa bir dil iken Arapça sağdan sola bir dildir.

Okuma sırası, [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) nesnesinin [**text_direction**](https://reference.aspose.com/cells/python-net/aspose.cells/style/text_direction) özelliği ile ayarlanır. Aspose.Cells for Python via .NET, [**TextDirectionType**](https://reference.aspose.com/cells/python-net/aspose.cells/textdirectiontype) enumerasyonunda önceden tanımlanmış metin yönü türleri sağlar.

|**Metin Yönü Türleri**|**Açıklama**|
| :- | :- |
|KONTEXP|İlk girilen karakterin diline uygun okuma sırası|
|SOL_İÇ|Soldan sağa okuma sırası|
|SAĞ_İÇ|Sağdan sola okuma sırası|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ChangeTextDirection-1.py" >}}

## **Gelişmiş Konular**
- [Hücre Düzenini Değiştirme ve Mevcut Biçimlendirmeyi Koruma](/cells/tr/python-net/change-cells-alignment-and-keep-existing-formatting/)
- [Satır Sonları ve Metin Kaydırma](/cells/tr/python-net/line-breaks-and-text-wrapping/)


