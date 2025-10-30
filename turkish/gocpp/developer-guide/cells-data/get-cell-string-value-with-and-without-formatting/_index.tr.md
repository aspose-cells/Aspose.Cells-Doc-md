---
title: Golang ile C++ üzerinden Formatlama ile ve Formatlama olmadan Hücre Dizesi Değeri Al
linktitle: Hücre Dizisi Değeri Alma
type: docs
weight: 240
url: /tr/go-cpp/get-cell-string-value-with-and-without-formatting/
description: Aspose.Cells for C++ API kullanarak, Formatlama ve Formatlamadan Hücre Dizisi Değeri Alma yöntemlerini öğrenin.
keywords: Biçimlendirme ile ve biçimlendirme olmadan Hücre Dize Değeri Almayı, Biçimlendirme ile ve biçimlendirme olmadan Hücre Dize Değeri Almayı Kurtarma, Biçimlendirme ile ve biçimlendirme olmadan Hücre Dize Değeri Almayı Elde Etme
---

{{% alert color="primary" %}}

Aspose.Cells, hücrenin değerini ve nan herhangi bir biçimlendirme ile veya biçimlendirmeden almak için kullanılabilecek [**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/) yöntemini sağlar. Diyelim ki, değeri 0.012345 olan bir hücreniz var ve sadece iki ondalık gösterilecek şekilde biçimlendirilmiş. Bu durumda, Excel'de 0.01 olarak görüntülenir. Hem 0.01 hem de 0.012345 şeklinde string değerleri `[**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/)` yöntemi ile alabilirsiniz. Bu yöntem, aşağıdaki değerleri içeren `[**CellValueFormatStrategy**](https://reference.aspose.com/cells/cpp/aspose.cells/cellvalueformatstrategy/)` enum parametresi alır:

- CellValueFormatStrategy::CellStyle
- CellValueFormatStrategy::DisplayStyle
- CellValueFormatStrategy::DisplayString
- CellValueFormatStrategy::Hiçbiri

{{% /alert %}}

Aşağıdaki örnek kod, [**Cell::GetStringValue()**](https://reference.aspose.com/cells/go-cpp/cell/getstringvalue_cellvalueformatstrategy/) yönteminin kullanımını açıklar.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetCellStringValueWithAndWithoutFormatting.go" >}}
