---
title: Aspose.Cells 8.2.1 da Genel API Değişiklikleri
type: docs
weight: 80
url: /tr/net/public-api-changes-in-aspose-cells-8-2-1/
---

{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricileri için ilgi çekebilecek Aspose.Cells API'sindeki değişiklikleri 8.2.0'den 8.2.1'e, yalnızca yeni ve güncellenmiş genel yöntemleri değil, aynı zamanda Aspose.Cells'in arka plandaki davranışındaki değişikliklerin açıklamasını da içermektedir.

{{% /alert %}} 
## **Hücre Sınıfı İçin GetValidation() Yöntemi Eklendi**
Veri doğrulama, elektronik tablo tasarımcılarının belirli bir hücreye geçersiz değerlerin girilmesini engellemek için kullandığı özelliklerden biridir. Aspose.Cells for .NET 8.2.1 ile, API, hücre üzerinde uygulanan veri doğrulamasını tanımlayan basit bir mekanizma açığa çıkarmıştır. Bir hücrede herhangi bir uygulanan doğrulamanın olup olmadığını tespit etmek için Hücre sınıfının GetValidation yöntemini kullanın. Doğrulama yoksa, yöntem null değer döndürür. Benzer şekilde, satır ve sütun dizinlerini sağlayarak ValidationCollection sınıfının GetValidationInCell yöntemini kullanarak, herhangi bir hücreye uygulanan doğrulamayı alabilirsiniz.

{{% alert color="primary" %}} 

Lütfen daha fazla bilgi için [Bir Hücre Üzerine Uygulanan Doğrulamayı Almak](/cells/tr/net/get-validation-applied-on-a-cell/) detaylı makalesini kontrol edin.

{{% /alert %}}
## **Hücre Sınıfı İçin GetValidationValue() Yöntemi Eklendi**
Uygulanan doğrulamanın olup olmadığını belirlemenin yanı sıra, belirli bir hücre için verilen değerin veri doğrulama kurallarını karşılayıp karşılamadığını da doğrulayabilirsiniz. Bu özellik, hücreye girilen değerin, veri doğrulama kurallarını karşılayıp karşılamadığını doğrulamak istediğiniz senaryolarda yararlıdır. Aspose.Cells API, Hücre sınıfı için GetValidationValue yöntemini açığa çıkarmıştır. Bir hücreye girilen değer, veri doğrulama kurallarını sağlamıyorsa, Hücre sınıfı için GetValidationValue yöntemi false değer döndürür.

{{% alert color="primary" %}} 

Lütfen daha fazla bilgi için [Hücre Değerinin Veri Doğrulama Kurallarını Karşıladığını Doğrulama](/cells/tr/net/verify-that-cell-value-satisfies-data-validation-rules/) detaylı makalesi kontrol edin.

{{% /alert %}}
## **WorkbookRender sınıfı için PrinterSettings ile ToPrinter(PrinterSettings printerSettings) yöntemi aşırı yüklemesi eklendi**
WorkbookRender sınıfı için aşırı yüklenmiş yöntemi kullanarak çalışma sayfasını Yazıcı üzerine oluşturabilirsiniz.
{{< app/cells/assistant language="csharp" >}}
