---
title: Paylaşılan Formülü Ayarlama
type: docs
weight: 10
url: /tr/java/setting-shared-formula/
---

{{% alert color="primary" %}} 

Aşağıdaki örnek elektronik tabloya benzer biçimde veriyle dolu bir çalışma sayfasını varsayalım.

**Tek sütun veya veri içeren giriş dosyası** 

![todo:image_alt_text](setting-shared-formula_1.png)

Bir fonksiyon eklemek istiyorsunuz ve bu fonksiyon, verinin ilk satırı için satış vergisini hesaplayacak. Vergi **%9**. Satış vergisini hesaplayan formül şudur: **"=A2*0.09"**. Bu makale, bu formülü Aspose.Cells ile nasıl uygulayacağınızı açıklar.

{{% /alert %}} 

Aspose.Cells, [Cell.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) özelliğini, özellikle [Cell.setFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) ve [Cell.getFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) yöntemlerini kullanarak formül belirtmenizi sağlar.

Sütunun diğer hücrelerine formül eklemek için iki seçenek bulunmaktadır.

İlk hücre için yaptığınız işlemi diğer hücreler için de yapabilir ve hücre referansını buna göre güncelleyebilirsiniz (`A3*0.09`, `A4*0.09`, `A5*0.09` ve benzeri). Bu, her satır için hücre referanslarının güncellenmesini gerektirir. Ayrıca Aspose.Cells'in her formülü ayrı ayrı analiz etmesini gerektirir ve büyük elektronik tablolar ve karmaşık formüller için zaman alıcı olabilir. Ayrıca, döngüler ek bir dizi kod ekler, her ne kadar döngüler bunu biraz azaltabilir.

Başka bir yaklaşım ise **paylaşılan formül** kullanmaktır. Paylaşılan formüller ile, formüller her satırdaki hücre referansları için otomatik olarak güncellenir, böylece vergi doğru hesaplanır. [Cell.setSharedFormula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setSharedFormula-java.lang.String-int-int-) yöntemi ilk yöntemden daha verimlidir.

Aşağıdaki örnek bunu nasıl kullanacağınızı gösterir. Aşağıdaki ekran görüntüsü çıkış dosyasını gösterir.

**Çıkış dosyası: paylaşılan formül uygulandı** 

![todo:image_alt_text](setting-shared-formula_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingSharedFormula-SettingSharedFormula.java" >}}
{{< app/cells/assistant language="java" >}}
