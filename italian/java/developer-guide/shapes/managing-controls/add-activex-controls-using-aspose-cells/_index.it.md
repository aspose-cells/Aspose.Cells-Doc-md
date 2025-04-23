---
title: Aggiungi controlli ActiveX usando Aspose.Cells
type: docs
weight: 720
url: /it/java/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}} 

Puoi aggiungere controlli ActiveX con Aspose.Cells usando il metodo [ShapeCollection.addActiveXControl()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addActiveXControl-int-int-int-int-int-int-int-). Questo metodo accetta un parametro [ControlType](https://reference.aspose.com/cells/java/com.aspose.cells/ControlType) che indica quale tipo di controllo ActiveX deve essere aggiunto all'interno di un foglio di lavoro. Ha i seguenti valori.

- [CHECK_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#CHECK-BOX)
- [COMBO_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO-BOX)
- [COMMAND_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMMAND-BUTTON)
- [IMAGE](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#IMAGE)
- [LABEL](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LABEL)
- [LIST_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LIST-BOX)
- [RADIO_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#RADIO-BUTTON)
- [SCROLL_BAR](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SCROLL-BAR)
- [PULSANTE_DI_SCORRIMENTO](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SPIN-BUTTON)
- [CASSETTA_DEGLI_STRUMENTI_DI_TESTO](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TEXT-BOX)
- [PULSANTE_DI_ATTIVAZIONE](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TOGGLE-BUTTON)
- [Sconosciuto](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#UNKNOWN)

Una volta aggiunto il controllo ActiveX all'interno della raccolta di forme, è possibile accedere all'oggetto controllo ActiveX tramite la proprietà [Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl) e impostarne le varie proprietà.

{{% /alert %}} 
## **Aggiungi il controllo ActiveX del pulsante di attivazione utilizzando Aspose.Cells**
Il seguente codice di esempio aggiunge il controllo ActiveX del pulsante di attivazione utilizzando Aspose.Cells. Si prega di scaricare il [file Excel di output](5473427.xlsx) generato con questo codice per il vostro riferimento.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddActiveXControl-AddActiveXControl.java" >}}
{{< app/cells/assistant language="java" >}}
