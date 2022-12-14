---
title: Gestisci i codici VBA della cartella di lavoro con attivazione macro di Excel.
linktitle: Progetto Macro
type: docs
weight: 200
url: /it/net/manage-vba-project/
description: Aggiungi modulo VBA e modifica VBA o macro con la libreria Aspose.Cells.
---
## **Aggiungi un modulo VBA in C#**
{{% alert color="primary" %}}

 Aspose.Cells consente di aggiungere un nuovo modulo VBA e codice macro utilizzando Aspose.Cells. Utilizzare il[**Cartella di lavoro.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/add/index) metodo per aggiungere il nuovo modulo VBA all'interno della cartella di lavoro

{{% /alert %}}

Il seguente codice di esempio crea una nuova cartella di lavoro e aggiunge un nuovo modulo VBA e codice macro e salva l'output nel formato XLSM. Una volta, aprirai il file XLSM di output in Microsoft Excel e fai clic su**Sviluppatore > Visual Basic** comandi di menu, vedrai un modulo chiamato "TestModule" e al suo interno vedrai il seguente codice macro.

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Ecco il codice di esempio per generare il file XLSM di output con il modulo VBA e il codice macro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AddVBAModuleOrCode-AddVBAModuleOrCode.cs" >}}

## **Modifica VBA o Macro in C#**

{{% alert color="primary" %}} 

È possibile modificare VBA o codice macro utilizzando Aspose.Cells. Aspose.Cells ha aggiunto il seguente spazio dei nomi e classi per leggere e modificare il progetto VBA nel file Excel.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- Modulo Vba

Questo articolo ti mostrerà come modificare il VBA o il codice macro all'interno del file Excel di origine utilizzando Aspose.Cells.

{{% /alert %}} 

Il seguente codice di esempio carica il file Excel di origine che contiene un codice VBA o macro seguente

{{< highlight "java" >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

Dopo l'esecuzione del codice di esempio Aspose.Cells, il codice VBA o Macro verrà modificato in questo modo

{{< highlight "java" >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

 Puoi scaricare il[file Excel di origine](5112508.xlsm) e il[file Excel di output](5112511.xlsm) dai link indicati.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-ModifyingVBAOrMacroCode-ModifyingVBAOrMacroCode.cs" >}}

## **Argomenti avanzati**
- [Aggiungi un riferimento alla libreria al progetto VBA nella cartella di lavoro](/cells/it/net/add-a-library-reference-to-vba-project-in-workbook/)
- [Assegna macro al controllo del modulo](/cells/it/net/assign-macro-to-form-control/)
- [Controlla se la firma digitale del codice VBA è valida](/cells/it/net/check-if-digital-signature-of-vba-code-is-valid/)
- [Controlla se il codice VBA è firmato](/cells/it/net/check-if-vba-code-is-signed/)
- [Controlla se il progetto VBA in una cartella di lavoro è firmato](/cells/it/net/check-if-vba-project-in-a-workbook-is-signed/)
- [Controlla se il progetto VBA è protetto e bloccato per la visualizzazione](/cells/it/net/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Copia VBA Macro UserForm DesignerStorage dal modello alla cartella di lavoro di destinazione](/cells/it/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Firma digitalmente un progetto di codice VBA con certificato](/cells/it/net/digitally-sign-a-vba-code-project-with-certificate/)
- [Esporta certificato VBA su file o stream](/cells/it/net/export-vba-certificate-to-file-or-stream/)
- [Filtra il progetto VBA durante il caricamento di una cartella di lavoro](/cells/it/net/filter-vba-project-while-loading-a-workbook/)
- [Scopri se il progetto VBA è protetto](/cells/it/net/find-out-if-vba-project-is-protected/)
- [Proteggi con password il progetto VBA della cartella di lavoro di Excel](/cells/it/net/password-protect-the-vba-project-of-excel-workbook/)

