---
title: Çalışma Sayfasını Koruma ve Kaldırma
type: docs
weight: 50
url: /tr/java/protect-and-unprotect-worksheet/
---

## **Çalışma Sayfalarını Koruma**

Bir çalışma sayfası korunduğunda, bir kullanıcının yapabileceği eylemler sınırlıdır. Örneğin, veri girişi yapamaz, satır veya sütun ekleyemez veya silemez vb. Microsoft Excel'de genel koruma seçenekleri:

- İçerik
- Nesneler
- Senaryolar

Korunan çalışma sayfaları hassas verileri gizlemez veya korumaz, bu yüzden dosya şifrelemesinden farklıdır. Genellikle çalışma sayfası koruması sunum amaçları için uygundur. Bu, son kullanıcının çalışma sayfasındaki verileri, içeriği ve biçimlendirmeyi değiştirmesini engeller.

### **Koruma Ekleme veya Kaldırma**

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfını sağlar. Workbook sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişmeyi sağlayan bir WorksheetCollection içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı tarafından temsil edilir.

Worksheet sınıfı, bir çalışma sayfasına koruma uygulamak için kullanılan [**Protect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#protect-int-) metodunu sağlar. Protect metodu aşağıdaki parametreleri kabul eder:

- Koruma Türü, çalışma sayfasına uygulanacak koruma türü. Koruma türü, [**ProtectionType**](https://reference.aspose.com/cells/java/com.aspose.cells/ProtectionType) numaralandırması ile uygulanır.
- Yeni Parola, çalışma sayfasını korumak için kullanılan yeni parola.
- Eski Şifre, çalışma sayfası zaten şifre korumalıysa eski şifre. Eğer çalışma sayfası zaten korumalı değilse, sadece bir null geçin.

ProtectionType numaralandırması aşağıdaki önceden tanımlanmış koruma türlerini içerir:

|**Koruma Türleri**|**Açıklama**|
| :- | :- |
|[**ALL**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#ALL)|Kullanıcı bu çalışma kitabında hiçbir şeyi değiştiremez|
|[**CONTENTS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#CONTENTS)|Kullanıcı bu çalışma kitabına veri giremez|
|[**OBJECTS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#OBJECTS)|Kullanıcı çizim nesnelerini değiştiremez|
|[**SCENARIOS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#SCENARIOS)|Kullanıcı kaydedilmiş senaryoları değiştiremez|
|[**STRUCTURE**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#STRUCTURE)|Kullanıcı kaydedilmiş yapısı değiştiremez|
|[**WINDOWS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#WINDOWS)|Kullanıcı kaydedilmiş pencereleri değiştiremez|
|[**NONE**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#NONE)|Koruma yok|

Aşağıdaki örnek, bir çalışma sayfasını bir şifre ile korumanın nasıl yapıldığını göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingWorksheet-ProtectingWorksheet.java" >}}

Yukarıdaki kod çalışma kitabını korumak için kullanıldıktan sonra, korumanın çalışma kitabı üzerinde kontrol edilmesi içindir. Dosyayı açtığınızda ve çalışma kitabına birkaç veri eklemeye çalıştığınızda, aşağıdaki iletişim kutusu görüntülenir:

**Kullanıcının çalışma kitabını değiştiremeyeceğine dair bir iletişim kutusu uyarısı** 

![todo:image_alt_text](protect-and-unprotect-worksheet_1.png)

Çalışma kitabında çalışmak için, aşağıda gösterildiği gibi **Araçlar** menü öğesinden **Koruma**, ardından **Çalışma Kitabının Korumasını Kaldır** seçilerek çalışma kitabının korumasını kaldırın.

**Koruma Çalışma Çalışma Kitabını Korumasını Kaldır seçmek** 

![todo:image_alt_text](protect-and-unprotect-worksheet_2.png)

Bir iletişim kutusu, bir parola girmenizi isteyerek açılır.

**Çalışma tablosunu korumak için parolayı girme** 

![todo:image_alt_text](protect-and-unprotect-worksheet_3.png)

### **Bazı Hücreleri Koruma**

Çalışma kitabında sadece belirli hücreleri kilitlemeniz gereken belirli senaryolar olabilir. Çalışma kitabında belirli hücreleri kilitlemek istiyorsanız, çalışma kitabındaki diğer tüm hücreleri kilitsiz bırakmalısınız. Bir çalışma kitabındaki tüm hücreler zaten kilitlemek için başlatılmıştır, bunu kontrol edebilirsiniz MS Excel'e herhangi bir Excel dosyasını açarak ve **Format | Hücreler...** tıklayarak **Hücreleri Biçimlendir** iletişim kutusunu göstermek ve ardından **Koruma** sekmesine tıklayarak "Kilitli" olarak adlandırılan bir onay kutusu işaretlenmiş olduğunu görebilirsiniz.

Görevi uygulamanın iki yaklaşımı aşağıda belirtilmiştir.

**Yöntem1:**

MS Excel kullanarak birkaç hücreyi kilitlemenin aşağıdaki adımları açıklar. Bu yöntem, Microsoft Office Excel 97, 2000, 2002, 2003 ve daha yüksek sürümlerine uygulanır.

1. İlk satırın üstünde ve A sütununun solunda yer alan gri dikdörtgen olan Tümünü Seç düğmesine tıklayarak tüm çalışma kitabını seçin.
1. Format menüsünde Hücreleri tıklayın, Koruma sekmesine tıklayın ve ardından Kilitli onay kutusunu temizleyin.

   Bu, çalışma sayfasındaki tüm hücreleri kilidini açar.

{{% alert color="primary" %}}

Hücreler komutu mevcut değilse, çalışma kitabının bazı bölümleri zaten kilitli olabilir. Araçlar menüsünde Koruma'ya gelin ve ardından Çalışma Kitabının Korumasını Kaldır'ı tıklayın.

{{% /alert %}}

1. Kilitlemek istediğiniz hücreleri seçin ve adım 2'yi tekrarlayın, bu sefer Kilitli onay kutusunu işaretleyin.
1. **Araçlar** menüsünde **Koruma** seçin, **Çalışma Kitabını Koruma**'yı tıklayın ve ardından **Tamam**'ı tıklayın.

{{% alert color="primary" %}}

Çalışma Kitabını Koruma iletişim kutusunda, kullanıcıların değiştirebileceği öğeleri belirtme seçeneğiniz vardır.

{{% /alert %}}

**Yöntem2:**

Bu yöntemde, yalnızca görevi gerçekleştirmek için Aspose.Cells API kullanıyoruz.

Aşağıdaki örnek, çalışma kitabında birkaç hücreyi nasıl koruyacağınızı göstermektedir. İlk olarak çalışma kitabındaki tüm hücreleri kilitsiz bırakır ve ardından (A1, B1, C1) 3 hücreyi kilitleyerek çalışma kitabını korur. Son olarak, çalışma kitabını korur. Bir satır/sütun, kilitleme veya kilidi açma yöntemi içeren bir Stil API'sine sahiptir. Bu yöntemi kullanarak satırı/sütunu kilitleyebilir veya kilidini açabilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingSpecificCellsinaWorksheet-ProtectingSpecificCellsinaWorksheet.java" >}}

### **Çalışma Sayfasında Bir Satırı Koruma**

Aspose.Cells, çalışma tablosundaki herhangi bir satırı kolayca kilitlemenizi sağlar. Burada, çalışma tablosundaki belirli bir satıra stil uygulamak için [**Row**](https://reference.aspose.com/cells/java/com.aspose.cells/Row) sınıfının [**applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/row#applyStyle-com.aspose.cells.Style-com.aspose.cells.StyleFlag-) yöntemini kullanabiliriz. Bu yöntem iki argüman alır: bir [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) nesnesi ve uygulanan biçimlendirmeye ilişkin tüm üyelere sahip olan bir [**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) yapısı.

Aşağıdaki örnek, çalışma tablosunda bir satırı korumanın nasıl yapılacağını göstermektedir. İlk olarak, çalışma tablosundaki tüm hücreleri kilidini açar ve ardından ilk satırı kilitler. Son olarak, çalışma tablosunu korur. Bir satır / sütun, bir setCellLocked yöntemi içeren bir Stil API'ye sahiptir. StilFlag yapısını kullanarak satırı / sütunu kilitleyebilir veya kilidini açabilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectRowWorksheet-ProtectRowWorksheet.java" >}}

### **Çalışma Sayfasında Bir Sütunu Koruma**

Aspose.Cells, çalışma tablosundaki herhangi bir sütunu kolayca kilitlemenizi sağlar. Burada, çalışma tablosundaki belirli bir sütuna stil uygulamak için [**Column**](https://reference.aspose.com/cells/java/com.aspose.cells/Column) sınıfının [**applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/column#applyStyle-com.aspose.cells.Style-com.aspose.cells.StyleFlag-) yöntemini kullanabiliriz. Bu yöntem iki argüman alır: bir [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style) nesnesi ve uygulanan biçimlendirmeye ilişkin tüm üyelere sahip olan bir [**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag) yapısı.

Aşağıdaki örnek, çalışma tablosunda bir sütunu korumanın nasıl yapılacağını göstermektedir. İlk olarak, çalışma tablosundaki tüm hücreleri kilidini açar ve ardından ilk sütunu kilitler. Son olarak, çalışma tablosunu korur. Bir satır / sütun, bir set Locked yöntemi içeren bir Stil API'ye sahiptir. StilFlag yapısını kullanarak satırı / sütunu kilitleyebilir veya kilidini açabilirsiniz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectColumnWorksheet-ProtectColumnWorksheet.java" >}}

## **Bir Çalışma Sayfasını Korumayı Kaldırma**

Microsoft Excel Kullanarak

### **Microsoft Excel Kullanımı**

Çalışma sayfasından korumayı kaldırmak için:

**Tabloyu Korumayı Kaldır** Seçimi

Koruma kaldırıldı, eğer çalışma tablosu parola ile korunmuşsa bir iletişim kutusu parola için istemde bulunur. 

![todo:image_alt_text](protect-and-unprotect-worksheet_4.png)

Koruma kaldırılır, ancak elektronik tablonun parola korunmuş olması durumunda bir parola için bir iletişim kutusu belirir.

**Çalışma tablosunu korumak için parolayı girme** 

![todo:image_alt_text](protect-and-unprotect-worksheet_5.png)

### **Aspose.Cells Kullanımı**

Bir çalışma tablosu, [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfının [**Unprotect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect--) yöntemi çağrılarak korumasız hale getirilebilir. Aşağıda açıklanan iki şekilde unprotect yöntemi kullanılabilir.

### **Basitçe Korumalı Bir Çalışma Tablosu Korumasız Yapma**

Basitçe korunmuş bir çalışma tablosu, parola ile korunmamış olan çalışma tablosudur. Bu tür çalışma tabloları, bir parametre geçirmeden unprotect yöntemi çağrılarak korumasız hale getirilebilir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectingSimplyProtectedWorksheet-UnprotectingSimplyProtectedWorksheet.java" >}}

### **Parola ile Korunan Bir Çalışma Tablosu Korumasız Yapma**

Parola ile korunan bir çalışma tablosu, parola ile korunan bir çalışma tablosudur. Bu tür çalışma tabloları, parolayı parametre olarak alan Unprotect yönteminin aşırı yüklenmiş bir sürümünü çağırarak korumasız hale getirilebilir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectProtectSheet-UnprotectProtectSheet.java" >}}

## **Excel XP’den bu yana Gelişmiş Koruma Ayarları**

[Çalışma Tablolarını Koruma](/cells/tr/java/protect-and-unprotect-worksheet/#protect-worksheets), Microsoft Excel 97 ve 2000'de bir çalışma tablosunu korumanın farklı yaklaşımlarını tartışmıştır. Ancak, Excel 2002 veya XP'nin piyasaya sürülmesinden bu yana, Microsoft birçok gelişmiş koruma ayarı eklemiştir. Bu koruma ayarları kullanıcıların şunları yapmasını kısıtlar veya izin verir:

- Satırları veya sütunları sil.
- İçerik, nesneler veya senaryoları düzenle.
- Hücreleri, satırları veya sütunları biçimlendir.
- Satırları, sütunları veya hyperlinkleri ekle.
- Kilitli veya kilitsiz hücreleri seç.
- Özet tabloları ve çok daha fazlasını kullanın.

Aspose.Cells, Excel XP ve sonraki sürümlerinin sunduğu tüm gelişmiş koruma ayarlarını destekler.

### **Excel XP'de bulunan koruma ayarlarını görüntülemek için:**

**Araçlar** menüsünden **Koruma** ardından **Sayfayı Koru**'yu seçin.

Bir iletişim kutusu görüntülenir.
   Bir iletişim kutusu görüntülenir.

   **Excel XP'de koruma seçeneklerini gösteren iletişim kutusu**

![todo:image_alt_text](protect-and-unprotect-worksheet_6.png)

1. İzinleri belirleyin veya kısıtlayın veya bir şifre uygulayın.

### **Aspose.Cells Kullanarak Gelişmiş Koruma Ayarları**

Aspose.Cells, tüm gelişmiş koruma ayarlarını destekler.

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfını sağlar. Workbook sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan WorksheetCollection koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı tarafından temsil edilir.

Protection özelliğini sağlayan Worksheet sınıfı ise bu gelişmiş koruma ayarlarını uygulamak için kullanılır. Protection özelliği aslında, devre dışı bırakma veya kısıtlamaları etkinleştirmek için çeşitli Boolean özellikleri kapsayan [**Protection**](https://reference.aspose.com/cells/java/com.aspose.cells/protection) sınıfının bir nesnesidir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtectionSettingsUsingAsposeCells-AdvancedProtectionSettingsUsingAsposeCells.java" >}}

Aşağıda küçük bir örnek uygulama bulunmaktadır. Bir Excel dosyası açar ve Excel XP ve sonraki sürümler tarafından desteklenen gelişmiş koruma ayarlarının çoğunu kullanır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtection-AdvancedProtection.java" >}}

{{% alert color="primary" %}}

Bu gelişmiş koruma ayarları sadece MS Excel XP ve sonraki sürümler tarafından desteklendiği için dosyayı EXCEL97TO2003 veya XLSX formatına kaydedin.

{{% /alert %}}

### **Hücre Kilitleme Sorunu**

Hücreleri düzenleme yasağını kullanıcıların sınırlandırmak istiyorsanız, koruma ayarları uygulanmadan önce hücrelerin kilidini yapmanız gerekmektedir. Aksi takdirde, sayfa korunmuş olsa bile hücreler düzenlenebilir. Microsoft Excel XP'de, hücreleri aşağıdaki iletişim kutusu aracılığıyla kilitleyebilirsiniz:

Excel XP'de hücreleri kilitlemek için iletişim kutusu 

![todo:image_alt_text](protect-and-unprotect-worksheet_7.png)

Aspose.Cells API'sını kullanarak hücreleri kilitlemek de mümkündür. Her hücrenin bir Style API'si vardır ve bunun içinde hücreleri kilitlemek veya kilidini açmak için setLocked yöntemini içerir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-LockCell-LockCell.java" >}}
{{< app/cells/assistant language="java" >}}
