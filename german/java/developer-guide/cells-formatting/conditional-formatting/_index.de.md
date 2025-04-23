---
title: Bedingte Formatierung
type: docs
weight: 120
url: /de/java/conditional-formatting/
---

{{% alert color="primary" %}} 

Bedingte Formatierung ist ein erweitertes Feature von Microsoft Excel, das es Ihnen ermöglicht, Formate auf eine Zelle oder einen Zellenbereich anzuwenden und dieses Format je nach Wert der Zelle oder des Wertes einer Formel zu ändern. Beispielsweise kann eine Zelle nur fett erscheinen, wenn der Wert der Zelle größer als 500 ist. Wenn der Wert der Zelle die Bedingung erfüllt, wird das angegebene Format auf die Zelle angewendet. Wenn der Wert der Zelle die Bedingung nicht erfüllt, wird das Standardformat verwendet. In Microsoft Excel wählen Sie **Format** und dann **Bedingte Formatierung**, um den Dialog für die bedingte Formatierung zu öffnen.

**Bedingte Formatierung in Microsoft Excel** 

![todo:image_alt_text](conditional-formatting_1.png)

Aspose.Cells unterstützt das Anwenden von bedingten Formatierungen auf Zellen zur Laufzeit. Dieser Artikel erklärt, wie das funktioniert.

{{% /alert %}} 
## **Anwendung von bedingten Formaten**
Aspose.Cells unterstützt bedingte Formatierungen auf zwei Arten:

- [Verwendung einer Designer-Tabelle](/cells/de/java/conditional-formatting/).
- [Erstellung der bedingten Formatierung zur Laufzeit](/cells/de/java/conditional-formatting/).
### **Verwenden der Designer-Tabelle**
Entwickler können eine Designer-Tabelle erstellen, die bedingte Formatierungen in Microsoft Excel enthält, und dann diese Tabelle mit Aspose.Cells öffnen. Aspose.Cells lädt und speichert die Designer-Tabelle und behält dabei die Einstellungen für bedingte Formatierungen bei. Weitere Informationen zu Designer-Tabellen finden Sie unter [Was ist eine Designer-Tabelle](/cells/de/java/what-is-a-designer-spreadsheet/).
## **Bedingte Formatierung zur Laufzeit anwenden**
Aspose.Cells unterstützt das Anwenden von bedingten Formatierungen zur Laufzeit.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ConditionalFormattingatRuntime-ConditionalFormattingatRuntime.java" >}}
### **Schriftart festlegen**
**Schriftarten festlegen in Microsoft Excel** 

![todo:image_alt_text](conditional-formatting_2.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SettingFontStyle-SettingFontStyle.java" >}}
### **Rahmen festlegen**
**Festlegen von Rahmen in Microsoft Excel** 

![todo:image_alt_text](conditional-formatting_3.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetBorder-SetBorder.java" >}}
### **Muster festlegen**
**Festlegen eines Zellenmusters in Microsoft Excel** 

![todo:image_alt_text](conditional-formatting_4.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-SetPattern-SetPattern.java" >}}

## **Erweiterte Themen**
- [Hinzufügen eines bedingten Symbolsets mit dem Zelltext](/cells/de/java/add-conditional-icons-set-with-the-cell-text/)
- [Hinzufügen von 2-Farben-Skalen und 3-Farben-Skalen bedingter Formatierungen](/cells/de/java/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [Bedingte Formatierung in Arbeitsblättern anwenden](/cells/de/java/apply-conditional-formatting-in-worksheets/)
- [Abwechselnde Zeilen und Spalten mit bedingter Formatierung schattieren](/cells/de/java/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)

{{< app/cells/assistant language="java" >}}
