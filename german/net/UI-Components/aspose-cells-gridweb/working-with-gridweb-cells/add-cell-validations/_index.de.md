---
title: Cell Validierungen hinzufügen
type: docs
weight: 70
url: /de/net/add-cell-validations/
---
{{% alert color="primary" %}} 

Eine der erweiterten Funktionen von Aspose.Cells.GridWeb ist das Hinzufügen von Eingabevalidierungsregeln für Zellen. Entwickler können verschiedene Arten von Validierungsregeln für Zellen erstellen, um Eingabewerte zu steuern und zu validieren. In diesem Thema werden die unterstützten Validierungstypen und ihre Erstellung erläutert.

{{% /alert %}} 
## **Arten von Validierungen**
Mit Aspose.Cells.GridWeb können drei Arten von Validierungen angewendet werden:

- Listenvalidierung.
- Dropdown-Listenvalidierung.
- Validierung benutzerdefinierter Ausdrücke.

Jede wird unten im Detail besprochen.
### **Listenvalidierung**
Die Listenvalidierung ermöglicht es Benutzern, Zelleneingaben bereitzustellen, indem sie entweder einen Wert eingeben oder einen Wert aus einem Menü auswählen. So erstellen Sie eine Listenvalidierung für eine Zelle:

1. Fügen Sie einem Webformular das Aspose.Cells.GridWeb-Steuerelement hinzu.
1. Greifen Sie auf ein Arbeitsblatt zu.
1. Greifen Sie auf die Zelle zu, der eine Validierung hinzugefügt werden soll.
1. Erstellen Sie die Validierung für die Zelle und geben Sie den Validierungstyp als Liste an.
1. Fügen Sie Werte für die Listenvalidierung hinzu.

Der Beispielcode fügt C1 eine Listenvalidierung hinzu. Wenn ein Benutzer auf die Zelle klickt, wird eine Liste angezeigt.

**Ausgabe: Auswahl eines Wertes aus der Liste** 

![todo: Bild_alt_Text](add-cell-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddListValidation.aspx-AddListValidation.cs" >}}
### **Dropdown-Listenvalidierung**
Die Dropdown-Listenvalidierung ermöglicht es Benutzern, Eingaben für Zellen bereitzustellen, indem sie einen Wert aus einer vordefinierten Liste auswählen. So erstellen Sie eine Dropdown-Listenvalidierung:

1. Fügen Sie einem Webformular das Aspose.Cells.GridWeb-Steuerelement hinzu.
1. Greifen Sie auf ein Arbeitsblatt zu.
1. Greifen Sie auf die Zelle zu, für die die Validierung erstellt werden soll.
1. Erstellen Sie eine Validierung für die Zelle und geben Sie den Typ als DropDownList an.
1. Fügen Sie Werte für die Validierung hinzu.

Der Beispielcode fügt C1 eine Dropdown-Listenvalidierung hinzu. Wenn ein Benutzer auf die Zelle klickt, wird ein Dropdown-Menü angezeigt, aus dem Benutzer einen Wert auswählen können.

**Auswahl eines Werts aus einem Dropdown-Menü** 

![todo: Bild_alt_Text](add-cell-validations_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDropdownListValidation.aspx-AddDropDownListValidation.cs" >}}
### **Benutzerdefinierte Ausdrucksvalidierung**
Die Validierung benutzerdefinierter Ausdrücke ermöglicht es Entwicklern, ihre eigenen benutzerdefinierten regulären Ausdrücke zu schreiben, um Eingabewerte zu validieren. So erstellen Sie eine benutzerdefinierte Ausdrucksvalidierung:

1. Fügen Sie einem Webformular das Aspose.Cells.GridWeb-Steuerelement hinzu.
1. Greifen Sie auf ein Arbeitsblatt zu.
1. Greifen Sie auf die Zelle zu, für die Sie eine Validierung erstellen möchten.
1. Erstellen Sie eine Validierung für die Zelle und geben Sie den Typ als CustomExpression an.
1. Legen Sie den regulären Ausdruck der Validierung fest.

Der Beispielcode fügt C1 eine benutzerdefinierte Ausdrucksvalidierung hinzu. Benutzer können nur gemäß dem durch den regulären Ausdruck angegebenen Format ein Datum in die Zelle einfügen.

**Hinzufügen eines Datumswerts zu C1 gemäß einem regulären Ausdruck** 

![todo: Bild_alt_Text](add-cell-validations_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddCustomValidation.aspx-AddCustomValidation.cs" >}}
### **Validierung erzwingen**
Mit Aspose.Cells.GridWeb können Benutzer Eingabedaten an einen Server senden. Selbst wenn Validierungsregeln für verschiedene Zellen vorhanden sind, die ForceValidation-Eigenschaft des GridWeb-Steuerelements jedoch nicht auf „true“ festgelegt ist, werden auch falsche Eingabedaten an den Server gesendet, und es wird keine Validierung erzwungen. Die ForceValidation-Eigenschaft von GridWeb ist standardmäßig immer auf true festgelegt.

 Wenn die ForceValidation-Eigenschaft wahr ist, sendet das Steuerelement keine Daten an den Webserver, bis die Eingabewerte aller Zellen gültig sind. Wenn beispielsweise jemand einen ungültigen Eingabewert in eine Zelle eingibt oder keinen Wert eingibt, wird die clientseitige Validierung aktiviert und die Benutzer können keine Daten posten, selbst wenn sie darauf klicken**Einreichen**.

**Falscher Eingabewert von GridWeb hervorgehoben** 

![todo: Bild_alt_Text](add-cell-validations_4.png)
