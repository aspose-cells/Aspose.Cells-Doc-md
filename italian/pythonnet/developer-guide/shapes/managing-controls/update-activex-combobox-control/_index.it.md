---
title: Aggiorna il controllo ComboBox ActiveX
type: docs
weight: 170
url: /it/python-net/update-activex-combobox-control/
---

## **Possibili Scenari di Utilizzo**
Puoi leggere o scrivere i valori del controllo ComboBox ActiveX usando Aspose.Cells per Python via .NET. Accedi al controllo ActiveX tramite la proprietà [Shape.active_x_control](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/active_x_control) e verifica il suo tipo tramite la proprietà [ActiveXControl.type](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/activexcontrolbase/type/), che dovrebbe restituire il valore [ControlType.COMBO_BOX](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/controltype) e poi castarlo in un oggetto [ComboBoxActiveXControl](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/comboboxactivexcontrol) per leggere o modificare le sue varie proprietà.

Si prega di scaricare il [file Excel di esempio](5115124.xlsx) utilizzato nel seguente codice di esempio.
## **Aggiorna il controllo ComboBox ActiveX**
Lo screenshot seguente mostra l'effetto del codice di esempio sul [file Excel di esempio](5115124.xlsx). Come si può vedere, il valore del ComboBox ActiveX è stato aggiornato a "Questo è un controllo combobox".

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **Codice di Esempio**
Il seguente codice di esempio aggiorna il valore del controllo ActiveX ComboBox presente all'interno del [file Excel di esempio](5115124.xlsx).



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-UpdateActiveXComboBoxControl.py" >}}
{{< app/cells/assistant language="python-net" >}}
