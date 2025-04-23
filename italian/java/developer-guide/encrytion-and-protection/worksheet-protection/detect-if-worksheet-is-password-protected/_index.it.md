---
title: Scoprire se il foglio di lavoro è protetto da password
type: docs
weight: 280
url: /it/java/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

È possibile proteggere i fogli di lavoro e i fogli di lavoro separatamente. Ad esempio, un foglio di calcolo può contenere uno o più fogli di lavoro protetti da password, tuttavia, il foglio di calcolo stesso può essere protetto o meno. Le API di Aspose.Cells forniscono il modo per rilevare se un determinato foglio di lavoro è protetto da password o meno. Questo articolo dimostra l'uso dell'API Aspose.Cells for Java per ottenere lo stesso.

{{% /alert %}}

## **Verificare se il foglio di lavoro è protetto da password**

Aspose.Cells for Java 8.7.0 ha esposto la proprietà [**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) per rilevare se un foglio di lavoro è protetto da password o meno. Il campo di tipo booleano [**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) restituisce true se [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) è protetto da password e false se non lo è.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectWorksheetisPasswordProtected-DetectWorksheetisPasswordProtected.java" >}}
{{< app/cells/assistant language="java" >}}
