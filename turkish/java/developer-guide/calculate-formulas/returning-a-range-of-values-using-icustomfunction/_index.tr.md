---
title: ICustomFunction kullanarak bir Değer Aralığı Döndürme
type: docs
weight: 270
url: /tr/java/returning-a-range-of-values-using-icustomfunction/
---
{{% alert color="primary" %}}

 bu[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) Aspose.Cells for Java 20.8 sürümünden beri kullanımdan kaldırılmıştır. lütfen[**SoyutHesaplamaMotoru**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) sınıf. kullanımı[**SoyutHesaplamaMotoru**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) sınıfı aşağıdaki makalede açıklanmıştır.

[AbstractCalculationEngine kullanarak bir Değer Aralığı Döndürme](/cells/tr/java/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

 Aspose.Cells sağlar[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)yerleşik işlevler olarak Microsoft Excel tarafından desteklenmeyen kullanıcı tanımlı veya özel işlevleri uygulamak için kullanılan arabirim.

 Çoğunlukla uyguladığınızda[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) arayüz yöntemi, tek bir hücre değeri döndürmeniz gerekir. Ancak bazen, bir dizi değer döndürmeniz gerekir. Bu makale, değer aralığının nasıl döndürüleceğini açıklayacaktır.[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{% /alert %}}

## **ICustomFunction kullanarak bir Değer Aralığı Döndürme**

 Aşağıdaki kod uygular[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) ve yöntemi aracılığıyla değer aralığını döndürür. lütfen kontrol ediniz[çıktı excel dosyası](5472922.xlsx) ve[pdf](5472925.pdf) referansınız için kod ile oluşturulmuştur.

Bir işleve sahip bir sınıf oluşturun*CalculateCustomFunction*. Bu sınıf uygular[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

Şimdi programınıza yukarıdaki işlevi kullanın.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReturningRangeOfValues-ReturningRangeOfValues.java" >}}
