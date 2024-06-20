---
title: Aspose.Cells, Excel, ICustomFunction, bir dizi değeri döndürür
type: docs
weight: 270
url: /tr/java/returning-a-range-of-values-using-icustomfunction/
---

{{% alert color="primary" %}}

[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction), Aspose.Cells for Java sürümü ile kullanımdan kaldırılmıştır 20.8. Lütfen [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) sınıfını kullanın. [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) sınıfının kullanımı aşağıdaki makalede açıklanmaktadır.

[AbstractCalculationEngine Kullanarak Değer Aralığı Döndürme](/cells/tr/java/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}}

{{% alert color="primary" %}}

Aspose.Cells, Microsoft Excel tarafından desteklenmeyen kullanıcı tanımlı veya özel işlevleri uygulamak için kullanılan [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) arayüzünü sağlar.

Çoğunlukla [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) arayüz methodunu uyguladığınızda tek hücre değeri döndürmeniz gerekir. Ancak bazen, [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) aralığındaki değerleri döndürmeniz gerekir. Bu makale, [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) aralığındaki değerlerin nasıl döndürüleceğini açıklayacaktır.

{{% /alert %}}

## **ICustomFunction Kullanarak Bir Değer Aralığı Döndürme**

Aşağıdaki kod [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) uygular ve yöntemi aracılığıyla değer aralığını döndürür. Referans için, kod ile oluşturulan [çıktı Excel dosyasını](5472922.xlsx) ve [pdf](5472925.pdf) dosyasını kontrol edin.

Bir sınıf oluşturun ve içine *CalculateCustomFunction* fonksiyonunu ekleyin. Bu sınıf [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)'ı uygular.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

Şimdi yukarıdaki işlevi programınıza ekleyin.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReturningRangeOfValues-ReturningRangeOfValues.java" >}}
