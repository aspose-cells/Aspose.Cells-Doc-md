---
title: Matrixbericht erstellen
type: docs
weight: 10
url: /de/reportingservices/creating-matrix-report/
---

{{% alert color="primary" %}} 

Aspose.Cells for Reporting Services ermöglicht es Ihnen, eine Matrix in Microsoft Excel zu entwerfen. 

{{% /alert %}} 
### **Matrixvorlage**
In einem Aspose.Cells-Berichts-Template besteht eine Matrix aus Ecken, Zeilengruppen, Spaltengruppen und Datenbereichen. Eine Beispielsmatrix wird unten angezeigt.

**Eine Beispielsmatrix** 

![todo:image_alt_text](creating-matrix-report_1.png)

- **Matrix-Ecke**: befindet sich in der oberen linken Ecke, oder in der oberen rechten Ecke für rechts-nach-links (RTL)-Layouts. Dieser Bereich wird automatisch erstellt, wenn Sie sowohl Zeilengruppen als auch Spaltengruppen zu einem Matrix-Datenbereich hinzufügen. In diesem Bereich können Sie Zellen mit eingebettetem Textfeld-Berichtselement zusammenführen.
- **Bereich mit Matrix-Spaltengruppen**: befindet sich in der oberen rechten Ecke (obere linke Ecke für RTL-Layout). Dieser Bereich wird automatisch erstellt, wenn Sie eine Spaltengruppe hinzufügen. Die Zellen in diesem Bereich repräsentieren Elemente der Spaltengruppenhierarchie und zeigen die Werte der Spaltengruppeninstanz an. In der Abbildung sind die Zellen, die OrderYear anzeigen, eine verschachtelte Spaltengruppe, und die Zelle, die OrderQtr anzeigt, eine benachbarte Spaltengruppe.
- **Bereich mit Matrix-Zeilengruppen**: befindet sich in der unteren linken Ecke (unten rechts für RTL-Layout). Dieser Bereich wird automatisch erstellt, wenn Sie eine Zeilengruppe hinzufügen. Die Zellen in diesem Bereich repräsentieren Elemente der Zeilengruppenhierarchie und zeigen die Werte der Zeilengruppeninstanz an. In der Abbildung handelt es sich um verschachtelte Zeilengruppen.
- **Bereich mit Matrix-Daten**: befindet sich in der unteren rechten Ecke (unten links für RTL-Layout). Die Matrixdaten zeigen Detail- und gruppierte Daten an. In diesem Beispiel werden nur aggregierte Daten verwendet. Standardmäßig bewerten sich die Zellen in einer Gruppenzeile oder -spalte, die einfache Ausdrücke enthalten, die keine Aggregatfunktion enthalten, zum ersten Wert in der Gruppe. In der Abbildung zeigen die Zellen die aggregierten Summen für die Gesamtsummen für alle Verkaufsbestellungen an.
#### **Erstellen einer Matrixvorlage**
Bevor Sie einen Matrixbericht erstellen, erstellen Sie die Datenquellen, Datensätze und optionalen Berichtsparameter (Folgen Sie den Anweisungen in [Datenquellen und Abfragen](/cells/de/reportingservices/data-sources-and-queries/), wenn Sie Hilfe benötigen.) Im Beispiel verwenden wir die AdventureWorks-Beispieldatenbank, die mit SQL Server Reporting Services 2008 ausgeliefert wird.

Um eine neue Matrix zu erstellen:

1. Öffnen Sie Microsoft Excel.
1. Klicken Sie auf **Bericht öffnen**, um eine RDL-Berichtsdatei zu öffnen, die im Voraus erstellte Datenquellen, Datensätze und Berichtsparameter enthält.
   Sobald die Datei erfolgreich geöffnet wurde, steht alle ihre Informationen zur Verfügung, zum Beispiel sind ihre Datensätze in der **Datensatz**-Liste aufgeführt.
1. Öffnen Sie ein Microsoft Excel-Arbeitsblatt und wählen Sie ein Datenset aus. 

![todo:image_alt_text](creating-matrix-report_2.png)




1. Legen Sie Zeilengruppen und Spaltengruppen durch **Gruppe fest** fest. 

![todo:image_alt_text](creating-matrix-report_3.png)




1. Führen Sie Zellen zusammen, um die Matrixecke festzulegen.

![todo:image_alt_text](creating-matrix-report_4.png)




1. Legen Sie die Matrixecke durch Einfügen einer Formel fest. 

![todo:image_alt_text](creating-matrix-report_5.png)




![todo:image_alt_text](creating-matrix-report_6.png)




1. Klicken Sie auf **Attribut festlegen**, um Matrixattribut festzulegen. 

![todo:image_alt_text](creating-matrix-report_7.png)



Es besteht aus Name, Bereich, Gruppe und Reihenfolge.

1. Durch Klicken auf Attribut ändern werden alle Matrixattribute des aktuellen Arbeitsblatts überprüft und geändert.

![todo:image_alt_text](creating-matrix-report_8.png)




1. Speichern, veröffentlichen und Bericht überprüfen.
