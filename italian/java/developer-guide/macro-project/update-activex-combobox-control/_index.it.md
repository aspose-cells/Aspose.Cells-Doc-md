---
title: Aggiorna il controllo ComboBox ActiveX
type: docs
weight: 900
url: /it/java/update-activex-combobox-control/
---

## **Possibili Scenari di Utilizzo**
È possibile leggere o scrivere i valori del controllo ComboBox ActiveX utilizzando Aspose.Cells. Si prega di accedere al Controllo ActiveX tramite la proprietà [Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl) e controllarne il tipo tramite la proprietà [ActiveXControl.Type](https://reference.aspose.com/cells/java/com.aspose.cells/activexcontrol#Type), dovrebbe restituire il valore [ControlType.ComboBox](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO_BOX) e quindi fare il cast in [ComboBoxActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/ComboBoxActiveXControl) per leggere o modificare le sue varie proprietà.

Si prega di scaricare il [file Excel di esempio](5473374.xlsx) utilizzato nel seguente codice di esempio e il [file Excel di output](5473375.xlsx) generato da esso.
## **Aggiorna il controllo ComboBox ActiveX**
Lo screenshot seguente mostra l'effetto del codice di esempio sul [file Excel di esempio](5473374.xlsx). Come si può vedere, il valore del ComboBox ActiveX è stato aggiornato a "This is combo box control".

![todo:image_alt_text](update-activex-combobox-control_1.png)
## **Codice di Esempio**
Il seguente codice di esempio aggiorna il valore del controllo ComboBox ActiveX presente nel [file Excel di esempio](5473374.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UpdateActiveXComboBoxControl-UpdateActiveXComboBoxControl.java" >}}
