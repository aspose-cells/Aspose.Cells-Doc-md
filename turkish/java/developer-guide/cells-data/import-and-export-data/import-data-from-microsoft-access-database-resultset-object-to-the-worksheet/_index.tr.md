---
title: Microsoft Access Veritabanı ResultSet Nesnesinden Çalışma Sayfasına Veri Aktarma
type: docs
weight: 200
url: /tr/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/
---

## **Olası Kullanım Senaryoları**
Aspose.Cells, herhangi bir veritabanından oluşturulabilen ResultSet nesnesinden çalışma sayfalarına veri aktarabilir. Ancak, bu makale özellikle Microsoft Access Veritabanından bir ResultSet nesnesi oluşturur. Kod tüm veritabanı türleri için aynı olduğu için bunu genel olarak kullanabilirsiniz.
## **UCanAccess - Microsoft Access Veritabanına Bağlanmak için Gerekli**
Lütfen [UCanAccess'i](http://ucanaccess.sourceforge.net/site.html) indirin. Aşağıdaki JAR dosyalarını içerir. Tümünü classpath'e ekleyin.

- ucanaccess-4.0.1.jar
- commons-lang-2.6.jar
- commons-logging-1.1.1.jar
- hsqldb.jar
- jackcess-2.1.6.jar

Daha fazla yardım için lütfen bu Stack Overflow bağlantısını ziyaret edin.

- [JAR dosyalarını projenize el ile ekleyin](https://stackoverflow.com/questions/21955256/manipulating-an-access-database-from-java-without-odbc/21955257#21955257)
## **Örnek Microsoft Access 2016 Veritabanı Dosyası, Örnek Kod İçinde Kullanıldı**
Aşağıdaki örnek Microsoft Access 2016 Veritabanı Dosyası, örnek kod içinde kullanıldı. Herhangi bir veritabanı dosyasını kullanabilir veya kendi dosyanızı oluşturabilirsiniz.

- [Students.accdb](48496712.accdb)

Aşağıdaki ekran görüntüsü, Microsoft Access 2016'da açıldığında veritabanı dosyasını gösterir.

![todo:image_alt_text](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_1.png)
## **Microsoft Access Veritabanı ResultSet Object'ten Veri İçeri Aktarma**
Aşağıdaki örnek kod, Microsoft Access veritabanından SQL sorgusu çalıştırır ve ResultSet nesnesi oluşturur. Daha sonra, ResultSet'ten alınan verileri [Worksheet.getCells().importResultSet()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importResultSet-java.sql.ResultSet-int-int-boolean-) yöntemiyle çalışma sayfasına aktarır. İlk olarak satır ve sütun indekslerini kullanır, ardından hücre adıyla verileri içeri aktarır. Son olarak, çalışma kitabını bir [Çıkış Excel Dosyası](48496713.xlsx) olarak kaydeder. Ekran görüntüsü, örnek kodun çıktı Excel dosyası üzerindeki etkisini gösterir.

![todo:image_alt_text](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_2.png)
## **Örnek Kod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportDataFromMicrosoftAccessDatabaseResultSetObjectToWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}
