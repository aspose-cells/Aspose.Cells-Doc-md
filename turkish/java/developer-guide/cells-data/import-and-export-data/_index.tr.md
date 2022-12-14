---
title: Verileri İçe ve Dışa Aktarma
type: docs
weight: 130
url: /tr/java/import-and-export-data/
---
{{% alert color="primary" %}}

Bu makalede, geliştiricilerin Aspose.Cells aracılığıyla erişebildiği bazı veri içe ve dışa aktarma teknikleri ele alınmaktadır.

{{% /alert %}}

## Verileri Çalışma Sayfasına Aktarın

Veriler dünyayı olduğu gibi temsil eder. Verileri anlamlandırmak için, onu analiz eder ve dünyayı anlarız. Veri bilgiye dönüşür.

Analizi gerçekleştirmenin birçok yolu vardır: verileri elektronik tablolara koymak ve farklı şekillerde manipüle etmek yaygın bir yöntemdir. Aspose.Cells ile, çeşitli dış kaynaklardan veri alan ve bunları analiz için hazırlayan elektronik tablolar oluşturmak kolaydır.

Bu makalede, geliştiricilerin Aspose.Cells aracılığıyla erişebildiği bazı veri içe aktarma teknikleri açıklanmaktadır.

### Aspose.Cells Kullanarak Verileri İçe Aktarma

Aspose.Cells ile bir Excel dosyasını açtığınızda, dosyadaki tüm veriler otomatik olarak içe aktarılır. Aspose.Cells, diğer veri kaynaklarından da veri alabilir:

- [Dizi](/cells/tr/java/import-and-export-data/).
- [dizi listesi](/cells/tr/java/import-and-export-data/).
- [Sonuç kümesi](/cells/tr/java/import-and-export-data/).
- [JSON](/cells/tr/java/import-and-export-data/)

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıf koleksiyonu içerir[**Çalışma Sayfası Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) Excel dosyasındaki her çalışma sayfasına erişim sağlar. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıf bir sağlar[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) Toplamak.[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)toplama, diğer veri kaynaklarından veri almak için çok kullanışlı yöntemler sağlar. Bu makalede, bu yöntemlerin nasıl kullanılabileceği açıklanmaktadır.

#### Diziden İçe Aktarma

 Bir diziden elektronik tabloya veri aktarmak için, importArray yöntemini çağırın.[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)Toplamak. importArray yönteminin birçok aşırı yüklenmiş sürümü vardır, ancak tipik bir aşırı yükleme aşağıdaki parametreleri alır:

- **Dizi**, içeriği içe aktardığınız dizi nesnesi.
- **Satır numarası**verilerin içe aktarılacağı ilk hücrenin satır numarası.
- **sütun numarası**, verilerin içe aktarılacağı ilk hücrenin sütun numarası.
- **dikey mi**, verilerin dikey mi yoksa yatay olarak mı içe aktarılacağını belirten bir Boole değeri.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArray-ImportingFromArray.java" >}}

#### Çok Boyutlu Dizilerden İçe Aktarma

 Çok boyutlu dizilerden bir elektronik tabloya veri aktarmak için ilgili importArray aşırı yüklemesini çağırın.[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)Toplamak:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromMultiDimensionalArray-ImportingFromMultiDimensionalArray.java" >}}

#### ArrayList'ten içe aktarma

 Verileri içe aktarmak için bir*Dizi Listesi* çalışma sayfalarına[**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean) ) yöntemi[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) Toplamak. bu[**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList(java.util.ArrayList,%20int,%20int,%20boolean)) yöntemi aşağıdaki parametreleri alır:

- **Dizi Listesi** ,*Dizi Listesi*içeriği içe aktarılacak nesne.
- **Satır numarası**, içeriğin içe aktarılacağı hücre aralığının ilk hücresinin satır numarası.
- **Sütun Numarası**, verilerin içe aktarılacağı ilk hücrenin sütun numarası.
- **Dikey mi**verilerin dikey mi yoksa yatay olarak mı içe aktarılacağını belirten bir Boole değeridir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### Özel Nesnelerden birleştirilmiş alana içe aktarma

Nesne koleksiyonundan birleştirilmiş hücreler içeren bir çalışma sayfasına veri aktarmak için şunu kullanın:[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)Emlak. Excel şablonunda birleştirilmiş hücreler varsa, değerini ayarlayın.[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)özellik doğru. Geç[**ImportTableOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImportTableOptions)istediğiniz nesne listesini görüntülemek için yönteme sütunlar/özellikler listesiyle birlikte nesne. Aşağıdaki kod örneği, kullanımını gösterir[**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells)Özel Nesnelerden birleştirilmiş hücrelere veri aktarmak için özellik. Lütfen eke bakın[kaynak Excel](90112035.xlsx)dosya ve[Excel çıktısı](90112036.xlsx)referans için dosya.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### JSON'dan Verileri İçe Aktarma

 Aspose.Cells bir sağlar[**Json Yardımcı Programı**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) JSON'u işlemek için sınıf.[**Json Yardımcı Programı**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) sınıfın bir[**Verileri İçe Aktar**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions) ) JSON verilerini içe aktarma yöntemi. Aspose.Cells ayrıca bir[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions)JSON düzeninin seçeneklerini temsil eden sınıf. bu[**Verileri İçe Aktar**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData(java.lang.String,%20com.aspose.cells.Cells,%20int,%20int,%20com.aspose.cells.JsonLayoutOptions) ) yöntemi kabul eder[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) parametre olarak. bu[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) sınıf aşağıdaki özellikleri sağlar.

- [**DiziAsTablosu**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable): Dizide tablo olarak işlenip işlenmeyeceğini belirtir.
- [**NümerikOrTarihi Dönüştür**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ConvertNumericOrDate): JSON'daki dizenin sayısala mı yoksa tarihe mi dönüştürüleceğini gösteren bir değer alır veya ayarlar.
- [**Tarih formatı**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#DateFormat): Tarih değerinin biçimini alır ve ayarlar.
- [**Dizi Başlığını Yoksay**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle): Nesnenin özelliği bir dizi ise, başlığın göz ardı edilip edilmeyeceğini belirtir
- [**YoksayNull**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreNull): Boş değerin göz ardı edilip edilmeyeceğini gösterir.
- [**Nesne Başlığını Yoksay**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreObjectTitle): Nesnenin özelliği bir nesne ise, başlığın göz ardı edilip edilmeyeceğini belirtir.
- [**Sayı Biçimi**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#NumberFormat): Sayısal değerin biçimini alır ve ayarlar.
- [**BaşlıkStil**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#TitleStyle): Başlığın stilini alır ve ayarlar.

 Aşağıda verilen örnek kod,[**Json Yardımcı Programı**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) ve[**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) JSON verilerini içe aktarmak için sınıflar.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportingFromJson-1.java" >}}

## Çalışma Sayfasından Verileri Dışa Aktarma

Aspose.Cells, kullanıcılarının yalnızca harici veri kaynaklarından çalışma sayfalarına veri aktarmalarına izin vermekle kalmaz, aynı zamanda çalışma sayfası verilerini bir diziye vermelerine de izin verir.

### Aspose.Cells Kullanarak Verileri Dışa Aktarma - Verileri Diziye Aktarma

 Aspose.Cells bir sınıf sağlar,[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , bu bir Microsoft Excel dosyasını temsil eder. bu[**Çalışma kitabı**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıf bir içerir[**Çalışma Sayfası Koleksiyonu**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) Excel dosyasındaki her çalışma sayfasına erişim sağlar. Bir çalışma sayfası şununla temsil edilir:[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıf. bu[**Çalışma kağıdı**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıf bir sağlar[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) Toplamak.

 Veriler, kullanılarak kolayca bir Array nesnesine aktarılabilir.[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) sınıf'[**dışa aktarma dizisi**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int)) yöntem.

#### Kesinlikle Yazılmış Verileri İçeren Sütunlar

 Elektronik tablolar, verileri bir dizi satır ve sütun olarak depolar. Kullan[**dışa aktarma dizisi**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int) ) verileri bir çalışma sayfasından bir diziye aktarma yöntemi.[**dışa aktarma dizisi**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray(int,%20int,%20int,%20int) ) çalışma sayfası verilerini dışa aktarmak için aşağıdaki parametreleri alır.*Dizi* nesne:

- Satır numarası, verilerin dışa aktarılacağı ilk hücrenin satır numarası.
- Sütun numarası, verilerin dışa aktarılacağı ilk hücrenin sütun numarası
- Satır sayısı, dışa aktarılacak satır sayısı.
- Sütun sayısı, dışa aktarılacak sütun sayısı.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ExportingDataFromWorksheets-1.java" >}}

## **ileri konular**
- [Microsoft Veritabanı ResultSet Nesnesinden Çalışma Sayfasına Veri Aktarın](/cells/tr/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/)
- [Verileri Çalışma Sayfasına Aktarırken Formül Alanlarını Belirtin](/cells/tr/java/specify-formula-fields-while-importing-data-to-worksheet/)
