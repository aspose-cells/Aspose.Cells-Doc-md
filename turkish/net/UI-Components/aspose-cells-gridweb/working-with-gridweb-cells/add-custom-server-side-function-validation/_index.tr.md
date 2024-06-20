---
title: Özel Sunucu Tarafı Fonksiyon Doğrulaması Ekleyin
type: docs
weight: 110
url: /tr/net/aspose-cells-gridweb/add-custom-server-side-function-validation/
keywords: GrindWeb, sunucu tarafı doğrulaması ekleyin.
description: Bu makale, GridWeb deki sunucu tarafı doğrulama ile nasıl çalışılacağını tanıtır.
---

## **Olası Kullanım Senaryoları**
Bazen sunucu tarafında veri doğrulaması uygulamanız gerekebilir. Aspose.Cells.GridWeb, özel sunucu tarafı veri doğrulaması eklemenize olanak tanır. Hücre aralığını veya alanını belirtmeniz gerekmektedir. Ayrıca, özel sunucu tarafı doğrulaması için geri arama için istemci tarafı doğrulama işlevlerini ayarlayabilirsiniz.
## **Özel Sunucu Tarafı İşlev Doğrulaması Ekleme**
 **GridValidation.ServerValidation** özniteliği aracılığıyla **GridCustomServerValidation** arabirimini uygulayan sunucu doğrulama sınıfını ayarlamanız gerekmektedir. Ayrıca, istemci tarafı doğrulama işlevini (bu işlev istemci tarafında JavaScript dilinde yazılmalıdır), bu işlev geri aramada veriyi doğrulamak için zorunludur. İhtiyaçlarınız için **GridValidation.ErrorMessage** ve **GridValidation.ErrorTitle** özelliklerini kullanarak hata ileti dizesini ve başlığını ayarlamanız gerekmektedir. Aşağıdaki örnek kodu çalıştırdıktan sonra verilen senaryoda nasıl adım adım çalıştığını gösteren bir dizi ekran görüntüsünü inceleyebilirsiniz. Örnekte, B2:C3 hücrelerinde verileri güncelleyemezsiniz. Sayfada bu hücreleri düzenlemeye çalıştığınızda, bazı hata iletileri alacaksınız ve önceki değer geri yüklenecektir. Belirli olaylar için hücrenin ayrıntılarını/kimlik bilgilerini yazdırmak için (tarayıcınızda) Konsol penceresini açabilirsiniz. 

![todo:image_alt_text](add-custom-server-side-function-validation_1.png)

![todo:image_alt_text](add-custom-server-side-function-validation_2.png)

![todo:image_alt_text](add-custom-server-side-function-validation_3.png)

![todo:image_alt_text](add-custom-server-side-function-validation_4.png)

![todo:image_alt_text](add-custom-server-side-function-validation_5.png)
## **Örnek Kod**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Cells-AddCustomServerSideFunctionValidation.aspx.cs" >}}
