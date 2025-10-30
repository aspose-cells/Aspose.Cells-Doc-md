---
title: Golang kullanarak C++ ile Hücre Değeri Veri Doğrulama Kurallarını doğrula
linktitle: Hücre Değerinin Veri Doğrulama Kurallarına Uygun Olup Olmadığını Doğrulayın
type: docs
weight: 210
url: /tr/go-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Aspose.Cells for C++ API’sini kullanarak Hücre Değerinin Veri Doğrulama Kurallarını Sağlayıp Sağlamadığını nasıl teyit edeceğinizi öğrenin.
keywords: Hücre Doğrulama Değeri Al, Hücre Doğrulama Değeri Al, Bir değerin hücreye uygulanan veri doğrulama kurallarını karşılayıp karşılamadığını doğrulayın
---

{{% alert color="primary" %}} 

Microsoft Excel, kullanıcılara hücrelere veri doğrulama kuralları ekleme imkanı tanır. Örneğin, ondalık doğrulama, yalnızca 10 ile 20 arasında sayıların girilmesine izin verir. Kullanıcı farklı bir sayı girerse, Microsoft Excel hata mesajı gösterir ve doğru aralıkta sayı girmesini ister. Bir sayıyı kopyalayıp yapıştırırsanız, diyelim ki 3, Excel doğrulama kontrolü yapmaz veya hata mesajı göstermez.

Bazen, bir değerin hücreye uygulanan veri doğrulama kurallarını programlı olarak karşılayıp karşılamadığını doğrulamak gereklidir. Yukarıdaki durumda, örneğin, giriş başarısız olmalıdır.

{{% /alert %}} 

## **Giriş**
Aspose.Cells, hücre değerlerini programatik olarak doğrulamak için [Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/) yöntemini sağlar. Bir hücredeki değer, o hücreye uygulanan veri doğrulama kuralını karşılamıyorsa, **False** döner, diğer durumda **True** döner.

Aşağıdaki örnek kod, [Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/) yönteminin nasıl çalıştığını gösterir. İlk olarak, C1'e 3 değeri girilir. Bu, veri doğrulama kuralını karşılamadığı için, [Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/) yöntemi **False** döner. Daha sonra, C1'e 15 değeri girilir. Bu değer veri doğrulama kuralını karşıladığı için, [Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/) yöntemi **True** döner. Benzer şekilde, 30 değeri için **False** döner.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-VerifyThatCellValueSatisfiesDataValidationRules.go" >}}
### **Çıktı**
{{< highlight java >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
