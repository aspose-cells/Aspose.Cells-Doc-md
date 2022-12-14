---
title: Genel API Aspose.Cells 8.2.0'daki değişiklikler
type: docs
weight: 70
url: /tr/net/public-api-changes-in-aspose-cells-8-2-0/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürüm 8.1.2'den 8.2.0'a modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranışlardaki değişikliklerin açıklamasını da içerir.

{{% /alert %}} 
## **Cells Sınıfı İçin MultiThreadReading Özelliği Eklendi**
Aspose.Cells for .NET 8.2.0 ile birden çok iş parçacığına sahip hücre değerlerini aynı anda okumak için daha sağlam bir mekanizma sağlamak amacıyla Cells sınıfına MultiThreadReading özelliği eklenmiştir. Çoklu iş parçacıklı uygulamada Boole tipi özelliğinin true olarak ayarlanması, her iş parçacığının doğru hücre değerini almasını sağlar.

{{% alert color="primary" %}} 

 Lütfen adresindeki ayrıntılı makaleyi kontrol edin.[Multi-Threaded Ortamında Cells Değerlerini Aynı Anda Okuyun](http://aspose.com/docs/display/cellsnet/Reading+Cells+Values+in+Multiple+Threads+Simultaneously) daha fazla bilgi için.

{{% /alert %}}
## **AutoFitRows & AutoFitColumns Yöntemleri için Aşırı Yüklemeler Eklendi**
 Worksheet sınıfına AutoFitRows ve AutoFitColumns için yeni aşırı yüklemeler eklenerek, geliştiricilerin AutoFitterOptions sınıfının bir örneğini geçirirken ilgili aralıklarına göre satırları ve sütunları otomatik olarak sığdırmalarına olanak sağlanmıştır.

Söz konusu yöntemlerin imzaları aşağıdaki gibidir:

1. AutoFitRows(int startRow, int endRow, AutoFitterOptions seçenekleri)
1. AutoFitColumns(int firstColumn, int lastColumn, AutoFitterOptions seçenekleri)

{{% alert color="primary" %}} 

 Lütfen adresindeki ayrıntılı makaleyi kontrol edin.[Satırları ve Sütunları Otomatik Sığdır](http://aspose.com/docs/display/cellsnet/AutoFit+Rows+and+Columns).

{{% /alert %}}
