---
title: Verificare la password per la modifica utilizzando Aspose.Cells
type: docs
weight: 2400
url: /it/net/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}}

A volte è necessario verificare se la password fornita corrisponde alla **Password per la modifica** in modo programmatico. Aspose.Cells fornisce il metodo WorkbookSettings.WriteProtection.ValidatePassword() che è possibile utilizzare per verificare se la Password per la modifica fornita è corretta o no.

{{% /alert %}}

## **Verificare la password per modificare in Microsoft Excel**

È possibile assegnare **Password per aprire** e **Password per modificare** durante la creazione dei propri workbook in Microsoft Excel. Si prega di vedere questa schermata che mostra l'interfaccia fornita da Microsoft Excel per specificare queste password.

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|
| :- |

## **Controllare la password per la modifica utilizzando Aspose.Cells**

I seguenti codici di esempio caricano il [file Excel di origine](5112232.xlsx). Ha una Password per aprire come 1234 e una Password per modificare come 5678. Il codice prima verifica se 567 è la Password per modificare corretta e restituisce false e poi verifica se 5678 è la Password per modificare e restituisce true.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckPasswordToModify-CheckPasswordToModifyUsingAsposeCells.cs" >}}

### **Output della console**

Ecco l'output della console del codice di esempio precedente dopo aver caricato il [file Excel di origine](5112232.xlsx).

{{< highlight java >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
