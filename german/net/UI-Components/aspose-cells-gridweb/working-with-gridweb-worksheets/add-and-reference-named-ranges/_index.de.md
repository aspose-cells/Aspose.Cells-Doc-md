---
title: Benannte Bereiche hinzufügen und referenzieren
type: docs
weight: 120
url: /de/net/add-and-reference-named-ranges/
---
{{% alert color="primary" %}} 

 Normalerweise werden Spalten- und Zeilenbeschriftungen verwendet, um eindeutig auf Zellen zu verweisen. Sie können jedoch aussagekräftige Namen erstellen, um Zellen, Zellbereiche, Formeln oder konstante Werte darzustellen. Das Wort**Name**kann sich auf eine Zeichenfolge beziehen, die eine Zelle, einen Zellbereich, eine Formel oder einen konstanten Wert darstellt. Verwenden Sie beispielsweise leicht verständliche Namen wie Produkte, um auf schwer verständliche Bereiche wie Sales!C20:C30 zu verweisen. Beschriftungen können in Formeln verwendet werden, die auf Daten auf demselben Arbeitsblatt verweisen; Wenn Sie einen Bereich auf einem anderen Arbeitsblatt darstellen möchten, können Sie einen Namen verwenden.**Benannte Bereiche** ist eine der leistungsstärksten Funktionen von Microsoft Excel. Benutzer können einem Bereich einen Namen zuweisen und diesen Namen in Formeln verwenden. Aspose.Cells. GridWeb unterstützt diese Funktion.

{{% /alert %}} 
## **Benannte Bereiche in Formeln hinzufügen/referenzieren**
Das GridWeb-Steuerelement stellt zwei Klassen (GridName und GridNameCollection) zum Arbeiten mit benannten Bereichen bereit. Das folgende Code-Snippet hilft Ihnen zu verstehen, wie Sie den benannten Bereich erstellen und in den Formeln darauf zugreifen.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AccessNamedRanges.aspx-AddNamedRange.cs" >}}
