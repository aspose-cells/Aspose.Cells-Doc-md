---
title: Çerçeve Betiklerini ve Belge Özelliklerini dışa aktarmayı devre dışı bırakma Golang ve C++ ile
type: docs
weight: 310
url: /tr/go-cpp/disable-exporting-frame-scripts-and-document-properties/
description: Çerçeve betiklerini ve belge özelliklerini dışa aktarmayı devre dışı bırakma Golang ve C++ ile
---

{{% alert color="primary" %}}

Aspose.Cells, çalışma kitabını HTML'ye dönüştürürken çerçeve çalışması ve belge özelliklerini dışa aktarır. Aspose.Cells for C++ sürümünün 8.6.0, çerçeve çalışması ve belge özelliklerini isteğe bağlı olarak devre dışı bırakma seçeneği sunar. Lütfen çeviriyi devre dışı bırakmak için HtmlSaveOptions.ExportFrameScriptsAndProperties özelliğini kullanın.

{{% /alert %}}

## **Çerçeve betikleri ve belge özelliklerinin dışa aktarılmasını devre dışı bırak**

Aşağıdaki örnek kod, çerçeve betikleri ve belge özelliklerinin dışa aktarılmasını devre dışı bırakmanıza olanak tanır. Bir çalışma kitabını HTML'e dönüştürdüğünüzde, çıktı dosyası herhangi bir çerçeve betiği ve belge özelliği içermez.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableExportingFrameScriptsAndDocumentProperties.go" >}}
