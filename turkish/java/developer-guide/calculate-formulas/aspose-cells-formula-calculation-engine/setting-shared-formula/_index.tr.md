---
title: Paylaşılan Formülü Ayarlama
type: docs
weight: 10
url: /tr/java/setting-shared-formula/
---
{{% alert color="primary" %}} 

Aşağıdaki örnek çalışma sayfasına benzeyen biçimde verilerle dolu bir çalışma sayfanız olduğunu varsayalım.

**Bir sütun veya veri içeren girdi dosyası** 

![yapılacaklar:resim_alternatif_Metin](setting-shared-formula_1.png)

 B2'de ilk veri satırı için satış vergisini hesaplayacak bir işlev eklemek istiyorsunuz. vergi**9%** Satış vergisini hesaplayan formül şu şekildedir:**"=A2*0,09"**. Bu makalede, bu formülün Aspose.Cells ile nasıl uygulanacağı açıklanmaktadır.

{{% /alert %}} 

 Aspose.Cells, şunu kullanarak bir formül belirlemenizi sağlar:[Cell.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) mülkiyet, özellikle[Cell.setFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) ve[Cell.getFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula).

Sütundaki diğer hücrelere (B3, B4, B5 vb.) formül eklemek için iki seçenek vardır.

Ya ilk hücre için yaptığınızı yapın, her hücre için formülü etkili bir şekilde ayarlayın, hücre referansını buna göre güncelleyin (A3*0,09, A4*0,09, A5*0,09 vb.). Bu, her satır için hücre başvurularının güncellenmesini gerektirir. Ayrıca, Aspose.Cells'in her formülü ayrı ayrı ayrıştırmasını gerektirir; bu, büyük elektronik tablolar ve karmaşık formüller için zaman alıcı olabilir. Ayrıca fazladan kod satırları ekler, ancak döngüler bunları bir şekilde azaltabilir.

 Başka bir yaklaşım, bir**paylaşılan formül** Paylaşılan bir formül ile, verginin doğru bir şekilde hesaplanması için formüller her satırdaki hücre referansları için otomatik olarak güncellenir. bu[Cell.setSharedFormula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setSharedFormula\(java.lang.String,%20int,%20int\)) yöntemi birinci yöntemden daha etkilidir.

Aşağıdaki örnek nasıl kullanılacağını göstermektedir. Aşağıdaki ekran görüntüsü çıktı dosyasını göstermektedir.

**Çıktı dosyası: paylaşılan formül uygulandı** 

![yapılacaklar:resim_alternatif_Metin](setting-shared-formula_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingSharedFormula-SettingSharedFormula.java" >}}
