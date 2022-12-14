---
title: Çalışma Sayfası Görünümleri
type: docs
weight: 10
url: /tr/java/worksheet-views/
---
## **Sayfa Sonu Önizlemesi**
Tüm çalışma sayfaları iki modda görüntülenebilir:

- Normal görünüm.
- Sayfa sonu önizlemesi.

Normal görünüm, çalışma sayfasının varsayılan görünümüdür. Sayfa sonu önizlemesi, bir çalışma sayfasını yazdırılacağı şekilde görüntüleyen bir düzenleme görünümüdür. Sayfa sonu önizlemesi, yazdırma alanını ve sayfa sonlarını ayarlayabilmeniz için her sayfada hangi verilerin olacağını gösterir. Aspose.Cells'i kullanan geliştiriciler, normal görünüm veya sayfa sonu önizleme modlarını etkinleştirebilir.
### **Görünüm Modlarını Kontrol Etme**
 Aspose.Cells bir sağlar[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Microsoft Excel dosyasını temsil eden sınıf. bu[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıf bir içerir[Çalışma Sayfası Koleksiyonu](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)Bu, bir Excel dosyasındaki her çalışma sayfasına erişim sağlar.

 Bir çalışma sayfası şununla temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf. bu[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) class, çalışma sayfalarını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Normal veya sayfa sonu önizleme modlarını etkinleştirmek için[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf'[setPageBreakÖnizleme](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)yöntem.
#### **Normal Görünümü Etkinleştirme**
kullanarak herhangi bir çalışma sayfasını normal görünüme ayarlayın.[setPageBreakÖnizleme](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) yöntemi[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf ve geçiş**yanlış** parametre olarak.
#### **Sayfa Sonu Önizlemesini Etkinleştirme**
kullanarak herhangi bir çalışma sayfasını sayfa sonu önizlemesine ayarlayın.[setPageBreakÖnizleme](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)yöntemi[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf ve geçiş**doğru**parametre olarak.

 kullanımını gösteren tam bir örnek aşağıda verilmiştir.[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf'[setPageBreakÖnizleme](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview)Excel dosyasının ilk çalışma sayfası için sayfa sonu önizleme modunu etkinleştirme yöntemi.

Aşağıdaki ekran görüntüsünde Book1.xls dosyasının Normal Görünümde olduğunu görebilirsiniz.

**Book1.xls: Değişiklikten önceki çalışma sayfası** 

![yapılacaklar:resim_alternatif_Metin](worksheet-views_1.png)

 Book1.xls ile açılır[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)class ve mod, ilk çalışma sayfası için sayfa sonu önizlemesine geçer. Değiştirilen dosya output.xls olarak kaydedilir.

**Çıktı.xls: değişiklikten sonra çalışma sayfası** 

![yapılacaklar:resim_alternatif_Metin](worksheet-views_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageBreakPreview-PageBreakPreview.java" >}}
## **Yakınlaştırma Faktörü**
Microsoft Excel, kullanıcıların bir çalışma sayfasının yakınlaştırma veya ölçekleme faktörünü ayarlamasına olanak tanıyan bir özellik sağlar. Bu özellik, kullanıcıların çalışma sayfası içeriğini daha küçük veya daha büyük görünümlerde görmelerine yardımcı olur. Kullanıcılar yakınlaştırma faktörünü herhangi bir değere ayarlayabilir.

**Microsoft Excel kullanarak Yakınlaştırma Faktörünü Ayarlama** 

![yapılacaklar:resim_alternatif_Metin](worksheet-views_3.png)

Aspose.Cells, geliştiricilerin çalışma sayfası yakınlaştırma faktörünü ayarlamasına da olanak tanır.
### **Yakınlaştırma Faktörünü Kontrol Etme**
Aspose.Cells bir sağlar[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Microsoft Excel dosyasını temsil eden sınıf. bu[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıf bir içerir[Çalışma Sayfası Koleksiyonu](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)Bu, bir Excel dosyasındaki her çalışma sayfasına erişim sağlar.

 Bir çalışma sayfası şununla temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf. bu[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) class, çalışma sayfalarını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Bir çalışma sayfasının yakınlaştırma faktörünü ayarlamak için[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf'[yakınlaştırmayı ayarla](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom)yöntem.

 nasıl kullanılacağını gösteren eksiksiz bir örnek aşağıda verilmiştir.[yakınlaştırmayı ayarla](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom)Excel dosyasındaki ilk çalışma sayfasının yakınlaştırma faktörünü ayarlama yöntemi.

Aşağıdaki ekran görüntüsünde Book1.xls dosyasını varsayılan görünümde görebilirsiniz.

**Book1.xls: değişiklikten önceki çalışma sayfası** 

![yapılacaklar:resim_alternatif_Metin](worksheet-views_4.png)

 Book1.xls dosyası şu şekilde açılır:[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)class ve ilk çalışma sayfasının yakınlaştırma faktörü 75 olarak ayarlanır. Değiştirilen dosya output.xls olarak kaydedilir.

**Output.xls: değişiklikten sonra çalışma sayfası** 

![yapılacaklar:resim_alternatif_Metin](worksheet-views_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ZoomFactor-ZoomFactor.java" >}}
## **Donma bölmeleri**
Bölmeleri dondur, Microsoft Excel tarafından sağlanan bir özelliktir. Bölmeleri dondurmak, bir çalışma sayfasında kaydırırken görünür kalacak verileri seçmenize olanak tanır.

**Microsoft Excel'de donma bölmelerini kullanma** 

![yapılacaklar:resim_alternatif_Metin](worksheet-views_6.png)

Aspose.Cells, geliştiricilerin çalışma zamanında çalışma sayfalarına bölmeleri dondurma uygulamasına da izin verir.

Aspose.Cells bir sağlar[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Microsoft Excel dosyasını temsil eden sınıf. bu[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıf bir içerir[Çalışma Sayfası Koleksiyonu](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)Bu, bir Excel dosyasındaki her çalışma sayfasına erişim sağlar.

 Bir çalışma sayfası şununla temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf. bu[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) class, çalışma sayfalarını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Bölmeleri dondurmak için,[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf'[donma bölmeleri](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\) ) yöntem. bu[donma bölmeleri](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\)) yöntemi aşağıdaki parametreleri alır:

- **Sıra**, dondurmanın başlayacağı hücrenin satır dizini.
- **Kolon**, dondurmanın başlayacağı hücrenin sütun dizini.
- **Donmuş satırlar**, üst bölmedeki görünür satırların sayısı.
- **Dondurulmuş sütunlar**, sol bölmedeki görünür sütunların sayısı

 nasıl kullanılacağını gösteren eksiksiz bir örnek aşağıda verilmiştir.[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf'[donma bölmeleri](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\)) Excel dosyasının ilk çalışma sayfasının satırlarını ve sütunlarını dondurma yöntemi (C4'ten başlayarak, 4. satır ve 3. sütunla temsil edilir, burada satırlar ve sütunlar 0 dizinden başlar).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FreezePanes-FreezePanes.java" >}}


Aşağıdaki ekran görüntüsünde, Book1.xls dosyasını donma bölmeleri olmadan görebilirsiniz.

**Book1.xls: herhangi bir değişiklikten önce çalışma sayfası görünümü** 

![yapılacaklar:resim_alternatif_Metin](worksheet-views_7.png)

 Book1.xls dosyası şu şekilde açılır:[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)class ve ardından ilk çalışma sayfasında birkaç satır ve sütun dondurulur. Değiştirilen dosya output.xls olarak kaydedilir.

**Outlook.xls: değişiklikten sonra çalışma sayfası görünümü** 

![yapılacaklar:resim_alternatif_Metin](worksheet-views_8.png)
## **Bölme Bölmeleri**
Aynı çalışma sayfasında iki farklı görünüm elde etmek için ekranı bölmeniz gerekiyorsa bölmeleri ayırın. Microsoft Excel, çalışma sayfanızın birden fazla kopyasını görüntülemenize ve çalışma sayfanızın her bölmesinde bağımsız olarak kaydırmanıza izin veren çok kullanışlı bir özellik sunar: bölünmüş bölmeler.

Bölmeler aynı anda çalışır. Birinde değişiklik yaparsanız, değişiklik aynı anda diğerinde de görünür. Aspose.Cells, kullanıcılar için bölünmüş bölmeler özelliği sağlar.
### **Bölünmüş Bölmeleri Uygulama ve Kaldırma**
#### **bölme bölmeleri**
Aspose.Cells bir sağlar[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Microsoft Excel dosyasını temsil eden sınıf. bu[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)class, Excel dosyalarını yönetmek için çok çeşitli özellikler ve yöntemler sağlar. Bölünmüş görünümler uygulamak için[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf'[bölmek](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#split\(\) ) yöntem. Bölünmüş bölmeleri kaldırmak için,[kaldırSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit\(\)) yöntem.

Örnekte, yüklenen basit bir şablon dosyası kullanıyoruz, ardından ilk çalışma sayfasındaki bir hücreye bölünmüş bölmeleri ayarla özelliği uygulandı. Güncellenen dosya kaydedilir.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SplitPanes-SplitPanes.java" >}}



Yukarıdaki kodu çalıştırdıktan sonra, oluşturulan dosya bölünmüş bir görünüme sahip olur.

**Çıkış dosyasındaki bölünmüş bölmeler** 

![yapılacaklar:resim_alternatif_Metin](worksheet-views_9.png)
#### **Bölmeleri Kaldırma**
 Geliştiriciler, bölünmüş bölmeleri kullanarak kaldırabilir[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıf'[kaldırSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit\(\)) yöntem.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovePanes-RemovePanes.java" >}}


## **ileri konular**
- [Çalışma Sayfasında Sıfır Değerlerinin Görüntülenmesini Gizleme](/cells/tr/java/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Çalışma Sayfası Sekme Rengini Ayarla](/cells/tr/java/set-worksheet-tab-color/)
- [Öğeleri Göster ve Gizle](/cells/tr/java/show-and-hide-elements/)
- [Çalışma Sayfasında Değerler Yerine Formülleri Gösterme](/cells/tr/java/show-formulas-instead-of-values-in-a-worksheet/)
- [Hata Denetimi Seçeneklerini Kullanın](/cells/tr/java/use-error-checking-options/)
