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
[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonunun [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) yöntemini çağırarak herhangi bir konuma bir satır ekleyin. [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) yöntemi, yeni satırın ekleneceği satırın endeksini ilk argüman olarak alır ve eklenecek satır sayısını ikinci argüman olarak alır.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
## **Birkaç Satır Nasıl Eklenir**
Çalışma sayfasına birden çok satır eklemek için, [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonunun [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) yöntemini çağırın. [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) yöntemi iki parametre alır:

- Satır endeksi: Yeni satırların ekleneceği satırın endeksi.
- Satır sayısı: Silinmesi gereken toplam satır sayısı.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
## **Biçimlendirme Seçenekleriyle Bir Satır Nasıl Eklenir**
Biçimlendirme seçenekleriyle bir satır eklemek için, [InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions) olarak parametre alan [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int,%20com.aspose.cells.InsertOptions\)) aşırı yüklemesini kullanın. [InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions) sınıfının [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/insertoptions#CopyFormatType) özelliğini [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType) Numaralandırmasıyla ayarlayın. [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType) Numaralandırması aşağıda listelenmiş üç üyeye sahiptir.

- [ŞUNUN AYNI](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_ABOVE): Satırı yukarıdaki satıra benzer şekilde biçimlendirir.
- [AŞAĞIDAKİYLE AYNI](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_BELOW):  Satırı alttaki satıra benzer şekilde biçimlendirir.
- [TEMİZLE](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR): Biçimlendirmeyi temizler.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
## **Bir Satır Nasıl Silinir**
Herhangi bir konumda bir satırı silmek için, [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonunun [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) yöntemini çağırın. [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) yöntemi iki parametre alır:

- Satır endeksi: Silinecek satırların endeksi.
- Satır sayısı: Silinmesi gereken toplam satır sayısı.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
## **Birden Fazla Satır Nasıl Silinir**
Çalışma sayfasından birden çok satırı silmek için, [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonunun [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) yöntemini çağırın. [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) yöntemi iki parametre alır:

- Satır endeksi: Silinecek satırların endeksi.
- Satır sayısı: Silinmesi gereken toplam satır sayısı.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
## **Bir veya Birden Fazla Sütunun Nasıl Eklenir**
Geliştiriciler, [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonunun [insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\)) yöntemini çağırarak çalışma sayfasına herhangi bir konuma bir sütun da ekleyebilir. [insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\)) yöntemi iki parametre alır:

- Sütun endeksi, sütunun ekleneceği sütunun endeksi
- Sütun sayısı, eklenmek istenen toplam sütun sayısı

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
## **Bir Sütunu Nasıl Silebilirsiniz**
Herhangi bir konumda çalışma sayfasından bir sütunu silmek için, [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) koleksiyonunun [deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\)) yöntemini çağırın. [deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\)) yöntemi aşağıdaki parametreleri alır:

- Sütun endeksi: Sütunun silineceği sütunun endeksi.
- Sütun sayısı: Silinmesi gereken toplam sütun sayısı.
- Referans Güncelleme: Başka çalışma sayfalarındaki referansları güncellemek için bir Boolean parametresi.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

