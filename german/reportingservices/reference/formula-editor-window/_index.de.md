---
title: Formeleditorfenster
type: docs
weight: 20
url: /de/reportingservices/formula-editor-window/
---

{{% alert color="primary" %}} 

Der Formeleditor ermöglicht es Ihnen, Formeln für einen Bericht zu erstellen.

{{% /alert %}} 

Um eine Formel in einer Zelle von Microsoft Excel zu bearbeiten:

1. Wählen Sie in Microsoft Excel eine Zelle aus.
1. Öffnen Sie den Dialog „Formel bearbeiten“, indem Sie auf **Formel bearbeiten** in der Symbolleiste klicken.
   ([Das Hinzufügen von Reporting Services Formeln](/cells/de/reportingservices/adding-reporting-services-formulas/) durchläuft anhand eines Beispiels das Bearbeiten einer Formel.)
   Der Dialog ist in zwei Bereiche unterteilt: Der Bearbeitungsbereich oben und der Formelbereich unten. Verwenden Sie den Formelbereich, um den Bearbeitungsbereich zu füllen.
1. Wählen Sie eine Kategorie (Benutzer, Parameter, Felder usw.) aus der Liste **Berichtsfelder** (linke Liste).
1. Wählen Sie den Typ aus der Liste **Funktionen** (in der Mitte) aus.
1. Wählen Sie eine Option aus der Liste **Operatoren** (rechte Liste) aus.
1. Klicken Sie auf **Einfügen**, um den Ausdruck in den **Bearbeiten**-Bereich hinzuzufügen.
1. Klicken Sie auf **Einfügen**, wenn der Ausdruck vollständig ist.
   Die Formel wird in die Zelle eingefügt.

**Der Dialog zum Bearbeiten der Formel** 

![todo:image_alt_text](formula-editor-window_1.png)

Der Dialog „Formel bearbeiten“ ist in unten beschriebene Bereiche unterteilt.
#### **Bearbeitungsbereich**
Dies ist der Bereich, in dem Sie eine Formel erstellen oder bearbeiten. Erstellen Sie eine Formel, indem Sie auf eines der Komponenten in den Listen **Berichtsfelder**, **Funktionen** oder **Operatoren** doppelklicken. Wenn Sie eine Komponente auswählen, wird auch die erforderliche Syntax eingefügt. Sie können auch manuell eine Formel eingeben. 
#### **Formelbereich**
Der Formelbereich enthält drei Abschnitte, die jeweils Informationen enthalten, die zum Erstellen einer Formel verwendet werden.

- Berichtsfelder - Die Liste auf der linken Seite enthält alle für den Bericht zugänglichen Datenbankfelder. Sie enthält auch bereits erstellte Formeln oder Gruppen.
- Funktionen - Die mittlere Liste enthält Funktionen, vorgefertigte Verfahren, die Werte zurückgeben. Sie führen Berechnungen wie AVERAGE, SUM, COUNT, SIN, UPPERCASE usw. durch.
- Operatoren - die „handelnden Verben“ in Formeln. Operatoren beschreiben eine Operation oder eine Aktion, die zwischen zwei oder mehr Werten stattfinden soll. Beispiele für Operatoren: addieren, subtrahieren, kleiner als und größer als usw.
#### **Steuerungen**
Der Dialog enthält mehrere Steuerelemente:

|**Schaltflächenname** |**Beschreibung** |
| :- | :- |
|Undo |Macht eine Aktion rückgängig.|
|Paste |Fügt eine Zeichenfolge ein, die aus den im Formelbereich aufgelisteten Komponenten besteht, in den Bearbeitungsbereich ein.|
|Insert |Nimmt den Wert im Bearbeitungsbereich und fügt ihn als Formel in eine Zelle ein.|
|Exit |Schließt den Formel-Editor.|
{{% alert color="primary" %}} 

Verwandte Themen:

- [Formelliste](/cells/de/reportingservices/formula-list/) - eine Liste von Feldern und Operatoren.

{{% /alert %}}
