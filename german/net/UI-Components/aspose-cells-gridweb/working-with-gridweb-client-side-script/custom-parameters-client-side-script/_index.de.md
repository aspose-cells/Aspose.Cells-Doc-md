---
title: Anpassen von Initialisierungsparametern
type: docs
weight: 10
url: /de/net/aspose-cells-gridweb/customize-parameters-in-client-side-script/
keywords: GridWeb,anpassen,Anpassen von Parametern
description: Wie man Initialisierungsparameter in Aspose.Cells.GridWeb Client Seitenskript anpasst.
---

{{% alert color="primary" %}} 

Entwickler können unterschiedliche Initialisierungsparameterwerte setzen, um unterschiedliches Verhalten für die Aspose.Cells.GridWeb-Steuerung in acwmain.js auszuführen.  

{{% /alert %}} 

### **Parameter**

|**Parameter**|**Beschreibung**|
| :- | :- |
|needInitAlignmentAdjust| ob die vertikale Ausrichtung für Zelleninhalt bei der Initialisierung erfolgen soll, es dauert einige Zeit, um die Ausrichtungsarbeit durchzuführen, wenn das Arbeitsblatt große Zellen hat, wird die Leistung schlecht sein, wenn der Benutzer sich nicht um die vertikale Ausrichtung kümmert, dann kann er sie auf false setzen, der Standardwert ist true |
|focusinside| ob der Fokus im Zellbereich liegen soll, der Standardwert ist true |
|copy_with_style| ob mit Stil kopiert werden soll, der Standardwert ist false, was bedeutet, dass nur der Zelleninhalt kopiert wird|
|useESCAsLeave| das Standardverhalten beim Drücken von Esc funktioniert wie der Vorgang zum Bearbeiten in der Zelle abbrechen, wenn wir diesen Wert auf true setzen, behandeln wir es nur als eine Kurztaste zum Verlassen der Zelle, ohne zum vorherigen Wert zurückzukehren, und es ändert auch die Art des inneren Bearbeitungswegs in den Schnellbearbeitungsweg, der Standardwert ist false|
|needValidateall| ob bei Validierung alle Validierungen auf dem aktiven Blatt durchgeführt werden sollen, wenn die Validierung durchgeführt wird, (in der aspx-Steuerungsseite ForceValidation="True" gesetzt ist). der Standardwert ist false|
|scrollToInvalidate| ob beim Setzen von needValidateall auf true gescrollt und die erste ungültige Zelle ins Blickfeld gebracht werden soll. der Standardwert ist true.|


Die Ausgabe des Codebeispiels wird unten angezeigt. Bitte überprüfen Sie die [Beispieldatei](valign.xlsx):

**needInitAlignmentAdjust=true** 

![todo:image_alt_text](align_true.png)

**needInitAlignmentAdjust=false** 

![todo:image_alt_text](align_false.png)

**focusinside=true** 
Inside-Edit-Weg - Wenn Sie Text eingeben, wird der alte Zellenwert beibehalten.   

![todo:image_alt_text](focus_inside_true.png)

**focusinside=false** 
Schneller Bearbeitungsweg - Wenn Sie Text eingeben, wird der alte Zellenwert überschrieben. Wenn Sie basierend auf dem alten Zellenwert bearbeiten möchten, können Sie auf die Zelle klicken.

![todo:image_alt_text](focus_inside_false.png)



