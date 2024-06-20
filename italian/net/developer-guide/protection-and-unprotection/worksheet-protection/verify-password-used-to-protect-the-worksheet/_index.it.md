---
title: Verificare la password utilizzata per proteggere il foglio di lavoro
type: docs
weight: 370
url: /it/net/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

Le API di Aspose.Cells hanno potenziato la classe [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/protection) introducendo alcune proprietà e metodi utili. Uno di questi metodi è il [**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) che consente di specificare una password come istanza di *stringa* e verifica se la stessa password è stata utilizzata per proteggere il [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

{{% /alert %}}

Il metodo [**Protection.VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) restituisce **true** se la password specificata corrisponde alla password utilizzata per proteggere il foglio di lavoro dato e **false** se la password specificata non corrisponde. Il seguente codice utilizza il metodo [**Protection.VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) in combinazione con la proprietà [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) per rilevare la protezione della password e verificare la password.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-VerifyPasswordUsedToProtectWorksheets-VerifyPasswordUsedToProtectWorksheets.cs" >}}
