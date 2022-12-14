---
title: Zeilen und Spalten schützen
type: docs
weight: 60
url: /de/net/protect-rows-and-columns/
---
{{% alert color="primary" %}} 

In diesem Thema werden einige Techniken zum Schützen von Zellen in Zeilen und Spalten vor jeder Art von Aktion erläutert, die von Endbenutzern ausgeführt wird. Entwickler können diesen Schutz mit zwei Techniken implementieren: indem sie Zellen in Zeilen und Spalten schreibgeschützt machen oder indem sie die Kontextmenüoptionen von Aspose.Cells.GridWeb einschränken. Beide Techniken werden im Folgenden anhand von Beispielen diskutiert.

{{% /alert %}} 
## **Schützen von Cells in Zeilen und Spalten**
### **Zeilen und Spalten schreibgeschützt machen**
Eine Möglichkeit, Zeilen und Spalten in einem Arbeitsblatt zu schützen, besteht darin, die Zellen schreibgeschützt zu machen. Dann können sie von Endbenutzern nicht gelöscht werden.

So machen Sie Zeilen und Spalten schreibgeschützt:

1. Fügen Sie einem Webformular das Aspose.Cells.GridWeb-Steuerelement hinzu.
1. Greifen Sie auf das GridWorksheet in der Sammlung zu.
1. Setzen Sie Ihre gewünschten Zellen in Zeilen oder Spalten auf schreibgeschützt.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-MakeRowsColumnsReadOnly.aspx-MakeCellReadOnly.cs" >}}
### **Einschränken der Kontextmenüoptionen**
Aspose.Cells.GridWeb bietet ein Kontextmenü, das Endbenutzer verwenden können, um Vorgänge auf dem Steuerelement auszuführen. Das Menü bietet viele Optionen zum Bearbeiten von Zellen, Zeilen und Spalten.

**Vollständige kontextbezogene Optionen** 

![todo: Bild_alt_Text](protect-rows-and-columns_1.png)

Es ist möglich, jede Art von clientseitigen Operationen auf Zeilen und Spalten einzuschränken, indem Sie die im Kontextmenü verfügbaren Optionen einschränken. Dies kann durch Festlegen der Eigenschaften EnableClientColumnOperations und EnableClientRowOperations des GridWeb-Steuerelements auf false erfolgen. Es ist auch möglich, Benutzer daran zu hindern, Zeilen und Spalten einzufrieren, indem Sie die EnableClientFreeze-Eigenschaft des GridWeb-Steuerelements auf „false“ festlegen.

**Kontextmenü nach dem Einschränken der Zeilen- und Spaltenoptionen** 

![todo: Bild_alt_Text](protect-rows-and-columns_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-RestrictContextMenu.aspx-RestrictContextMenu.cs" >}}
