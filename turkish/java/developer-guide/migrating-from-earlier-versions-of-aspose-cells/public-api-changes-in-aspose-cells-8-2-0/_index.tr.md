---
title: Aspose.Cells 8.2.0 da Genel API Değişiklikleri
type: docs
weight: 80
url: /tr/java/public-api-changes-in-aspose-cells-8-2-0/
---

{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricileri için ilgi çekebilecek Aspose.Cells API'sindeki değişiklikleri 8.1.2'den 8.2.0'a, yalnızca yeni ve güncellenmiş genel yöntemleri değil, aynı zamanda Aspose.Cells'in arka plandaki davranışındaki değişikliklerin açıklamasını da içermektedir.

{{% /alert %}} 
## **Cells Sınıfı için MultiThreadReading Özelliği Eklendi**
Aspose.Cells for Java 8.2.0 ile ÇokluThreadOkuma özelliği, hücre değerlerini çoklu thread'lerle aynı anda daha sağlam bir mekanizma ile okumak için Cells sınıfına eklenmiştir. Boolean tipindeki özelliği çoklu-thread uygulamasında true olarak ayarlamak, her bir thread'in doğru hücre değerini alacağından emin olur.

{{% alert color="primary" %}} 

Çoklu İş Parçacıklı Ortamda Hücre Değerlerini Eşzamanlı Okuma hakkındaki detaylı makaleyi inceleyin

{{% /alert %}}
## **autoFitRows ve autoFitColumns Metodları için Overload'lar Eklendi**
AutoFitRows ve autoFitColumns için yeni aşırı yüklemeler Worksheet sınıfına eklenmiştir, geliştiricilere AutoFitterOptions sınıfının örneğini geçirerek ilgili aralıklara göre satırları ve sütunları otomatik olarak uyarlama imkanı sağlar. 

Yukarıda bahsedilen metodların imzaları aşağıdaki gibidir:

1. autoFitRows(int startRow, int endRow, AutoFitterOptions options)
1. autoFitColumns(int firstColumn, int lastColumn, AutoFitterOptions options)

{{% alert color="primary" %}} 

[Otomatik Satır ve Sütun Uyarlamak](http://aspose.com/docs/display/cellsjava/AutoFit+Rows+and+Columns) hakkındaki detaylı makaleye göz atın.

{{% /alert %}}
