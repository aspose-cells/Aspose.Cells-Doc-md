---
title: Verificare la password utilizzata per proteggere il foglio di lavoro
type: docs
weight: 370
url: /it/net/verify-password-used-to-protect-the-worksheet/
---
{{% alert color="primary" %}}

 Aspose.Cells Le API hanno migliorato il file[**Protezione**](https://reference.aspose.com/cells/net/aspose.cells/protection) class introducendo alcune utili proprietà e metodi. Uno di questi metodi è il[**Verifica la password**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) che consente di specificare una password come istanza di*corda* e verifica se la stessa password è stata utilizzata per proteggere il[**Foglio di lavoro**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

{{% /alert %}}

 Il[**Protezione.VerificaPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) metodo restituisce**VERO**se la password specificata corrisponde alla password utilizzata per proteggere il foglio di lavoro specificato e**falso** se la password specificata non corrisponde. La parte di codice seguente utilizza il[**Protezione.VerificaPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) metodo in combinazione con[**Protezione.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword)property per rilevare la protezione tramite password e verifica la password.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-VerifyPasswordUsedToProtectWorksheets-VerifyPasswordUsedToProtectWorksheets.cs" >}}
