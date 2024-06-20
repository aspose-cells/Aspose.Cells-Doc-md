---
title: Hücre Veri Doğrulamaları Ekle
type: docs
weight: 90
url: /tr/net/aspose-cells-gridweb/add-cell-data-validations/
keywords: GridWeb, validation, veri doğrulama, GridValidation
description: Bu makale, GridWeb de veri doğrulamanın (GridValidation) nasıl eklenileceğini tanıtıyor.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb, GridWorksheet.Validations.Add() yöntemini kullanarak **Veri Doğrulaması** eklemenizi sağlar. Bu yöntemi kullanarak **Hücre Aralığı**nı belirtmeniz gerekmektedir. Ancak tek bir GridCell'de Veri Doğrulaması oluşturmak istiyorsanız, GridCell.CreateValidation() yöntemini doğrudan kullanabilirsiniz. Benzer şekilde, GridCell.RemoveValidation() yöntemini kullanarak bir GridCell'den **Veri Doğrulaması** kaldırabilirsiniz.

{{% /alert %}} 
## **GridWeb'in GridCell'inde Veri Doğrulama Oluşturma**
Aşağıdaki örnek kod, B3 hücresinde bir **Veri Doğrulaması** oluşturur. 20 ile 40 arasında olmayan bir değer girerseniz, B3 hücresi **Kırmızı XXXX** şeklinde bir **Doğrulama Hatası** gösterecektir, bu ekran görüntüsünde gösterildiği gibi.

![todo:image_alt_text](add-cell-data-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDataValidation.aspx-AddDataValidation.cs" >}}
