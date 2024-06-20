---
title: Formel zu Zelle hinzufügen
type: docs
weight: 30
url: /de/net/aspose-cells-griddesktop/adding-formula-to-cell/
keywords: GridDesktop, Formel
description: Dieser Artikel zeigt, wie man die Formel in der Zelle im Arbeitsblatt in GridDesktop erhält oder setzt.
---

{{% alert color="primary" %}} 

Eine Zelle kann nicht nur einen einfachen Wert wie eine numerische Figur oder einen Text enthalten, sondern auch eine Formel als ihren Wert. Eine Formel wird in einer Zelle verwendet, wenn der Wert der Zelle nach einigen Berechnungen bestimmt werden muss. In diesem Thema werden wir diskutieren, wie man auf eine eingefügte Formel zugreift und diese ändert.

{{% /alert %}} 
## **Formel zu einer Zelle hinzufügen**
Eine Formel zu einer Zelle hinzuzufügen ist ganz ähnlich wie den Wert einer Zelle festzulegen, wie wir es in unserem vorherigen Thema besprochen haben: [Zugriff und Änderung des Werts einer Zelle](/cells/de/net/zugriff-und-änderung-des-werts-einer-zelle/), mit der Ausnahme, dass in diesem Fall nur einfache Werte zu Zellen hinzugefügt wurden. Jetzt werden Formeln hinzugefügt. Entwickler können die Value-Eigenschaft einer Zelle verwenden, um auf die Formel zuzugreifen und diese zu ändern, oder alternativ kann auch die **SetCellValue** Methode der Zelle verwendet werden, um eine Formel in einer Zelle hinzuzufügen oder zu ändern.

**WICHTIG:** Der grundlegende Unterschied zwischen der Verwendung der Value-Eigenschaft oder der **SetCellValue** Methode einer Zelle besteht darin, dass die Value-Eigenschaft automatisch die **RunAllFormulas** Methode von Grid aufruft, um die Werte aller Formeln neu zu berechnen, während im Fall der **SetCellValue** Methode Entwickler die **RunAllFormulas** Methode explizit aufrufen müssen, nachdem die Formeln zu den Zellen hinzugefügt wurden. Tatsächlich setzt die **SetCellValue** Methode einer Zelle den Wert der Zelle nur auf **FormulaType** und berechnet die Formel nicht. Außerdem ist es nicht notwendig, die **RunAllFormulas** Methode jedes Mal aufzurufen. Wenn Sie viele Formeln zu den Zellen eines Arbeitsblatts hinzufügen möchten, können Sie die **RunAllFormulas** Methode am Ende nur einmal aufrufen.

Eine Formel wird als Zeichenfolgenwert zu einer Zelle hinzugefügt. Außerdem muss die Formelstruktur mit der Formelstruktur von MS Excel kompatibel sein. Alle Formeln müssen mit einem **Gleichheitszeichen (=)** beginnen.

Im untenstehenden Beispiel haben wir eine Formel hinzugefügt, um die Werte von zwei Zellen des Arbeitsblatts zu multiplizieren und das Ergebnis in eine andere Zelle zu speichern. Am Ende wird auch die Methode **RunAllFormulas** aufgerufen.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddingCellFormulas-1.cs" >}}



Führen Sie nun die Anwendung aus. Wenn Sie auf die Zelle doppelklicken, in der die Formel hinzugefügt wurde, stellen Sie fest, dass der Wert durch die Formel ersetzt wird, die tatsächlich den Wert im Hintergrund berechnet.

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop unterstützt die meisten der häufig verwendeten Funktionen von MS Excel. Für weitere Details zur Liste der unterstützten Funktionen klicken Sie bitte [hier](/cells/de/net/list-of-supported-functions/).

{{% /alert %}}
