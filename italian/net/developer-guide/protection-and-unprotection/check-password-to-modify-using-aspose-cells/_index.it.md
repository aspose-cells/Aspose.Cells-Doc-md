---
title: Controllare la password da modificare utilizzando Aspose.Cells
type: docs
weight: 2400
url: /it/net/check-password-to-modify-using-aspose-cells/
---
{{% alert color="primary" %}}

 A volte, è necessario verificare se la password fornita corrisponde al file**Password da modificare** programmaticamente. Aspose.Cells fornisce il metodo WorkbookSettings.WriteProtection.ValidatePassword() che è possibile utilizzare per verificare se la password specificata da modificare è corretta o meno.

{{% /alert %}}

## **Controllare la password da modificare in Microsoft Excel**

Puoi assegnare**Password per aprire** e**Password da modificare** durante la creazione delle cartelle di lavoro in Microsoft Excel. Si prega di vedere questo screenshot che mostra l'interfaccia fornita da Microsoft Excel per specificare queste password.

|![cose da fare:immagine_alt_testo](check-password-to-modify-using-aspose-cells_1.png)|
|:- |

## **Controllare la password da modificare utilizzando Aspose.Cells**

 I seguenti codici di esempio caricano il file[fonte Excel](5112232.xlsx) file. Ha una Password da aprire come 1234 e una Password da modificare come 5678. Il codice controlla prima se 567 è Password corretta da modificare e restituisce false e poi controlla se 5678 è Password da modificare e restituisce true.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckPasswordToModify-CheckPasswordToModifyUsingAsposeCells.cs" >}}

### **Uscita console**

 Ecco l'output della console del codice di esempio precedente dopo aver caricato il file[fonte Excel](5112232.xlsx) file.

{{< highlight "java" >}}

Is 567 correct Password to modify: False

Is 5678 correct Password to modify: True

{{< /highlight >}}
