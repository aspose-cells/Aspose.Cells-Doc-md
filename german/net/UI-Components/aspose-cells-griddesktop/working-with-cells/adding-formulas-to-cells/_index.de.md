---
title: Formeln zu Cells hinzufügen
type: docs
weight: 30
url: /de/net/adding-formulas-to-cells/
---
{{% alert color="primary" %}} 

Eine Zelle kann nicht nur einen einfachen Wert wie eine Zahl oder einen Text enthalten, sondern wir können auch eine Formel als Wert in eine Zelle einfügen. Eine Formel wird in einer Zelle verwendet, wenn der Wert einer Zelle nach einigen Berechnungen bestimmt werden muss. In diesem Thema werden wir erörtern, wie wir auf eine Formel zugreifen und diese ändern können, die auf eine Zelle angewendet wird.

{{% /alert %}} 
## **Formel zu Cell hinzufügen**
 Das Hinzufügen einer Formel zu einer Zelle ist genauso wie das Festlegen des Werts einer Zelle, wie wir in unserem vorherigen Thema besprochen haben:[Zugreifen auf und Ändern des Werts einer Cell](/cells/de/net/accessing-and-modifying-the-value-of-a-cell/) außer dass wir in diesem Fall nur einfache Werte zu Zellen hinzugefügt haben. Jetzt werden wir Formeln hinzufügen. Entwickler können die Value-Eigenschaft einer Zelle verwenden, um auf die Formel zuzugreifen und sie zu ändern oder auf andere Weise**SetCellValue** Methode der Zelle kann auch verwendet werden, um die Formel in einer Zelle hinzuzufügen oder zu ändern.

**WICHTIG:** Der grundlegende Unterschied zwischen der Verwendung der Value-Eigenschaft oder**SetCellValue** Methode einer Zelle ist die Value-Eigenschaft, die aufgerufen wird**RunAllFormulas** Methode von Grid automatisch die Werte aller Formeln neu zu berechnen, wo wie im Fall von**SetCellValue** Methodenentwickler müssen anrufen**RunAllFormulas** -Methode explizit, nachdem die Formeln zu Zellen hinzugefügt wurden. Eigentlich, wenn wir verwenden**SetCellValue** Methode einer Zelle, dann setzt diese Methode den Wert der Zelle auf**Formeltyp** nur und berechnen Sie nicht die Formel. Außerdem anrufen**RunAllFormulas**Methode jedes Mal ist nicht erforderlich. Wenn Sie viele Formeln in die Zellen eines Arbeitsblatts einfügen möchten, können Sie anrufen**RunAllFormulas** Methode nur einmal am Ende.

 Eine Formel wird einer Zelle als Zeichenfolgewert hinzugefügt. Außerdem muss die Formelstruktur mit der Formelstruktur von MS Excel kompatibel sein. Alle Formeln müssen mit einem beginnen**Gleichheitszeichen (=)**.

 In dem unten angegebenen Beispiel haben wir eine Formel hinzugefügt, um die Werte von zwei Zellen des Arbeitsblatts zu multiplizieren und das Ergebnis in einer anderen Zelle zu speichern.**RunAllFormulas** -Methode wird ebenfalls am Ende aufgerufen.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddingCellFormulas-1.cs" >}}



Führen Sie nun die Anwendung aus. Wenn Sie auf die Zelle doppelklicken, in der die Formel hinzugefügt wurde, werden Sie feststellen, dass der Wert durch die Formel ersetzt wird, die den Wert tatsächlich im Backend berechnet.

{{% alert color="primary" %}} 

 Aspose.Cells.GridDesktop unterstützt die meisten häufig verwendeten Funktionen von MS Excel. Weitere Einzelheiten zur Liste der unterstützten Funktionen finden Sie unter[klicken Sie hier.](/cells/de/net/list-of-supported-functions/)

{{% /alert %}}
