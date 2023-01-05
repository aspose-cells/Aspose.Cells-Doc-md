---
title: Genel API Aspose.Cells 8.2.0'daki değişiklikler
type: docs
weight: 80
url: /tr/java/public-api-changes-in-aspose-cells-8-2-0/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürüm 8.1.2'den 8.2.0'a modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranışlardaki değişikliklerin açıklamasını da içerir.

{{% /alert %}} 
## **Cells Sınıfı İçin MultiThreadReading Özelliği Eklendi**
Aspose.Cells for Java 8.2.0 ile birden çok iş parçacığına sahip hücre değerlerini aynı anda okumak için daha sağlam bir mekanizma sağlamak amacıyla Cells sınıfına MultiThreadReading özelliği eklenmiştir. Çoklu iş parçacıklı uygulamada Boole tipi özelliğinin true olarak ayarlanması, her iş parçacığının doğru hücre değerini almasını sağlar.

{{% alert color="primary" %}} 

 Lütfen adresindeki ayrıntılı makaleyi kontrol edin.[Multi-Threaded Ortamında Cells Değerlerini Aynı Anda Okuyun](/cells/tr/java/reading-cell-values-in-multiple-threads-simultaneously/) daha fazla bilgi için.

{{% /alert %}}
## **autoFitRows & autoFitColumns Yöntemleri için Aşırı Yüklemeler eklendi**
 Worksheet sınıfına autoFitRows ve autoFitColumns için yeni aşırı yüklemeler eklenerek, geliştiricilerin AutoFitterOptions sınıfının bir örneğini geçirirken ilgili aralıklarına göre satırları ve sütunları otomatik olarak sığdırmalarına olanak sağlanmıştır.

Söz konusu yöntemlerin imzaları aşağıdaki gibidir:

1. autoFitRows(int startRow, int endRow, AutoFitterOptions seçenekleri)
1. autoFitColumns(int firstColumn, int lastColumn, AutoFitterOptions seçenekleri)

{{% alert color="primary" %}} 

 Lütfen adresindeki ayrıntılı makaleyi kontrol edin.[Satırları ve Sütunları Otomatik Sığdır](http://aspose.com/docs/display/cellsjava/AutoFit+Rows+and+Columns).

{{% /alert %}}
