---
title: Aspose.Cells, Excel, ICustomFunction, bir dizi değeri döndürür
description: Bu makale, Aspose.Cells kitaplığını kullanarak Microsoft Excel de ICustomFunction ile bir değer aralığını döndürmeyi açıklar. Varolan bir Excel dosyasını yükleyerek veya yeni bir Excel dosyası oluşturarak, Aspose.Cells tarafından sağlanan yöntemleri kullanarak bir dizi değer alabilir ve sonucu döndürebiliriz. Son olarak, değiştirilmiş Excel dosyasını diske kaydederiz.
keywords: Aspose.Cells, Excel, ICustomFunction, bir dizi değeri döndürür
type: docs
weight: 50
url: /tr/net/returning-a-range-of-values-using-icustomfunction/
---

{{% alert color="primary" %}}

[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction), Aspose.Cells for Java sürümü ile kullanımdan kaldırılmıştır 20.8. Lütfen [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) sınıfını kullanın. [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) sınıfının kullanımı aşağıdaki makalede açıklanmaktadır.

[AbstractCalculationEngine Kullanarak Bir Değer Aralığı Döndürme](/cells/tr/net/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

Aspose.Cells, Microsoft Excel tarafından desteklenmeyen kullanıcı tanımlı veya özel işlevleri uygulamak için kullanılan [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) arayüzünü sağlar.

Çoğunlukla [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) arayüz methodunu uyguladığınızda tek hücre değeri döndürmeniz gerekir. Ancak bazen, [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) aralığındaki değerleri döndürmeniz gerekir. Bu makale, [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) aralığındaki değerlerin nasıl döndürüleceğini açıklayacaktır.

{{% /alert %}}

Aşağıdaki kod [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) uygular ve metodunu kullanarak değerlerin aralığını döndürür.

Bir *CalculateCustomFunction* işlevi olan bir sınıf oluşturun. Bu sınıf, [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) uygular.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-CustomFunctionStaticValue.cs" >}}

Şimdi yukarıdaki işlevi programınıza ekleyin.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-1.cs" >}}
