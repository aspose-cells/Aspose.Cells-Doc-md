---
title: Çalışma Sayfasını Koru ve Korumayı Kaldır
type: docs
weight: 50
url: /tr/java/protect-and-unprotect-worksheet/
---
## **Çalışma Sayfalarını Koruyun**

Bir çalışma sayfası korunduğunda, kullanıcının yapabileceği işlemler kısıtlanır. Örneğin, veri giremez, satır veya sütun ekleyemez veya silemezler vb. Microsoft Excel'deki genel koruma seçenekleri şunlardır:

- İçindekiler
- nesneler
- senaryolar

Korumalı çalışma sayfaları hassas verileri gizlemez veya korumaz, dolayısıyla dosya şifrelemeden farklıdır. Genel olarak, çalışma sayfası koruması sunum amaçları için uygundur. Son kullanıcının çalışma sayfasındaki verileri, içeriği ve biçimlendirmeyi değiştirmesini engeller.

### **Koruma Ekleme veya Kaldırma**

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. Workbook sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişmeye izin veren bir WorksheetCollection içerir. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf.

 Worksheet sınıfı şunları sağlar:[**Korumak**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#protect(int)) bir çalışma sayfasına koruma uygulamak için kullanılan yöntem. Protect yöntemi aşağıdaki parametreleri kabul eder:

-  Koruma Türü, çalışma sayfasına uygulanacak koruma türü. Koruma türü yardımı ile uygulanır.[**Koruma Türü**](https://reference.aspose.com/cells/java/com.aspose.cells/ProtectionType) numaralandırma.
- Yeni Parola, çalışma sayfasını korumak için kullanılan yeni parola.
- Eski Parola, eski parola, eğer çalışma sayfası zaten parola korumalıysa. Çalışma sayfası zaten korumalı değilse, sadece bir boş değer iletin.

ProtectionType numaralandırması, aşağıdaki önceden tanımlanmış koruma türlerini içerir:

|**Koruma Türleri**|**Tanım**|
|:- |:- |
|[**TÜM**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#ALL)|Kullanıcı bu çalışma sayfasındaki hiçbir şeyi değiştiremez|
|[**İÇİNDEKİLER**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#CONTENTS)|Kullanıcı bu çalışma sayfasına veri giremez|
|[**NESNELER**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#OBJECTS)|Kullanıcı çizim nesnelerini değiştiremez|
|[**SENARYOLAR**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#SCENARIOS)|Kullanıcı kaydedilen senaryoları değiştiremez|
|[**YAPI**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#STRUCTURE)|Kullanıcı kaydedilen yapıyı değiştiremez|
|[**PENCERELER**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#WINDOWS)|Kullanıcı kaydedilen pencereleri değiştiremez|
|[**YOK**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#NONE)|Koruma yok|

Aşağıdaki örnek, bir çalışma sayfasının parola ile nasıl korunacağını gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingWorksheet-ProtectingWorksheet.java" >}}

Çalışma sayfasını korumak için yukarıdaki kod kullanıldıktan sonra, çalışma sayfasını açarak korumayı kontrol edin. Dosyayı açıp çalışma sayfasına bazı veriler eklemeye çalıştığınızda, aşağıdaki iletişim kutusu görüntülenir:

**Bir kullanıcının çalışma sayfasını değiştiremeyeceğini belirten bir iletişim kutusu uyarısı** 

![yapılacaklar:resim_alternatif_Metin](protect-and-unprotect-worksheet_1.png)

Çalışma sayfası üzerinde çalışmak için, çalışma sayfasını seçerek korumayı kaldırın.**Koruma** , sonra**Sayfanın korumasını kaldır** dan**Aletler** Menü öğesi aşağıda gösterildiği gibi.

**Sayfanın Korumasını Kaldır menü öğesini seçme** 

![yapılacaklar:resim_alternatif_Metin](protect-and-unprotect-worksheet_2.png)

Parola isteyen bir iletişim kutusu açılır.

**Çalışma sayfasının korumasını kaldırmak için parola girme** 

![yapılacaklar:resim_alternatif_Metin](protect-and-unprotect-worksheet_3.png)

### **Birkaç Kişiyi Korumak Cells**

 Çalışma sayfasında yalnızca birkaç hücreyi kilitlemeniz gereken belirli senaryolar olabilir. Çalışma sayfasındaki bazı belirli hücreleri kilitlemek istiyorsanız, çalışma sayfasındaki diğer tüm hücrelerin kilidini açmanız gerekir. Bir çalışma sayfasındaki tüm hücreler zaten kilitleme için başlatılmıştır, bu herhangi bir excel dosyasını MS Excel'e açıp kontrol edebilirsiniz.**Biçim | Cells...** göstermek için**Biçim Cells** iletişim kutusunu tıklayın ve ardından Koruma sekmesini tıklayın ve "Kilitli" etiketli bir onay kutusunun varsayılan olarak işaretli olduğunu görün.

Görevi uygulamak için iki yaklaşım aşağıdadır.

**Yöntem 1:**

Aşağıdaki noktalar, MS Excel kullanılarak birkaç hücrenin nasıl kilitleneceğini açıklamaktadır. Bu yöntem Microsoft Office Excel 97, 2000, 2002, 2003 ve üzeri sürümler için geçerlidir.

1. Tümünü Seç düğmesini (1. satır için satır numarasının hemen üzerindeki ve A sütun harfinin solundaki gri dikdörtgen) tıklatarak tüm çalışma sayfasını seçin.
1. Biçim menüsünde Cells'e tıklayın, Koruma sekmesine tıklayın ve ardından Kilitli onay kutusunun işaretini kaldırın.

 Bu, çalışma sayfasındaki tüm hücrelerin kilidini açar

{{% alert color="primary" %}}

Hücre komutu kullanılamıyorsa, çalışma sayfasının bazı bölümleri zaten kilitli olabilir. Araçlar menüsünde, Koruma'nın üzerine gelin ve ardından Sayfanın Korumasını Kaldır'a tıklayın.

{{% /alert %}}

1. Yalnızca kilitlemek istediğiniz hücreleri seçin ve 2. adımı tekrarlayın, ancak bu sefer Kilitli onay kutusunu seçin.
1.  Üzerinde**Aletler** menü, seç**Koruma** , Tıklayın**Sayfayı Koruyun** ve ardından tıklayın**TAMAM**.

{{% alert color="primary" %}}

Sayfayı Koru iletişim kutusunda, bir parola belirleme ve kullanıcıların değiştirebilmesini istediğiniz öğeleri seçme seçeneğiniz vardır.

{{% /alert %}}

**Yöntem2:**

Bu yöntemde sadece görevi yapmak için Aspose.Cells API kullanıyoruz.

Aşağıdaki örnek, çalışma sayfasındaki birkaç hücrenin nasıl korunacağını gösterir. Önce çalışma sayfasındaki tüm hücrelerin kilidini açar ve ardından çalışma sayfasındaki 3 hücreyi (A1, B1, C1) kilitler. Son olarak, çalışma sayfasını korur. Bir satır/sütun, ayrıca bir dizi Kilitli yöntemi içeren bir Stil API'e sahiptir. Satırı / sütunu kilitlemek veya kilidini açmak için bu yöntemi kullanabilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingSpecificCellsinaWorksheet-ProtectingSpecificCellsinaWorksheet.java" >}}

### **Çalışma Sayfasında Bir Satırı Koruma**

 Aspose.Cells, çalışma sayfasındaki herhangi bir satırı kolayca kilitlemenizi sağlar. Burada, kullanabiliriz[**ApplyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/row#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag) ) yöntemi[**Sıra**](https://reference.aspose.com/cells/java/com.aspose.cells/Row) çalışma sayfasındaki belirli bir satıra Stil uygulamak için sınıf. Bu yöntem iki argüman alır: a[**stil**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) nesne ve[**Stil Bayrağı**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) Uygulanan biçimlendirme ile ilgili tüm üyeleri içeren yapı.

Aşağıdaki örnek, çalışma sayfasındaki bir satırın nasıl korunacağını gösterir. Önce çalışma sayfasındaki tüm hücrelerin kilidini açar ve ardından ilk satırı kilitler. Son olarak, çalışma sayfasını korur. Bir satır/sütun, ayrıca bir setCellLocked yöntemi içeren bir Stil API'e sahiptir. StyleFlag yapısını kullanarak satırı / sütunu kilitleyebilir veya kilidini açabilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectRowWorksheet-ProtectRowWorksheet.java" >}}

### **Çalışma Sayfasında Bir Sütunu Koruma**

 Aspose.Cells, çalışma sayfasındaki herhangi bir sütunu kolayca kilitlemenizi sağlar. Burada, kullanabiliriz[**ApplyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/column#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag) ) yöntemi[**Kolon**](https://reference.aspose.com/cells/java/com.aspose.cells/Column) çalışma sayfasındaki belirli bir sütuna Stil uygulamak için sınıf. Bu yöntem iki argüman alır: a[**stil**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) nesne ve[**Stil Bayrağı**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) Uygulanan biçimlendirme ile ilgili tüm üyeleri içeren yapı.

Aşağıdaki örnek, çalışma sayfasındaki bir sütunun nasıl korunacağını gösterir. Önce çalışma sayfasındaki tüm hücrelerin kilidini açar ve ardından ilk sütunu kilitler. Son olarak, çalışma sayfasını korur. Bir satır/sütun, ayrıca bir dizi Kilitli yöntemi içeren bir Stil API'e sahiptir. StyleFlag yapısını kullanarak satırı / sütunu kilitleyebilir veya kilidini açabilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectColumnWorksheet-ProtectColumnWorksheet.java" >}}

## **Bir Çalışma Sayfasının korumasını kaldırın**

[Çalışma Sayfalarını Koruma](/cells/tr/java/protect-and-unprotect-worksheet/#protect-worksheets) ve[Excel XP'den bu yana Gelişmiş Koruma Ayarları](/cells/tr/java/protect-and-unprotect-worksheet/#advanced-protection-settings-since-excel-xp) çalışma sayfalarını korumaya yönelik farklı yaklaşımları tartıştı. Bir geliştiricinin dosyada bazı değişiklikler yapılabilmesi için çalışma zamanında korumalı bir çalışma sayfasındaki korumayı kaldırması gerekirse ne olur? Bu, Aspose.Cells ile kolayca yapılabilir.

### **Microsoft Excel'i kullanma**

Bir çalışma sayfasından korumayı kaldırmak için:

 itibaren**Aletler** menü, seç**Koruma** bunu takiben**Sayfanın korumasını kaldır**.

**Korumayı Kaldır Sayfasını Seçme** 

![yapılacaklar:resim_alternatif_Metin](protect-and-unprotect-worksheet_4.png)

Çalışma sayfası parola korumalı olmadığı sürece koruma kaldırılır. Bu durumda, bir iletişim kutusu parola ister.

**Çalışma sayfasının korumasını kaldırmak için parola girme** 

![yapılacaklar:resim_alternatif_Metin](protect-and-unprotect-worksheet_5.png)

### **Aspose.Cells'i kullanma**

 Bir çalışma sayfası, çağrılarak korumasız bırakılabilir.[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf'[**Korumayı kaldır**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect() ) yöntem. bu[**Korumayı kaldır**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect()) yöntemi aşağıda açıklanan iki şekilde kullanılabilir.

### **Basitçe Korunan Bir Çalışma Sayfasının Korumasını Kaldırma**

Basitçe korunan bir çalışma sayfası, parola ile korunmayan bir çalışma sayfasıdır. Bu tür çalışma sayfaları, bir parametre geçirmeden unprotect yöntemi çağrılarak korumasızlaştırılabilir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectingSimplyProtectedWorksheet-UnprotectingSimplyProtectedWorksheet.java" >}}

### **Parola Korumalı Çalışma Sayfasının Korumasını Kaldırma**

Parola korumalı bir çalışma sayfası, parolayla korunan bir çalışma sayfasıdır. Bu tür çalışma sayfaları, parolayı parametre olarak alan Unprotect yönteminin aşırı yüklenmiş bir sürümü çağrılarak korumasız bırakılabilir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectProtectSheet-UnprotectProtectSheet.java" >}}

## **Excel XP'den bu yana Gelişmiş Koruma Ayarları**

[Çalışma Sayfalarını Koruma](/cells/tr/java/protect-and-unprotect-worksheet/#protect-worksheets) Microsoft Excel 97 ve 2000'de bir çalışma sayfasının korunması ele alındı. Ancak Excel 2002 veya XP'nin piyasaya sürülmesinden bu yana, Microsoft birçok gelişmiş koruma ayarı ekledi. Bu koruma ayarları, kullanıcıların şunları yapmasına izin verir veya kısıtlar:

- Satırları veya sütunları silin.
- İçeriği, nesneleri veya senaryoları düzenleyin.
- Hücreleri, satırları veya sütunları biçimlendirin.
- Satırları, sütunları veya köprüleri ekleyin.
- Kilitli veya kilidi açılmış hücreleri seçin.
- Pivot tabloları ve çok daha fazlasını kullanın.

Aspose.Cells, Excel XP ve sonraki sürümleri tarafından sunulan tüm gelişmiş koruma ayarlarını destekler.

### **Excel XP ve Sonraki Sürümleri Kullanan Gelişmiş Koruma Ayarları**

Excel XP'de bulunan koruma ayarlarını görüntülemek için:

1.  itibaren**Aletler** menü, seç**Koruma** bunu takiben**Sayfayı Koruyun**.
 Bir iletişim kutusu görüntülenir.

   **Excel XP'de koruma seçeneklerini gösteren iletişim kutusu**

![yapılacaklar:resim_alternatif_Metin](protect-and-unprotect-worksheet_6.png)

1. Çalışma sayfası özelliklerine izin verin veya bunları kısıtlayın ya da bir parola uygulayın.

### **Aspose.Cells Kullanarak Gelişmiş Koruma Ayarları**

Aspose.Cells, tüm gelişmiş koruma ayarlarını destekler.

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. Workbook sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir WorksheetCollection koleksiyonu içerir. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf.

 Worksheet sınıfı, bu gelişmiş koruma ayarlarını uygulamak için kullanılan Koruma özelliğini sağlar. Koruma özelliği aslında bir nesnesidir.[**Koruma**](https://reference.aspose.com/cells/java/com.aspose.cells/protection) kısıtlamaları devre dışı bırakmak veya etkinleştirmek için çeşitli Boolean özelliklerini kapsayan sınıf.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtectionSettingsUsingAsposeCells-AdvancedProtectionSettingsUsingAsposeCells.java" >}}

Aşağıda küçük bir örnek uygulama var. Bir Excel dosyasını açar ve Excel XP ve sonraki sürümleri tarafından desteklenen gelişmiş koruma ayarlarının çoğunu kullanır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtection-AdvancedProtection.java" >}}

{{% alert color="primary" %}}

Bu gelişmiş koruma ayarları yalnızca MS Excel XP ve sonraki sürümler tarafından desteklendiğinden, dosyayı EXCEL97TO2003 veya XLSX biçiminde kaydedin.

{{% /alert %}}

### **Cell Kilitleme Sorunu**

Kullanıcıların hücreleri düzenlemesini kısıtlamak istiyorsanız, herhangi bir koruma ayarı uygulanmadan önce hücreler kilitlenmelidir. Aksi takdirde, çalışma sayfası korumalı olsa bile hücreler düzenlenebilir. Microsoft Excel XP'de hücreler aşağıdaki iletişim kutusu aracılığıyla kilitlenebilir:

**Excel XP'de hücreleri kilitlemek için iletişim kutusu** 

![yapılacaklar:resim_alternatif_Metin](protect-and-unprotect-worksheet_7.png)

Aspose.Cells API kullanarak da hücreleri kilitlemek mümkündür. Her hücre, ayrıca bir setLocked yöntemi içeren bir Stil API'e sahiptir. Hücreleri kilitlemek veya kilidini açmak için kullanın.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-LockCell-LockCell.java" >}}
