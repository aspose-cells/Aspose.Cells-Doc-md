---
title: Çalışma Kitabının Yönetilmeyen Kaynaklarını Serbest Bırak
type: docs
weight: 290
url: /tr/java/release-unmanaged-resources-of-the-workbook/
---

{{% alert color="primary" %}} 

Aspose.Cells, [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose--) yöntemiyle, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) nesnesinin yönetilmeyen kaynaklarını serbest bırakmayı sağlar. Dispose kalıbı, yalnızca yönetilmeyen kaynaklara erişen nesneler için kullanılır; örneğin dosya ve boru tutamacı, kayıt defteri tutamacı, bekleme tutamacı veya yönetilmeyen bellek bloklarına işaretçiler. Bunun nedeni, çöp toplayıcının kullanılmayan yönetilen nesneleri geri kazanmakta çok verimli olması, ancak yönetilmeyen nesneleri geri alamamasıdır.

{{% /alert %}} 
## **Çalışma Kitabının Yönetilmeyen Kaynaklarını Serbest Bırak**
Aşağıdaki örnek kod, [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose--) yönteminin nasıl kullanılacağını gösterir.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReleaseUnmanagedResources-ReleaseUnmanagedResources.java" >}}
{{< app/cells/assistant language="java" >}}
