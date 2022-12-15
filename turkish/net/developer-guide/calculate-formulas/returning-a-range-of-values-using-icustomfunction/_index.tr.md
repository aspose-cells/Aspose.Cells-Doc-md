---
title: ICustomFunction kullanarak bir Değer Aralığı Döndürme
type: docs
weight: 50
url: /tr/net/returning-a-range-of-values-using-icustomfunction/
---
{{% alert color="primary" %}}

 bu[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) Aspose.Cells for Java 20.8 sürümünden beri kullanımdan kaldırılmıştır. lütfen[**SoyutHesaplamaMotoru**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) sınıf. kullanımı[**SoyutHesaplamaMotoru**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) sınıfı aşağıdaki makalede açıklanmıştır.

[AbstractCalculationEngine kullanarak bir Değer Aralığı Döndürme](/cells/tr/net/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

 Aspose.Cells sağlar[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)yerleşik işlevler olarak Microsoft Excel tarafından desteklenmeyen kullanıcı tanımlı veya özel işlevleri uygulamak için kullanılan arabirim.

 Çoğunlukla uyguladığınızda[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) arayüz yöntemi, tek bir hücre değeri döndürmeniz gerekir. Ancak bazen, bir dizi değer döndürmeniz gerekir. Bu makale, değer aralığının nasıl döndürüleceğini açıklayacaktır.[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{% /alert %}}

 Aşağıdaki kod uygular[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)ve yöntemi aracılığıyla değer aralığını döndürür.

 Bir işleve sahip bir sınıf oluşturun*CalculateCustomFunction*. Bu sınıf uygular[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-CustomFunctionStaticValue.cs" >}}

Şimdi programınıza yukarıdaki işlevi kullanın

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-1.cs" >}}
