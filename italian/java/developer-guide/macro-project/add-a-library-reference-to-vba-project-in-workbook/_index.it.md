---
title: Aggiungi un riferimento alla libreria al progetto VBA nella cartella di lavoro
type: docs
weight: 10
url: /it/java/add-a-library-reference-to-vba-project-in-workbook/
---
{{% alert color="primary" %}}

 In Microsoft Excel è possibile aggiungere un riferimento alla libreria al progetto VBA facendo clic su**Strumenti > Riferimenti...** manualmente. Si aprirà la seguente finestra di dialogo che ti aiuterà a selezionare dai riferimenti esistenti o a sfogliare la tua libreria da solo.

![cose da fare:immagine_alt_testo](add-a-library-reference-to-vba-project-in-workbook_1.png)

 Ma a volte è necessario aggiungere o registrare il riferimento della libreria al progetto VBA tramite codice. Puoi farlo utilizzando lo Aspose.Cells[**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)) metodo.

{{% /alert %}}

## **Aggiungi un riferimento alla libreria al progetto VBA nella cartella di lavoro**

 Il codice di esempio seguente aggiunge o registra due riferimenti di libreria al progetto VBA della cartella di lavoro che utilizza[**VbaProject.getReferences().addRegisteredReference()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaprojectreferencecollection#addRegisteredReference(java.lang.String,%20java.lang.String)) metodo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddLibraryReference-AddLibraryReference.java" >}}
