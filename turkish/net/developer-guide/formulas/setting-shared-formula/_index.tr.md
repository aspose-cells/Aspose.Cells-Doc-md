---
title: Paylaşılan Formülü Ayarlama
type: docs
weight: 10
url: /tr/net/setting-shared-formula/
---

{{% alert color="primary" %}}

Çalışma tablosuna hesaplamalar yapacak bir fonksiyon eklemek istiyorsanız. Bu makale, bu görevi Aspose.Cells kullanarak nasıl gerçekleştireceğinizi açıklar.

{{% /alert %}}

## Aspose.Cells kullanarak Paylaşılan Formül Ayarlama

Aşağıdaki örnek elektronik tabloya benzer biçimde veriyle dolu bir çalışma sayfasını varsayalım.

|**Tek sütunlu veya veri içeren giriş dosyası**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Bir fonksiyon eklemek istiyorsunuz ve bu fonksiyon, verinin ilk satırı için satış vergisini hesaplayacak. Vergi **%9**. Satış vergisini hesaplayan formül şudur: **"=A2*0.09"**. Bu makale, bu formülü Aspose.Cells ile nasıl uygulayacağınızı açıklar.

Aspose.Cells, [**Cell.Formula**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula) özelliğini kullanarak bir formül belirtmenizi sağlar. Sütunun diğer hücrelerine (B3, B4, B5 ve benzeri) formül eklemek için iki seçenek bulunmaktadır.

İlk hücre için yapılanı yaparak her hücre için formülü ayarlayın, hücre referansını güncelleyerek (A3*0.09, A4*0.09, A5*0.09 ve benzeri). Her satırın hücre referanslarının güncellenmesini gerektirir. Ayrıca, Aspose.Cells'in her formülü ayrı ayrı ayrıştırmasını gerektirir, bu da büyük elektronik tablolar ve karmaşık formüller için zaman alıcı olabilir. Bu ayrıca biraz kodları azaltsa da döngüler biraz azaltabilir.

Başka bir yaklaşım, **paylaşılan bir formül** kullanmaktır. Paylaşılan formülle, formüller her satırın hücre referansları için otomatik olarak güncellenir, böylece vergi uygun şekilde hesaplanır. [**Cell.SetSharedFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setsharedformula/index) yöntemi, birinci yöntemden daha verimlidir.

Aşağıdaki örnek, bunu nasıl kullanacağınızı göstermektedir.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-SettingSharedFormula-1.cs" >}}
