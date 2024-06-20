---
title: Benannte Bereiche hinzufügen und referenzieren
type: docs
weight: 120
url: /de/net/aspose-cells-gridweb/add-and-reference-named-ranges/
keywords: GridWeb,GridName,Names
description: In diesem Artikel wird erläutert, wie mit benannten Bereichen in GridWeb gearbeitet wird. 
---

{{% alert color="primary" %}} 

Normalerweise werden Spalten- und Zeilenbeschriftungen verwendet, um eindeutig auf Zellen zu verweisen. Sie können jedoch beschreibende Namen erstellen, um Zellen, Zellenbereiche, Formeln oder Konstantenwerte zu repräsentieren. Das Wort **Name** kann eine Zeichenfolge darstellen, die eine Zelle, einen Zellenbereich, eine Formel oder einen Konstantenwert repräsentiert. Verwenden Sie beispielsweise leicht verständliche Namen wie 'Produkte', um auf schwer verständliche Bereiche wie 'Verkäufe!C20:C30' zu verweisen. Beschriftungen können in Formeln verwendet werden, die auf Daten im selben Arbeitsblatt verweisen; wenn Sie einen Bereich in einem anderen Arbeitsblatt darstellen möchten, können Sie einen Namen verwenden. **Benannte Bereiche** sind eine der leistungsstärksten Funktionen von Microsoft Excel. Benutzer können einem Bereich einen Namen zuweisen und diesen Namen in Formeln verwenden. Aspose.Cells.GridWeb unterstützt diese Funktion.

{{% /alert %}} 
## **Hinzufügen/Referenzierung benannter Bereiche in Formeln**
Die GridWeb-Steuerung bietet zwei Klassen (GridName und GridNameCollection) zur Arbeit mit benannten Bereichen. Der folgende Codeausschnitt wird Ihnen zeigen, wie Sie den benannten Bereich erstellen und in den Formeln darauf zugreifen können.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AccessNamedRanges.aspx-AddNamedRange.cs" >}}
