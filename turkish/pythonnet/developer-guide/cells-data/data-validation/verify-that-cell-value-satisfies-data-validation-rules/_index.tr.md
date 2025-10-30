---
title: Hücre Değerinin Veri Doğrulama Kurallarına Uygun Olup Olmadığını Doğrulayın
type: docs
weight: 210
url: /tr/python-net/verify-that-cell-value-satisfies-data-validation-rules/
description: Aspose.Cells for Python via .NET API si aracılığıyla Hücre Değerinin Veri Doğrulama Kurallarını Karşılayıp Karşılamadığını Doğrulamanın Nasıl Yapılacağını Öğrenin.
keywords: Python Excel Kütüphanesi, Python Hücre Doğrulama Değerini Al, Python Hücre Doğrulama Değeri Al, Python Bir değerin hücreye uygulanan veri doğrulama kurallarını karşılayıp karşılamadığını doğrulayın.
---

{{% alert color="primary" %}} 

Microsoft Excel, kullanıcılara hücrelere veri doğrulama kuralları eklemelerine izin verir. Örneğin, ondalık doğrulama sadece 10 ile 20 arasındaki sayıların girilebileceğini belirtir. Bir kullanıcı farklı bir sayı girerse, Microsoft Excel bir hata mesajı gösterir ve doğru aralıkta bir sayı girmelerini isteyerek uyarır. Eğer 3 gibi bir sayıyı yapıştırırsanız, Excel doğrulama kontrolü yapmaz veya bir hata mesajı göstermez.

Bazen, bir değerin hücreye uygulanan veri doğrulama kurallarını programlı olarak karşılayıp karşılamadığını doğrulamak gereklidir. Yukarıdaki durumda, örneğin, giriş başarısız olmalıdır.

{{% /alert %}} 
## **Giriş**
Aspose.Cells for Python via .NET, hücre değerlerini programlı olarak doğrulamak için [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) yöntemi sağlar. Bir hücredeki değer, o hücreye uygulanan veri doğrulama kuralını karşılamıyorsa **False** değerini, aksi takdirde **True** değerini döndürür.

Aşağıdaki örnek kod, [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) yönteminin nasıl çalıştığını gösterir. İlk olarak, C1'e 3 değeri girer. Bu, veri doğrulama kuralını karşılamadığı için [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) yöntemi **False** değerini döndürür. Daha sonra, C1'e 15 değeri girer. Bu değer veri doğrulama kuralını karşıladığı için [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) yöntemi **True** değerini döndürür. Benzer şekilde, 30 değeri için **False** değerini döndürür.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-DataValidationRules-1.py" >}}

### **Çıktı**
{{< highlight java >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
