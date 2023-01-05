---
title: Initialisierungsparameter anpassen
type: docs
weight: 10
url: /de/net/aspose-cells-gridweb/customize-parameters-in-client-side-script/
description: wie man die Initialisierungsparameter im clientseitigen Skript Aspose.Cells.GridWeb anpasst.
---
{{% alert color="primary" %}} 

 Entwickler können einen anderen Initialisierungsparameterwert festlegen, um ein anderes Verhalten für das Aspose.Cells.GridWeb-Steuerelement in acwmain.js auszuführen.

{{% /alert %}} 
 
### **Parameter**
 
|**Parameter**|**Beschreibung**|
|:- |:- |
|needInitAlignmentAdjust|Ob eine vertikale Ausrichtung für den Zelleninhalt bei der Initialisierung durchgeführt werden soll, es wird einige Zeit dauern, die Ausrichtungsarbeit durchzuführen, wenn das Arbeitsblatt große Zellen hat, wird die Leistung schlecht sein, wenn der Benutzer die vertikale Ausrichtung nicht interessiert, dann kann er es einstellen falsch sein, der Standardwert ist wahr|
|Fokus nach innen| Ob innerhalb der Zellspanne fokussiert werden soll, der Standardwert ist wahr|
|Kopieren_mit_Stil|Ob mit Stil kopiert werden soll, der Standardwert ist falsch, was bedeutet, dass nur der Zelleninhalt kopiert wird|
|Verwenden Sie ESCAsLeave|Das Standardverhalten beim Drücken von Esc funktioniert als Bearbeitungsvorgang für die Zelle abbrechen. Wenn wir diesen Wert auf „true“ setzen, behandeln wir ihn nur als kurze Taste, um die Zelle zu verlassen, ohne zum vorherigen Wert zurückzukehren, und es ändert auch die innere Bearbeitungsmethode Um schnell zu bearbeiten, ist der Standardwert falsch|
|NeedValidateall|ob alle Validierungen auf dem aktiven Blatt validiert werden sollen, wenn die Validierung durchgeführt wird, (in aspx control page set ForceValidation="True") . der Standardwert ist falsch|
|scrollToInvalidate|ob gescrollt und die erste ungültig gemachte Zelle angezeigt werden soll, wenn needValidateall auf true gesetzt ist. Der Standardwert ist true.|
 
 
 Die Ausgabe des Codebeispiels ist unten dargestellt,Bitte überprüfen Sie die[Excel-Beispieldatei](valign.xlsx):

**needInitAlignmentAdjust=true** 

![todo: Bild_alt_Text](align_true.png)

**needInitAlignmentAdjust=false** 

![todo: Bild_alt_Text](align_false.png)

**focusinside=true** 
 Innerhalb der Bearbeitungsmethode - Wenn Sie Text eingeben, bleibt der alte Zellenwert erhalten

![todo: Bild_alt_Text](focus_inside_true.png)

**focusinside=false** 
schnelle Bearbeitungsmethode - Wenn Sie Text eingeben, wird der alte Zellenwert überschrieben. Wenn Sie basierend auf dem alten Zellenwert bearbeiten möchten, können Sie auf die Zelle klicken

![todo: Bild_alt_Text](focus_inside_false.png)

 
 