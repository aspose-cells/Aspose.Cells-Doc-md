---
title: Benannte Bereiche verwenden
type: docs
weight: 110
url: /de/net/using-named-ranges/
---
{{% alert color="primary" %}} 

 Normalerweise verwenden Sie die Beschriftungen von Spalten und Zeilen auf einem Arbeitsblatt, um auf die Zellen in diesen Spalten und Zeilen zu verweisen. Sie können jedoch aussagekräftige Namen erstellen, um Zellen, Zellbereiche, Formeln oder konstante Werte darzustellen. Das Wort**Name**kann sich auf eine Zeichenfolge beziehen, die eine Zelle, einen Zellbereich, eine Formel oder einen konstanten Wert darstellt. Verwenden Sie beispielsweise leicht verständliche Namen wie Produkte, um auf schwer verständliche Bereiche zu verweisen, wie z. B. Sales!C20:C30, um eine Zelle, einen Zellbereich, eine Formel oder einen konstanten Wert darzustellen. Beschriftungen können in Formeln verwendet werden, die auf Daten auf demselben Arbeitsblatt verweisen; Wenn Sie einen Bereich auf einem anderen Arbeitsblatt darstellen möchten, können Sie einen Namen verwenden.**Benannte Bereiche** gehören zu den leistungsstärksten Funktionen von Microsoft. Benutzer können einem benannten Bereich einen Namen zuweisen, sodass auf diesen Zellbereich mit seinem Namen in den Formeln verwiesen werden kann.**Aspose.Cells.GridDesktop** unterstützt diese Funktion.

{{% /alert %}} 
## **Benannte Bereiche in Formeln hinzufügen/referenzieren**
Das GridDesktop-Steuerelement unterstützt den Import/Export benannter Bereiche in Excel-Dateien, es bietet zwei Klassen (**Name** und**Namenssammlung**), um mit benannten Bereichen zu arbeiten.

Das folgende Code-Snippet hilft Ihnen bei der Verwendung.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingNamedRanges-1.cs" >}}
