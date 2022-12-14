---
title: Suchen und Ersetzen in GridWeb
type: docs
weight: 90
url: /de/net/search-and-replace-in-gridweb/
---
{{% alert color="primary" %}} 

Eine der schnellsten Möglichkeiten, sich wiederholende Änderungen in einer großen Tabelle vorzunehmen, ist die Verwendung der Funktion „Suchen und Ersetzen“. Suchen hilft Ihnen, eine Textzeichenfolge oder Daten zu finden und sie durch einen neuen Wert zu ersetzen. Aspose.Cells. GridWeb bietet diese Funktion. Es ermöglicht Ihnen das Suchen und Ersetzen durch eine bestimmte Textzeichenfolge oder einen bestimmten Wert auf der Arbeitsblatt-Client-Seite über einen einfachen Dialog. Sie können sogar nach Teildaten suchen.

{{% /alert %}} 
## **Arbeiten mit Suchen/Ersetzen**
### **Der Dialog Suchen/Ersetzen**
Es gibt zwei Möglichkeiten, das Dialogfeld „Suchen/Ersetzen“ zu öffnen:

1.  Wenn die Steuerung aktiv ist, drücken Sie**STRG+F** um das Dialogfeld zu öffnen, oder drücken Sie**STRG+R** Taste, um den Dialog mit der zu öffnen**Ersetzen** Schaltfläche aktiviert.
1.  Bewegen Sie den Cursor auf den Zellenbereich im Arbeitsblatt und klicken Sie dann mit der rechten Maustaste. Auswählen**Finden** oder**Ersetzen** aus dem Menü.

   **Auswählen von Suchen** 

![todo: Bild_alt_Text](search-and-replace-in-gridweb_1.png)




 Ein Stildialog wird angezeigt.

**Der Dialog Suchen/Ersetzen** 

![todo: Bild_alt_Text](search-and-replace-in-gridweb_2.png)
### **Verwenden von Suchen**
Suchen:

1. Öffnen Sie das Dialogfeld „Suchen/Ersetzen“.
1.  Geben Sie die Zeichenfolge ein, nach der Sie suchen möchten**Finde was** aufstellen.
1.  Klicken**Nächstes finden** suchen.

Die nächste Zelle, die Ihrer Suchbedingung entspricht, wird hervorgehoben.

{{% alert color="primary" %}} 

Wenn Ihr Suchkriterium nicht gefunden wird, wird ein Dialog angezeigt, der Sie darüber informiert.

{{% /alert %}} 
### **Suchoptionen**
Es gibt einige Suchoptionen, die Sie im Dialogfeld anpassen können. Die folgende Tabelle listet sie auf.

|**Nein.** |**Optionsname** |**Beschreibung** |
|:- |:- |:- |
|1 | Streichholzschachtel| Gibt an, ob bei der Suche zwischen Groß- und Kleinschreibung unterschieden werden soll.|
|2 | Ganzes Wort abgleichen| Gibt an, ob bei der Suche nach ganzen Wörtern gesucht werden soll.|
|3 | Nachschlagen|Gibt an, ob die Suche von unten nach oben durchgeführt wird.|
|4 | Regulären Ausdruck| Wenn diese Option aktiviert ist, behandelt das Steuerelement die Zeichenfolge im Textfeld Suchen nach als regulären Ausdruck im Suchprozess.|
|5 | Suchen Sie in Formeln/Werte| Wenn Formeln ausgewählt ist, stimmt das Steuerelement mit der Formel oder dem unformatierten Wert der Zellen überein, wenn die Formel oder der unformatierte Wert vorhanden ist. Wenn die Werte ausgewählt sind, stimmt das Steuerelement nur mit dem angezeigten Wert der Zellen überein.|
### **Verwendung von Ersetzen**
So ersetzen Sie Text oder Werte:

1.  Öffnen Sie das Dialogfeld „Suchen/Ersetzen“, indem Sie auf drücken**STRG+F** , oder wählen Sie aus, klicken Sie mit der rechten Maustaste auf eine Zelle, und wählen Sie sie aus**Finden** vor dem Klicken**Ersetzen**.
1.  Geben Sie die Ersetzungszeichenfolge in die ein**Ersetzen mit** aufstellen.
1.  Klicken**Ersetzen**.

So ersetzen Sie Text:

1. Öffnen Sie das Dialogfeld.
1.  Geben Sie den gesuchten Text ein**Finde was** Feld und den Text, durch den Sie es ersetzen möchten, im**Ersetzen mit** aufstellen.
1.  Ersetzen Sie jeweils ein Vorkommen, indem Sie auf klicken**Nächstes finden** gefolgt von**Ersetzen**.
1.  Wenn Sie sich sehr sicher sind, was das Arbeitsblatt enthält, klicken Sie auf**Alles ersetzen**.

{{% alert color="primary" %}} 

 Wenn sich das Arbeitsblatt nicht im Bearbeitungsmodus befindet, wird die**Ersetzen** Schaltfläche wird nicht angezeigt.

{{% /alert %}}
