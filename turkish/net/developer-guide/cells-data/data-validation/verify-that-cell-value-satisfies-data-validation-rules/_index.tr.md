---
title: Cell Değerinin Veri Doğrulama Kurallarını Karşıladığını Doğrulayın
type: docs
weight: 210
url: /tr/net/verify-that-cell-value-satisfies-data-validation-rules/
---
{{% alert color="primary" %}} 

Microsoft Excel, kullanıcıların hücrelere veri doğrulama kuralları eklemesine izin verir. Örneğin, bir ondalık doğrulama yalnızca 10 ile 20 arasındaki sayıların girilebileceğini belirtir. Bir kullanıcı farklı bir numara girerse. Microsoft Excel bir hata mesajı gösteriyor ve onlardan doğru aralıkta bir sayı girmelerini istiyor. Bir sayıyı, örneğin 3'ü kopyalayıp hücreye yapıştırırsanız, Excel bir doğrulama denetimi çalıştırmaz veya bir hata mesajı göstermez.

Bazen, bir değerin hücreye programlı olarak uygulanan veri doğrulama kurallarını karşılayıp karşılamadığını doğrulamak gerekir. Örneğin yukarıdaki durumda, giriş başarısız olmalıdır.

{{% /alert %}} 
## **giriiş**
 Aspose.Cells şunları sağlar:[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) hücre değerlerini programlı olarak doğrulama yöntemi. Bir hücredeki değer, o hücreye uygulanan veri doğrulama kuralını karşılamıyorsa,**Yanlış** , başka**Doğru**.

 Aşağıdaki örnek kod,[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) yöntem çalışır. İlk önce C1'e 3 değerini girer. Bu, veri doğrulama kuralını karşılamadığından,[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) yöntem döndürür**Yanlış** . Daha sonra C1'e 15 değerini girer. Bu değer, veri doğrulama kuralını karşıladığından,[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) yöntem döndürür**Doğru** . Benzer şekilde, geri döner**Yanlış** 30 değeri için.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}
### **Çıktı**
{{< highlight "java" >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
