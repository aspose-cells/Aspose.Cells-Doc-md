---
title: 释放工作簿的非托管资源
type: docs
weight: 290
url: /zh/java/release-unmanaged-resources-of-the-workbook/
---

{{% alert color="primary" %}} 

Aspose.Cells 提供 [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose--) 方法，用于释放 [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) 对象的非托管资源。dispose 模式仅用于访问非托管资源（如文件句柄、管道句柄、注册表句柄、等待句柄或非托管内存块指针）的对象。这是因为垃圾回收器在回收未使用的托管对象方面非常高效，但无法回收非托管对象。

{{% /alert %}} 
## **释放工作簿的非托管资源**
以下示例代码展示了如何使用 [Workbook.dispose()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#dispose--) 方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReleaseUnmanagedResources-ReleaseUnmanagedResources.java" >}}
{{< app/cells/assistant language="java" >}}
