---
title: Cell Veri Doğrulamaları Ekle
type: docs
weight: 90
url: /tr/net/add-cell-data-validations/
---
{{% alert color="primary" %}} 

 Aspose.Cells.GridWeb eklemenizi sağlar**Veri doğrulama** GridWorksheet.Validations.Add() yöntemini kullanarak. Bu yöntemi kullanarak, belirtmeniz gerekir**Cell Aralık** Ancak, tek bir GridCell'de Veri Doğrulama oluşturmak istiyorsanız, bunu doğrudan GridCell.CreateValidation() yöntemini kullanarak yapabilirsiniz. Benzer şekilde, kaldırabilirsiniz**Veri doğrulama** GridCell.RemoveValidation() yöntemini kullanarak bir GridCell'den.

{{% /alert %}} 
## **GridWeb'in GridCell'inde Veri Doğrulaması Oluşturma**
 Aşağıdaki örnek kod, bir**Veri doğrulama** B3 hücresinde. 20 ile 40 arasında olmayan bir değer girerseniz, B3 hücresi görünecektir.**Doğrulama Hatası** şeklinde**kırmızı XXXX** bu ekran görüntüsünde gösterildiği gibi.

![yapılacaklar:resim_alternatif_Metin](add-cell-data-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDataValidation.aspx-AddDataValidation.cs" >}}
