---
title: Füge Zellvalidierungen hinzu
type: docs
weight: 70
url: /de/net/aspose-cells-gridweb/add-cell-validations/
keywords: GridWeb,GridValidierung,Listvalidation,benutzerdefinierte Ausdrucksvalidierung
description: Dieser Artikel zeigt, wie man Listvalidation, Dropdown Listvalidation und benutzerdefinierte Ausdrucksvalidierung in GridWeb hinzufügt.
---

{{% alert color="primary" %}} 

Eine der fortschrittlichen Funktionen von Aspose.Cells.GridWeb ist das Hinzufügen von Eingabevalidierungsregeln für Zellen. Entwickler können verschiedene Arten von Validierungsregeln für Zellen erstellen, um Eingabewerte zu kontrollieren und zu validieren. Dieses Thema behandelt die unterstützten Validierungstypen und wie man sie erstellt.

{{% /alert %}} 
## **Arten von Validierungen**
Drei Arten von Validierungen können unter Verwendung von Aspose.Cells.GridWeb angewendet werden:

- Listenvalidierung.
- Drop-down-Listenvalidierung.
- Benutzerdefinierte Ausdrucksvalidierung.

Jede wird unten im Detail diskutiert.
### **Listenvalidierung**
Die Listenvalidierung ermöglicht es Benutzern, Zelleneingaben entweder durch Eingabe oder Auswahl eines Werts aus einem Menü bereitzustellen. Um eine Listenvalidierung für eine Zelle zu erstellen:

1. Fügen Sie der Webformularsteuerung Aspose.Cells.GridWeb hinzu.
1. Greifen Sie auf ein Arbeitsblatt zu.
1. Zugriff auf die Zelle, um die Validierung hinzuzufügen.
1. Erstellen Sie die Validierung für die Zelle und geben Sie den Validierungstyp als Liste an.
1. Fügen Sie Werte für die Listenvalidierung hinzu.

Der Beispielcode fügt eine Listenvalidierung zu C1 hinzu. Wenn ein Benutzer auf die Zelle klickt, wird eine Liste angezeigt.

**Ausgabe: Auswahl eines Werts aus der Liste** 

![todo:image_alt_text](add-cell-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddListValidation.aspx-AddListValidation.cs" >}}
### **Drop-down-Listenvalidierung**
Die Drop-down-Listenvalidierung ermöglicht es Benutzern, Eingaben für Zellen zu liefern, indem sie einen Wert aus einer vordefinierten Liste auswählen. Um eine Drop-down-Listenvalidierung zu erstellen:

1. Fügen Sie der Webformularsteuerung Aspose.Cells.GridWeb hinzu.
1. Greifen Sie auf ein Arbeitsblatt zu.
1. Zugriff auf die Zelle, um die Validierung zu erstellen.
1. Erstellen Sie eine Validierung für die Zelle und geben Sie den Typ als DropDownList an.
1. Fügen Sie Werte für die Validierung hinzu.

Der Beispielcode fügt eine Drop-down-Listenvalidierung zu C1 hinzu. Wenn ein Benutzer auf die Zelle klickt, wird ein Dropdown-Menü angezeigt und Benutzer können einen Wert daraus auswählen.

**Auswahl eines Werts aus dem Dropdown-Menü** 

![todo:image_alt_text](add-cell-validations_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDropdownListValidation.aspx-AddDropDownListValidation.cs" >}}
### **Benutzerdefinierte Ausdrucksvalidierung**
Die benutzerdefinierte Ausdrucksvalidierung ermöglicht es Entwicklern, ihre eigenen benutzerdefinierten regulären Ausdrücke zu schreiben, um Eingabewerte zu validieren. Um eine benutzerdefinierte Ausdrucksvalidierung zu erstellen:

1. Fügen Sie der Webformularsteuerung Aspose.Cells.GridWeb hinzu.
1. Greifen Sie auf ein Arbeitsblatt zu.
1. Greifen Sie auf die Zelle zu, für die Sie eine Validierung erstellen möchten.
1. Erstellen Sie eine Validierung für die Zelle und geben Sie den Typ als Benutzerdefinierte Ausdruck an.
1. Legen Sie den regulären Ausdruck der Validierung fest.

Der Beispielcode fügt eine benutzerdefinierte Ausdrucksvalidierung zu C1 hinzu. Benutzer können nur ein Datum in die Zelle einfügen, das dem im regulären Ausdruck angegebenen Format entspricht.

**Hinzufügen eines Datums zum C1 gemäß einem regulären Ausdruck** 

![todo:image_alt_text](add-cell-validations_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddCustomValidation.aspx-AddCustomValidation.cs" >}}
### **Erzwingen der Validierung**
Mit Aspose.Cells.GridWeb können Benutzer Eingabedaten an einen Server senden. Auch wenn es Validierungsregeln für verschiedene Zellen gibt, aber die Eigenschaft ForceValidation des GridWeb-Steuerelements nicht auf true festgelegt ist, werden falsche Eingabedaten auch an den Server übermittelt und es wird keine Validierung erzwungen. Die Eigenschaft ForceValidation des GridWeb-Steuerelements ist standardmäßig immer auf true gesetzt.

Wenn die Eigenschaft ForceValidation true ist, sendet das Steuerelement keine Daten an den Webserver, bis die Eingabewerte aller Zellen gültig sind. Wenn z.B. jemand einen ungültigen Eingabewert in eine Zelle eingibt oder keinen Wert eingibt, wird die clientseitige Validierung aktiviert und die Benutzer können keine Daten senden, auch wenn sie auf **Senden** klicken.

**Falscher Eingabewert, hervorgehoben durch GridWeb** 

![todo:image_alt_text](add-cell-validations_4.png)
