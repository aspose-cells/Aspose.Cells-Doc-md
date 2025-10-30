---
title: Çalışma Kitabının Yönetilmeyen Kaynaklarını Serbest Bırakma Golang ile C++
linktitle: Çalışma Kitabının Yönetilmeyen Kaynaklarını Serbest Bırak
type: docs
weight: 310
url: /tr/go-cpp/release-unmanaged-resources-of-the-workbook/
description: Golang kullanarak C++ ile Aspose.Cells ile Çalışma Kitabının yönetilmeyen kaynaklarını serbest bırakmayı öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) nesnesinin yönetilmeyen kaynaklarını serbest bırakmak için [**Workbook.Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/) yöntemi sağlar. Temizleme deseni, yalnızca dosya ve boru tanıtıcıları, kayıt defteri tanıtıcıları, bekleme tanıtıcıları veya yönetilmeyen bellek bloklarına erişen nesneler için kullanılır. Bu, çöp toplayıcısının kullanılmayan yönetilen nesneleri geri kazanmadaki çok etkili olmasından dolayıdır, ancak yönetilmeyen nesneleri geri kazanamaz.

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/go-cpp/workbook/) nesnesi artık *IDisposable* arayüzünü uygular ve bu arayüz tek bir yöntem [**Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/) içerir. [**Workbook.Dispose()**](https://reference.aspose.com/cells/go-cpp/workbook/dispose/) yöntemini doğrudan çağırabilir veya bu yöntemi otomatik çağırmak için *Using* ifadesini kullanabilirsiniz.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ReleaseUnmanagedResourcesOfTheWorkbook.go" >}}
