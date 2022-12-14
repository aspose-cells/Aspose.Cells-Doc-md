---
title: Aspose.Cells for Java 8.9.0 Sürüm Notları
type: docs
weight: 70
url: /tr/java/aspose-cells-for-java-8-9-0-release-notes/
---
## **1) Aspose.Cells**

|**Anahtar** |**Özet** |**Kategori** |
|:- |:- |:- |
|CELLSJAVA-41901 | Çıktı PDF'sinde çubuklar yukarı doğru hareket ediyor| Artırma|
|CELLSJAVA-41909 | Çalışma Kitabı için Özel Ondalık Sayı ve Grup Ayırıcıları Belirtme Çalışmıyor| Böcek|
|CELLSJAVA-41895 | Formül hesaplama sonucu, Excel yerel hesaplamasından farklıdır| Böcek|
|CELLSJAVA-41917 | SheetRender.toImage() yöntemi kullanılırken onay kutuları doğru şekilde oluşturulmuyor| Böcek|
|CELLSJAVA-41903 | PDF'ye dönüştürülürken karakter yönü farklı| Böcek|
|CELLSJAVA-41896 | Bazı karakterler eksik veya doğrudan Excel'den PDF'e dönüştürme işlemine yapıştırılmamış| Böcek|
|CELLSJAVA-41740 | DataBar resimlerinden bazıları boş| Böcek|
|CELLSJAVA-41769 | Grafiğin çubukları, PDF'deki hücrelerle düzgün şekilde hizalanmamış| Böcek|
|CELLSJAVA-41905 | Elektronik tablo EMF'ye dönüştürüldükten sonra yanlış hizalanmış çubuklar| Böcek|
|CELLSJAVA-41894 |Elektronik tabloyu PDF'ye dönüştürürken karakter boşlukları sorunu| Böcek|
|CELLSJAVA-41893 | Çıkış PDF'sinde arka plan görüntüsü bozuk veya bulanık| Böcek|
|CELLSJAVA-41892 | Çıktı PDF'sinde arka plan görüntüsü uzatılır| Böcek|
|CELLSJAVA-41916 | Cells.copyColumns kullanılırken bozulan harici formül referansları| Böcek|
|CELLSJAVA-41915 | Metin değiştirildikten sonra bozuk XLSX dosyası| Böcek|
|CELLSJAVA-41912 | Adlandırılmış Aralıklara başvuran bir e-tabloda removeFormula ile ilgili sorun| Böcek|
|CELLSJAVA-41899 | FileFormatUtil.detectFileFormat ile XLSX yükleme biçimi algılanamıyor| Böcek|
|CELLSJAVA-41328 | frenchCommonWords.xlsx'te metin bloğu kaybı| Böcek|
|CELLSJAVA-40307 | Metin taşma kontrolü ile ilgili sorun| Böcek|
|CELLSJAVA-41919 | CellsException: 2"="Stra?e zu breit",", Workbook ctor'da| İstisna|
|CELLSJAVA-41914 | java.lang.ArrayIndexOutOfBoundsException: 4 hücrenin yazı tipini alırken| İstisna|
|CELLSJAVA-41920 | StringIndexOutOfBoundsException: Grafiği resme aktarırken dize dizini aralığın dışında: 7| İstisna|
|CELLSJAVA-41913 | İstisna: Excel (XLS) dosyası yüklenirken "IllegalArgumentException: uzunluk"| İstisna|
|CELLSJAVA-41911 | İstisna: Aspose.Cells API'leri aracılığıyla bir Excel dosyası yüklenirken "Cell'de hata: ... -Geçersiz formül"| İstisna|
|CELLSJAVA-41906 |Çalışma kitabı oluşturucu İstisna atar: "java.lang.NumberFormatException: boş Dize"| İstisna|
## **Herkese Açık API ve Geriye Dönük Uyumsuz Değişiklikler**
Aşağıda, API numaralı telefon numarasına eklenen, yeniden adlandırılan, kaldırılan veya kullanımdan kaldırılan üyeler gibi genele açık olarak yapılan tüm değişikliklerin ve Aspose.Cells for Java numaralı telefona yapılan geriye dönük uyumlu olmayan değişikliklerin bir listesi bulunmaktadır. Listelenen herhangi bir değişiklikle ilgili endişeleriniz varsa lütfen şu adrese bildirin: Aspose.Cells destek forumu.
### **HtmlSaveOptions.DefaultFontName özelliğini ekler**
HTML dışa aktarılırken varsayılan yazı tipi adını belirtir, stil yazı tipi olmadığında varsayılan yazı tipi kullanılacaktır. Bu özellik null ise, Aspose.Cells orijinal yazı tipiyle aynı aileye sahip evrensel yazı tipini kullanır, varsayılan değer boştur.
### **PivotTable.IsExcel2003Compatible özelliğini ekler**
PivotTable yenilenirken PivotTable'ın Excel2003 için uyumlu olup olmadığını belirtir. true ise, bir dize 255 karakterden küçük veya buna eşit olmalıdır, bu nedenle dize 255 karakterden büyükse kesilecektir. False ise, bir dize yukarıda belirtilen kısıtlamaya sahip olmayacaktır. Varsayılan değer doğrudur.
### **ImageOrPrintOptions.DefaultFont özelliğini ekler**
Excel'deki karakterler unicode olduğunda ve hücre stilinde doğru yazı tipiyle ayarlanmadığında, PDF ve görüntüde blok olarak görünebilirler.
Bu karakterleri göstermek için MingLiu veya MS Gothic gibi bir Varsayılan Yazı Tipi ayarlayın. Bu özellik ayarlanmazsa, Aspose.Cells, bu unicode karakterleri göstermek için Sistemin varsayılan yazı tipini kullanır.
### **GridWeb'de GetVersion yöntemini ekler.**
Yayın sürümünü edinin.

{{% alert color="primary" %}} 

Aspose.Cells for Java kod tabanı, ilgili .NET sürümünün koduyla eşleştiğinden, Aspose.Cells for .NET v8.9.0'da bulunan değişikliklerin, geliştirmelerin ve düzeltmelerin çoğu bu Aspose.Cells for Java v8.9.0'da da yer almaktadır.

{{% /alert %}}
