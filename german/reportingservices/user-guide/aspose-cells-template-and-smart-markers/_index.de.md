---
title: Aspose.Cells Schablone und intelligente Marker
type: docs
weight: 30
url: /de/reportingservices/aspose-cells-template-and-smart-markers/
---
{{% alert color="primary" %}} 

Eine Aspose.Cells-Vorlage ist eine Microsoft-Excel-Arbeitsmappe, die Smart Marker enthält. Intelligente Markierungen fungieren als Datenplatzhalter für Berichtselemente und werden beim Rendern durch die entsprechenden Daten ersetzt. Es gibt fünf Arten von Smart-Markern, die unten aufgeführt sind. Alle Marker können per Aspose.Cells.Report.Designer in eine Vorlage eingefügt werden. Die können auch manuell bearbeitet werden.

{{% /alert %}} 
### **Intelligente Markierungen**
#### **Datenmarkierungen**
 Das Format von**Datenmarkierungen** ist &=Datensatzname.Feldname. Beispiel: &=SalesDetail.sales wobei SalesDetail der Name eines Datensatzes oder einer Abfrage und sales der Name eines seiner Felder ist. Beim Rendern werden Datenmarkierungen durch die Werte des von Reporting Services bereitgestellten Datensatzes ersetzt.
#### **Reporting Services-Formelmarkierungen**
 Das Format von Reporting Services'**Formeln Markierungen**ist &=Ausdruck. Beispiel: &=sum(SalesDetail.sales)/100. Der Ausdruck besteht aus Funktion, Datensatzfeldern, Operator usw. Zur Renderzeit. Reporting Services-Formelmarkierungen werden durch berechnete Werte ersetzt.
#### **Globale Variablenmarkierungen von Reporting Services**
 Das Format von Reporting Services'**globale Variablenmarker** ist &=Global! Variablennamen. Beispiel: &=Globals!ExecutionTime wobei ExecutionTime der Name einer globalen Variablen ist. Globale Variablenmarkierungen werden zum Zeitpunkt des Renderns durch globale Variablenwerte ersetzt.
#### **Reporting Services-Parametermarkierungen**
 Ein Berichtsparameter hat zwei Attribute: Wert und Bezeichnung. Folglich,**Parametermarkierungen** haben zwei Formate: &= Parameter! ParamName.Wert und &=Parameter! ParamName.Label. Sie geben den Namen bzw. das Label des Parameters an. Beim Rendern werden Parametermarkierungen durch die vom Benutzer eingegebenen Parameterwerte ersetzt.
#### **Dynamische Formeln**
 Verwenden Sie dynamische Formeln, um Berechnungen für eingefügte Zeilen durchzuführen.**Dynamische Formeln** ermöglichen Ihnen das Einfügen von Microsoft Excel-Formeln in Zellen, selbst wenn eine Formel auf Zeilen verweist, die während des Exportvorgangs eingefügt werden. Sie können für jede eingefügte Zeile wiederholt oder nur mit Zellen verwendet werden, in denen Datenmarkierungen für sie platziert sind.

Das Format dynamischer Formeln ist &=&=RepeatDynamicFormula.

Dynamische Formeln ermöglichen die folgenden zusätzlichen Optionen:

- {r} – Aktuelle Zeilennummer.
- {2}, {-1} – Offset zur aktuellen Zeilennummer.

**Eine sich wiederholende dynamische Formel und das resultierende Excel-Arbeitsblatt** 

![todo: Bild_alt_Text](aspose-cells-template-and-smart-markers_1.png)
