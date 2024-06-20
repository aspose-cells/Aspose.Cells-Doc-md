---
title: Aspose.Cells 8.2.1 da Genel API Değişiklikleri
type: docs
weight: 90
url: /tr/java/public-api-changes-in-aspose-cells-8-2-1/
---

{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricileri için ilgi çekebilecek Aspose.Cells API'sindeki değişiklikleri 8.2.0'den 8.2.1'e, yalnızca yeni ve güncellenmiş genel yöntemleri değil, aynı zamanda Aspose.Cells'in arka plandaki davranışındaki değişikliklerin açıklamasını da içermektedir.

{{% /alert %}} 
## **Cell Sınıfı için getValidation() Metodu Eklendi**
Veri doğrulama, belirli bir hücreye geçersiz değerlerin eklenmesini önlemek için elektronik tablo tasarımcılarının kullandığı özelliklerden biridir. Aspose.Cells for Java 8.2.1 ile API, bir hücreye uygulanan veri doğrulamasını belirleyen basit bir mekanizmayı ortaya çıkarmıştır. Herhangi bir uygulama olmadığında yöntem null döner. Benzer şekilde, satır ve sütun indislerini vererek herhangi bir hücreye uygulanan doğrulamayı almak için ValidationCollection sınıfının getValidationInCell yöntemini kullanabilirsiniz.

{{% alert color="primary" %}} 

Daha fazla bilgi için [Hücreye Uygulanan Doğrulamayı Alın](https://docs.aspose.com/cells/java/get-validation-applied-on-a-cell/) üzerinde detaylı makaleyi kontrol edin.

{{% /alert %}}
## **Hücre sınıfı için getValidationValue() yöntemi eklendi**
Uygulanan doğrulamanın belirlenmesine ek olarak, belirli bir hücre için veri doğrulama kurallarını karşılayıp karşılamadığını da doğrulayabilirsiniz. Bu özellik, hücreye girilen değerin doğrulama kurallarını anında karşılayıp karşılamadığını doğrulamak istediğiniz senaryolarda kullanışlıdır. Aspose.Cells API, Cell sınıfı için getValidationValue yöntemini açığa çıkardı. Bir hücreye girilen değer, doğrulama kurallarını karşılamıyorsa, Cell sınıfı için getValidationValue yöntemi false değerini döndürür.

{{% alert color="primary" %}} 

[Hücre Değerinin Veri Doğrulama Kurallarını Karşıladığını Doğrula](/cells/tr/java/verify-that-cell-value-satisfies-data-validation-rules/) üzerinde detaylı makaleyi kontrol edin.

{{% /alert %}}
## **WorkbookRender sınıfı için PrinterSettings printerSettings aşırı yüklenmiş yöntemi eklendi**
WorkbookRender sınıfı için aşırı yüklenmiş yöntemi kullanarak çalışma sayfasını Yazıcı üzerine oluşturabilirsiniz.
