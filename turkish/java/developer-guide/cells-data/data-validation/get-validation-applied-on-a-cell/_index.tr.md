---
title: Hücreye Uygulanan Doğrulamayı Al
type: docs
weight: 80
url: /tr/java/get-validation-applied-on-a-cell/
description: Bu makale, Java ile bir Hücreye Doğrulama Uygulamanın nasıl yapıldığını gösterir
keywords: java da excel ile hücre doğrulaması uygula, java da hücreye doğrulama uygula, excel ile java da doğrulama uygula, excel de java ile doğrulama uygulama, java da excel hücresine doğrulama uygula, java da excelde hücreye doğrulama uygula, java da excel hücre doğrulama, java da excel hücre doğrulama
---

{{% alert color="primary" %}}

Herhangi bir hücreye uygulanan doğrulamayı almak için Aspose.Cells API'sini kullanabilirsiniz. Bu amaçla Aspose.Cells, [**Cell.getValidation()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidation--) yöntemini sağlar. Eğer hücrede doğrulama yoksa null döner. Benzer şekilde, satır ve sütun indislerini sağlayarak bir hücreye uygulanan doğrulamayı almak için [**Worksheet.getValidations().getValidationInCell(int row, int column)**](https://reference.aspose.com/cells/java/com.aspose.cells/validationcollection#getValidationInCell-int-int-) yöntemini kullanabilirsiniz.

{{% /alert %}}

Aşağıdaki ekran görüntüsü, örnek Microsoft Excel dosyasını gösterir; C1 hücresine **ondalık doğrulama** uygulanmıştır ve sadece **10 ile 20 arasındaki** değerleri alabilir.

**Doğrulamalı bir hücre**

![todo:image_alt_text](get-validation-applied-on-a-cell_1.png)

Örnek kod aşağıda C1'e uygulanan doğrulamayı alır ve çeşitli özelliklerini okur.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetValidationAppliedonCell-GetValidationAppliedonCell.java" >}}

Aşağıdaki örnek dosyasıyla birlikte çalıştırılan örnek kodun konsol çıktısı burada gösterilen ekran görüntüsünde gösterilmektedir.

{{< highlight java >}}

Reading Properties of Validation

\--------------------------------

Type: 2

Operator: 0

Formula1: =10

Formula2: =20

Ignore blank: true

{{< /highlight >}}

## İlgili Makaleler

- [Veri Doğrulama](/cells/tr/java/data-validation/)
{{< app/cells/assistant language="java" >}}
