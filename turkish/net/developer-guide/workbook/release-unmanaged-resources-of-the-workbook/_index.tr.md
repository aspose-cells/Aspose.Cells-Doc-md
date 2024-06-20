---
title: Çalışma Kitabının Yönetilmeyen Kaynaklarını Serbest Bırak
type: docs
weight: 310
url: /tr/net/release-unmanaged-resources-of-the-workbook/
---

{{% alert color="primary" %}}

Aspose.Cells, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) nesnesinin yönetilmeyen kaynaklarını serbest bırakmak için [**Workbook.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) yöntemi sağlar. Temizleme deseni, yalnızca dosya ve boru tanıtıcıları, kayıt defteri tanıtıcıları, bekleme tanıtıcıları veya yönetilmeyen bellek bloklarına erişen nesneler için kullanılır. Bu, çöp toplayıcısının kullanılmayan yönetilen nesneleri geri kazanmadaki çok etkili olmasından dolayıdır, ancak yönetilmeyen nesneleri geri kazanamaz.

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) nesnesi artık *System.IDisposable* arayüzünü uygulamaktadır, bu arayüzün [**Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) geçerli bir yöntemi bulunmaktadır. Bu yöntemi doğrudan çağırabilir veya bu yöntemi otomatik olarak çağırmak için *Using* ifadesini kullanabilirsiniz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ReleaseUnmanagedResources-ReleaseUnmanagedResourcesForWorkbooks.cs" >}}
