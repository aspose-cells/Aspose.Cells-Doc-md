---
title: Satır ve Sütun Ekleme ve Silme
type: docs
weight: 60
url: /tr/java/inserting-and-deleting-rows-and-columns/
---
## **giriiş**
Sıfırdan yeni bir çalışma sayfası oluştururken veya mevcut bir çalışma sayfası üzerinde çalışırken, daha fazla veriyi barındırmak için fazladan satır veya sütun eklememiz gerekebilir. Tersine, çalışma sayfasında belirtilen konumlardaki satırları veya sütunları da silmemiz gerekebilir.

Bu gereklilikleri yerine getirmek için Aspose.Cells, aşağıda tartışılan çok basit bir sınıflar ve yöntemler seti sağlar.
## **Satırları/Sütunları Yönetme**
 Aspose.Cells bir sağlar[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Microsoft Excel dosyasını temsil eden sınıf. bu[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıf bir içerir[Çalışma Sayfası Koleksiyonu](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) Bu, bir Excel dosyasındaki her çalışma sayfasına erişim sağlar. Bir çalışma sayfası şununla temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıf. bu[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıf bir sağlar[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)çalışma sayfasındaki tüm hücreleri temsil eden koleksiyon.

 bu[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)koleksiyon, bir çalışma sayfasındaki satırları ve sütunları yönetmek için çeşitli yöntemler sağlar. Bunlardan bazıları aşağıda tartışılmaktadır.

{{% alert color="primary" %}} 

Satır veya sütun eklendiğinde çalışma sayfasındaki içerik aşağı veya sağa kaydırılır, ancak satır veya sütunlar kaldırılırsa içerik yukarı veya sola kaydırılır.

{{% /alert %}} 
## **Satır Ekleme**
 öğesini çağırarak herhangi bir konuma bir satır ekleyin.[EkleSatırlar](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\) ) yöntemi[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Toplamak. bu[EkleSatırlar](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\))yöntemi ilk argüman olarak yeni satırın ekleneceği satırın indeksini, ikinci argüman olarak eklenecek satır sayısını alır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
## **Birden Çok Satır Ekleme**
 Çalışma sayfasına birden çok satır eklemek için[EkleSatırlar](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\) ) yöntemi[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Toplamak. bu[EkleSatırlar](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) yöntemi iki parametre alır:

- Satır dizini: Yeni satırların ekleneceği satırın dizini.
- Satır sayısı: eklenmesi gereken toplam satır sayısı.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
## **Biçimlendirmeyle Satır Ekleme**
Biçimlendirme seçenekleriyle bir satır eklemek için[EkleSatırlar](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int,%20com.aspose.cells.InsertOptions\)) aşırı yükleme[Ekleme Seçenekleri](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)parametre olarak. Yı kur[Kopya BiçimiTürü](https://reference.aspose.com/cells/java/com.aspose.cells/insertoptions#CopyFormatType)mülkiyet[Ekleme Seçenekleri](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)ile sınıf[Kopya BiçimiTürü](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)Numaralandırma. bu[Kopya BiçimiTürü](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)Numaralandırmanın aşağıda listelendiği gibi üç üyesi vardır.

- [AYNI_OLARAK_ÜSTÜNDE](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_ABOVE)Satırı yukarıdaki satırla aynı şekilde biçimlendirir.
- [AYNI_OLARAK_AŞAĞIDA](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_BELOW): Satırı aşağıdaki satırla aynı şekilde biçimlendirir.
- [AÇIK](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR): Biçimlendirmeyi temizler.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
## **Satır Silme**
 Herhangi bir konumdaki bir satırı silmek için[satırları sil](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\) ) yöntemi[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Toplamak. bu[satırları sil](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) yöntemi iki parametre alır:

- Satır dizini: Satırların silineceği satırın dizini.
- Satır sayısı: silinmesi gereken toplam satır sayısı.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
## **Birden Çok Satırı Silme**
Bir çalışma sayfasından birden çok satırı silmek için[satırları sil](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\) ) yöntemi[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Toplamak. bu[satırları sil](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) yöntemi iki parametre alır:

- Satır dizini: Satırların silineceği satırın dizini.
- Satır sayısı: silinmesi gereken toplam satır sayısı.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
## **Bir veya Birden Çok Sütun Ekleme**
 Geliştiriciler ayrıca, çalışma sayfasına herhangi bir konumda şunu çağırarak bir sütun ekleyebilir:[EkleSütunlar](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\) ) yöntemi[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)Toplamak. bu[EkleSütunlar](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\)) yöntemi iki parametre alır:

- Sütun dizini, sütunun ekleneceği sütunun dizini
- Sütun sayısı, eklenmesi gereken toplam sütun sayısı

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
## **Sütun Silme**
 Herhangi bir konumdaki çalışma sayfasından bir sütunu silmek için[sütunları sil](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\) ) yöntemi[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Toplamak. bu[sütunları sil](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\)) yöntemi aşağıdaki parametreleri alır:

- Sütun dizini: Sütunun silineceği sütunun dizini.
- Sütun sayısı: silinmesi gereken toplam sütun sayısı.
- Referansı Güncelle: Diğer çalışma sayfalarındaki referansların güncellenip güncellenmeyeceğini gösteren Boolean parametresi.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

