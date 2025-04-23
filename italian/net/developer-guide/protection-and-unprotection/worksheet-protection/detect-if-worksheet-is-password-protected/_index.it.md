---
title: Scoprire se il foglio di lavoro è protetto da password
type: docs
weight: 360
url: /it/net/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

È possibile proteggere i workbook e i fogli di lavoro separatamente. Ad esempio, un foglio di calcolo può contenere uno o più fogli di lavoro protetti da password, tuttavia il foglio di calcolo stesso può essere protetto o meno. Le API di Aspose.Cells forniscono i mezzi per verificare se un dato foglio di lavoro è protetto da password o meno. Questo articolo illustra l'uso dell'API Aspose.Cells for .NET per ottenere lo stesso risultato.

{{% /alert %}}

Aspose.Cells for .NET 8.7.0 ha esposto la proprietà [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) per sapere se un foglio di lavoro è protetto da password o meno. La proprietà di tipo booleano [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) restituisce **true** se [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) è protetto da password e **false** se non lo è.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckIfPasswordProtected-CheckIfPasswordProtected.cs" >}}
{{< app/cells/assistant language="csharp" >}}
