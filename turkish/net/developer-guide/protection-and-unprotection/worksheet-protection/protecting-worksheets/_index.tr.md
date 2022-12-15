---
title: Çalışma Sayfalarını Koruma
type: docs
weight: 10
url: /tr/net/protecting-worksheets/
---
{{% alert color="primary" %}}

Bir çalışma sayfası korunduğunda, kullanıcının yapabileceği işlemler kısıtlanır. Örneğin, veri giremez, satır veya sütun ekleyemez veya silemezler vb.

{{% /alert %}}

## **Çalışma Sayfalarını Koruyun**

### **giriiş**

Microsoft Excel'deki genel koruma seçenekleri şunlardır:

- İçindekiler
- nesneler
- senaryolar

Korumalı çalışma sayfaları hassas verileri gizlemez veya korumaz, dolayısıyla dosya şifrelemeden farklıdır. Genel olarak, çalışma sayfası koruması sunum amaçları için uygundur. Son kullanıcının çalışma sayfasındaki verileri, içeriği ve biçimlendirmeyi değiştirmesini engeller.

### **Çalışma Sayfasını Koruma**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf bir içerir[**çalışma sayfaları**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan koleksiyon. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)sınıf.

 bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sınıf sağlar[**Korumak**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index) çalışma sayfasına koruma uygulamak için kullanılan yöntem.[**Korumak**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/protect/methods/1) yöntem aşağıdaki parametreleri kabul eder:

-  Koruma Türü, çalışma sayfasına uygulanacak koruma türü. Koruma türü yardımı ile uygulanır.[**Koruma Türü**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype)numaralandırma.
- Yeni Parola, çalışma sayfasını korumak için kullanılan yeni parola.
- Eski Parola, eski parola, eğer çalışma sayfası zaten parola korumalıysa. Çalışma sayfası zaten korumalı değilse, sadece boş değeri iletin.

 bu[**Koruma Türü**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype)numaralandırma, aşağıdaki önceden tanımlanmış koruma türlerini içerir:

|**Koruma Türleri**|**Tanım**|
|:- |:- |
|Herşey|Kullanıcı bu çalışma sayfasındaki hiçbir şeyi değiştiremez|
|İçindekiler|Kullanıcı bu çalışma sayfasına veri giremez|
|nesneler|Kullanıcı çizim nesnelerini değiştiremez|
|senaryolar|Kullanıcı kaydedilen senaryoları değiştiremez|
|Yapı|Kullanıcı yapıyı değiştiremez|
|Windows|Koruma pencerelere uygulanır|
|Hiçbiri|Koruma uygulanmaz|

Aşağıdaki örnek, bir çalışma sayfasının parola ile nasıl korunacağını gösterir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingWorksheet-1.cs" >}}

Yukarıdaki kod çalışma sayfasını korumak için kullanıldıktan sonra, çalışma sayfasını açarak korumayı kontrol edebilirsiniz. Dosyayı açıp çalışma sayfasına bazı veriler eklemeye çalıştığınızda, aşağıdaki iletişim kutusunu göreceksiniz:

|**Bir kullanıcının çalışma sayfasını değiştiremeyeceğini belirten bir iletişim kutusu uyarısı**|
|:- |
|![yapılacaklar:resim_alternatif_Metin](protecting-worksheets_1.png)|

Çalışma sayfası üzerinde çalışmak için, çalışma sayfasını seçerek korumayı kaldırın.**Koruma** , sonra**Sayfanın korumasını kaldır** dan**Aletler** menü seçeneği.

Sayfanın Korumasını Kaldır menü öğesini seçtikten sonra, aşağıda gösterildiği gibi çalışma sayfası üzerinde çalışabilmeniz için parolayı girmenizi isteyen bir iletişim kutusu açılır:

|![yapılacaklar:resim_alternatif_Metin](protecting-worksheets_2.png)|

### **Microsoft Excel'i Kullanarak Çalışma Sayfasında birkaç Cells'i koruyun**

 Çalışma sayfasında yalnızca birkaç hücreyi kilitlemeniz gereken belirli senaryolar olabilir. Çalışma sayfasındaki bazı belirli hücreleri kilitlemek istiyorsanız, çalışma sayfasındaki diğer tüm hücrelerin kilidini açmanız gerekir. Bir çalışma sayfasındaki tüm hücreler zaten kilitleme için başlatılmıştır, bu herhangi bir excel dosyasını MS Excel'e açıp kontrol edebilirsiniz.**Biçim | Cells...** göstermek için**Biçim Cells**iletişim kutusuna tıklayın ve ardından**Koruma** sekmesine gidin ve "Kilitli" etiketli bir onay kutusunun varsayılan olarak işaretli olduğunu görün.

Aşağıdaki noktalar, MS Excel kullanılarak birkaç hücrenin nasıl kilitleneceğini açıklamaktadır. Bu yöntem Microsoft Office Excel 97, 2000, 2002, 2003 ve üzeri sürümler için geçerlidir.

1.  Tüm çalışma sayfasını tıklayarak seçin**Hepsini seç** düğmesi (1. satır için satır numarasının hemen üzerindeki ve A sütun harfinin solundaki gri dikdörtgen).
1.  Tıklamak**Cells** üzerinde**Biçim** menü, tıklayın**Koruma** sekmesini seçin ve ardından**Kilitli** onay kutusu.
 Bu, çalışma sayfasındaki tüm hücrelerin kilidini açar
 Eğer**Cells** komutu kullanılamıyorsa, çalışma sayfasının bazı bölümleri zaten kilitli olabilir. Üzerinde**Aletler** menü, üzerine gelin**Koruma** ve ardından tıklayın**Sayfanın korumasını kaldır**.
1.  Yalnızca kilitlemek istediğiniz hücreleri seçin ve 2. adımı tekrarlayın, ancak bu kez**Kilitli** onay kutusu.
1.  Üzerinde**Aletler** menü, üzerine gelin**Koruma** , Tıklayın**Sayfayı Koruyun** ve ardından tıklayın**TAMAM**.
1.  İçinde**Sayfayı Koruyun** iletişim kutusunda, bir parola belirleme ve kullanıcıların değiştirebilmesini istediğiniz öğeleri seçme seçeneğiniz vardır.

### **Aspose Cells'i Kullanarak Çalışma Sayfasında birkaç Cells'i koruyun**

Bu yöntemde sadece görevi yapmak için Aspose.Cells API kullanıyoruz.

 Örnek: Aşağıdaki örnek, çalışma sayfasındaki birkaç hücrenin nasıl korunacağını gösterir. Önce çalışma sayfasındaki tüm hücrelerin kilidini açar ve ardından çalışma sayfasındaki 3 hücreyi (A1, B1, C1) kilitler. Son olarak, çalışma sayfasını korur. bu[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style)nesne bir boolean özelliği içeriyor,[**Kilitli**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) . ayarlayabilirsin[**Kilitli**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) özelliği true veya false olarak değiştirin ve uygulayın*Sütun/Satır.ApplyStyle()* Satırı/sütunları istediğiniz niteliklerle kilitlemek veya kilidini açmak için yöntem.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificCellsinaWorksheet-1.cs" >}}

### **Çalışma Sayfasında Bir Satırı Koruma**

 Aspose.Cells, çalışma sayfasındaki herhangi bir satırı kolayca kilitlemenizi sağlar. Burada, kullanabiliriz[**UygulaStyle()**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle) yöntemi[**Aspose.Cells.Row**](https://reference.aspose.com/cells/net/aspose.cells/row) başvurulacak sınıf[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style) çalışma sayfasındaki belirli bir satıra. Bu yöntem iki argüman alır: a[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesne ve[**Stil Bayrağı**](https://reference.aspose.com/cells/net/aspose.cells/styleflag) Uygulanan biçimlendirmeyle ilgili tüm üyeleri içeren nesne.

 Aşağıdaki örnek, çalışma sayfasındaki bir satırın nasıl korunacağını gösterir. Önce çalışma sayfasındaki tüm hücrelerin kilidini açar ve ardından ilk satırı kilitler. Son olarak, çalışma sayfasını korur. bu[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesne bir boolean özelliği içeriyor,[**Kilitli**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) . ayarlayabilirsin[**Kilitli**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) kullanarak satırı/sütunları kilitlemek veya kilidini açmak için özelliği true veya false olarak değiştirin.[**Stil Bayrağı**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)nesne.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificRowInWorksheet-1.cs" >}}

### **Çalışma Sayfasında Bir Sütunu Koruma**

 Aspose.Cells, çalışma sayfasındaki herhangi bir sütunu kolayca kilitlemenizi sağlar. Burada, kullanabiliriz[**UygulaStyle()**](https://reference.aspose.com/cells/net/aspose.cells/column/methods/applystyle) yöntemi[**Aspose.Cells.Column**](https://reference.aspose.com/cells/net/aspose.cells/column) başvurulacak sınıf[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style) çalışma sayfasındaki belirli bir sütuna. Bu yöntem iki argüman alır: a[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesne ve[**Stil Bayrağı**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)Uygulanan biçimlendirmeyle ilgili tüm üyeleri içeren nesne.

Aşağıdaki örnek, çalışma sayfasındaki bir sütunun nasıl korunacağını gösterir. Önce çalışma sayfasındaki tüm hücrelerin kilidini açar ve ardından ilk sütunu kilitler. Son olarak, çalışma sayfasını korur. bu[**stil**](https://reference.aspose.com/cells/net/aspose.cells/style) nesne bir boolean özelliği içeriyor,[**Kilitli**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) . ayarlayabilirsin[**Kilitli**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) kullanarak satırı/sütunları kilitlemek veya kilidini açmak için özelliği true veya false olarak değiştirin.[**Stil Bayrağı**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)nesne.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectColumnWorksheet-1.cs" >}}

### **Kullanıcıların Aralıkları Düzenlemesine İzin Ver**

Aşağıdaki örnek, kullanıcıların korumalı bir çalışma sayfasındaki bir aralığı düzenlemesine nasıl izin verileceğini gösterir.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-EditRangesWorksheet-1.cs" >}}
