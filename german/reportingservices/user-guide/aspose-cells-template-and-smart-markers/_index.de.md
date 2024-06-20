---
title: Aspose.Cells Vorlage und Smart Marker
type: docs
weight: 30
url: /de/reportingservices/aspose-cells-template-and-smart-markers/
---

{{% alert color="primary" %}} 

Eine Aspose.Cells-Vorlage ist eine Microsoft Excel-Arbeitsmappe, die Smart-Marker enthält. Smart-Marker fungiert als Datenplatzhalter für Berichtselemente und wird zur Zeit der Ausgabe durch die entsprechenden Daten ersetzt. Es gibt fünf Arten von Smart-Markern, die unten aufgeführt sind. Alle Marker können von Aspose.Cells.Report.Designer in eine Vorlage eingefügt werden. Sie können auch manuell bearbeitet werden. 

{{% /alert %}} 
### **Smart Marker**
#### **Datenmarker**
Das Format von **Datenmarkern** lautet &=DataSetName.FieldName. Zum Beispiel: &=SalesDetail.sales, wobei SalesDetail der Name eines Datensatzes oder einer Abfrage und sales der Name eines seiner Felder ist. Zur Zeit der Ausgabe werden Datenmarker durch die Werte des von Reporting Services bereitgestellten Datensatzes ersetzt.
#### **Markersätze von Reporting Services-Formeln**
Das Format der **Formel-Marker** von Reporting Services ist &=expression. Zum Beispiel: &=sum(SalesDetail.sales)/100. Der Ausdruck besteht aus Funktionen, Datensatzfeldern, Operatoren usw. Zur Renderzeit werden die Marker für Reporting Services-Formeln durch berechnete Werte ersetzt.
#### **Markersätze von Reporting Services-Globalvariablen**
Das Format der **Marker für globale Variablen** von Reporting Services ist &=Globals!Variablenname. Zum Beispiel: &=Globals!ExecutionTime, wobei ExecutionTime der Name einer globalen Variablen ist. Die Marker für globale Variablen werden zur Renderzeit durch die Werte globaler Variablen ersetzt.
#### **Markersätze von Reporting Services-Parametern**
Ein Berichtsparameter hat zwei Attribute: Wert und Beschriftung. Dementsprechend haben **Parametermarker** zwei Formate: &= Parameters!ParamName.Value und &=Parameters!ParamName.Label. Sie geben den Namen und die Beschriftung des Parameters an. Zur Renderzeit werden die Parametermarker durch die vom Benutzer eingegebenen Parameterwerte ersetzt.
#### **Dynamische Formeln**
Um Berechnungen für eingefügte Zeilen durchzuführen, verwenden Sie dynamische Formeln. **Dynamische Formeln** ermöglichen es Ihnen, Microsoft Excel-Formeln in Zellen einzufügen, auch wenn eine Formel auf Zeilen verweist, die während des Exportvorgangs eingefügt werden. Sie können für jede eingefügte Zeile wiederholt oder nur mit Zellen verwendet werden, in denen Datenmarker für sie platziert sind.

Das Format dynamischer Formeln ist &=&=RepeatDynamicFormula.

Dynamische Formeln ermöglichen die folgenden zusätzlichen Optionen:

- {r} – Aktuelle Zeilennummer.
- {2}, {-1} – Versatz zur aktuellen Zeilennummer.

**Eine wiederholte dynamische Formel und das resultierende Excel-Arbeitsblatt** 

![todo:image_alt_text](aspose-cells-template-and-smart-markers_1.png)
