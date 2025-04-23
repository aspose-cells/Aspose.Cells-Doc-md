---
title: Verifica la password di modifica usando Aspose.Cells per Python via .NET
type: docs
weight: 2400
url: /it/python-net/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}}

A volte, è necessario verificare se la password data corrisponde alla **Password di modifica** tramite programmazione. Aspose.Cells per Python via .NET fornisce il metodo WorkbookSettings.write_protection.validate_password() che può essere usato per verificare se la Password di modifica è corretta o meno.

{{% /alert %}}

## **Verificare la password per modificare in Microsoft Excel**

È possibile assegnare **Password per aprire** e **Password per modificare** durante la creazione dei propri workbook in Microsoft Excel. Si prega di vedere questa schermata che mostra l'interfaccia fornita da Microsoft Excel per specificare queste password.

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## **Verifica la password di modifica usando Aspose.Cells per Python via .NET**

I seguenti codici di esempio caricano il [file Excel di origine](5112232.xlsx). Ha una Password per aprire come 1234 e una Password per modificare come 5678. Il codice prima verifica se 567 è la Password per modificare corretta e restituisce false e poi verifica se 5678 è la Password per modificare e restituisce true.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-CheckPasswordToModifyUsingAsposeCells.py" >}}

### **Output della console**

Ecco l'output della console del codice di esempio precedente dopo aver caricato il [file Excel di origine](5112232.xlsx).

{{< highlight java >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}

