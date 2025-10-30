---
title: Paylaşılan Formülü Ayarlama
type: docs
weight: 10
url: /tr/python-net/setting-shared-formula/
---

{{% alert color="primary" %}}

Çalışma Sayfasına bazı hesaplamalar yapacak bir fonksiyon eklemek istiyorsanız. Bu makale, Aspose.Cells for Python via .NET kullanarak bu görevi nasıl başaracağınızı açıklamaktadır.

{{% /alert %}}

## Aspose.Cells for Python via .NET ile Paylaşılan Formülü Ayarlama

Aşağıdaki örnek elektronik tabloya benzer biçimde veriyle dolu bir çalışma sayfasını varsayalım.

|**Tek sütunlu veya veri içeren giriş dosyası**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

B2 hücresine ilk veri satırının satış vergisini hesaplayacak bir fonksiyon eklemek istiyorsanız. Vergi **%9**. Satış vergisini hesaplayan formül: **"=A2*0.09"**. Bu makale, Aspose.Cells for Python via .NET kullanarak bu formülü nasıl uygulayacağınızı açıklamaktadır.

Aspose.Cells for Python via .NET, [**Cell.formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/formula) özelliği kullanılarak formül belirlemenize olanak tanır. Sütundaki diğer hücrelere (B3, B4, B5 ve devamı) formüller ekmek için iki seçenek vardır.

İlk hücreye yaptığınız gibi yapabilir, her hücre için formülü ayarlayabilir ve hücre referansını uygun şekilde güncelleyebilirsiniz (A3*0.09, A4*0.09, A5*0.09 ve devamı). Bu, her satırdaki hücre referanslarının güncellenmesini gerektirir. Ayrıca, Aspose.Cells for Python via .NET bu formülleri tek tek ayrıştırmak zorunda kalacağından, büyük tablolar ve karmaşık formüller için zaman alıcı olabilir. Ayrıca, döngüler biraz azaltabilir, fakat ek kod satırları eklenir.

Başka bir yaklaşım, **paylaşılan bir formül** kullanmaktır. Paylaşılan formülle, formüller her satırın hücre referansları için otomatik olarak güncellenir, böylece vergi uygun şekilde hesaplanır. [**Cell.set_shared_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_shared_formula) yöntemi, birinci yöntemden daha verimlidir.

Aşağıdaki örnek, bunu nasıl kullanacağınızı göstermektedir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingSharedFormula-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
