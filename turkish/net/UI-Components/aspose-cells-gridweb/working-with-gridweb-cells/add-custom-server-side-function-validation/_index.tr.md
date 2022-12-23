---
title: Özel Sunucu Tarafı İşlev Doğrulaması Ekleme
type: docs
weight: 110
url: /tr/net/add-custom-server-side-function-validation/
---
## **Olası Kullanım Senaryoları**
Bazen, sunucu tarafında veri doğrulama uygulamanız gerekebilir. Aspose.Cells.GridWeb, özel sunucu tarafı veri doğrulaması eklemenizi sağlar. Hücre aralığını veya alanını belirtmeniz gerekir. Özel sunucu tarafı doğrulaması ile geri aramalar için istemci tarafı doğrulama işlevleri de ayarlayabilirsiniz.
## **Özel Sunucu Tarafı İşlev Doğrulaması Ekleme**
 uygulayan sunucu doğrulama sınıfını ayarlamanız gerekir.**GridCustomServerValidation** arayüz üzerinden**GridValidation.ServerValidation** bağlanmak. İstemci tarafı doğrulama işlevini de ayarlamanız gerekir (istemci tarafında JavaScript ile yazılmalıdır), bu işlev, geri arama sırasında istemci tarafındaki verileri doğrulamak için zorunludur. Hata mesajı dizesini şu şekilde ayarlayabilirsiniz:**GridValidation.ErrorMessage** ve aracılığıyla başlık**GridValidation.ErrorTitle**ihtiyaçlarınız için özellikler. Lütfen aşağıdaki örnek kodu çalıştırdıktan sonra belirli bir senaryoda nasıl çalıştığını (adım adım) gösteren bir dizi ekran görüntüsüne bakın. Örnekte, B2:C3 hücrelerindeki verileri güncelleyemezsiniz. Sayfadaki bu hücreleri düzenlemeye çalıştığınızda, size bazı hata mesajları sorulacak ve önceki değer geri yüklenecektir. Belirli olaylar için hücre bilgilerini/ayrıntılarını yazdırmak için Konsol penceresini (tarayıcınızda) açabilirsiniz.

![yapılacaklar:resim_alternatif_metin](add-custom-server-side-function-validation_1.png)

![yapılacaklar:resim_alternatif_metin](add-custom-server-side-function-validation_2.png)

![yapılacaklar:resim_alternatif_metin](add-custom-server-side-function-validation_3.png)

![yapılacaklar:resim_alternatif_metin](add-custom-server-side-function-validation_4.png)

![yapılacaklar:resim_alternatif_metin](add-custom-server-side-function-validation_5.png)
## **Basit kod**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Cells-AddCustomServerSideFunctionValidation.aspx.cs" >}}
