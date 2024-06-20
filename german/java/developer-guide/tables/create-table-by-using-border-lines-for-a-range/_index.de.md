---
title: Tabelle erstellen und dabei Bereich mithilfe von Rahmenlinien
type: docs
weight: 50
url: /de/java/create-table-by-using-border-lines-for-a-range/
description: So erstellen Sie eine Tabelle mit einem Bereich mithilfe von Rahmenlinien. Aspose.Cells for Java bietet eine einfach zu verwendende API, mit der Sie Rahmen zu einem Bereich hinzufügen können.
keywords: Tabelle erstellen, Bereich in Tabelle, Bereich in Tabelle Excel, Excel Bereich in Tabelle, Bereich in Tabelle mit Rahmen, wie man eine Tabelle aus einem Bereich erstellt, Bereich in Tabelle konvertieren, Excel Bereich in Tabelle konvertieren, Excel Tabelle erstellen, Bereich in Tabelle Java 
---

{{% alert color="primary" %}}

Manchmal möchten Sie eine Tabelle erstellen, indem Sie Rahmenlinien für einen **Bereich**/**Zellbereich** basierend auf der Adresse der Zellen hinzufügen. Sie können die Methode [**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange(int,%20int,%20boolean)) verwenden, um einen Zellenbereich zu erstellen. Die Methode [**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange(int,%20int,%20boolean)) gibt ein [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range)-Objekt zurück. Sie können ein [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style)-Objekt erstellen und die Optionen für Rahmen (oben, links, unten, rechts) entsprechend festlegen. Später können Sie die Zellen des [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) erhalten und Ihr gewünschtes Format auf die Zellen anwenden.

{{% /alert %}}

Das folgende Beispiel zeigt, wie eine [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) erstellt und die Rahmenlinien für die Bereichszellen festgelegt werden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateTableforRange-CreateTableforRange.java" >}}

Nach Ausführen des obigen Codes wird die generierte Excel-Datei mit der formatierten Tabelle erstellt; hier ist ein Screenshot der Datei.

![todo:image_alt_text](create-table-by-using-border-lines-for-a-range_1.png)
