---
title: Cell Değerinin Veri Doğrulama Kurallarını Karşıladığını Doğrulayın
type: docs
weight: 90
url: /tr/java/verify-that-cell-value-satisfies-data-validation-rules/
---
{{% alert color="primary" %}}

Microsoft Excel, kullanıcıların çalışma sayfası hücrelerine veri doğrulama kuralları eklemesine izin verir. Örneğin, 10 ile 20 arasındaki sayıları kısıtlamak için bir ondalık doğrulama uygulanabilir. Belirtilen aralığın dışında herhangi bir sayı girilirse, Microsoft Excel bir hata mesajı gösterir ve kullanıcıdan doğru aralıktan bir sayı girmesini ister. Kullanıcı kopyası hücreye bir sayı, örneğin 3 yapıştırırsa, Excel doğrulama denetimini çalıştırmaz veya bir hata mesajı göstermez.

{{% /alert %}}

## Cell Değerinin Veri Doğrulama Kurallarını Karşıladığını Doğrulayın

Bazen, belirli bir değerin hücreye uygulanan veri doğrulama kurallarını karşılayıp karşılamadığını dinamik olarak doğrulamak gerekir. Bu amaçla, Aspose.Cells API'leri şunları sağlar:[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) yöntem. Bir hücredeki değer, o hücreye uygulanan veri doğrulama kuralını karşılamıyorsa,**Yanlış** , başka**Doğru**.

Aşağıdaki örnek Microsoft Excel dosyası, test etmek için aşağıdaki örnek kodla birlikte kullanılır.[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) yöntem. Anlık görüntüde görebileceğiniz gibi, hücreler**C1** sahip olmak**ondalık veri doğrulama** uygulandı ve yalnızca değerleri kabul edecek**10 ile 20 arasında** . Hücrenin değeri 10 ile 20 arasında olduğunda,[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) yöntemi geri dönecek**Doğru** , aksi takdirde geri döner**Yanlış**.

![yapılacaklar:resim_alternatif_Metin](verify-that-cell-value-satisfies-data-validation-rules_1.png)

 Aşağıdaki örnek kod,[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) yöntem çalışır. İlk önce C1'e 3 değerini girer. Bu, veri doğrulama kuralını karşılamadığından,[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) yöntem döndürür**Yanlış** . Daha sonra C1'e 15 değerini girer. Bu değer, veri doğrulama kuralını karşıladığından,[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) yöntem döndürür**Doğru** . Benzer şekilde, geri döner**Yanlış** 30 değeri için.

## Bir Cell değerinin veri doğrulama kurallarını karşılayıp karşılamadığını doğrulamak için Java kodu

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyCellValueSatisfiesDataValidationRules-VerifyCellValueSatisfiesDataValidationRules.java" >}}

## Örnek kod tarafından oluşturulan konsol çıktısı

Yukarıda gösterilen örnek Excel dosyasıyla örnek kod yürütüldüğünde oluşturulan konsol çıktısı aşağıdadır.

{{< highlight "java" >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
