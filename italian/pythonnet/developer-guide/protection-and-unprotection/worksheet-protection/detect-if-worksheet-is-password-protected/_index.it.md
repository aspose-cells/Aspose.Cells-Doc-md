---
title: Scoprire se il foglio di lavoro è protetto da password
type: docs
weight: 360
url: /it/python-net/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

È possibile proteggere workbooks e fogli di lavoro separatamente. Ad esempio, un foglio di calcolo può contenere uno o più fogli di lavoro protetti da password, tuttavia, il foglio di calcolo stesso può essere protetto o meno. Le API di Aspose.Cells per Python via .NET offrono i mezzi per rilevare se un determinato foglio di lavoro è protetto da password o meno. Questo articolo dimostra come usare l'API di Aspose.Cells per Python via .NET per ottenere lo stesso.

{{% /alert %}}

Aspose.Cells per Python via .NET ha esposto la proprietà [**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password) per rilevare se un foglio di lavoro è protetto da password o meno. La proprietà di tipo boolean [**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password) restituisce **true** se [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) è protetto da password e **false** se non lo è.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-CheckIfPasswordProtected.py" >}}

{{< app/cells/assistant language="python-net" >}}
