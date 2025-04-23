---
title: Sayfa Görünümleri
type: docs
weight: 10
url: /tr/java/worksheet-views/
---

## **Sayfa Kesme Önizleme**
Tüm çalışma sayfaları iki modda görüntülenebilir:

- Normal görünüm.
- Sayfa kesme önizlemesi.

Normal görünüm bir çalışsayfanın varsayılan görünümüdür. Sayfa arazi önizleme, bir çalışsayfanın baskı alacağı gibi bir çalışsayfayı gösteren bir düzenleme görünümüdür. Sayfa arazi önizleme, her sayfaya hangi verilerin gideceğini gösterir, böylece yazdırma alanını ve sayfa aralıklarını ayarlayabilirsiniz. Aspose.Cells geliştiricileri normal görünümü veya sayfa arazi önizlemesi modlarını etkinleştirebilirler.
### **Görünüm Modlarını Kontrol Etme**
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfını sağlar. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı, bir Excel dosyasındaki her çalışsayfaya erişim sağlayan bir [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) içerir.

Bir çalışsayfa, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı tarafından temsil edilir. [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı, çalışsayfaları yönetmek için çeşitli özellikler ve yöntemler sağlar. Normal veya sayfa arazi önizleme modlarını etkinleştirmek için [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfının [setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) yöntemini kullanın.
#### **Normal Görünümü Etkinleştirme**
Herhangi bir çalışsayfayı **false** olarak bir parametre olarak geçirerek [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfının [setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) yöntemini kullanarak herhangi bir çalışsayfayı normal görünüme ayarlayın.
#### **Sayfa Kesme Önizlemesini Etkinleştirme**
[1](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) yöntemini kullanarak **true** olarak herhangi bir çalışsayfayı sayfa arazi önizlemesi kullanacak şekilde ayarlayın.

Aşağıda, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfının [setPageBreakPreview](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsPageBreakPreview) yöntemini kullanarak Excel dosyasının ilk çalışsayfası için sayfa arazi önizleme modunu etkinleştiren bir örnek verilmiştir.

Aşağıdaki ekran görüntüsünde Book1.xls dosyasının Normal Görünümde olduğunu görebilirsiniz.

**Book1.xls: Modifikasyon öncesi çalışsayfa** 

![todo:image_alt_text](worksheet-views_1.png)

Book1.xls, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı ile açılır ve modu ilk çalışsayfa için sayfa arazi önizlemesi olarak değiştirilir. Modifiye edilmiş dosya output.xls olarak kaydedilir.

**Ouput.xls: Modifikasyon sonrası çalışsayfa** 

![todo:image_alt_text](worksheet-views_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageBreakPreview-PageBreakPreview.java" >}}
## **Yakınlaştırma Faktörü**
Microsoft Excel, kullanıcılara bir çalışma tablosunun yakınlaştırma veya ölçekleme faktörünü ayarlamalarına izin veren bir özellik sağlar. Bu özellik, kullanıcıların çalışma tablosu içeriğini daha küçük veya daha büyük görüntülemelerine yardımcı olur. Kullanıcılar yakınlaştırma faktörünü herhangi bir değere ayarlayabilirler.

**Microsoft Excel Kullanarak Yakınlaştırma Faktörünü Ayarlama** 

![todo:image_alt_text](worksheet-views_3.png)

Aspose.Cells ayrıca geliştiricilere çalışsayfanın yakınlaştırma faktörünü ayarlama imkanı sağlar.
### **Yakınlaştırma Faktörünü Kontrol Etme**
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfını sağlar. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı, bir Excel dosyasındaki her çalışsayfaya erişim sağlayan bir [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) içerir.

Bir çalışma sayfası, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı ile temsil edilir. [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı, çalışma sayfalarını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Bir çalışma sayfasının yakınlaştırma faktörünü ayarlamak için, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfının [setZoom](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom) yöntemini kullanın.

Aşağıda, Excel dosyasının ilk çalışma sayfasının yakınlaştırma oranını ayarlamak için [setZoom](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Zoom) yönteminin nasıl kullanılacağını gösteren tam bir örnek verilmiştir.

Aşağıdaki ekran görüntüsünde Book1.xls dosyasının varsayılan görünümde olduğunu görebilirsiniz.

**Book1.xls: herhangi bir değişiklik yapılmadan önce çalışma sayfası** 

![todo:image_alt_text](worksheet-views_4.png)

Book1.xls dosyası, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı aracılığıyla açılır ve ilk çalışsayfanın yakınlaştırma faktörü 75 olarak ayarlanır. Modifiye edilmiş dosya output.xls olarak kaydedilir.

**Output.xls: düzenlemeden sonra çalışma sayfası** 

![todo:image_alt_text](worksheet-views_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ZoomFactor-ZoomFactor.java" >}}
## **Pencereyi Dondurma**
Pencerelerin dondurulmasını sağlayan bir özellik, Microsoft Excel tarafından sağlanır. Pencereyi dondurma, bir çalışma tablosunda kaydırma yaparken görünmesini istediğiniz verileri seçmenize olanak tanır.

**Microsoft Excel'de pencereleri sabitleme kullanma** 

![todo:image_alt_text](worksheet-views_6.png)

Aspose.Cells, geliştiricilere çalışma zamanında çalışma sayfalarına pencereleri sabitleme imkanı sağlar.

Aspose.Cells, Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfını sağlar. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişime izin veren [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)'ı içerir.

Bir çalışma sayfası, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı ile temsil edilir. [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfı, çalışma sayfalarını yönetmek için geniş bir özellik ve yöntem yelpazesi sağlar. Dondurma bölmesi yapılandırmak için, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfının [freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes-int-int-int-int-) metodunu çağırın. [freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes-int-int-int-int-) yöntemi aşağıdaki parametreleri alır:

- **Satır**, dondurulmanın başlayacağı hücrenin satır indeksi.
- **Sütun**, dondurulmanın başlayacağı hücrenin sütun indeksi.
- **Dondurulan satırlar**, üst bölmedeki görünür satır sayısı.
- **Dondurulan sütunlar**, sol bölmedeki görünür sütun sayısı

Aşağıda, Excel dosyasının ilk çalışma sayfasındaki satır ve sütunları (C4'ten başlayarak, 4. satır ve 3. sütun ile temsil edilir, satırlar ve sütunlar 0 indeksinden başlar) dondurmak için [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfının [freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes-int-int-int-int-) yönteminin nasıl kullanılacağı gösterilmektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FreezePanes-FreezePanes.java" >}}


Aşağıdaki ekran görüntüsünde, dondurulmuş pencereler olmadan Book1.xls dosyasını görebilirsiniz.

**Book1.xls: herhangi bir değişiklik öncesi çalışma sayfası görünümü** 

![todo:image_alt_text](worksheet-views_7.png)

Book1.xls dosyası [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı ile açılır ve ardından ilk çalışma sayfasındaki birkaç satır ve sütun dondurulur. Değiştirilmiş dosya, output.xls olarak kaydedilir.

**Outlook.xls: değişiklik sonrası çalışma sayfası görünümü** 

![todo:image_alt_text](worksheet-views_8.png)
## **Bölmeler**
Aynı çalışma tablosunda farklı görünümler elde etmek için ekranı bölmek istemeniz durumunda bölmeler. Microsoft Excel, çalışma sayfanızın kopyasını birden fazla görüntülemenize ve her bir pencerede bağımsız olarak kaydırmanıza izin veren çok kullanışlı bir özellik sunar: bölmeler.

Pencereler aynı anda çalışır. Birinde değişiklik yaparsanız, değişiklik diğerinde aynı anda görünür. Aspose.Cells, kullanıcılar için bölme bölmeleri özelliği sağlar.
### **Bölmelerin Uygulanması ve Kaldırılması**
#### **Bölmeleri Böleme**
Aspose.Cells, Microsoft Excel dosyasını temsil eden bir [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı sağlar. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı, Excel dosyalarını yönetmek için geniş bir özellik ve yöntem yelpazesi sunar. Bölünmüş görünümler uygulamak için, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfının [split](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#split--) yöntemini kullanın. Bölünmüş bölmeleri kaldırmak için, [removeSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit--) yöntemini kullanın.

Örnekte, basit bir şablon dosyası kullanılır, ardından ilk çalışma sayfasındaki bir hücreye bölme bölmeleri özelliği uygulanır. Güncellenmiş dosya kaydedilir.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SplitPanes-SplitPanes.java" >}}



Yukarıdaki kodları çalıştırdıktan sonra, oluşturulan dosyanın bir yerleşik görünümü vardır.

**Çıktı dosyasında yerleşik pencereler** 

![todo:image_alt_text](worksheet-views_9.png)
#### **Pencereleri Kaldırma**
Geliştiriciler, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) sınıfının [removeSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit--) yöntemini kullanarak bölünmüş bölmeleri kaldırabilir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovePanes-RemovePanes.java" >}}


## **Gelişmiş Konular**
- [Çalışma Sayfasında Sıfır Değerlerinin Görüntüsünü Gizleme](/cells/tr/java/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Çalışma Sayfası Sekme Rengini Ayarlama](/cells/tr/java/set-worksheet-tab-color/)
- [Öğeleri Göster ve Gizle](/cells/tr/java/show-and-hide-elements/)
- [Bir Çalışma Kitabındaki Değerlerin Yerine Formülleri Göster](/cells/tr/java/show-formulas-instead-of-values-in-a-worksheet/)
- [Hata Kontrol Seçeneklerini Kullan](/cells/tr/java/use-error-checking-options/)
{{< app/cells/assistant language="java" >}}
