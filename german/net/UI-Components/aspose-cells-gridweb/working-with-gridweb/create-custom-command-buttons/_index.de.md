---
title: Erstellen benutzerdefinierter Befehlsschaltflächen
type: docs
weight: 100
url: /de/net/aspose-cells-gridweb/create-custom-command-buttons/
keywords: GridWeb, Befehl, Befehlsschaltflächen, benutzerdefiniert
description: Dieser Artikel zeigt, wie benutzerdefinierte Befehlsschaltflächen in GridWeb erstellt werden.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb enthält spezielle Schaltflächen wie **Senden**, **Speichern** und **Rückgängig machen**. All diese Schaltflächen führen spezifische Aufgaben für Aspose.Cells.GridWeb aus.
Es ist auch möglich, benutzerdefinierte Schaltflächen hinzuzufügen, die benutzerdefinierte Aufgaben ausführen. In diesem Artikel wird erläutert, wie diese Funktion verwendet wird.

{{% /alert %}} 
## **Erstellen von benutzerdefinierten Befehlsschaltflächen**
Um eine benutzerdefinierte Befehlsschaltfläche in Aspose.Cells.GridWeb zu erstellen:

1. Fügen Sie dem Webformular das Aspose.Cells.GridWeb-Steuerelement hinzu.
1. Greifen Sie auf ein Arbeitsblatt zu.
1. Erstellen Sie eine Instanz der Klasse CustomCommandButton.
1. Legen Sie den Befehl der Schaltfläche auf einen bestimmten Wert fest. Dieser Wert wird im Ereignishandler der Schaltfläche verwendet.
1. Legen Sie den Text der Schaltfläche fest.
1. Legen Sie die URL des Schaltflächenbilds fest.
1. Fügen Sie schließlich das Objekt CustomCommandButton zur CustomCommandButtons-Sammlung des GridWeb-Steuerelements hinzu.

{{% alert color="primary" %}} 

Benutzerdefinierte Befehlsschaltflächen können auch im WYSIWYG-Modus über das Eigenschaftenfenster von Visual Studio hinzugefügt werden.

{{% /alert %}} 

Die Ausgabe des Code-Snippets wird unten angezeigt:

**Eine benutzerdefinierte Befehlsschaltfläche wurde zum GridWeb-Steuerelement hinzugefügt** 

![todo:image_alt_text](create-custom-command-buttons_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitCustomCommandButton.aspx-InitCustomCommandButton.cs" >}}
### **Eventbehandlung der benutzerdefinierten Befehlsschaltfläche**
Der wichtigste Aspekt von benutzerdefinierten Befehlsschaltflächen ist die Aktion, die sie ausführen, wenn darauf geklickt wird. Um die Aktion einzustellen, erstellen Sie einen Ereignishandler für das CustomCommand-Ereignis des GridWeb-Steuerelements.

Das CustomCommand-Ereignis wird immer ausgelöst, wenn auf eine benutzerdefinierte Befehlsschaltfläche geklickt wird. Der Ereignishandler muss also die spezifische benutzerdefinierte Befehlsschaltfläche identifizieren, auf die er sich bezieht, indem der Befehl beim Hinzufügen der Schaltfläche zum GridWeb-Steuerelement festgelegt wird. Fügen Sie schließlich benutzerdefinierten Code hinzu, der ausgeführt wird, wenn auf die Schaltfläche geklickt wird.

Im nachfolgenden Codebeispiel wird eine Textnachricht der Zelle A1 hinzugefügt, wenn die Schaltfläche geklickt wird.

**Text zur Zelle A1 hinzugefügt, wenn benutzerdefinierte Schaltfläche geklickt wird** 

![todo:image_alt_text](create-custom-command-buttons_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleCustomCommandEvent.aspx-HandleCustomCommandEvent.cs" >}}
