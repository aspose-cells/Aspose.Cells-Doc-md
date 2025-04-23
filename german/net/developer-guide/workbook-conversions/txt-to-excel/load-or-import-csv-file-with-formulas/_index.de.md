---
title: Laden oder Importieren von CSV Dateien mit Formeln
type: docs
weight: 350
url: /de/net/load-or-import-csv-file-with-formulas/
---

{{% alert color="primary" %}} 

CSV-Dateien enthalten in der Regel Textdaten und keine Formeln. Manchmal kommt es jedoch vor, dass CSV-Dateien auch Formeln enthalten. Solche CSV-Dateien sollten geladen werden, indem die Eigenschaft [TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/hasformula) auf **true** gesetzt wird. Sobald diese Eigenschaft auf **true** gesetzt ist, behandelt Aspose.Cells die Formel nicht als einfachen Text. Sie werden als Formel behandelt und von Aspose.Cells Formelberechnungsmaschine wie gewöhnlich verarbeitet.

{{% /alert %}} 

Der folgende Code zeigt, wie Sie eine CSV-Datei mit Formeln laden und importieren können. Sie können jede CSV-Datei verwenden. Zu Veranschaulichungszwecken verwenden wir die [einfache CSV-Datei](5115034.csv), die diese Daten enthält. Wie Sie sehen, enthält sie eine Formel.

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ImportCSVWithFormulas-ImportCSVWithFormulas.cs" >}}



Der Code lädt zunächst die CSV-Datei, importiert sie dann erneut in die Zelle D4. Schließlich speichert er das Arbeitsmap-Objekt im XSLX-Format. Die [Ausgabe-XLSX-Datei](5115052.xlsx) sieht so aus. Wie Sie sehen, enthalten die Zelle C3 und F4 eine Formel und ihr Ergebnis 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |

{{< app/cells/assistant language="csharp" >}}
