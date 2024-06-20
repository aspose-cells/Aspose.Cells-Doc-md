---
title: Suchen und Ersetzen in GridWeb
type: docs
weight: 90
url: /de/net/aspose-cells-gridweb/search-and-replace-in-gridweb/
keywords: GridWeb,Suchen,Ersetzen
description: In diesem Artikel wird erläutert, wie Sie in GridWeb suchen und ersetzen können.
---

{{% alert color="primary" %}} 

Einer der schnellsten Wege, wiederholte Änderungen in einer großen Tabellenkalkulation vorzunehmen, besteht darin, die Suchen-und-Ersetzen-Funktion zu verwenden. Die Suchfunktion hilft Ihnen dabei, einen Textstring oder Daten zu finden, und die Ersetzen-Funktion ersetzt diesen durch einen neuen Wert. Aspose.Cells.GridWeb bietet diese Funktion. Sie ermöglicht es Ihnen, clientseitig nach einem spezifischen Textstring oder Wert zu suchen und diesen durch einen einfachen Dialog zu ersetzen. Sie ermöglicht es Ihnen sogar, nach Teildaten zu suchen.

{{% /alert %}} 
## **Arbeiten mit Suchen/Ersetzen**
### **Der Suchen/Ersetzen-Dialog**
Es gibt zwei Möglichkeiten, den Suchen/Ersetzen-Dialog zu öffnen:

1. Wenn die Steuerung aktiv ist, drücken Sie **STRG+F**, um den Dialog zu öffnen, oder drücken Sie die **STRG+R**-Taste, um den Dialog mit der **Ersetzen**-Schaltfläche zu öffnen.
1. Bewegen Sie den Cursor in den Zellenbereich des Arbeitsblatts, dann klicken Sie mit der rechten Maustaste. Wählen Sie **Suchen** oder **Ersetzen** aus dem Menü. 

   **Auswählen von Suchen** 

![todo:image_alt_text](search-and-replace-in-gridweb_1.png)




Ein Stiledialog wird angezeigt. 

**Der Suchen/Ersetzen-Dialog** 

![todo:image_alt_text](search-and-replace-in-gridweb_2.png)
### **Suchen verwenden**
Um zu suchen:

1. Öffnen Sie den Suchen/Ersetzen-Dialog.
1. Geben Sie den String, den Sie suchen möchten, in das Feld **Suchen nach** ein.
1. Klicken Sie auf **Nächster suchen**, um zu suchen.

Die nächste Zelle, die Ihrer Suchbedingung entspricht, wird hervorgehoben.

{{% alert color="primary" %}} 

Wenn Ihr Suchkriterium nicht gefunden wird, wird ein Dialog angezeigt, um Sie zu informieren.

{{% /alert %}} 
### **Suchoptionen**
Es gibt einige Suchoptionen, die Sie im Dialog anpassen können. Die Tabelle unten listet sie auf.

|**Nr.** |**Optionsname** |**Beschreibung** |
| :- | :- | :- |
|1 |Groß-/Kleinschreibung beachten |Gibt an, ob die Suche auf Groß- und Kleinschreibung achtet. |
|2 |Ganze Wörter suchen |Gibt an, ob ganze Wörter bei der Suche berücksichtigt werden. |
|3 |Nach oben suchen |Gibt an, ob die Suche von unten nach oben durchgeführt wird. |
|4 |Regulärer Ausdruck |Wenn aktiviert, behandelt das Steuerelement den Text im Feld „Suchen nach“ als regulären Ausdruck im Suchvorgang. |
|5 |In Formeln/Werten suchen |Wenn „Formeln“ ausgewählt ist, prüft das Steuerelement die Formel oder den nicht formatierten Wert der Zellen, sofern die Formel oder der nicht formatierte Wert vorhanden ist. Wenn „Werte“ ausgewählt ist, prüft das Steuerelement nur den angezeigten Wert der Zellen. |
### **Verwenden von Ersetzen**
Zum Ersetzen von Text oder Werten:

1. Öffnen Sie das Dialogfeld „Suchen/Ersetzen“, indem Sie **STRG+F** drücken, oder klicken Sie mit der rechten Maustaste auf eine Zelle und wählen Sie **Suchen** aus, bevor Sie auf **Ersetzen** klicken.
1. Geben Sie den Ersetzungstext im Feld „Ersetzen durch“ ein.
1. Klicken Sie auf **Ersetzen**.

Um Text zu ersetzen:

1. Öffnen Sie das Dialogfeld.
1. Geben Sie den Text ein, den Sie im Feld „Suchen nach“ finden möchten, und den Text, durch den Sie ihn im Feld „Ersetzen durch“ ersetzen möchten.
1. Ersetzen Sie jeweils ein Vorkommen, indem Sie zuerst auf **Weitersuchen** und dann auf **Ersetzen** klicken.
1. Wenn Sie sehr sicher sind, was sich auf dem Arbeitsblatt befindet, klicken Sie auf **Alle ersetzen**.

{{% alert color="primary" %}} 

Wenn sich das Arbeitsblatt nicht im Bearbeitungsmodus befindet, wird die Schaltfläche „Ersetzen“ nicht angezeigt.

{{% /alert %}}
