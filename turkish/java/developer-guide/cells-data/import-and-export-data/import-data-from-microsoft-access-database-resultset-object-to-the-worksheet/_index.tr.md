---
title: Microsoft Veritabanı ResultSet Nesnesinden Çalışma Sayfasına Veri Aktarın
type: docs
weight: 200
url: /tr/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/
---
## **Olası Kullanım Senaryoları**
Aspose.Cells, herhangi bir veritabanından oluşturulabilen ResultSet nesnesinden çalışma sayfalarına veri aktarabilir. Ancak, bu makale özellikle Microsoft Access Veritabanından bir ResultSet nesnesi oluşturur. Kod tüm veritabanı türleri için aynı olduğu için genel olarak kullanabilirsiniz.
## **UCanAccess - Microsoft Erişim Veritabanına Bağlanmak için Gerekli**
 Lütfen indir[UCanAccess](http://ucanaccess.sourceforge.net/site.html). Aşağıdaki JAR dosyalarını içerir. Hepsini sınıf yoluna ekleyin.

- ucanaccess-4.0.1.jar
- commons-lang-2.6.jar
- commons-log-1.1.1.jar
- hsqldb.jar
- jackcess-2.1.6.jar

Daha fazla yardım için lütfen bu Yığın Taşması bağlantısını ziyaret edin.

- [JAR'ları projenize manuel olarak ekleme](https://stackoverflow.com/questions/21955256/manipulating-an-access-database-from-java-without-odbc/21955257#21955257)
## **Örnek Kod içinde kullanılan Örnek Microsoft Access 2016 Veritabanı Dosyası**
Örnek kodun içinde aşağıdaki örnek Microsoft Access 2016 Veritabanı Dosyası kullanılmıştır. Herhangi bir veritabanı dosyasını kullanabilir veya kendinizinkini oluşturabilirsiniz.

- [Öğrenciler.accdb](48496712.accdb)

Aşağıdaki ekran görüntüsü, Microsoft Access 2016'da açıldığında veritabanı dosyasını gösterir.

![yapılacaklar:resim_alternatif_Metin](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_1.png)
## **Microsoft Veritabanı ResultSet Nesnesinden Çalışma Sayfasına Veri Aktarın.**
 Aşağıdaki örnek kod, Microsoft Access Veritabanından SQL sorgusu yürütür ve bir ResultSet nesnesi oluşturur. Ardından ResultSet nesnesinden verileri kullanarak çalışma sayfasına aktarır.[Worksheet.getCells().importResultSet()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importResultSet\(java.sql.ResultSet,%20int,%20int,%20boolean\)) yöntem. İlk seferde satır ve sütun indekslerini kullanır ve ardından verileri çalışma sayfasına almak için hücre adını kullanır. Son olarak, çalışma kitabını bir dosya olarak kaydeder.[Çıktı Excel Dosyası](48496713.xlsx). Ekran görüntüsü, bir referans için örnek kodun çıktı Excel dosyası üzerindeki etkisini gösterir.

![yapılacaklar:resim_alternatif_Metin](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_2.png)
## **Basit kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportDataFromMicrosoftAccessDatabaseResultSetObjectToWorksheet.java" >}}
