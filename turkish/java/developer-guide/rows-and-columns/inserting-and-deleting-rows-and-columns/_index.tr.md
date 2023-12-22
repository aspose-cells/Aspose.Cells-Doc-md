---
title: Satır ve Sütun Ekleme ve Silme
type: docs
weight: 60
url: /tr/java/inserting-and-deleting-rows-and-columns/
description: Aspose.Cells for Java API'leri aracılığıyla Satırları ve Sütunları nasıl ekleyeceğinizi ve sileceğinizi öğrenin.
keywords: How to Insert and Delete Rows and Columns in Java, Insert Rows and Columns using Java, Java Delete Rows and Columns, Insert Rows or Columns with Java, Delete Rows or Columns via Java.
---
##  **giriiş**
İster sıfırdan yeni bir çalışma sayfası oluşturun ister mevcut bir çalışma sayfası üzerinde çalışın, daha fazla veriyi barındırmak için fazladan satır veya sütun eklememiz gerekebilir. Bunun tersine, çalışma sayfasında belirtilen konumlardaki satırları veya sütunları da silmemiz gerekebilir.

Bu gereksinimleri karşılamak için Aspose.Cells, aşağıda tartışılan çok basit bir sınıf ve yöntem seti sağlar.
##  **Satırları/Sütunları Yönetme**
 Aspose.Cells şunları sağlar:[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) Microsoft Excel dosyasını temsil eden sınıf.[Çalışma kitabı](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıf bir içerir[Çalışma Sayfası Koleksiyonu](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) Bu, bir Excel dosyasındaki her çalışma sayfasına erişime izin verir. Bir çalışma sayfası şu şekilde temsil edilir:[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıf.[Çalışma kağıdı](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıf sağlar[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)çalışma sayfasındaki tüm hücreleri temsil eden koleksiyon.

[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)koleksiyon, bir çalışma sayfasındaki satırları ve sütunları yönetmek için çeşitli yöntemler sağlar. Bunlardan bazıları aşağıda tartışılmaktadır.

{{% alert color="primary" %}} 

Satır veya sütunlar eklendiğinde çalışma sayfasındaki içerik aşağı veya sağa kaydırılır, ancak satırlar veya sütunlar kaldırıldığında içerik yukarı veya sola kaydırılır.

{{% /alert %}} 
##  **Satır Nasıl Eklenir**
 arayarak herhangi bir konuma satır ekleyin.[satırları ekle](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\) ) yöntemi[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Toplamak.[satırları ekle](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) yöntemi, ilk argüman olarak yeni satırın ekleneceği satırın indeksini, ikinci argüman olarak eklenecek satır sayısını alır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
##  **Birden Çok Satır Nasıl Eklenir**
 Çalışma sayfasına birden çok satır eklemek için[satırları ekle](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\) ) yöntemi[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Toplamak.[satırları ekle](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) yöntemi iki parametre alır:

- Satır dizini: Yeni satırların ekleneceği satırın dizini.
- Satır Sayısı: Eklenmesi gereken toplam satır sayısı.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
##  **Biçimlendirmeyle Satır Nasıl Eklenir**
Biçimlendirme seçeneklerini içeren bir satır eklemek için[satırları ekle](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int,%20com.aspose.cells.InsertOptions\)aşırı yük[EkleSeçenekler](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)parametre olarak. Yı kur[CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/insertoptions#CopyFormatType)mülkiyet[EkleSeçenekler](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)ile sınıf[CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)Numaralandırma.[CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)Numaralandırmanın aşağıda listelendiği gibi üç üyesi vardır.

- [SAME_AS_ABOVE](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_ABOVE): Satırı yukarıdaki satırla aynı şekilde biçimlendirir.
- [SAME_AS_BELOW](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_BELOW): Satırı aşağıdaki satırla aynı şekilde biçimlendirir.
- [CLEAR](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR): Biçimlendirmeyi temizler.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
##  **Satır Nasıl Silinir?**
 Herhangi bir konumdaki bir satırı silmek için[Satırları sil](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\) ) yöntemi[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Toplamak.[Satırları sil](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) yöntemi iki parametre alır:

- Satır dizini: Satırların silineceği satırın dizini.
- Satır sayısı: Silinmesi gereken toplam satır sayısı.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
##  **Birden Çok Satır Nasıl Silinir?**
 Bir çalışma sayfasından birden çok satırı silmek için,[Satırları sil](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\) ) yöntemi[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Toplamak.[Satırları sil](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) yöntemi iki parametre alır:

- Satır dizini: Satırların silineceği satırın dizini.
- Satır sayısı: Silinmesi gereken toplam satır sayısı.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
##  **Bir veya Birden Çok Sütun Nasıl Eklenir?**
 Geliştiriciler ayrıca çalışma sayfasının herhangi bir yerindeki sütunu çağırarak da sütun ekleyebilirler.[sütunları ekle](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\) ) yöntemi[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)Toplamak.[sütunları ekle](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\)) yöntemi iki parametre alır:

- Sütun dizini, sütunun ekleneceği sütunun dizini
- Sütun sayısı, eklenmesi gereken toplam sütun sayısı

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
##  **Sütun Nasıl Silinir?**
 Çalışma sayfasında herhangi bir yerden bir sütunu silmek için[Sütunları sil](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\) ) yöntemi[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Toplamak.[Sütunları sil](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\)) yöntemi aşağıdaki parametreleri alır:

- Sütun dizini: Sütunun silineceği sütunun dizini.
- Sütun sayısı: Silinmesi gereken toplam sütun sayısı.
- Referansı Güncelle: Diğer çalışma sayfalarındaki referansların güncellenip güncellenmeyeceğini belirten Boolean parametresi.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

