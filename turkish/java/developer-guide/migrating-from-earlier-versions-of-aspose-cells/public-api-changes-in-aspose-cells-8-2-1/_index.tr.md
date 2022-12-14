---
title: Genel API Aspose.Cells 8.2.1'deki değişiklikler
type: docs
weight: 90
url: /tr/java/public-api-changes-in-aspose-cells-8-2-1/
---
{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API sürümünde 8.2.0'dan 8.2.1'e modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranışlardaki değişikliklerin açıklamasını da içerir.

{{% /alert %}} 
## **Cell Sınıfı için getValidation() yöntemi eklendi**
Veri doğrulama, elektronik tablo tasarımcılarının, kullanıcıların belirli bir hücreye geçersiz değerler girmesini engellemek için kullandıkları özelliklerden biridir. Aspose.Cells for Java 8.2.1 ile API, bir hücrede veri doğrulama uygulanıp uygulanmadığını belirleyen basit bir mekanizmayı ortaya çıkardı. Uygulanan herhangi bir doğrulamayı almak için Cell sınıfının getValidation yöntemini kullanın. Doğrulama yoksa, yöntem null döndürür. Benzer şekilde, ValidationCollection sınıfının getValidationInCell yöntemini, satır ve sütun dizinlerini sağlayarak herhangi bir hücreye uygulanan doğrulamayı elde etmek için kullanabilirsiniz.

{{% alert color="primary" %}} 

 Lütfen adresindeki ayrıntılı makaleyi kontrol edin.[Cell'de Doğrulama Uygulayın](https://docs.aspose.com/cells/java/get-validation-applied-on-a-cell/) daha fazla bilgi için.

{{% /alert %}}
## **Cell sınıfı için getValidationValue() yöntemi eklendi**
Doğrulamanın uygulanıp uygulanmadığını belirlemeye ek olarak, belirli bir değerin belirli bir hücre için veri doğrulama kurallarını karşılayıp karşılamadığını da doğrulayabilirsiniz. Bu özellik, hücreye girilen değerin anında veri doğrulama kurallarını karşılayıp karşılamadığını doğrulamak istediğiniz senaryolarda kullanışlıdır. Aspose.Cells API, Cell sınıfı için getValidationValue yöntemini kullanıma sundu. Bir hücreye girilen değer veri doğrulama kurallarını karşılamıyorsa Cell sınıfı için getValidationValue yöntemi false döndürür.

{{% alert color="primary" %}} 

 Lütfen adresindeki ayrıntılı makaleyi kontrol edin.[Cell Değerinin Veri Doğrulama Kurallarını Karşıladığını Doğrulayın](/cells/tr/java/verify-that-cell-value-satisfies-data-validation-rules/).

{{% /alert %}}
## **WorkbookRender sınıfı için aşırı yük toPrinter(PrinterSettings printerSettings) yöntemi eklendi**
Çalışma kitabını PrinterSettings aracılığıyla Yazıcıya işlemek için aşırı yüklenmiş yöntemi kullanabilirsiniz.
