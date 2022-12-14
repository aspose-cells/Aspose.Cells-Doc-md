---
title: Aggiungi controlli ActiveX utilizzando Aspose.Cells
type: docs
weight: 720
url: /it/java/add-activex-controls-using-aspose-cells/
---
{{% alert color="primary" %}} 

 È possibile aggiungere controlli ActiveX con Aspose.Cells utilizzando il file[ShapeCollection.addActiveXControl()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addActiveXControl\(int,%20int,%20int,%20int,%20int,%20int,%20int\) ) metodo. Questo metodo accetta un parametro[Tipo di controllo](https://reference.aspose.com/cells/java/com.aspose.cells/ControlType)che indica quale tipo di controllo ActiveX deve essere aggiunto all'interno di un foglio di lavoro. Ha i seguenti valori.

- [CHECK_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#CHECK_BOX)
- [COMBO BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO_BOX)
- [PULSANTE DI COMANDO](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMMAND_BUTTON)
- [IMMAGINE](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#IMAGE)
- [ETICHETTA](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LABEL)
- [LISTA_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LIST_BOX)
- [PULSANTE_RADIO](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#RADIO_BUTTON)
- [BARRA DI SCORRIMENTO](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SCROLL_BAR)
- [SPIN_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SPIN_BUTTON)
- [CASELLA DI TESTO](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TEXT_BOX)
- [INTERRUTTORE](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TOGGLE_BUTTON)
- [SCONOSCIUTO](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#UNKNOWN)

 Dopo aver aggiunto il controllo ActiveX all'interno della raccolta delle forme, è possibile accedere all'oggetto del controllo ActiveX tramite[Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl) property e quindi impostarne le varie proprietà.

{{% /alert %}} 
## **Aggiungi il controllo ActiveX del pulsante di commutazione utilizzando Aspose.Cells**
 Il seguente codice di esempio aggiunge Toggle Button ActiveX Control utilizzando Aspose.Cells. Scaricare il file[file excel di output](5473427.xlsx) generato con questo codice come riferimento.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddActiveXControl-AddActiveXControl.java" >}}
