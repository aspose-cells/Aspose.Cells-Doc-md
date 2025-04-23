---
title: Veri İçe ve Dışa Aktarma
type: docs
weight: 130
url: /tr/java/import-and-export-data/
---

{{% alert color="primary" %}}

Bu makale, geliştiricilerin Aspose.Cells aracılığıyla erişebildiği bazı veri içe ve dışa aktarma tekniklerini tartışmaktadır.

{{% /alert %}}

## Çalışsayfasına Veri İçe Aktar

Veri, olduğu gibi dünyayı temsil eder. Verinin anlamını çıkarmak ve dünyayı anlamak için veriyi analiz ederiz. Veri bilgiye dönüşür.

Analiz yapmanın birçok yolu vardır: veriyi elektronik tablolara yerleştirip farklı yollarla manipüle etme, yaygın bir yöntemdir. Aspose.Cells ile, harici kaynaklardan veri almayı ve analiz için hazırlamayı kolayca yapabilirsiniz.

Bu makale, geliştiricilerin Aspose.Cells üzerinden erişebilecekleri bazı veri aktarma tekniklerini tartışmaktadır.

### Aspose.Cells Kullanarak Veri İçe Aktarma

Aspose.Cells ile bir Excel dosyası açtığınızda, dosyadaki tüm veri otomatik olarak içe aktarılır. Aspose.Cells ayrıca diğer veri kaynaklarından veri içe aktarabilir:

- [Dizi](/cells/tr/java/import-and-export-data/).
- [Dizi listesi](/cells/tr/java/import-and-export-data/).
- [Sonuç kümesi](/cells/tr/java/import-and-export-data/).
- [JSON](/cells/tr/java/import-and-export-data/)

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışsayfaya erişimi sağlayan [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) koleksiyonunu içerir. Bir çalışsayfa, [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı, bir [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) koleksiyonu sağlar. [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) koleksiyonu, diğer veri kaynaklarından veri içe aktarmak için çok kullanışlı yöntemler sağlar. Bu makale, bu yöntemlerin nasıl kullanılabileceğini açıklar.

#### Diziden İçe Aktarma

Bir diziden elektronik tabloya veri aktarmak için, [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) koleksiyonunun importArray metodunu çağırın. importArray metodunun birçok aşırı yüklenmiş sürümü bulunmaktadır, ancak tipik bir aşırı yükleme aşağıdaki parametreleri alır:

- **Dizi**, içeriği aktardığınız dizi nesnesi.
- **Satır numarası**, verilerin aktarılacağı ilk hücrenin satır numarası.
- **Sütun numarası**, verilerin aktarılacağı ilk hücrenin sütun numarası.
- **Dikey mi**, verinin dikey olarak mı yoksa yatay olarak mı aktarılacağını belirten bir Boolean değeri.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArray-ImportingFromArray.java" >}}

#### Çok Boyutlu Dizilerden İçe Aktarma

Çok boyutlu dizilerden elektronik tabloya veri aktarmak için, [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) koleksiyonunun ilgili importArray aşırı yükleme metodunu çağırın:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromMultiDimensionalArray-ImportingFromMultiDimensionalArray.java" >}}

#### Bir ArrayList'ten İçe Aktarma

Verileri bir *ArrayList* koleksiyonundan çalışma sayfalarına aktarmak için, [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) koleksiyonunun [**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList-java.util.ArrayList-int-int-boolean-) metodunu çağırın. [**ImportArrayList**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importArrayList-java.util.ArrayList-int-int-boolean-) metodu aşağıdaki parametreleri alır:

- **ArrayList**, içeriği aktarılacak *ArrayList* nesnesi.
- **Satır Numarası**, içeriğin aktarılacağı hücre aralığının ilk hücresinin satır numarası.
- **Sütun Numarası**, verilerin aktarılacağı ilk hücrenin sütun numarası.
- **Dikey Mi**, verilerin dikey veya yatay olarak mı aktarılacağını belirten bir Boolean değeri.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### Özel Nesnelerden Birleştirilmiş Alanlara Aktarma

Bir nesne koleksiyonundan birleştirilmiş hücrelere sahip bir çalışma sayfasına veri aktarmak için [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells) özelliğini kullanın. Eğer Excel şablonunda birleştirilmiş hücreler varsa, [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells) özelliğinin değerini true olarak ayarlayın. Dilediğiniz nesne listesini görüntülemek için  [**ImportTableOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImportTableOptions) nesnesini ve sütun/özellik listesini metodlara geçirin. Aşağıdaki kod örneği, Özel Nesnelerden birleştirilmiş hücrelere veri aktarma işleminin [**ImportTableOptions.CheckMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#CheckMergedCells) özelliğini kullanımını göstermektedir. Referans için lütfen ekli [kaynak Excel](90112035.xlsx) dosyasını ve [çıktı Excel](90112036.xlsx) dosyasını inceleyin.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ImportingFromArrayList-ImportingFromArrayList.java" >}}

#### JSON'dan Veri Aktarma

Aspose.Cells, JSON işleme için bir [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) sınıfı sağlar. [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) sınıfı, JSON verilerini içe aktarmak için bir [**ImportData**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData-java.lang.String-com.aspose.cells.Cells-int-int-com.aspose.cells.JsonLayoutOptions-) metodu içerir. Aspose.Cells ayrıca, JSON düzeni seçeneklerini temsil eden bir [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) sınıfı da sağlar. [**ImportData**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonutility#importData-java.lang.String-com.aspose.cells.Cells-int-int-com.aspose.cells.JsonLayoutOptions-) metodu, [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) olarak bir parametre kabul eder. [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) sınıfı aşağıdaki özellikleri sağlar.

- [**ArrayAsTable**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ArrayAsTable): Array içindeki öğenin tablo olarak işlenip işlenmeyeceğini belirtir.
- [**ConvertNumericOrDate**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#ConvertNumericOrDate): JSON'daki dizeyi sayısal veya tarihi veriye dönüştürüp dönüştürmeyeceğini belirler.
- [**DateFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#DateFormat): Tarih değerinin biçimlendirilmesini alır ve ayarlar.
- [**IgnoreArrayTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreArrayTitle): Nesnenin özelliği bir dizi ise başlığı görmezden gelip gelmeyeceğini belirtir.
- [**IgnoreNull**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreNull): null değerinin dikkate alınıp alınmayacağını belirler.
- [**IgnoreObjectTitle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#IgnoreObjectTitle): Nesnenin özelliği bir nesne ise başlığı görmezden gelip gelmeyeceğini belirtir.
- [**NumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#NumberFormat): Sayısal değerin biçimlendirmesini alır ve ayarlar.
- [**TitleStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/jsonlayoutoptions#TitleStyle): Başlık stilini alır ve ayarlar.

Aşağıda verilen örnek kod, JSON verilerini içe aktarmak için [**JsonUtility**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonUtility) ve [**JsonLayoutOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonLayoutOptions) sınıflarının kullanımını göstermektedir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportingFromJson-1.java" >}}

## Çalışma Sayfasından Veri Aktarma

Aspose.Cells, kullanıcılarının elektronik tablolara dış veri kaynaklarından veri içe aktarmasının yanı sıra çalışma sayfasındaki veriyi bir diziye aktarmasına da olanak tanır.

### Aspose.Cells Kullanarak Veri Aktarma - Veriyi Diziye Aktarma

Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir sınıf olan [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sağlar. [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı bir [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) koleksiyonu sağlar.

Veri, [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) sınıfının [**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray-int-int-int-int-) metodu kullanılarak kolayca bir Dizi nesnesine aktarılabilir.

#### Güçlü Türde Veri İçeren Sütunlar

Hesap tabloları verileri bir dizi satır ve sütun olarak saklar. Verileri bir çalışma sayfasından bir diziye aktarmak için [**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray-int-int-int-int-) metodunu kullanın. *Array* nesnesi olarak çalışma sayfası verilerini dışa aktarmak için [**exportArray**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#exportArray-int-int-int-int-) aşağıdaki parametreleri alır:

- Satır numarası, verilerin aktarılacağı ilk hücrenin satır numarası.
- Sütun numarası, verilerin aktarılacağı ilk hücrenin sütun numarası.
- Satır sayısı, dışa aktarılacak satır sayısı.
- Sütun sayısı, dışa aktarılacak sütun sayısı.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ExportingDataFromWorksheets-1.java" >}}

## **Gelişmiş Konular**
- [Microsoft Access Veritabanı ResultSet Nesnesinden Veri Alma](/cells/tr/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/)
- [Çalışma Sayfasına Veri İçeri Aktarırken Formül Alanlarını Belirt](/cells/tr/java/specify-formula-fields-while-importing-data-to-worksheet/)
{{< app/cells/assistant language="java" >}}
