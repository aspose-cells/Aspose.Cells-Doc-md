---
title: Wenden Sie die bedingte Formatierung im Arbeitsblatt an
type: docs
weight: 40
url: /de/cpp/apply-conditional-formatting-in-worksheet/
---
## **Mögliches Nutzungsszenario**
 Aspose.Cells ermöglicht es Ihnen, alle Arten von bedingter Formatierung hinzuzufügen, z. B. Formel, Überdurchschnittlich, Farbskala, Datenleiste, Symbolsatz, Top10 usw. Es bietet die[IFormatCondition](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition)Klasse, die über alle notwendigen Methoden verfügt, um eine bedingte Formatierung Ihrer Wahl anzuwenden. Hier ist die Liste einiger Get-Methoden.

- [GetIAoverAverage()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#aff550fd834cd78967ec440492ff012d5)
- [GetIColorScale()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a3348a7c447dc564ceabc22c9c89bd6f5)
- [GetIDataBar()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a4415a87833c41386ed1595e742485e07)
- [GetIIconSet()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a011b2c7dbaaf671819d09f5d1df865e3)
- [GetITop10()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a64388aaf1b43811f5ee1ee3090c9bd4a)
## **Wenden Sie die bedingte Formatierung im Arbeitsblatt an**
 Der folgende Beispielcode zeigt, wie eine bedingte Formatierung Cell Wert in den Zellen A1 und B2 hinzugefügt wird. Bitte sehen Sie sich ... an[Excel-Datei ausgeben](23167004.xlsx) generiert durch den Code und den folgenden Screenshot, der die Wirkung des Codes auf die erklärt[Excel-Datei ausgeben](23167004.xlsx). Wenn Sie in Zelle A2 und B2 einen Wert größer als 100 eingeben, verschwindet die rote Füllfarbe aus Zelle A1 und B2.

![todo: Bild_alt_Text](apply-conditional-formatting-in-worksheet_1.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ApplyConditionalFormattingInWorksheet.cpp" >}}
