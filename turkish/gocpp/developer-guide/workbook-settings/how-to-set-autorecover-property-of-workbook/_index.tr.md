---
title: Golang ile C++ kullanarak Çalışma Kitabının Otomatik Kurtarma özelliğini nasıl ayarlayacağınızı öğrenin
linktitle: Çalışma Kitabının Otomatik Kurtarma Özelliğini Ayarlamak
type: docs
weight: 220
url: /tr/go-cpp/how-to-set-autorecover-property-of-workbook/
description: Bir çalışma kitabının Otomatik Kurtarma özelliğini etkinleştirmek veya devre dışı bırakmak için Aspose.Cells for C++ kullanmayı öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells kullanarak, bir çalışma kitabının Otomatik Kurtarma özelliğini ayarlayabilirsiniz. Bu özelliğin varsayılan değeri **true**'dur. Bunu bir çalışma kitabında **false** olarak ayarladığınızda, Microsoft Excel, AutoRecover (Otomatik Kaydetme) fonksiyonunu devre dışı bırakır.

Aspose.Cells, bu seçeneği etkinleştirmek veya devre dışı bırakmak için [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getautorecover/) özelliğini sağlar.

{{% /alert %}}

Aşağıdaki kod, çalışma kitabının [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getautorecover/) özelliğinin nasıl kullanılacağını açıklar. Öncelikle bu özelliğin varsayılan değeri olan **true** okunur, ardından **false** olarak ayarlanır ve çalışma kitabı kaydedilir. Ardından, tekrar okunur ve bu özelliğin değeri, şu anda **false** olarak okunur.

## C++ ile WorkBook'un Otomatik Kurtarma Özelliğini Ayarlama Kodu

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetAutorecoverPropertyOfWorkbook.go" >}}
## **Çıktı**

Yukarıdaki örnek kodun konsol çıktısı burada gösterilmektedir.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
