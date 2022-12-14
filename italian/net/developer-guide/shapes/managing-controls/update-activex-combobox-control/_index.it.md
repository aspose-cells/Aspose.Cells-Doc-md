---
title: Aggiorna controllo ComboBox ActiveX
type: docs
weight: 170
url: /it/net/update-activex-combobox-control/
---
## **Possibili scenari di utilizzo**
È possibile leggere o scrivere i valori del controllo ActiveX ComboBox utilizzando Aspose.Cells. Accedere al controllo ActiveX tramite[Shape.ActiveXControl](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/activexcontrol) property e controllarne il tipo tramite[ActiveXControl.Type](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/activexcontrolbase/properties/type) proprietà, dovrebbe tornare[ControlType.ComboBox](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/controltype) value e quindi digitarlo in[ComboBoxActiveXControl](https://reference.aspose.com/cells/net/aspose.cells.drawing.activexcontrols/comboboxactivexcontrol)oggetto e leggere o modificare le sue varie proprietà.

 Si prega di scaricare il[file excel di esempio](5115124.xlsx) utilizzato nel codice di esempio seguente.
## **Aggiorna controllo ComboBox ActiveX**
 Lo screenshot seguente mostra l'effetto del codice di esempio su[file excel di esempio](5115124.xlsx). Come puoi vedere, il valore di ActiveX ComboBox è stato aggiornato a "Questo è il controllo della casella combinata".

|![cose da fare:immagine_alt_testo](update-activex-combobox-control_1.png)|
|:- |
## **Codice di esempio**
 Il seguente codice di esempio aggiorna il valore del controllo ActiveX ComboBox presente all'interno di[file excel di esempio](5115124.xlsx).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateActiveXComboBoxControl-UpdateActiveXComboBoxControl.cs" >}}
