---
title: Hücre Değerinin Veri Doğrulama Kurallarına Uygun Olup Olmadığını Doğrulayın
type: docs
weight: 210
url: /tr/nodejs-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Hücre değeriyle Veri Doğrulama Kurallarını nasıl doğrulayacağınızı Aspose.Cells for Node.js via C++ API’sini kullanarak öğrenin.
keywords: Node.js kullanarak Hücre Doğrulama Değerini alın, C++ kullanarak Hücre Doğrulama Değerini alın, Bir değerin hücreye uygulanan veri doğrulama kurallarını karşılayıp karşılamadığını doğrulayın, Node.js (C++ aracılığıyla)
---

{{% alert color="primary" %}} 

Microsoft Excel, kullanıcılara hücrelere veri doğrulama kuralları ekleme imkanı tanır. Örneğin, ondalık doğrulama, yalnızca 10 ile 20 arasında sayıların girilmesine izin verir. Kullanıcı farklı bir sayı girerse, Microsoft Excel hata mesajı gösterir ve doğru aralıkta sayı girmesini ister. Bir sayıyı kopyalayıp yapıştırırsanız, diyelim ki 3, Excel doğrulama kontrolü yapmaz veya hata mesajı göstermez.

Bazen, bir değerin hücreye uygulanan veri doğrulama kurallarını programlı olarak karşılayıp karşılamadığını doğrulamak gereklidir. Yukarıdaki durumda, örneğin, giriş başarısız olmalıdır.

{{% /alert %}} 
## **Giriş**
Aspose.Cells for Node.js via C++, hücre değerlerini programatik olarak doğrulamak için {0} metodunu sağlar. Bir hücredeki değer, o hücreye uygulanan veri doğrulama kuralını karşılamıyorsa, **false** döner, aksi takdirde **true** döner.

Aşağıdaki örnek kod, [Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--) metodunun nasıl çalıştığını gösterir. Önce, C1 hücresine 3 değeri girilir. Bu, veri doğrulama kurallarını karşılamadığı için, [Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--) metodu **false** döner. Ardından, C1'e 15 değeri girilir. Bu değer veri doğrulama kurallarını karşıladığı için, method **true** döner. Aynı şekilde, 30 değeri için **false** döner.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-VerifyValidationCellValues.js" >}}


### **Çıktı**
{{< highlight javascript >}}

 Is 3 a Valid Value for this Cell: false

Is 15 a Valid Value for this Cell: true

Is 30 a Valid Value for this Cell: false

{{< /highlight >}}
