---
title: Zugreifen auf und Ändern des Werts von Cell
type: docs
weight: 20
url: /de/net/accessing-and-modifying-the-value-of-a-cell/
---
{{% alert color="primary" %}} 

In unserem vorherigen Thema haben wir über den Zugriff auf Zellen eines Arbeitsblatts gesprochen. In diesem Thema erweitern wir dieses Thema einfach, um Entwicklern zu zeigen, wie sie mithilfe von API von Aspose.Cells.GridDesktop auf die Werte von Zellen zugreifen und diese ändern können.

{{% /alert %}} 
## **Greifen Sie mit Aspose.Cells.GridDesktop auf den Wert Cell zu und ändern Sie ihn**
 Bevor wir auf den Wert einer Zelle zugreifen und ihn ändern, sollten wir wissen, wie man auf Zellen zugreift. Es gibt drei Ansätze, um auf Zellen eines Arbeitsblatts zuzugreifen. Weitere Einzelheiten zu diesen drei Ansätzen finden Sie hier[Zugriff auf Cells in einem Arbeitsblatt.](/cells/de/net/accessing-cells-in-a-worksheet/)

Jede Zelle hat eine Eigenschaft namens Value . Sobald also auf eine Zelle zugegriffen wird, können Entwickler auf den Inhalt der Value-Eigenschaft zugreifen und diesen ändern, um auf den Wert einer Zelle zuzugreifen und ihn zu ändern.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingValue.cs" >}}


**WICHTIG:**Die Verwendung der Value-Eigenschaft einer Zelle zum Ändern ihres Werts ist ein guter Ansatz, um den Wert einer einzelnen oder weniger Zellen festzulegen. Wenn Sie die Werte vieler Zellen festlegen müssen, wäre die Leistung dieses Ansatzes nicht gut. Um also die Werte vieler Zellen festzulegen, sollten Sie verwenden**SetCellValue** Methode der Zelle zur Leistungssteigerung Ihrer Anwendungen. Eine modifizierte Version des obigen Code-Snippets mit**SetCellValue** Methode ist unten gezeigt.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingSetCellValue.cs" >}}
