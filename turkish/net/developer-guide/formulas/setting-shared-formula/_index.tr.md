---
title: Paylaşılan Formülü Ayarlama
type: docs
weight: 10
url: /tr/net/setting-shared-formula/
---
{{% alert color="primary" %}}

Çalışma sayfasına bazı hesaplamalar yapacak bir işlev eklemek istiyorsanız. Bu makale, Aspose.Cells kullanarak bu görevin nasıl gerçekleştirileceğini açıklamaktadır.

{{% /alert %}}

## Aspose.Cells kullanarak Paylaşılan Formülü ayarlama

Aşağıdaki örnek çalışma sayfasına benzeyen biçimde verilerle dolu bir çalışma sayfanız olduğunu varsayalım.

|**Bir sütun veya veri içeren girdi dosyası**|
|:- |
|![yapılacaklar:resim_alternatif_metin](setting-shared-formula_1.png)|

 B2'de ilk veri satırı için satış vergisini hesaplayacak bir işlev eklemek istiyorsunuz. vergi**9%** Satış vergisini hesaplayan formül şu şekildedir:**"=A2*0,09"**. Bu makalede, bu formülün Aspose.Cells ile nasıl uygulanacağı açıklanmaktadır.

 Aspose.Cells, şunu kullanarak bir formül belirlemenizi sağlar:[**Cell.Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula)Emlak. Sütundaki diğer hücrelere (B3, B4, B5 vb.) formül eklemek için iki seçenek vardır.

Ya ilk hücre için yaptığınızı yapın, her hücre için formülü etkili bir şekilde ayarlayın, hücre referansını buna göre güncelleyin (A3*0,09, A4*0,09, A5*0,09 vb.). Bu, her satır için hücre başvurularının güncellenmesini gerektirir. Ayrıca, Aspose.Cells'in her formülü ayrı ayrı ayrıştırmasını gerektirir; bu, büyük elektronik tablolar ve karmaşık formüller için zaman alıcı olabilir. Ayrıca fazladan kod satırları ekler, ancak döngüler bunları bir şekilde azaltabilir.

 Başka bir yaklaşım, bir**paylaşılan formül** Paylaşılan bir formül ile, verginin doğru bir şekilde hesaplanması için formüller her satırdaki hücre referansları için otomatik olarak güncellenir. bu[**Cell.SetSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setsharedformula/index)yöntem birinci yöntemden daha etkilidir.

Aşağıdaki örnek nasıl kullanılacağını göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingSharedFormula-1.cs" >}}
