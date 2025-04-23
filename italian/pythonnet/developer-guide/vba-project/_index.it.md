---
title: Gestire i codici VBA della cartella di lavoro abilitata per i macro di Excel.
linktitle: Progetto macro
type: docs
weight: 200
url: /it/python-net/manage-vba-project/
description: Aggiungi modulo VBA e modifica VBA o Macro con la libreria Aspose.Cells for Python via .NET.
---

## **Aggiungi un modulo VBA in Python**
{{% alert color="primary" %}}

Aspose.Cells consente di aggiungere un nuovo modulo VBA e codice Macro utilizzando Aspose.Cells for Python via .NET. Si prega di usare il metodo [**Workbook.vba_project.modules.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/add/) per aggiungere il nuovo modulo VBA all’interno del file di lavoro

{{% /alert %}}

Il seguente codice di esempio crea un nuovo workbook e aggiunge un nuovo modulo VBA e codice macro e salva l'output nel formato XLSM. Una volta aperto il file XLSM di output in Microsoft Excel e fare clic sui comandi del menu **Sviluppo > Visual Basic**, verrà visualizzato un modulo chiamato "TestModule" e al suo interno verrà visualizzato il seguente codice macro.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Qui si trova il codice di esempio per generare il file XLSM di output con un modulo VBA e un codice macro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-AddVBAModuleOrCode.py" >}}

## **Modifica VBA o Macro in Python**

{{% alert color="primary" %}} 

Puoi modificare il codice VBA o Macro usando Aspose.Cells for Python via .NET. Aspose.Cells for Python via .NET ha aggiunto il seguente namespace e le classi per leggere e modificare il progetto VBA nel file Excel.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Questo articolo mostrerà come cambiare il codice VBA o Macro all’interno del file Excel di origine usando Aspose.Cells for Python via .NET.

{{% /alert %}} 

Il seguente codice di esempio carica il file Excel di origine che contiene il seguente codice VBA o Macro al suo interno

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

Dopo l’esecuzione del codice di esempio di Aspose.Cells for Python via .NET, il codice VBA o Macro verrà modificato così

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

Puoi scaricare il [file Excel di origine](5112508.xlsm) e il [file Excel di output](5112511.xlsm) dai link forniti.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-ModifyingVBAOrMacroCode.py" >}}

## **Argomenti avanzati**
- [Aggiungi un riferimento alla libreria al progetto VBA nel foglio di lavoro](/cells/it/python-net/add-a-library-reference-to-vba-project-in-workbook/)
- [Verifica se la firma digitale del codice VBA è valida](/cells/it/python-net/check-if-digital-signature-of-vba-code-is-valid/)
- [Verifica se il codice VBA è firmato](/cells/it/python-net/check-if-vba-code-is-signed/)
- [Verifica se il progetto VBA in un foglio di lavoro è firmato](/cells/it/python-net/check-if-vba-project-in-a-workbook-is-signed/)
- [Verifica se il progetto VBA è protetto e bloccato per la visualizzazione](/cells/it/python-net/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Firma digitalmente un progetto di codice VBA con un certificato](/cells/it/python-net/digitally-sign-a-vba-code-project-with-certificate/)
- [Esporta il certificato VBA su file o flusso](/cells/it/python-net/export-vba-certificate-to-file-or-stream/)
- [Filtra il progetto VBA durante il caricamento di un libro di lavoro](/cells/it/python-net/filter-vba-project-while-loading-a-workbook/)
- [Scopri se il progetto VBA è protetto](/cells/it/python-net/find-out-if-vba-project-is-protected/)
- [Proteggi con password il progetto VBA del foglio di lavoro Excel](/cells/it/python-net/password-protect-the-vba-project-of-excel-workbook/)

