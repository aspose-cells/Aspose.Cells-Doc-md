---
title: Erstellen Sie benutzerdefinierte Befehlsschaltflächen
type: docs
weight: 100
url: /de/net/create-custom-command-buttons/
---
{{% alert color="primary" %}} 

 Aspose.Cells.GridWeb enthält spezielle Schaltflächen wie**einreichen**, **Speichern** und**Rückgängig machen**. Alle diese Schaltflächen führen bestimmte Aufgaben für Aspose.Cells.GridWeb aus.
Es ist auch möglich, benutzerdefinierte Schaltflächen hinzuzufügen, die benutzerdefinierte Aufgaben ausführen. In diesem Thema wird die Verwendung dieser Funktion erläutert.

{{% /alert %}} 
## **Erstellen von benutzerdefinierten Befehlsschaltflächen**
So erstellen Sie eine benutzerdefinierte Befehlsschaltfläche in Aspose.Cells.GridWeb:

1. Fügen Sie dem Webformular das Aspose.Cells.GridWeb-Steuerelement hinzu.
1. Greifen Sie auf ein Arbeitsblatt zu.
1. Erstellen Sie eine Instanz der CustomCommandButton-Klasse.
1. Setzen Sie den Befehl der Schaltfläche auf einen Wert. Dieser Wert wird im Ereignishandler der Schaltfläche verwendet.
1. Legen Sie den Text der Schaltfläche fest.
1. Legen Sie die Bild-URL der Schaltfläche fest.
1. Fügen Sie schließlich das CustomCommandButton-Objekt der CustomCommandButtons-Auflistung des GridWeb-Steuerelements hinzu.

{{% alert color="primary" %}} 

Benutzerdefinierte Befehlsschaltflächen können auch im WYSIWYG-Modus mithilfe des Eigenschaftendialogfelds von Visual Studio hinzugefügt werden.

{{% /alert %}} 

Die Ausgabe des Code-Snippets ist unten dargestellt:

**Eine benutzerdefinierte Befehlsschaltfläche, die dem GridWeb-Steuerelement hinzugefügt wurde** 

![todo: Bild_alt_Text](create-custom-command-buttons_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitCustomCommandButton.aspx-InitCustomCommandButton.cs" >}}
### **Ereignisbehandlung der benutzerdefinierten Befehlsschaltfläche**
Der wichtigste Aspekt benutzerdefinierter Befehlsschaltflächen ist die Aktion, die sie ausführen, wenn sie angeklickt wird. Erstellen Sie zum Festlegen der Aktion einen Ereignishandler für das CustomCommand-Ereignis des GridWeb-Steuerelements.

Das CustomCommand-Ereignis wird immer ausgelöst, wenn auf eine benutzerdefinierte Befehlsschaltfläche geklickt wird. Daher muss der Ereignishandler die spezifische benutzerdefinierte Befehlsschaltfläche identifizieren, auf die er durch den Befehlssatz angewendet wird, wenn die Schaltfläche dem GridWeb-Steuerelement hinzugefügt wird. Fügen Sie schließlich benutzerdefinierten Code hinzu, der ausgeführt wird, wenn auf die Schaltfläche geklickt wird.

Im folgenden Codebeispiel wird der Zelle A1 eine Textnachricht hinzugefügt, wenn auf die Schaltfläche geklickt wird.

**Text, der der A1-Zelle hinzugefügt wird, wenn auf eine benutzerdefinierte Befehlsschaltfläche geklickt wird** 

![todo: Bild_alt_Text](create-custom-command-buttons_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleCustomCommandEvent.aspx-HandleCustomCommandEvent.cs" >}}
