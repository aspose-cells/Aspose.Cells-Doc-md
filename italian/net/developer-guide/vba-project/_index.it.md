---
title: Gestire i codici VBA della cartella di lavoro abilitata per i macro di Excel.
linktitle: Progetto macro
type: docs
weight: 200
url: /it/net/manage-vba-project/
description: Aggiungi un modulo VBA e modifica il VBA o il macro con la libreria Aspose.Cells.
---

## **Aggiungi un modulo VBA in C#**
{{% alert color="primary" %}}

Aspose.Cells consente di aggiungere un nuovo modulo VBA e codice macro utilizzando Aspose.Cells. Si prega di utilizzare il metodo [**Workbook.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/add/index) per aggiungere il nuovo modulo VBA all'interno del workbook

{{% /alert %}}

Il seguente codice di esempio crea un nuovo workbook e aggiunge un nuovo modulo VBA e codice macro e salva l'output nel formato XLSM. Una volta aperto il file XLSM di output in Microsoft Excel e fare clic sui comandi del menu **Sviluppo > Visual Basic**, verrà visualizzato un modulo chiamato "TestModule" e al suo interno verrà visualizzato il seguente codice macro.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Qui si trova il codice di esempio per generare il file XLSM di output con un modulo VBA e un codice macro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AddVBAModuleOrCode-AddVBAModuleOrCode.cs" >}}

## **Modifica il VBA o il macro in C#**

{{% alert color="primary" %}} 

È possibile modificare il codice VBA o macro utilizzando Aspose.Cells. Aspose.Cells ha aggiunto i seguenti namespace e classi per leggere e modificare il progetto VBA nel file Excel.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Questo articolo ti mostrerà come modificare il codice VBA o Macro all'interno del file Excel di origine usando Aspose.Cells.

{{% /alert %}} 

Il seguente codice di esempio carica il file Excel di origine che contiene il seguente codice VBA o Macro al suo interno

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

Dopo l'esecuzione del codice di esempio di Aspose.Cells, il codice VBA o Macro sarà modificato in questo modo

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

Puoi scaricare il [file Excel di origine](5112508.xlsm) e il [file Excel di output](5112511.xlsm) dai link forniti.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-ModifyingVBAOrMacroCode-ModifyingVBAOrMacroCode.cs" >}}

## **Argomenti avanzati**
- [Aggiungi un riferimento alla libreria al progetto VBA nel foglio di lavoro](/cells/it/net/add-a-library-reference-to-vba-project-in-workbook/)
- [Assegna una Macro al controllo del modulo](/cells/it/net/assign-macro-to-form-control/)
- [Verifica se la firma digitale del codice VBA è valida](/cells/it/net/check-if-digital-signature-of-vba-code-is-valid/)
- [Verifica se il codice VBA è firmato](/cells/it/net/check-if-vba-code-is-signed/)
- [Verifica se il progetto VBA in un foglio di lavoro è firmato](/cells/it/net/check-if-vba-project-in-a-workbook-is-signed/)
- [Verifica se il progetto VBA è protetto e bloccato per la visualizzazione](/cells/it/net/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Copia il DesignerStorage del modulo utente VBA Macro dal modello al foglio di lavoro di destinazione](/cells/it/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Firma digitalmente un progetto di codice VBA con un certificato](/cells/it/net/digitally-sign-a-vba-code-project-with-certificate/)
- [Esporta il certificato VBA su file o flusso](/cells/it/net/export-vba-certificate-to-file-or-stream/)
- [Filtra il progetto VBA durante il caricamento di un libro di lavoro](/cells/it/net/filter-vba-project-while-loading-a-workbook/)
- [Scopri se il progetto VBA è protetto](/cells/it/net/find-out-if-vba-project-is-protected/)
- [Proteggi con password il progetto VBA del foglio di lavoro Excel](/cells/it/net/password-protect-the-vba-project-of-excel-workbook/)

{{< app/cells/assistant language="csharp" >}}
