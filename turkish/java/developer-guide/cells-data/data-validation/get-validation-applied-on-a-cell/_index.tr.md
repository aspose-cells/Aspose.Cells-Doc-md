---
title: Cell'de Doğrulama Uygulayın
type: docs
weight: 80
url: /tr/java/get-validation-applied-on-a-cell/
description: Bu makale, Java ile Cell üzerinde doğrulamanın nasıl uygulanacağını gösterir.
keywords: apply cell validation in excel with java, apply validation on a cell in excel with java, apply validation in excel with java, cell validation in excel with java, java apply cell validation in excel, java apply validation on a cell in excel, java cell validation in excel, java cell validation
---
{{% alert color="primary" %}}

 Herhangi bir hücreye uygulanan doğrulamayı almak için Aspose.Cells API'i kullanabilirsiniz. Aspose.Cells sağlar[**Cell.getValidation**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidation() ) yöntemi bu amaç için. Hücrede doğrulama yoksa, null değerini döndürür. Benzer şekilde,[**Worksheet.getValidations().getValidationInCell(int satır, int sütun)**](https://reference.aspose.com/cells/java/com.aspose.cells/validationcollection#getValidationInCell(int,%20int)) satır ve sütun indekslerini sağlayarak bir hücreye uygulanan doğrulamayı elde etme yöntemi.

{{% /alert %}}

 Aşağıdaki anlık görüntü, aşağıdaki örnek kodda kullanılan örnek Microsoft Excel dosyasını göstermektedir. Cell**C1** vardır**ondalık doğrulama** uygulanır ve yalnızca değer alabilir**10 ile 20 arasında**.

**Doğrulamalı bir hücre**

![yapılacaklar:resim_alternatif_metin](get-validation-applied-on-a-cell_1.png)

Aşağıdaki örnek kod, C1'e uygulanan doğrulamayı alır ve çeşitli özelliklerini okur.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetValidationAppliedonCell-GetValidationAppliedonCell.java" >}}

İşte yukarıdaki anlık görüntüde gösterilen örnek dosyayla yürütülen örnek koddan elde edilen konsol çıktısı.

{{< highlight "java" >}}

Reading Properties of Validation

\--------------------------------

Type: 2

Operator: 0

Formula1: =10

Formula2: =20

Ignore blank: true

{{< /highlight >}}

## İlgili Makaleler

- [Veri doğrulama](/cells/tr/java/data-validation/)
