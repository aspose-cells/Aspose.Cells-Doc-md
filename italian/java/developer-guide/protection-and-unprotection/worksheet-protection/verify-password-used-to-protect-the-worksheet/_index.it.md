---
title: Verificare la password utilizzata per proteggere il foglio di lavoro
type: docs
weight: 290
url: /it/java/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

Le API di Aspose.Cells hanno migliorato la classe [**Protection**](https://reference.aspose.com/cells/java/com.aspose.cells/Protection) introducendo alcune proprietà e metodi utili. Uno di questi metodi è [**verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword-java.lang.String-) che consente di specificare una password come istanza di String e verifica se la stessa password è stata utilizzata per proteggere il foglio di lavoro.

{{% /alert %}}

## **Verificare la password utilizzata per proteggere il foglio di lavoro**

Il metodo [**Protection.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword-java.lang.String-) restituisce true se la password specificata corrisponde alla password utilizzata per proteggere il foglio di lavoro fornito, false se la password specificata non corrisponde. Il seguente pezzo di codice utilizza il metodo [**Protection.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword-java.lang.String-) in combinazione con la proprietà [**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword) per rilevare la protezione con password e verifica la password.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyPasswordtoProtectWorksheet-VerifyPasswordtoProtectWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}
