---
title: Matrixbericht erstellen
type: docs
weight: 10
url: /de/reportingservices/creating-matrix-report/
---
{{% alert color="primary" %}} 

 Mit Aspose.Cells for Reporting Services können Sie eine Matrix in Microsoft Excel entwerfen.

{{% /alert %}} 
### **Matrix-Vorlage**
In einer Aspose.Cells-Berichtsvorlage besteht eine Matrix aus Ecken, Zeilengruppen, Spaltengruppen und Datenteilen. Eine Beispielmatrix ist unten gezeigt.

**Eine Probenmatrix** 

![todo: Bild_alt_Text](creating-matrix-report_1.png)

- **Matrix-Ecke**: befindet sich in der oberen linken Ecke oder in der oberen rechten Ecke für von rechts nach links (RTL) Layouts. Dieser Bereich wird automatisch erstellt, wenn Sie einem Matrixdatenbereich sowohl Zeilengruppen als auch Spaltengruppen hinzufügen. In diesem Bereich können Sie eingebettete Textfeld-Berichtselemente in Zellen zusammenführen.
- **Bereich Matrixspaltengruppen**befindet sich in der oberen rechten Ecke (obere linke Ecke für RTL-Layout). Dieser Bereich wird automatisch erstellt, wenn Sie eine Spaltengruppe hinzufügen. Die Zellen in diesem Bereich stellen Mitglieder der Spaltengruppenhierarchie dar und zeigen die Instanzwerte der Spaltengruppe an. In der Abbildung sind die Zellen, die OrderYear anzeigen, eine verschachtelte Spaltengruppe, und die Zelle, die OrderQtr anzeigt, ist eine benachbarte Spaltengruppe.
- **Bereich Matrixzeilengruppen**: befindet sich in der unteren linken Ecke (unten rechts für RTL-Layout). Dieser Bereich wird automatisch erstellt, wenn Sie eine Zeilengruppe hinzufügen. Die Zellen in diesem Bereich stellen Mitglieder der Zeilengruppenhierarchie dar und zeigen Zeilengruppeninstanzwerte an. In der Abbildung sind diese Zellen verschachtelte Zeilengruppen.
- **Matrixdatenbereich**befindet sich in der unteren rechten Ecke (unten links für RTL-Layout). Die Matrixdaten zeigen detaillierte und gruppierte Daten an. In diesem Beispiel werden nur aggregierte Daten verwendet. Standardmäßig werden die Zellen in einer Gruppenzeile oder -spalte, die einfache Ausdrücke enthalten, die keine Aggregatfunktion enthalten, mit dem ersten Wert in der Gruppe ausgewertet. In der Abbildung zeigen die Zellen die aggregierten Summen für die Zeilensummen für alle Verkaufsaufträge.
#### **Erstellen einer Matrixvorlage**
 Erstellen Sie vor dem Erstellen eines Matrixberichts die Datenquellen, Datensätze und Berichtsparameter (optional). (Folgen Sie den Anweisungen in[Datenquellen und Abfragen](/cells/de/reportingservices/data-sources-and-queries/) falls Sie Hilfe benötigen.) Im Beispiel verwenden wir die AdventureWorks-Beispieldatenbank, die im Lieferumfang von SQL Server Reporting Services 2008 enthalten ist.

So erstellen Sie eine neue Matrix:

1. Öffnen Sie Microsoft Excel.
1.  Klicken**Bericht öffnen** , um eine RDL-Berichtsdatei zu öffnen, die die im Voraus erstellten Datenquellen, Datensätze und Berichtsparameter enthält.
Sobald die Datei erfolgreich geöffnet wurde, stehen alle ihre Informationen zur Verwendung zur Verfügung, beispielsweise werden ihre Datensätze in der aufgelistet**Datensatz** aufführen.
1.  Öffnen Sie ein Microsoft Excel-Arbeitsblatt und wählen Sie einen Datensatz aus.

![todo: Bild_alt_Text](creating-matrix-report_2.png)




1.  Setzen Sie Zeilengruppen und Spaltengruppen durch**Gruppe festlegen**. 

![todo: Bild_alt_Text](creating-matrix-report_3.png)




1. Verbinden Sie Zellen, um die Matrixecke festzulegen.

![todo: Bild_alt_Text](creating-matrix-report_4.png)




1.  Matrixecke durch Einfügen einer Formel setzen.

![todo: Bild_alt_Text](creating-matrix-report_5.png)




![todo: Bild_alt_Text](creating-matrix-report_6.png)




1.  Klicken**Attribut festlegen** um das Matrixattribut zu setzen.

![todo: Bild_alt_Text](creating-matrix-report_7.png)



Es besteht aus Name, Bereich, Gruppe und Reihenfolge.

1. Durch Klicken auf Attribut ändern werden alle Matrixattribute des aktuellen Arbeitsblatts überprüft und geändert.

![todo: Bild_alt_Text](creating-matrix-report_8.png)




1. Bericht speichern, veröffentlichen und überprüfen.
