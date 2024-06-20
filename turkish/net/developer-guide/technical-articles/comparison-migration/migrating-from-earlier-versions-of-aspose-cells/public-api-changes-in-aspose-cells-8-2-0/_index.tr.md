---
title: Aspose.Cells 8.2.0 da Genel API Değişiklikleri
type: docs
weight: 70
url: /tr/net/public-api-changes-in-aspose-cells-8-2-0/
---

{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricileri için ilgi çekebilecek Aspose.Cells API'sindeki değişiklikleri 8.1.2'den 8.2.0'a, yalnızca yeni ve güncellenmiş genel yöntemleri değil, aynı zamanda Aspose.Cells'in arka plandaki davranışındaki değişikliklerin açıklamasını da içermektedir.

{{% /alert %}} 
## **Cells Sınıfı için MultiThreadReading Özelliği Eklendi**
Aspose.Cells for .NET 8.2.0 ile, hücrelerin değerlerini birden çok thread ile eşzamanlı olarak okumak için daha güçlü bir mekanizma sağlamak adına MultiThreadReading özelliği hücreler sınıfına eklenmiştir. Boolean türünde özelliği çoklu iş parçacıklı uygulamada true olarak ayarlamak, her bir iş parçacığının doğru hücre değerini alacağını sağlar.

{{% alert color="primary" %}} 

Lütfen daha fazla bilgi için [Eşzamanlı Olarak Birden Çok İş Parçacığında Hücre Değerlerini Okuma](http://aspose.com/docs/display/cellsnet/Reading+Cells+Values+in+Multiple+Threads+Simultaneously) detaylı makalesini kontrol edin.

{{% /alert %}}
## **AutoFitRows ve AutoFitColumns Yöntemleri İçin Aşırı Yükleme Eklendi**
AutoFitRows ve AutoFitColumns için yeni aşırı yüklemeler, geliştiricilere AutoFitterOptions sınıfının bir örneğini ileterek ilgili aralıklara dayalı olarak satırları ve sütunları otomatik olarak ayarlamalarını sağlar. 

Yukarıda bahsedilen metodların imzaları aşağıdaki gibidir:

1. AutoFitRows(int startRow, int endRow, AutoFitterOptions options)
1. AutoFitColumns(int firstColumn, int lastColumn, AutoFitterOptions options)

{{% alert color="primary" %}} 

Lütfen [Otomatik Olarak Satırları ve Sütunları Ayarlama](http://aspose.com/docs/display/cellsnet/AutoFit+Rows+and+Columns) hakkında detaylı makaleyi kontrol edin

{{% /alert %}}
