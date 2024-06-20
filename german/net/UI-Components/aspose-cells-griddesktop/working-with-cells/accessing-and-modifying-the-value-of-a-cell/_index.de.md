---
title: Zugriff und Änderung des Werts einer Zelle
type: docs
weight: 20
url: /de/net/aspose-cells-griddesktop/accessing-and-modifying-the-value-of-a-cell/
keywords: GridDesktop,cell,modify cell,get cell,modify cell value,get cell value
description: Dieser Artikel zeigt, wie der Zellwert in einem GridDesktop abgerufen und geändert werden kann.
---

{{% alert color="primary" %}} 

In unserem vorherigen Thema haben wir darüber gesprochen, auf Zellen eines Arbeitsblatts zuzugreifen. In diesem Thema erweitern wir einfach dieses Thema, um Entwicklern zu zeigen, wie sie die Werte von Zellen mithilfe der API von Aspose.Cells.GridDesktop abrufen und ändern können.

{{% /alert %}} 
## **Zugriff und Änderung des Zellwerts mithilfe von Aspose.Cells.GridDesktop**
Bevor Sie den Wert einer Zelle abrufen und ändern, sollten Sie wissen, wie Sie auf Zellen zugreifen können. Es gibt drei Ansätze, um auf Zellen eines Arbeitsblatts zuzugreifen. Weitere Details zu diesen drei Ansätzen finden Sie unter [Zugriff auf Zellen in einem Arbeitsblatt.](/cells/de/net/zugriff-auf-zellen-in-einem-arbeitsblatt/)

Jede Zelle hat eine Eigenschaft namens Wert. Sobald eine Zelle abgerufen wurde, können Entwickler auf die Inhalte der Wert-Eigenschaft zugreifen und diese ändern, um den Wert einer Zelle abzurufen und zu ändern.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingValue.cs" >}}


**WICHTIG:** Die Verwendung der Wert-Eigenschaft einer Zelle zur Änderung ihres Werts ist ein guter Ansatz, um den Wert einer einzelnen oder weniger Zellen festzulegen. Wenn Sie die Werte vieler Zellen setzen müssen, ist die Leistung dieses Ansatzes jedoch nicht gut. Um die Werte vieler Zellen zu setzen, sollten Sie die **SetCellValue**-Methode der Zelle verwenden, um die Leistung Ihrer Anwendungen zu verbessern. Eine modifizierte Version des obigen Code-Snippets unter Verwendung der **SetCellValue**-Methode wird unten angezeigt.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingSetCellValue.cs" >}}
