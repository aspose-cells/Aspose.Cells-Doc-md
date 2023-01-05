---
title: Çalışma Kitabının Yönetilmeyen Kaynaklarını Serbest Bırakma
type: docs
weight: 310
url: /tr/net/release-unmanaged-resources-of-the-workbook/
---
{{% alert color="primary" %}}

 Aspose.Cells sağlar[**Workbook.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) yönetilmeyen kaynakları serbest bırakma yöntemi[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook)nesne. Dispose modeli yalnızca dosya ve yönlendirme tanıtıcıları, kayıt tanıtıcıları, bekleme tutamaçları veya yönetilmeyen bellek bloklarına yönelik işaretçiler gibi yönetilmeyen kaynaklara erişen nesneler için kullanılır. Bunun nedeni, çöp toplayıcının kullanılmayan yönetilen nesneleri geri alma konusunda çok verimli olmasına karşın yönetilmeyen nesneleri geri alamamasıdır.

{{% /alert %}}

[**Çalışma kitabı**](https://reference.aspose.com/cells/net/aspose.cells/workbook) nesne şimdi uygular*System.IDdisposable* tek bir yöntemi olan arayüz[**Elden çıkarmak()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) . doğrudan arayabilirsiniz[**Workbook.Dispose()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/dispose) yöntemini kullanabilir veya*kullanma*Bu yöntemi otomatik olarak çağırmak için deyim.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ReleaseUnmanagedResources-ReleaseUnmanagedResourcesForWorkbooks.cs" >}}
