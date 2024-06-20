---
title: Aspose.Cells kitaplığını kullanarak Microsoft Excel de bir dizi değeri döndüren soyut bir hesaplama motoru tanıtır. Varolan bir Excel dosyasını yükleyerek veya yeni bir Excel dosyası oluşturarak, Aspose.Cells tarafından sağlanan yöntemleri kullanarak bir dizi değeri alabiliriz ve sonucu döndürebiliriz. Son olarak, değiştirilmiş Excel dosyasını diske kaydederiz.
type: docs
weight: 275
url: /tr/java/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells, Microsoft Excel tarafından desteklenmeyen kullanıcı tanımlı veya özel işlevleri uygulamak için kullanılan [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) sınıfını sağlar.

Bu makale, [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) aralığındaki değerlerin nasıl döndürüleceğini açıklayacaktır.

{{% /alert %}}

Aşağıdaki kod, [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) kullanımını gösterir ve yöntemi aracılığıyla değer aralığını döndürür.

Bir sınıf oluşturun ve içine *CalculateCustomFunction* fonksiyonunu ekleyin. Bu sınıf [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)'ı genişletir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

Şimdi yukarıdaki işlevi programınıza ekleyin.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ReturningRangeOfValues-1.java" >}}
