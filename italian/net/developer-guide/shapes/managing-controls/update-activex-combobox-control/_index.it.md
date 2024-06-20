---
title: Aggiorna il controllo ComboBox ActiveX
type: docs
weight: 170
url: /it/net/update-activex-combobox-control/
---

## **Possibili Scenari di Utilizzo**
È possibile leggere o scrivere i valori del controllo ActiveX ComboBox utilizzando Aspose.Cells. Accedere al controllo ActiveX tramite la proprietà [Shape.ActiveXControl](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol) e controllare il suo tipo tramite la proprietà [ActiveXControl.Type](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/activexcontrolbase/properties/type) , dovrebbe restituire il valore [ControlType.ComboBox](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/controltype) e quindi fare il casting in un oggetto [ComboBoxActiveXControl](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/comboboxactivexcontrol) e leggere o modificare le sue varie proprietà.

Si prega di scaricare il [file Excel di esempio](5115124.xlsx) utilizzato nel seguente codice di esempio.
## **Aggiorna il controllo ComboBox ActiveX**
Lo screenshot seguente mostra l'effetto del codice di esempio sul [file Excel di esempio](5115124.xlsx). Come si può vedere, il valore del ComboBox ActiveX è stato aggiornato a "Questo è un controllo combobox".

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **Codice di Esempio**
Il seguente codice di esempio aggiorna il valore del controllo ActiveX ComboBox presente all'interno del [file Excel di esempio](5115124.xlsx).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateActiveXComboBoxControl-UpdateActiveXComboBoxControl.cs" >}}
