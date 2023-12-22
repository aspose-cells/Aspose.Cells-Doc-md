---
title: Cell Değerinin Veri Doğrulama Kurallarını Karşıladığını Doğrulayın
type: docs
weight: 210
url: /tr/net/verify-that-cell-value-satisfies-data-validation-rules/
description: Cell Değerinin Veri Doğrulama Kurallarını Karşıladığını Aspose.Cells for .NET API aracılığıyla nasıl doğrulayacağınızı öğrenin.
keywords: Get Cell Validation Value, Obtain Cell Validation Value, Verify whether a value satisfies the data validation rules applied to the cell
---
{{% alert color="primary" %}} 

Microsoft Excel, kullanıcıların hücrelere veri doğrulama kuralları eklemesine olanak tanır. Örneğin, ondalık doğrulama yalnızca 10 ile 20 arasındaki sayıların girilebileceğini belirtir. Kullanıcı farklı bir numara girerse. Microsoft Excel bir hata mesajı gösteriyor ve doğru aralığa bir sayı girmelerini istiyor. Bir sayıyı (örneğin 3) kopyalayıp hücreye yapıştırırsanız, Excel bir doğrulama kontrolü çalıştırmaz veya bir hata mesajı göstermez.

Bazen bir değerin hücreye programlı olarak uygulanan veri doğrulama kurallarını karşılayıp karşılamadığını doğrulamak gerekir. Örneğin yukarıdaki durumda giriş başarısız olmalıdır.

{{% /alert %}} 
##  **giriiş**
 Aspose.Cells şunları sağlar[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue)Hücre değerlerini programlı olarak doğrulama yöntemi. Bir hücredeki değer, o hücreye uygulanan veri doğrulama kuralını karşılamıyorsa *Yanlış**, aksi halde *Doğru** değerini döndürür.

 Aşağıdaki örnek kod,[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) yöntem işe yarıyor. Öncelikle C1’e 3 değerini girer. Bu, veri doğrulama kuralını karşılamadığından,[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) yöntem geri dönüşleri**YANLIŞ**. Daha sonra C1’e 15 değerini girer. Bu değer veri doğrulama kuralını karşıladığından, [Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) yöntemi **True** değerini döndürür. Benzer şekilde **False değerini döndürür** 30 değeri için.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}
###  **Çıktı**
{{< highlight "java" >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
