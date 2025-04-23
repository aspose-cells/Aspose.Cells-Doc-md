---
title: Hücreye Uygulanan Doğrulamayı Al
type: docs
weight: 200
url: /tr/nodejs-cpp/get-validation-applied-on-a-cell/
description: Bu makale, Node.js (C++ aracılığıyla) kullanarak bir Hücreye nasıl doğrulama uygulanacağını gösterir.
keywords: Node.js kullanarak Excel de hücre doğrulaması uygulama, C++ kullanarak Excel de hücre doğrulaması uygula, Node.js ile Excel de doğrulama uygula, hücre doğrulaması yap in Excel with Node.js via C++, hücre doğrulamasını uygulamak için Node.js ve C++ kullanın
---

{{% alert color="primary" %}}

Node.js için Aspose.Cells kullanarak hücreye uygulanan doğrulamayı alabilirsiniz. Aspose.Cells, bunun için [**Cell.getValidation()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidation--) metodunu sağlar. Eğer hücrede doğrulama uygulanmamışsa, null döner.

Benzer şekilde, [**Worksheet.validations.getValidationInCell(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/validationcollection/#getValidationInCell-number-number-) yöntemini kullanarak bir hücreye uygulanan doğrulamayı alabilirsiniz. Bu yöntem, satır ve sütun indislerini sağlayarak çalışmaktadır.

{{% /alert %}}

## Node.js kodu ile bir Hücreye uygulanan doğrulamayı alın

Aşağıdaki kod örneği, hücreye uygulanan doğrulamayı nasıl alacağınızı gösterir.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-ReadingValidationPropertiesOfCell.js" >}}


## İlgili Makaleler

- [Veri Doğrulama](/cells/tr/nodejs-cpp/data-validation/)
