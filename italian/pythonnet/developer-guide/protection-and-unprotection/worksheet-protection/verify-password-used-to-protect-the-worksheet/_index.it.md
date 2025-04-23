---
title: Verificare la password utilizzata per proteggere il foglio di lavoro
type: docs
weight: 370
url: /it/python-net/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

Le API di Aspose.Cells per Python via .NET hanno migliorato la classe [**Protection**](https://reference.aspose.com/cells/python-net/aspose.cells/protection) introducendo alcune proprietà e metodi utili. Uno di questi metodi è [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password) che consente di specificare una password come istanza di *stringa* e verifica se la stessa password è stata utilizzata per proteggere il [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

{{% /alert %}}

Il metodo [**Protection.verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password) restituisce **true** se la password specificata corrisponde alla password utilizzata per proteggere il foglio di lavoro dato e **false** se la password specificata non corrisponde. Il seguente codice utilizza il metodo [**Protection.verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password) in combinazione con la proprietà [**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password) per rilevare la protezione della password e verificare la password.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPasswordUsedToProtectWorksheets.py" >}}

