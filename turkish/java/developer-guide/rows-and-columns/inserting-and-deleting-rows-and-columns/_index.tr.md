---
title: Satırları ve Sütunları Eklemek ve Silmek
type: docs
weight: 60
url: /tr/java/inserting-and-deleting-rows-and-columns/
description: Aspose.Cells for Java API si aracılığıyla Satır ve Sütun Ekleme ve Silmeyi Öğrenin.
keywords: Satır ve Sütunları Java da Nasıl Ekleyebilir ve Silebilirsiniz, Java da Satır ve Sütun Ekleme, Java da Satır ve Sütun Silme, Java da Satır veya Sütunları Ekleme, Java da Satır ve Sütunları Silme via Java.
---

## **Giriş**
Sıfırdan yeni bir çalışma sayfası oluştururken veya mevcut bir çalışma sayfası üzerinde çalışırken, daha fazla veri eklemek için ekstra satırlar veya sütunlar eklememiz gerekebilir. Tersine, çalışma sayfasının belirli pozisyonlarından satırları veya sütunları silebiliriz.

Bu gereksinimleri karşılamak için Aspose.Cells, aşağıda tartışılan çok basit bir sınıf ve yöntem seti sağlar.
## **Satır/Sütun Yönetimi**
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfını sağlar. [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sınıfı, bir Excel dosyasındaki her bir çalışma sayfasına erişime izin veren bir [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) içerir. Bir çalışma sayfası, [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı tarafından temsil edilir. [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) sınıfı, çalışma sayfasındaki tüm hücreleri temsil eden bir [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) koleksiyonu sağlar.

[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) koleksiyonu, bir çalışma sayfasındaki satırları ve sütunları yönetmek için birkaç yöntem sağlar. Bunlardan bazıları aşağıda açıklanmıştır.

{{% alert color="primary" %}} 

Satırlar veya sütunlar eklenirse, çalışma sayfasındaki içerik aşağı veya sağa kayar, ancak satırlar veya sütunlar kaldırılırsa, içerik yukarı veya sola kayar.

{{% /alert %}} 
## **Bir Satır Nasıl Eklenir**
Yeni bir satır eklemek için [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) yöntemini çağırın. Bu yöntem, yeni satırın ekleneceği satırın indeksini ilk argüman olarak ve eklenecek satırların sayısını ikinci argüman olarak alır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
## **Birkaç Satır Nasıl Eklenir**
Çoklu satır eklemek için [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) yöntemini çağırın. Bu yöntem iki parametre alır:

- Satır endeksi: Yeni satırların ekleneceği satırın endeksi.
- Satır sayısı: Silinmesi gereken toplam satır sayısı.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
## **Biçimlendirme Seçenekleriyle Bir Satır Nasıl Eklenir**
Biçimlendirme seçenekleriyle birlikte satır eklemek için, [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-com.aspose.cells.InsertOptions-) aşırı yüklemesini kullanın ve parametre olarak [InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions) verin. [InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions) sınıfının [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/insertoptions#CopyFormatType) özelliğini [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType) Enum’ı ile ayarlayın. [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType) Enum’ında aşağıda listelenen üç üye vardır.

- [SAME_AS_ABOVE](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME-AS-ABOVE): Satırı yukarıdaki satırla aynı biçimde biçimlendirir.
- [SAME_AS_BELOW](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME-AS-BELOW):  Satırı aşağıdaki satırla aynı biçimde biçimlendirir.
- [TEMİZLE](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR): Biçimlendirmeyi temizler.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
## **Bir Satır Nasıl Silinir**
Herhangi bir konumda satırı silmek için, [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) yöntemini çağırın. Bu yöntem iki parametre alır:

- Satır endeksi: Silinecek satırların endeksi.
- Satır sayısı: Silinmesi gereken toplam satır sayısı.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
## **Birden Fazla Satır Nasıl Silinir**
Bir çalışma sayfasından çoklu satır silmek için [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) yöntemini çağırın. Bu yöntem iki parametre alır:

- Satır endeksi: Silinecek satırların endeksi.
- Satır sayısı: Silinmesi gereken toplam satır sayısı.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
## **Bir veya Birden Fazla Sütunun Nasıl Eklenir**
Geliştiriciler, herhangi bir konuma sütun eklemek için [insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns-int-int-) yöntemini çağırabilir. Bu yöntem iki parametre alır:

- Sütun endeksi, sütunun ekleneceği sütunun endeksi
- Sütun sayısı, eklenmek istenen toplam sütun sayısı

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
## **Bir Sütunu Nasıl Silebilirsiniz**
Herhangi bir konumda çalışma sayfasından sütunu silmek için, [deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns-int-int-boolean-) yöntemini çağırın. Bu yöntem aşağıdaki parametreleri alır:

- Sütun endeksi: Sütunun silineceği sütunun endeksi.
- Sütun sayısı: Silinmesi gereken toplam sütun sayısı.
- Referans Güncelleme: Başka çalışma sayfalarındaki referansları güncellemek için bir Boolean parametresi.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

{{< app/cells/assistant language="java" >}}
