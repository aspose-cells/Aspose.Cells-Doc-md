---
title: Hücre Değerinin Veri Doğrulama Kurallarına Uygun Olup Olmadığını Doğrulayın
type: docs
weight: 210
url: /tr/net/verify-that-cell-value-satisfies-data-validation-rules/
description: Aspose.Cells for .NET API si aracılığıyla Hücre Değeri Doğrulamasının Doğrulandığını Onaylamanın nasıl öğrenileceği.
keywords: Hücre Doğrulama Değeri Al, Hücre Doğrulama Değeri Al, Bir değerin hücreye uygulanan veri doğrulama kurallarını karşılayıp karşılamadığını doğrulayın
---

{{% alert color="primary" %}} 

Microsoft Excel, kullanıcılara hücrelere veri doğrulama kuralları eklemelerine izin verir. Örneğin, ondalık doğrulama sadece 10 ile 20 arasındaki sayıların girilebileceğini belirtir. Bir kullanıcı farklı bir sayı girerse, Microsoft Excel bir hata mesajı gösterir ve doğru aralıkta bir sayı girmelerini isteyerek uyarır. Eğer 3 gibi bir sayıyı yapıştırırsanız, Excel doğrulama kontrolü yapmaz veya bir hata mesajı göstermez.

Bazen, bir değerin hücreye uygulanan veri doğrulama kurallarını programlı olarak karşılayıp karşılamadığını doğrulamak gereklidir. Yukarıdaki durumda, örneğin, giriş başarısız olmalıdır.

{{% /alert %}} 
## **Giriş**
Aspose.Cells, hücre değerlerini programlı olarak doğrulamak için [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) metodunu sağlar. Bir hücredeki değer, o hücreye uygulanan veri doğrulama kuralını karşılamıyorsa **False**, aksi takdirde **True** döndürür.

Aşağıdaki örnek kod, [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) metodunun nasıl çalıştığını gösterir. İlk olarak, C1 hücresine 3 değerini girer. Bu, veri doğrulama kuralını karşılamadığı için [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) metodu **False** döndürür. Daha sonra, C1 hücresine 15 değerini girer. Bu değer, veri doğrulama kuralını karşıladığı için [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) metodu **True** döndürür. Benzer şekilde, 30 değeri için **False** döndürür.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}
### **Çıktı**
{{< highlight java >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
