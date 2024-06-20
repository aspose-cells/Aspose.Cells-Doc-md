---
title: Zeilen und Spalten schützen
type: docs
weight: 60
url: /de/net/aspose-cells-gridweb/protect-rows-and-columns/
keywords: GridWeb schützen
description: Dieser Artikel erklärt, wie man Zeilen und Spalten in GridWeb schützt.
---

{{% alert color="primary" %}} 

In diesem Thema werden einige Techniken zum Schützen von Zellen in Zeilen und Spalten vor von Endbenutzern durchgeführten Aktionen erörtert. Entwickler können diesen Schutz mithilfe von zwei Techniken implementieren: indem sie Zellen in Zeilen und Spalten schreibgeschützt machen oder indem sie die Kontextmenüoptionen des Aspose.Cells.GridWeb einschränken. Beide Techniken werden im Folgenden anhand von Beispielen erläutert.

{{% /alert %}} 
## **Schützen von Zellen in Zeilen & Spalten**
### **Machen von Zeilen & Spalten schreibgeschützt**
Ein Weg, um Zeilen und Spalten in einem Arbeitsblatt zu schützen, besteht darin, die Zellen schreibgeschützt zu machen. Dann können sie nicht von Endbenutzern gelöscht werden.

Um Zeilen und Spalten schreibgeschützt zu machen:

1. Fügen Sie der Webformularsteuerung Aspose.Cells.GridWeb hinzu.
1. Greifen Sie auf das GridWorksheet in der Sammlung zu.
1. Setzen Sie Ihre gewünschten Zellen in Zeilen oder Spalten auf schreibgeschützt.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-MakeRowsColumnsReadOnly.aspx-MakeCellReadOnly.cs" >}}
### **Einschränkung von Kontextmenüoptionen**
Aspose.Cells.GridWeb bietet ein Kontextmenü, das Endbenutzer zur Durchführung von Operationen auf dem Steuerelement verwenden können. Das Menü bietet viele Optionen zum Bearbeiten von Zellen, Zeilen und Spalten.

**Vollständige Kontextmenüoptionen** 

![todo:image_alt_text](protect-rows-and-columns_1.png)

Es ist möglich, jegliche Art von clientseitigen Operationen auf Zeilen und Spalten zu beschränken, indem die verfügbaren Optionen im Kontextmenü eingeschränkt werden. Dies kann erfolgen, indem die Eigenschaften EnableClientColumnOperations und EnableClientRowOperations des GridWeb-Steuerelements auf false gesetzt werden. Es ist auch möglich, Benutzer daran zu hindern, Zeilen und Spalten durch Setzen der Eigenschaft EnableClientFreeze des GridWeb-Steuerelements auf false einzufrieren.

**Kontextmenü nach Beschränkung der Zeilen- & Spaltenoptionen** 

![todo:image_alt_text](protect-rows-and-columns_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-RestrictContextMenu.aspx-RestrictContextMenu.cs" >}}
